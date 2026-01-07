"""
@author: admin
"""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import os
import matplotlib as mpl

time_steps = 600
case_number_list =[30,1,10,20]

for k, case_number in enumerate(case_number_list):
    #-------------------------------------------------------------读入数据，

    ######single case##############
    fDNS_all_cases = []
    IUFNO_40ep_all_cases = []
    F_IUFNO_40ep_all_cases = []
    F_IFNO_40ep_all_cases = []
    IFNO_all_cases = []
    DSM_all_cases = []
    

    # 循环加载 1 到 30 的数据
    for case_number in range(1, case_number+1):
        # fDNS 数据加载
        fDNS_0= np.loadtxt("../../../fDNS/N{}/avg_fDNS_{}case_vel_spec.dat".format(case_number, case_number), dtype=float)
       
        
        # IUFNO_40ep 数据加载
        IUFNO_40ep_0 = np.loadtxt("../../../IUFNO_40ep_k=1,2/N{}/avg_{}case_vel_spec.dat".format(case_number, case_number), dtype=float)
       
        
        # F_IUFNO_40ep 数据加载
        F_IUFNO_40ep_0 = np.loadtxt("../../../F-IUFNO_40ep_k=1,2/N{}/avg_{}case_vel_spec.dat".format(case_number, case_number), dtype=float)
        
        # F_IFNO_40ep 数据加载
        F_IFNO_40ep_0 = np.loadtxt("../../../F-IFNO_40ep_k=1,2/N{}/avg_{}case_vel_spec.dat".format(case_number, case_number), dtype=float)

        # IFNO 数据加载
        IFNO_0 = np.loadtxt("../../../IFNO_40ep_k=1,2/N{}/avg_{}case_vel_spec.dat".format(case_number, case_number), dtype=float)
        
        # DSM 数据加载
        DSM_0 = np.loadtxt("../../../DSM/N{}/avg_DSM_{}case_vel_spec.dat".format(case_number, case_number), dtype=float)
      
        fDNS_all_cases.append(fDNS_0)
        IUFNO_40ep_all_cases.append(IUFNO_40ep_0)
        F_IUFNO_40ep_all_cases.append(F_IUFNO_40ep_0)
        F_IFNO_40ep_all_cases.append(F_IFNO_40ep_0)
        IFNO_all_cases.append(IFNO_0)
        DSM_all_cases.append(DSM_0) 


    fDNS = np.vstack(fDNS_all_cases)                
    IUFNO_40ep = np.vstack(IUFNO_40ep_all_cases)       
    F_IUFNO_40ep = np.vstack(F_IUFNO_40ep_all_cases)  
    F_IFNO_40ep = np.vstack(F_IFNO_40ep_all_cases)  
    IFNO = np.vstack(IFNO_all_cases)  
    DSM = np.vstack(DSM_all_cases)  

    # 打印 fDNS 的形状
    print(f"fDNS shape for case {case_number}: {fDNS.shape}")

    #-------------------------输入参数
    period = 10 #10个波数
    # time_advance=[20]  #挑推进时间画图
    # time_advance=[40]  #挑推进时间画图
    #time_advance=[1,2,3,10,15,20,25,30,40,50,60,70,80,90,100,110,120,130,140,150,160,170,180,190,200,210,220,230,240,250]  #挑推进时间画图

    #time avg###
    fDNS_time_avg = [0.0] * period  # 初始化为长度为 period 的列表
    fDNS_time_avg= np.loadtxt("./fDNS_time_avg_vel_spec_{}case.dat".format(case_number),dtype=float)
    print("fDNS_time_avg:", fDNS_time_avg)

    #--------------------------
    y_fDNS1=[]
    #y_DSM=[]
    #y_DMM=[]

    y_F_IFNO_40ep=[]
    y_F_IUFNO_40ep=[]
    y_IUFNO_40ep=[]
    y_IFNO=[]
    y_DSM=[]

 
    for i in range(case_number*time_steps):
        fDNS1=0
        F_IFNO_40ep1=0
        F_IUFNO_40ep1=0
        IUFNO_40ep1=0
        IFNO1=0
        DSM1=0

        
        for j in range(period):
            fDNS1=(fDNS[j+period*i, 1]-fDNS_time_avg[j, 1])
            F_IFNO_40ep1=(F_IFNO_40ep[j+period*i, 1]-fDNS_time_avg[j, 1])
            F_IUFNO_40ep1=(F_IUFNO_40ep[j+period*i, 1]-fDNS_time_avg[j, 1])
            IUFNO_40ep1=(IUFNO_40ep[j+period*i, 1]-fDNS_time_avg[j, 1])
            IFNO1=(IFNO[j+period*i, 1]-fDNS_time_avg[j, 1])
            DSM1=(DSM[j+period*i, 1]-fDNS_time_avg[j, 1])

            
            y_F_IFNO_40ep.append(F_IFNO_40ep1)  
            y_F_IUFNO_40ep.append(F_IUFNO_40ep1)
            y_IUFNO_40ep.append(IUFNO_40ep1)
            y_IFNO.append(IFNO1)
            y_DSM.append(DSM1)
            y_fDNS1.append(fDNS1)

   
    #####savefiles###########
    step = np.arange(1, period*time_steps + 1)
    step = np.tile(step, case_number)  # 生成一维数组
    print(f"Shape of step: {step.shape}")
    y_F_IFNO_40ep = np.array(y_F_IFNO_40ep)
    print(f"Shape of y_F_IFNO_40ep: {y_F_IFNO_40ep.shape}")
    data1 = np.column_stack((step, y_fDNS1))    
    data2 = np.column_stack((step, y_F_IFNO_40ep))
    data3 = np.column_stack((step, y_F_IUFNO_40ep))
    data4 = np.column_stack((step, y_IUFNO_40ep))
    data5 = np.column_stack((step, y_IFNO))
    data6 = np.column_stack((step, y_DSM))
  
  
    # 将数据保存到 .dat 文件中
    np.savetxt('./result/{}cases/error_with_time_fDNS.dat'.format(case_number), data1, fmt='%d %.16f')
    np.savetxt('./result/{}cases/error_with_time_F_IFNO.dat'.format(case_number), data2, fmt='%d %.16f')
    np.savetxt('./result/{}cases/error_with_time_F_IUFNO.dat'.format(case_number), data3, fmt='%d %.16f')
    np.savetxt('./result/{}cases/error_with_time_IUFNO.dat'.format(case_number), data4, fmt='%d %.16f')
    np.savetxt('./result/{}cases/error_with_time_IFNO.dat'.format(case_number), data5, fmt='%d %.16f')
    np.savetxt('./result/{}cases/error_with_time_DSM.dat'.format(case_number), data6, fmt='%d %.16f')





