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
vel_k_list = [1,2,3,4,5,6,7,8,9,10]

for kk, case_number in enumerate(case_number_list):
    for k, vel_k in enumerate(vel_k_list):
        #-------------------------------------------------------------读入数据，
        #######avg case#########

        fDNS= np.loadtxt("./result/{}cases/error_with_time_fDNS.dat".format(case_number),dtype=float)
        IUFNO_40ep= np.loadtxt("./result/{}cases/error_with_time_IUFNO.dat".format(case_number),dtype=float)
        F_IUFNO_40ep= np.loadtxt("./result/{}cases/error_with_time_F_IUFNO.dat".format(case_number),dtype=float)
        F_IFNO_40ep= np.loadtxt("./result/{}cases/error_with_time_F_IFNO.dat".format(case_number),dtype=float)
        IFNO= np.loadtxt("./result/{}cases/error_with_time_IFNO.dat".format(case_number),dtype=float)
        DSM= np.loadtxt("./result/{}cases/error_with_time_DSM.dat".format(case_number),dtype=float)
               
        
        #-------------------------输入参数
        period = 10 #10个波数

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
             
            for j in range(1):

                F_IFNO_40ep1=(F_IFNO_40ep[vel_k-1+period*i, 1])
                F_IUFNO_40ep1=(F_IUFNO_40ep[vel_k-1+period*i, 1])
                IUFNO_40ep1=(IUFNO_40ep[vel_k-1+period*i, 1])
                IFNO1=(IFNO[vel_k-1+period*i, 1])
                DSM1=(DSM[vel_k-1+period*i, 1])
                fDNS1=(fDNS[vel_k-1+period*i, 1])

                
                y_F_IFNO_40ep.append(F_IFNO_40ep1)  
                y_F_IUFNO_40ep.append(F_IUFNO_40ep1)
                y_IUFNO_40ep.append(IUFNO_40ep1)
                y_IFNO.append(IFNO1) 
                y_DSM.append(DSM1)
                y_fDNS1.append(fDNS1)

         
        #####savefiles###########
        step = np.arange(1, time_steps + 1)
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
        np.savetxt('./result/{}cases/error_with_time_fDNS_k={}.dat'.format(case_number,vel_k), data1, fmt='%d %.16f')
        np.savetxt('./result/{}cases/error_with_time_F_IFNO_k={}.dat'.format(case_number,vel_k), data2, fmt='%d %.16f')
        np.savetxt('./result/{}cases/error_with_time_F_IUFNO_k={}.dat'.format(case_number,vel_k), data3, fmt='%d %.16f')
        np.savetxt('./result/{}cases/error_with_time_IUFNO_k={}.dat'.format(case_number,vel_k), data4, fmt='%d %.16f')
        np.savetxt('./result/{}cases/error_with_time_IFNO_k={}.dat'.format(case_number,vel_k), data5, fmt='%d %.16f')
        np.savetxt('./result/{}cases/error_with_time_DSM_k={}.dat'.format(case_number,vel_k), data6, fmt='%d %.16f')





