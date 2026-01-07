# -*- coding: utf-8 -*-
"""
Created on Fri Oct 22 03:33:23 2021

@author: admin
"""
import torch
import numpy as np
import torch.nn as nn
import torch.nn.functional as F
from torchvision import transforms

import matplotlib.pyplot as plt
from utilities3 import *


import operator
from functools import reduce
from functools import partial

from timeit import default_timer
import scipy.io
import os

torch.manual_seed(0)
np.random.seed(0)

# os.chdir(r'D:\BaiduNetdiskDownload\zhijie_recently_code\U-FNO_3D-tunning')
################################################################
# 4d fourier layers
class SpectralConv3d(nn.Module):
    def __init__(self, in_channels, out_channels, modes1, modes2, modes3):
        super(SpectralConv3d, self).__init__()

        """
        3D Fourier layer. It does FFT, linear transform, and Inverse FFT.    
        """

        self.in_channels = in_channels
        self.out_channels = out_channels
        self.modes1 = modes1 #Number of Fourier modes to multiply, at most floor(N/2) + 1
        self.modes2 = modes2
        self.modes3 = modes3

        self.scale = (1 / (in_channels * out_channels))
        self.weights1 = nn.Parameter(self.scale * torch.rand(in_channels, out_channels, self.modes1, self.modes2, self.modes3, dtype=torch.cfloat))
        self.weights2 = nn.Parameter(self.scale * torch.rand(in_channels, out_channels, self.modes1, self.modes2, self.modes3, dtype=torch.cfloat))
        self.weights3 = nn.Parameter(self.scale * torch.rand(in_channels, out_channels, self.modes1, self.modes2, self.modes3, dtype=torch.cfloat))
        self.weights4 = nn.Parameter(self.scale * torch.rand(in_channels, out_channels, self.modes1, self.modes2, self.modes3, dtype=torch.cfloat))

    # Complex multiplication
    def compl_mul3d(self, input, weights):
        # (batch, in_channel, x,y,z,t ), (in_channel, out_channel, x,y,z,t) -> (batch, out_channel, x,y,z,t)
        return torch.einsum("bixyz,ioxyz->boxyz", input, weights)

    def forward(self, x):
        batchsize = x.shape[0] 
        #Compute Fourier coeffcients up to factor of e^(- something constant)
        x_ft = torch.fft.rfftn(x, dim=[-3,-2,-1])

        # Multiply relevant Fourier modes
        out_ft = torch.zeros(batchsize, self.out_channels, x.size(-3), x.size(-2), x.size(-1)//2+1, dtype=torch.cfloat, device=x.device)
        out_ft[:, :, :self.modes1, :self.modes2, :self.modes3] = self.compl_mul3d(x_ft[:, :, :self.modes1, :self.modes2, :self.modes3], self.weights1)
        out_ft[:, :, -self.modes1:, :self.modes2, :self.modes3] = self.compl_mul3d(x_ft[:, :, -self.modes1:, :self.modes2, :self.modes3], self.weights2)
        out_ft[:, :, :self.modes1, -self.modes2:, :self.modes3] = self.compl_mul3d(x_ft[:, :, :self.modes1, -self.modes2:, :self.modes3], self.weights3)
        out_ft[:, :, -self.modes1:, -self.modes2:, :self.modes3] =self.compl_mul3d(x_ft[:, :, -self.modes1:, -self.modes2:, :self.modes3], self.weights4)

        #Return to physical space 转到波数空间截断后相乘，再转换物理空间
        x = torch.fft.irfftn(out_ft, s=(x.size(-3), x.size(-2), x.size(-1)))
        return x

class U_net(nn.Module):  
    def __init__(self, input_channels, output_channels, kernel_size, dropout_rate): #width,width,3,0
        super(U_net, self).__init__()
        self.input_channels = input_channels
        self.conv1 = self.conv(input_channels, output_channels, kernel_size=kernel_size, stride=2, dropout_rate = dropout_rate) #28,28,3,0
        self.conv2 = self.conv(input_channels, output_channels, kernel_size=kernel_size, stride=2, dropout_rate = dropout_rate)
        self.conv2_1 = self.conv(input_channels, output_channels, kernel_size=kernel_size, stride=1, dropout_rate = dropout_rate)
        self.conv3 = self.conv(input_channels, output_channels, kernel_size=kernel_size, stride=2, dropout_rate = dropout_rate)
        self.conv3_1 = self.conv(input_channels, output_channels, kernel_size=kernel_size, stride=1, dropout_rate = dropout_rate)
        
        self.deconv2 = self.deconv(input_channels, output_channels)
        self.deconv1 = self.deconv(input_channels*2, output_channels)
        self.deconv0 = self.deconv(input_channels*2, output_channels)
    
        self.output_layer = self.output(input_channels*2, output_channels, 
                                         kernel_size=kernel_size, stride=1, dropout_rate = dropout_rate)


    def forward(self, x):        #[BS,width,32,32,32]        
        batchsize, width = x.shape[0], x.shape[1]
        out_conv1 = self.conv1(x)  #[BS,width,16,16,16]
        out_conv2 = self.conv2_1(self.conv2(out_conv1)) #[BS,width,8,8,8]
        out_conv3 = self.conv3_1(self.conv3(out_conv2)) #[BS,width,4,4,4]

        out_deconv2 = self.deconv2(out_conv3)  #[BS,width,8,8,8]
        concat2 = torch.cat((out_conv2, out_deconv2), 1)  #[BS,2*width,8,8,8]
        out_deconv1 = self.deconv1(concat2)  #[BS,width,16,16,16]
        concat1 = torch.cat((out_conv1, out_deconv1), 1)  #[BS,2*width,16,16,16]
        out_deconv0 = self.deconv0(concat1)   #[BS,width,32,32,32]  
        concat0 = torch.cat((x, out_deconv0), 1)   #[BS,2*width,32,32,32]  
        out = self.output_layer(concat0) #[BS,width,32,32,32]  
        return out   


    def conv(self, input_channels, output_channels, kernel_size, stride, dropout_rate):
        return nn.Sequential(
            nn.Conv3d(input_channels, output_channels, kernel_size=kernel_size,
                      stride=stride, padding=(kernel_size - 1) // 2, bias = False),
            nn.LeakyReLU(0.1, inplace=True),  #x>0, is x; x<0 is 0.1x
            nn.Dropout(dropout_rate)
        )

    def deconv(self, input_channels, output_channels):
        return nn.Sequential(
            nn.ConvTranspose3d(input_channels, output_channels, kernel_size=4,
                                stride=2, padding=1),
            nn.LeakyReLU(0.1, inplace=True)
        )

    def output(self, input_channels, output_channels, kernel_size, stride, dropout_rate):
        return nn.Conv3d(input_channels, output_channels, kernel_size=kernel_size,
                          stride=stride, padding=(kernel_size - 1) // 2)


class FNO3d(nn.Module):
    def __init__(self, modes1, modes2, modes3, width, nlayer, T_in, var, T_out): # width相当于输入输出通道
        super(FNO3d, self).__init__()

        """
        input: the solution of the first 5 timesteps + 3 locations (u(1, x, y), ..., u(10, x, y),  x, y, t). It's a constant function in time, except for the last index.
        input shape: (batchsize, x=64, y=64, z=64, dim=3, c=5+3)
        output: the solution of the next  timestep
        output shape: (batchsize, x=64, y=64, z=64, dim=3, c=1)
        """

        self.modes1 = modes1
        self.modes2 = modes2
        self.modes3 = modes3
        self.width = width
        self.T_in = T_in
        self.var = var
        self.T_out = T_out
        
        # self.fc0 = nn.Linear(T_in*var+3, self.width)  
        self.nlayer = nlayer
        
        self.convlayer = nn.ModuleList([SpectralConv3d(self.width, self.width, self.modes1, self.modes2, self.modes3).cuda() for i in range(1)])
        self.w = nn.ModuleList([nn.Conv3d(self.width, self.width, 1).cuda() for i in range(1)])
        self.u = nn.ModuleList([U_net(self.width, self.width, 3, 0).cuda() for i in range(1)])
        
        self.enc = nn.Conv3d(var*T_in, width, 1)
        # self.dec_rec = nn.Conv3d(width, var*T_in, 1)
        self.dec = nn.Conv3d(width, var*T_out, 1)
        
        # self.fc1 = nn.Linear(self.width, 512)
        # self.fc2 = nn.Linear(512, 1)

    def forward(self, x):   #[2, 32, 32, 32, 3, 5] 
        batchsize, size_x, size_y, size_z, var, T_in = x.shape[0], x.shape[1], x.shape[2], x.shape[3], x.shape[4], x.shape[5]  
        coef = 1./self.nlayer
        # grid = self.get_grid(batchsize, size_x, size_y, size_z, x.device) #torch.Size([2, 32, 32, 32, 3])
        # x = torch.cat((x, grid), dim=-1) 
        # x = self.fc0(x)   #经过后输出[bs,32,32,32,3,width]
        # x = x.permute(0, 5, 1, 2, 3) #(2,28,32,32,32,3)
        
        # Reconstruct
        x = x.reshape(batchsize, size_x, size_y, size_z, var*T_in).permute([0,4,1,2,3]) # [BS,32,32,32,var*T_in]-->[BS,var*T_in,32,32,32]
        x_reconstruct = self.enc(x)  # [BS,width,32,32,32]
        x_reconstruct = torch.tanh(x_reconstruct)  # [BS,width,32,32,32]
        x_reconstruct = self.dec(x_reconstruct)  # [BS,var*T_in,32,32,32]
        x_reconstruct = x_reconstruct.permute([0,2,3,4,1]) # [BS,32,32,32,var*T_in]
        x_reconstruct = x_reconstruct.reshape(batchsize, size_x, size_y, size_z, var, T_in)  # [BS,32,32,32,var,T_in]
        
        #predict
        x = self.enc(x) # Encoder # [BS,width,32,32,32]
        x = torch.tanh(x)
        # x_w = x    # used for part5 convolution # [BS,width,32,32,32]

        for i in range(self.nlayer):
            # x1 = self.convlayer[i](x)
            # x2 = self.w[i](x.view(batchsize, self.width, -1)).view(batchsize, self.width, size_x, size_y, size_z, size_w)
            # x3 = self.u[i](x-x1)
            x1 = self.convlayer[0](x) #[BS,width,32,32,32]
            x2 = self.w[0](x)  #[BS,width,32,32,32]
            x3 = self.u[0](x-x1) #[BS,width,32,32,32]
            x = torch.tanh(x1+x2+x3)*coef + x   #[BS,width,32,32,32]

        # x1 = self.convlayer[self.nlayer-1](x)
        # x2 = self.w[self.nlayer-1](x.view(batchsize, self.width, -1)).view(batchsize, self.width, size_x, size_y, size_z, size_w)
        # x3 = self.u[self.nlayer-1](x-x1)
        #------nlayer-1
        # x1 = self.convlayer[0](x)
        # x2 = self.w[0](x)
        # x3 = self.u[0](x-x1)
        # x = (x1+x2+x3)*coef + x
      
        # x = x.permute(0, 2, 3, 4, 5, 1) #torch.Size([2, 32, 32, 32, 3, 28])
        # x = self.fc1(x)
        # x = F.gelu(x)
        # x = self.fc2(x)
        # return x  #torch.Size([2, 32, 32, 32, 3, 1])
    
        x = self.dec(x) # Decoder   #[BS,width,32,32,32]---->#[BS,var*T_out,32,32,32]
        x = x.permute(0,2,3,4,1) #[BS,32,32,32,,var*T_out]
        x = x.reshape(batchsize, size_x, size_y, size_z, var, T_out)
        return x, x_reconstruct   # beta_loss_[BS,32,32,32,var,T_out], alpha_loss_[BS,32,32,32,var,T_in]

    # def get_grid(self, batchsize, size_x, size_y, size_z, device ): #[bs,32,32,32,3]
    #     gridx = torch.tensor(np.linspace(0, 1, size_x), dtype=torch.float)
    #     gridx = gridx.reshape(1, size_x, 1, 1, 1).repeat([batchsize, 1, size_y, size_z, 1])
    #     gridy = torch.tensor(np.linspace(0, 1, size_y), dtype=torch.float)
    #     gridy = gridy.reshape(1, 1, size_y, 1, 1).repeat([batchsize, size_x, 1, size_z, 1])
    #     gridz = torch.tensor(np.linspace(0, 1, size_z), dtype=torch.float)
    #     gridz = gridz.reshape(1, 1, 1, size_z, 1).repeat([batchsize, size_x, size_y, 1, 1])
        # return torch.cat((gridx, gridy, gridz), dim=-1).to(device) #

# input size should be [bs,64,64,64,3,5]
################################################################
# modes = 10
# width = 30
# nlayer = 10
# T_in = 1
# var = 3
# T_out = 1
# device = torch.device('cuda:1')
# model = FNO3d(modes, modes, modes, width, nlayer, T_in, var, T_out).to(device)  #模型放到GPU上
# print(count_params(model)) 
# #(batchsize, x=32, y=32, z=32, c=3, t=5) c is 3 channel 
# x = torch.rand(2,32,32,32,var,T_in).to(device) #input 12 step, output 1 step
# print('input tensor size = ', x.shape)
# pred = model(x) 
# print(len(pred),pred[0].shape,pred[1].shape)



# configs
################################################################
# device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
device = torch.device("cuda")
#-------------------------------------------------------------------------------需要调节的参数
#tunning3
modes = 12
width = 90 #3n
nlayer = 40
#----------------data config
T_in = 1       # input step
T_out = 1       # output step
var = 3
#-----------------training setting
batch_size = 5
epochs = 40
learning_rate = 0.0005
weight_decay_value = 1e-8
scheduler_step = 5
scheduler_gamma = 0.5  # 衰减率
#-------------loss efficient
alpha = 1
beta = 0
#网络层数
#显卡内存有没有爆掉cd C:\Program Files\NVIDIA Corporation\NVSMI，nvidia-smi
#保存模型的文件名
#---------------------------------------------------------------------------------------------
print(f"modes: {modes}\nwidth: {width}\nnlayer: {nlayer}\nepochs: {epochs}\nlearning_rate: {learning_rate}\n"
      f"scheduler_step: {scheduler_step}\nscheduler_gamma: {scheduler_gamma}\nalpha: {alpha}\nbeta: {beta}")

#-------------------------------------------------上面4行运行一次后保存出数据，下次直接加载数据
vor_data = np.load('../../../../hit_vel_100g_200gap_601step.npy') #
vor_data = torch.from_numpy(vor_data) #[3000, 32, 32, 32, 3]

#######################################加载训练好的模型
model = FNO3d(modes, modes, modes, width, nlayer, T_in, var, T_out).to(device)
PATH = '../../m12w90n40g45_40ep1e8w.pth'
model.load_state_dict(torch.load(PATH))  #把模型的参数加载上去
model.eval() #告诉网络这是测试，不更新参数
# print(count_params(model)) 
#######################################################################################################################
########################################################################### 时间推进
pre_vor_t_total = torch.zeros([1,32,32,32,3,600])  #initial 
label_vor_total = torch.zeros([1,32,32,32,3,600]) 
#sample_id_data = [45,46,47,48,49]
sample_id_data = list(range(31))  # 从 0 到 30（包括 30）
time_id_data =[0]
for sample_id in sample_id_data:
    for time_id in time_id_data:    #起始步
        time_advanced_step = 600  #推进步
        input_vor = vor_data[sample_id, time_id:time_id+T_in,...].permute(1,2,3,4,0) #前5个时刻的值 #[32, 32, 32, 3, 1]
        label_vor = vor_data[sample_id, time_id+T_in:time_id+T_in+time_advanced_step,...].permute(1,2,3,4,0)  #从第6时刻起后N推进步
        ####################时间推进步数
        pre_vor_t = input_vor[:,:,:,:,0].unsqueeze(-1)  #相当于新建一个，后面会舍弃[32, 32, 32, 3, 1]
        for i in range(time_advanced_step):  
            print(i)
            #model要输入[bs,32,32,32,3,5],所以先unsqueeze给bs
            predict_vor = model(input_vor.unsqueeze(0).to(device))[0].squeeze(0).detach().cpu()  #[32, 32, 32, 3],output
            # print(predict_vor.shape,input_vor.shape)
            #predict_vor = predict_vor+input_vor # torch.Size([32, 32, 32, 3, 1])
            # print(predict_vor.shape)
            
            # 设定网格大小
            Nx, Ny, Nz = 32, 32, 32

            # 生成随机湍流速度场 (实部 + 复部)
            #predict_vor = torch.randn(Nx, Ny, Nz, 3, 1, dtype=torch.float64)

            # 计算 FFT
            vx_hat = torch.fft.rfftn(predict_vor[..., 0, 0],norm="ortho")   # vx 的 FFT
            vy_hat = torch.fft.rfftn(predict_vor[..., 1, 0],norm="ortho")  # vy 的 FFT
            vz_hat = torch.fft.rfftn(predict_vor[..., 2, 0],norm="ortho")  # vz 的 FFT

            # 计算波数
            kx = np.fft.fftfreq(Nx, d=1) * Nx
            ky = np.fft.fftfreq(Ny, d=1) * Ny
            kz = np.fft.rfftfreq(Nz, d=1) * Nz

            kx, ky, kz = torch.tensor(kx), torch.tensor(ky), torch.tensor(kz)
            # 生成 3D 网格 (保持正确的形状)
            KX, KY, KZ = torch.meshgrid(kx, ky, kz, indexing="ij")

            # 计算 k^2 并取整数部分
            k2 = KX**2 + KY**2 + KZ**2
            k_int = torch.round(torch.sqrt(k2)).int()   # 计算 k 的整数部分

            # 目标能量 (k=1, k=2)
            force = torch.tensor([1.242477, 0.391356], dtype=torch.float64)

            # 计算当前动能 tmp = |vx|^2 + |vy|^2 + |vz|^2
            tmp = vx_hat * torch.conj(vx_hat) + vy_hat * torch.conj(vy_hat) + vz_hat * torch.conj(vz_hat)
            tmp[:, :, 0] *= 0.5 
            tmp = tmp/(Nx * Ny * Nz)
            # 计算 k=1,2 的总能量
            ek_values_before = torch.stack([torch.sum(tmp[k_int == k]) for k in range(1, 3)])

            # 打印检测结果
            print("Before:")
            print(f"  k=1: {ek_values_before [0].item():.6f}, k=2: {ek_values_before [1].item():.6f}")

            # 计算缩放因子 ff，并调整速度谱
            ff_values = torch.sqrt(force / (ek_values_before ))  # 避免除零
            for k in range(1, 3):
                vx_hat[k_int == k] *= ff_values[k - 1]
                vy_hat[k_int == k] *= ff_values[k - 1]
                vz_hat[k_int == k] *= ff_values[k - 1]

            # 逆变换回时域
            vx_new = torch.fft.irfftn(vx_hat,norm="ortho")
            vy_new = torch.fft.irfftn(vy_hat,norm="ortho")
            vz_new = torch.fft.irfftn(vz_hat,norm="ortho")

            # 重新整理数据形状
            predict_vor = torch.stack([vx_new, vy_new, vz_new], dim=-1).unsqueeze(-1)  # [32, 32, 32, 3, 1]

            ####################check##################
            # 计算 FFT (rfftn)
            vx_hat = torch.fft.rfftn(predict_vor[..., 0, 0],norm="ortho")  # vx 的 FFT
            vy_hat = torch.fft.rfftn(predict_vor[..., 1, 0],norm="ortho")  # vy 的 FFT
            vz_hat = torch.fft.rfftn(predict_vor[..., 2, 0],norm="ortho")  # vz 的 FFT

            # 计算波数
            kx = np.fft.fftfreq(Nx, d=1) * Nx
            ky = np.fft.fftfreq(Ny, d=1) * Ny
            kz = np.fft.rfftfreq(Nz, d=1) * Nz

            kx, ky, kz = torch.tensor(kx), torch.tensor(ky), torch.tensor(kz)
            # 生成 3D 网格 (保持正确的形状)
            KX, KY, KZ = torch.meshgrid(kx, ky, kz, indexing="ij")

            # 计算 k^2 并取整数部分
            k2 = KX**2 + KY**2 + KZ**2
            k_int = torch.round(torch.sqrt(k2)).int()

            # 计算当前动能 tmp = |vx|^2 + |vy|^2 + |vz|^2
            tmp = vx_hat * torch.conj(vx_hat) + vy_hat * torch.conj(vy_hat) + vz_hat * torch.conj(vz_hat)
            tmp[:, :,0] *= 0.5 
            tmp = tmp/(Nx * Ny * Nz)
            # 确保 k_int 形状与 tmp 形状匹配
            assert k_int.shape == tmp.shape, f"Shape mismatch: k_int {k_int.shape}, tmp {tmp.shape}"

            # 计算 k=1,2 的总能量
            ek_values = torch.stack([torch.sum(tmp[k_int == k]) for k in range(1, 3)])

            # 打印检测结果
            print("After:")
            print(f"  k=1: {ek_values[0].item():.6f}, k=2: {ek_values[1].item():.6f}")           
            
            pre_vor_t = torch.cat((pre_vor_t, predict_vor),dim=-1)  #把每一次的pre值装载出去
            # print(pre_vor_t.shape)
            # vor_new = torch.cat((input_vor[:,:,:,:,1:],predict_vor.unsqueeze(-1)),dim=-1) #拼接成新的input
            vor_new = predict_vor
            input_vor = vor_new  #更新,input_vor装的是最新5个时刻
        pre_vor_t = pre_vor_t[:,:,:,:,1:]  #保留推测的N个步
        pre_vor_t_total = torch.cat((pre_vor_t_total, pre_vor_t.unsqueeze(0)),dim=0)
        label_vor_total  = torch.cat((label_vor_total, label_vor.unsqueeze(0)),dim=0)
pre_vor_t_total = pre_vor_t_total[1:,...]
label_vor_total = label_vor_total[1:,...] #(10, 32, 32, 32, 3, 250)

# pre_vor_t_total = pre_vor_t_total.permute(0,4,1,2,3,5)
# #######################################torch转成numpy格式
# #numpy_label_vor = label_vor.numpy()
# numpy_pre_vor_t_total = pre_vor_t_total.numpy()
# # numpy_pre_vor_t = input_vor.numpy()#用于训练前验证数据
# # case10_t5 = numpy_pre_vor_t_total[...,4]
# # case10_t15 = numpy_pre_vor_t_total[...,14]
# # case10_t25 = numpy_pre_vor_t_total[...,24]
# # case10_t30 = numpy_pre_vor_t_total[...,29]
# # case10_t35 = numpy_pre_vor_t_total[...,34]
# # case10_t40 = numpy_pre_vor_t_total[...,39]
# case10_t50 = numpy_pre_vor_t_total[...,49]
# case10_t60 = numpy_pre_vor_t_total[...,59]
# case10_t70 = numpy_pre_vor_t_total[...,69]
# case10_t80 = numpy_pre_vor_t_total[...,79]

# ##########################################save predicted vel field
# # case10_t3 = case10_t3[0:10,0:3,0:32,0:32,0:32]
# # casenumber = ['case10_t5','case10_t15','case10_t25','case10_t30','case10_t35','case10_t40']
# casenumber = ['case10_t50','case10_t60','case10_t70','case10_t80']
# qnumber = [50,60,70,80]
# for q in range(len(casenumber)):
#     tn = qnumber[q]
#     print(casenumber[q])
#     f = open("./predicted_data/FNO32_uxyz_gap200_t{}.dat".format(tn), "w")
#     for n in range(eval(casenumber[q]).shape[0]):
#         for m in range(eval(casenumber[q]).shape[1]):
#             for i in range(eval(casenumber[q]).shape[2]):
#                 for j in range(eval(casenumber[q]).shape[3]):
#                     for k in range(eval(casenumber[q]).shape[4]):
#                         f.writelines("%16.12f"%(eval(casenumber[q])[n,m,i,j,k])+'\n')
            
#     f.close()
#-----------------------------------------------------------------------------------------------------continue times output
#######################################torch转成numpy格式
pre_vor_t_total = pre_vor_t_total.permute(5,4,1,2,3,0)
numpy_pre_vor_t_total = pre_vor_t_total.numpy()
# numpy_pre_vor_t = input_vor.numpy()#用于训练前验证数据
case1 = numpy_pre_vor_t_total[..., 0]
case2 = numpy_pre_vor_t_total[..., 1]
case3 = numpy_pre_vor_t_total[..., 2]
case4 = numpy_pre_vor_t_total[..., 3]
case5 = numpy_pre_vor_t_total[..., 4]
case6 = numpy_pre_vor_t_total[..., 5]
case7 = numpy_pre_vor_t_total[..., 6]
case8 = numpy_pre_vor_t_total[..., 7]
case9 = numpy_pre_vor_t_total[..., 8]
case10 = numpy_pre_vor_t_total[..., 9]
case11 = numpy_pre_vor_t_total[..., 10]
case12 = numpy_pre_vor_t_total[..., 11]
case13 = numpy_pre_vor_t_total[..., 12]
case14 = numpy_pre_vor_t_total[..., 13]
case15 = numpy_pre_vor_t_total[..., 14]
case16 = numpy_pre_vor_t_total[..., 15]
case17 = numpy_pre_vor_t_total[..., 16]
case18 = numpy_pre_vor_t_total[..., 17]
case19 = numpy_pre_vor_t_total[..., 18]
case20 = numpy_pre_vor_t_total[..., 19]
case21 = numpy_pre_vor_t_total[..., 20]
case22 = numpy_pre_vor_t_total[..., 21]
case23 = numpy_pre_vor_t_total[..., 22]
case24 = numpy_pre_vor_t_total[..., 23]
case25 = numpy_pre_vor_t_total[..., 24]
case26 = numpy_pre_vor_t_total[..., 25]
case27 = numpy_pre_vor_t_total[..., 26]
case28 = numpy_pre_vor_t_total[..., 27]
case29 = numpy_pre_vor_t_total[..., 28]
case30 = numpy_pre_vor_t_total[..., 29]


##########################################save predicted vel field
#case10_t3 = case10_t3[0:10,0:3,0:32,0:32,0:32]
casenumber = [f'case{i}' for i in range(1, 31)]
qnumber = list(range(1, 31))
for q in range(len(casenumber)):
    tn = qnumber[q]
    print(casenumber[q])
    f = open("./600/IUFNO32_40ep_uxyz_gap200_case{}.dat".format(tn), "w")
    for n in range(eval(casenumber[q]).shape[0]):
        for m in range(eval(casenumber[q]).shape[1]):
            for i in range(eval(casenumber[q]).shape[2]):
                for j in range(eval(casenumber[q]).shape[3]):
                    for k in range(eval(casenumber[q]).shape[4]):
                        f.writelines("%16.12f"%(eval(casenumber[q])[n,m,i,j,k])+'\n')
            
    f.close()