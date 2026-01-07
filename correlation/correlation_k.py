# -*- coding: utf-8 -*-
"""
Created on Wed Nov 17 01:37:05 2021

@author: admin
"""
import numpy as np
import torch.nn as nn
import torch.nn.functional as F
import matplotlib as mpl
import matplotlib.pyplot as plt
import os
import torch

####ACF###
def compute_acf(u1, u2):
    """
    计算两个流场之间的自相关函数（ACF）
    
    参数:
    u1, u2: 形状为 [32, 32, 32, 3] 的流场数据
    
    返回:
    acf: 标量，表示 u1 和 u2 之间的 ACF
    """ 
    u1 = u1.cpu().numpy() if isinstance(u1, torch.Tensor) else u1
    u2 = u2.cpu().numpy() if isinstance(u2, torch.Tensor) else u2    
    # 计算分子部分: u1 * u2 在所有空间点上的均值
    numerator = np.mean(u1 * u2)

    # 计算分母部分: u1 的平方均值
    denominator = np.mean(u1**2)

    # 计算 ACF
    acf = numerator / denominator

    return acf

###correlation###
def compute_correlation(u1, u2):
    """
    计算两个张量的相关系数
    u1, u2: 形状相同的张量
    """
    u1 = u1.cpu().numpy() if isinstance(u1, torch.Tensor) else u1
    u2 = u2.cpu().numpy() if isinstance(u2, torch.Tensor) else u2        
    # 确保 u1 和 u2 形状相同
    assert u1.shape == u2.shape, "两个张量的形状必须相同"

    # 计算均值
    mean_u1 = np.mean(u1)
    mean_u2 = np.mean(u2)

    # 计算分子部分
    numerator = np.mean((u1 - mean_u1) * (u2 - mean_u2))

    # 计算分母部分
    denominator = np.sqrt(np.mean((u1 - mean_u1)**2) * np.mean((u2 - mean_u2)**2))

    # 计算相关系数
    correlation = numerator / denominator

    return correlation


###acf_k###
def compute_acf_k(u1, u2, k_max=10):
    """
    计算 u1, u2 在 k=1 到 k_max 各自的 ACF

    参数:
    u1, u2: 形状为 [32, 32, 32, 3] 的流场数据
    k_max: 计算的最大波数 k

    返回:
    k_acf_values: 长度为 k_max 的列表，存储各个 k 的 ACF
    """
    # 计算 3D FFT
    fft_u1 = np.fft.rfftn(u1, axes=(0,1,2))
    fft_u2 = np.fft.rfftn(u2, axes=(0,1,2))

    # 计算傅里叶频率对应的波数
    nx, ny, nz, _ = u1.shape
    kx = np.fft.fftfreq(nx) * nx
    ky = np.fft.fftfreq(ny) * ny
    kz = np.fft.rfftfreq(nz) * nz

    # 计算波数 k = sqrt(kx^2 + ky^2 + kz^2)
    KX, KY, KZ = np.meshgrid(kx, ky, kz, indexing='ij')
    k_magnitude = np.sqrt(KX**2 + KY**2 + KZ**2).astype(int)
    
    k_values = []
    k_acf_values = []

    for k in range(1, k_max + 1):
        # 创建掩码，筛选波数 k 处的傅里叶系数
        mask = (k_magnitude == k)

        if np.any(mask):
            # 仅保留波数 k 处的模式，其他设为 0
            fft_u1_k = np.zeros_like(fft_u1, dtype=complex)
            fft_u2_k = np.zeros_like(fft_u2, dtype=complex)

            fft_u1_k[mask, :] = fft_u1[mask, :]
            fft_u2_k[mask, :] = fft_u2[mask, :]

            # 逆傅里叶变换回物理空间
            u1_k = np.fft.irfftn(fft_u1_k, axes=(0,1,2))
            u2_k = np.fft.irfftn(fft_u2_k, axes=(0,1,2))

            # 计算 ACF
            acf_k = compute_acf(u1_k, u2_k)
        else:
            acf_k = np.nan  # 若 k 处无模式，则设为 NaN
        
        k_values.append(k)
        k_acf_values.append(acf_k)

    #return k_values, k_acf_values
    return k_acf_values

###correlation_k###
def compute_correlation_k(u1, u2, k_max=10):
    """
    计算 u1, u2 在 k=1 到 k_max 各自的 ACF

    参数:
    u1, u2: 形状为 [32, 32, 32, 3] 的流场数据
    k_max: 计算的最大波数 k

    返回:
    k_acf_values: 长度为 k_max 的列表，存储各个 k 的 ACF
    """
    # 计算 3D FFT
    fft_u1 = np.fft.rfftn(u1, axes=(0,1,2))
    fft_u2 = np.fft.rfftn(u2, axes=(0,1,2))

    # 计算傅里叶频率对应的波数
    nx, ny, nz, _ = u1.shape
    kx = np.fft.fftfreq(nx) * nx
    ky = np.fft.fftfreq(ny) * ny
    kz = np.fft.rfftfreq(nz) * nz

    # 计算波数 k = sqrt(kx^2 + ky^2 + kz^2)
    KX, KY, KZ = np.meshgrid(kx, ky, kz, indexing='ij')
    k_magnitude = np.sqrt(KX**2 + KY**2 + KZ**2).astype(int)
    
    k_values = []
    k_correlation_values = []

    for k in range(1, k_max + 1):
        # 创建掩码，筛选波数 k 处的傅里叶系数
        mask = (k_magnitude == k)

        if np.any(mask):
            # 仅保留波数 k 处的模式，其他设为 0
            fft_u1_k = np.zeros_like(fft_u1, dtype=complex)
            fft_u2_k = np.zeros_like(fft_u2, dtype=complex)

            fft_u1_k[mask, :] = fft_u1[mask, :]
            fft_u2_k[mask, :] = fft_u2[mask, :]

            # 逆傅里叶变换回物理空间
            u1_k = np.fft.irfftn(fft_u1_k, axes=(0,1,2))
            u2_k = np.fft.irfftn(fft_u2_k, axes=(0,1,2))

            # 计算 ACF
            correlation_k = compute_correlation(u1_k, u2_k)
        else:
            correlation_k = np.nan  # 若 k 处无模式，则设为 NaN
        
        k_values.append(k)
        k_correlation_values.append(correlation_k)

    #return k_values, k_correlation_values
    return k_correlation_values

###each###

vor_data = np.load('../hit_vel_100g_20gap_605step.npy') #
vor_data = torch.from_numpy(vor_data) #[100, 605, 32, 32, 32, 3]
print(vor_data.shape)

case, step, Nx, Ny, Nz = vor_data.shape[0], vor_data.shape[1], vor_data.shape[2], vor_data.shape[3], vor_data.shape[4]

step = [x // 20 for x in [20, 40, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]]  # 取整


for spec in range(10):

    acf_results = [[] for _ in step]
    correlation_results = [[] for _ in step]


    for k,t_k in enumerate(step):

        for i in range(0,case):
            for j in range(0,2):
                u1=vor_data[i,j,:,:,:,:]
                u2=vor_data[i,j+t_k,:,:,:,:]
                
                acf_temp=compute_acf_k(u1, u2)
                acf=acf_temp[spec]
                acf_results[k].append(acf)  

                correlation_temp=compute_correlation_k(u1, u2)
                correlation=correlation_temp[spec]    
                correlation_results[k].append(correlation)  

    print(spec)
    print(len(acf_results[k]))
    ###avg###
    ##acf
    acf_avg = []  # 用于存储每个 t_k 对应的均值

    for k in range(len(step)):  # 遍历不同的 t_k
        if len(acf_results[k]) > 0:  # 确保列表非空
            acf_avg.append(np.mean(acf_results[k]))  # 计算均值
        else:
            acf_avg.append(0)  # 如果列表为空，存 0 或 NaN


    ##correlation
    correlation_avg = []  # 用于存储每个 t_k 对应的均值

    for k in range(len(step)):  # 遍历不同的 t_k
        if len(correlation_results[k]) > 0:  # 确保列表非空
            correlation_avg.append(np.mean(correlation_results[k]))  # 计算均值
        else:
            correlation_avg.append(0)  # 如果列表为空，存 0 或 NaN


    ###save###

    #1找到 acf_results 中最长的行数（即最多的 (i, j) 组合）
    max_len = max(len(acf) for acf in acf_results)

    #创建填充后的数组
    acf_matrix = np.full((max_len, len(step)), np.nan)  # 用 NaN 填充，shape: (max_len, len(step))
    print(acf_matrix.shape)
    #填充数据
    for k in range(len(step)):
        acf_values = np.array(acf_results[k])  # 转换为 NumPy 数组
        acf_matrix[: len(acf_values), k] = acf_values  # 填充到对应列

    #保存 ACF 数据
    np.savetxt("./acf/acf_results_k={}.dat".format(spec+1), acf_matrix, fmt="%.6f", delimiter=" ")

    #保存 ACF 平均值
    step_array = np.array(step) * 20
    np.savetxt("./acf/acf_avg_k={}.dat".format(spec+1), np.column_stack((step_array, acf_avg)), fmt="%.6f", delimiter=" ", header="acf_avg")



    #2找到 correlation_results 中最长的行数（即最多的 (i, j) 组合）
    max_len = max(len(correlation) for correlation in correlation_results)

    #创建填充后的数组
    correlation_matrix = np.full((max_len, len(step)), np.nan)  # 用 NaN 填充，shape: (max_len, len(step))

    #填充数据
    for k in range(len(step)):
        correlation_values = np.array(correlation_results[k])  # 转换为 NumPy 数组
        correlation_matrix[: len(correlation_values), k] = correlation_values  # 填充到对应列

    #保存 correlation数据
    np.savetxt("./correlation/correlation_results_k={}.dat".format(spec+1), correlation_matrix, fmt="%.6f", delimiter=" ")

    #保存 correlation 平均值
    step_array = np.array(step) * 20
    np.savetxt("./correlation/correlation_avg_k={}.dat".format(spec+1), np.column_stack((step_array, correlation_avg)), fmt="%.6f", delimiter=" ", header="correlation_avg")













