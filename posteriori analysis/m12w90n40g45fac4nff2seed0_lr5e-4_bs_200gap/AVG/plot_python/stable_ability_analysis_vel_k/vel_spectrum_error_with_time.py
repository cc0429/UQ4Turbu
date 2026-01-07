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
    IUFNO_all_cases = []
    F_IUFNO_all_cases = []
    F_IFNO_all_cases = []
    IFNO_all_cases = []
    DSM_all_cases = []
    
    IUFNO_m01_all_cases = []
    F_IUFNO_m01_all_cases = []
    F_IFNO_m01_all_cases = []
    IFNO_m01_all_cases = []
    DSM_m01_all_cases = []
    
    IUFNO_m05_all_cases = []
    F_IUFNO_m05_all_cases = []
    F_IFNO_m05_all_cases = []
    IFNO_m05_all_cases = []
    DSM_m05_all_cases = []    
    
    IUFNO_m1_all_cases = []
    F_IUFNO_m1_all_cases = []
    F_IFNO_m1_all_cases = []
    IFNO_m1_all_cases = []
    DSM_m1_all_cases = []    
    
    IUFNO_m2_all_cases = []
    F_IUFNO_m2_all_cases = []
    F_IFNO_m2_all_cases = []
    IFNO_m2_all_cases = []
    DSM_m2_all_cases = []    
    
    IUFNO_m5_all_cases = []
    F_IUFNO_m5_all_cases = []
    F_IFNO_m5_all_cases = []
    IFNO_m5_all_cases = []
    DSM_m5_all_cases = []    
    
     
    IUFNO_m10_all_cases = []
    F_IUFNO_m10_all_cases = []
    F_IFNO_m10_all_cases = []
    IFNO_m10_all_cases = []
    DSM_m10_all_cases = []     

    # 循环加载 1 到 30 的数据
    for case_number in range(1, case_number+1):
        # fDNS 数据加载
        fDNS_0= np.loadtxt("../../fDNS/N{}/avg_fDNS_{}case_vel_spec.dat".format(case_number, case_number), dtype=float)

        # IUFNO 数据加载
        IUFNO_0 = np.loadtxt("../../IUFNO_40ep/N{}/avg_IUFNO_{}case_vel_spec.dat".format(case_number, case_number), dtype=float)
        IUFNO_m01_0 = np.loadtxt("../../IUFNO_40ep_mag0.1/N{}/avg_IUFNO_{}case_vel_spec.dat".format(case_number, case_number), dtype=float)
        IUFNO_m05_0 = np.loadtxt("../../IUFNO_40ep_mag0.5/N{}/avg_IUFNO_{}case_vel_spec.dat".format(case_number, case_number), dtype=float)
        IUFNO_m1_0 = np.loadtxt("../../IUFNO_40ep_mag1/N{}/avg_{}case_vel_spec.dat".format(case_number, case_number), dtype=float)
        IUFNO_m2_0 = np.loadtxt("../../IUFNO_40ep_mag2/N{}/avg_{}case_vel_spec.dat".format(case_number, case_number), dtype=float)
        IUFNO_m5_0 = np.loadtxt("../../IUFNO_40ep_mag5/N{}/avg_{}case_vel_spec.dat".format(case_number, case_number), dtype=float)
        IUFNO_m10_0 = np.loadtxt("../../IUFNO_40ep_mag10/N{}/avg_{}case_vel_spec.dat".format(case_number, case_number), dtype=float)
        
        # F_IUFNO 数据加载
        F_IUFNO_0 = np.loadtxt("../../F-IUFNO_40ep/N{}/avg_FIUFNO_{}case_vel_spec.dat".format(case_number, case_number), dtype=float)
        F_IUFNO_m01_0 = np.loadtxt("../../F-IUFNO_40ep_mag0.1/N{}/avg_FIUFNO_{}case_vel_spec.dat".format(case_number, case_number), dtype=float)
        F_IUFNO_m05_0 = np.loadtxt("../../F-IUFNO_40ep_mag0.5/N{}/avg_FIUFNO_{}case_vel_spec.dat".format(case_number, case_number), dtype=float)
        F_IUFNO_m1_0 = np.loadtxt("../../F-IUFNO_40ep_mag1/N{}/avg_{}case_vel_spec.dat".format(case_number, case_number), dtype=float)
        F_IUFNO_m2_0 = np.loadtxt("../../F-IUFNO_40ep_mag2/N{}/avg_{}case_vel_spec.dat".format(case_number, case_number), dtype=float)
        F_IUFNO_m5_0 = np.loadtxt("../../F-IUFNO_40ep_mag5/N{}/avg_{}case_vel_spec.dat".format(case_number, case_number), dtype=float)
        F_IUFNO_m10_0 = np.loadtxt("../../F-IUFNO_40ep_mag10/N{}/avg_{}case_vel_spec.dat".format(case_number, case_number), dtype=float)
        

        # F_IFNO数据加载
        F_IFNO_0 = np.loadtxt("../../F-IFNO_40ep/N{}/avg_FIFNO_{}case_vel_spec.dat".format(case_number, case_number), dtype=float)
        F_IFNO_m01_0 = np.loadtxt("../../F-IFNO_40ep_mag0.1/N{}/avg_FIFNO_{}case_vel_spec.dat".format(case_number, case_number), dtype=float)
        F_IFNO_m05_0 = np.loadtxt("../../F-IFNO_40ep_mag0.5/N{}/avg_FIFNO_{}case_vel_spec.dat".format(case_number, case_number), dtype=float)
        F_IFNO_m1_0 = np.loadtxt("../../F-IFNO_40ep_mag1/N{}/avg_FIFNO_{}case_vel_spec.dat".format(case_number, case_number), dtype=float)
        F_IFNO_m2_0 = np.loadtxt("../../F-IFNO_40ep_mag2/N{}/avg_FIFNO_{}case_vel_spec.dat".format(case_number, case_number), dtype=float)
        F_IFNO_m5_0 = np.loadtxt("../../F-IFNO_40ep_mag5/N{}/avg_FIFNO_{}case_vel_spec.dat".format(case_number, case_number), dtype=float)
        F_IFNO_m10_0 = np.loadtxt("../../F-IFNO_40ep_mag10/N{}/avg_FIFNO_{}case_vel_spec.dat".format(case_number, case_number), dtype=float)

        # IFNO 数据加载
        IFNO_0 = np.loadtxt("../../IFNO_40ep/N{}/avg_IFNO_{}case_vel_spec.dat".format(case_number, case_number), dtype=float)
        IFNO_m01_0 = np.loadtxt("../../IFNO_40ep_mag0.1/N{}/avg_IFNO_{}case_vel_spec.dat".format(case_number, case_number), dtype=float)
        IFNO_m05_0 = np.loadtxt("../../IFNO_40ep_mag0.5/N{}/avg_IFNO_{}case_vel_spec.dat".format(case_number, case_number), dtype=float)
        IFNO_m1_0 = np.loadtxt("../../IFNO_40ep_mag1/N{}/avg_{}case_vel_spec.dat".format(case_number, case_number), dtype=float)
        IFNO_m2_0 = np.loadtxt("../../IFNO_40ep_mag2/N{}/avg_{}case_vel_spec.dat".format(case_number, case_number), dtype=float)
        IFNO_m5_0 = np.loadtxt("../../IFNO_40ep_mag5/N{}/avg_{}case_vel_spec.dat".format(case_number, case_number), dtype=float)
        IFNO_m10_0 = np.loadtxt("../../IFNO_40ep_mag10/N{}/avg_{}case_vel_spec.dat".format(case_number, case_number), dtype=float)


        
        # DSM 数据加载
        DSM_0 = np.loadtxt("../../DSM/N{}/avg_DSM_{}case_vel_spec.dat".format(case_number, case_number), dtype=float)
        DSM_m01_0 = np.loadtxt("../../DSM_mag0.1/N{}/avg_DSM_mag0.1_{}case_vel_spec.dat".format(case_number, case_number), dtype=float)
        DSM_m05_0 = np.loadtxt("../../DSM_mag0.5/N{}/avg_DSM_mag0.5_{}case_vel_spec.dat".format(case_number, case_number), dtype=float)
        DSM_m1_0 = np.loadtxt("../../DSM_mag1/N{}/avg_DSM_{}case_vel_spec.dat".format(case_number, case_number), dtype=float)
        DSM_m2_0 = np.loadtxt("../../DSM_mag2/N{}/avg_DSM_{}case_vel_spec.dat".format(case_number, case_number), dtype=float)
        DSM_m5_0 = np.loadtxt("../../DSM_mag5/N{}/avg_DSM_{}case_vel_spec.dat".format(case_number, case_number), dtype=float)
        DSM_m10_0 = np.loadtxt("../../DSM_mag10/N{}/avg_DSM_{}case_vel_spec.dat".format(case_number, case_number), dtype=float)
      
        fDNS_all_cases.append(fDNS_0)
        IUFNO_all_cases.append(IUFNO_0)
        F_IUFNO_all_cases.append(F_IUFNO_0)
        F_IFNO_all_cases.append(F_IFNO_0)
        IFNO_all_cases.append(IFNO_0)
        DSM_all_cases.append(DSM_0)

        IUFNO_m01_all_cases.append(IUFNO_m01_0)
        F_IUFNO_m01_all_cases.append(F_IUFNO_m01_0)
        F_IFNO_m01_all_cases.append(F_IFNO_m01_0)
        IFNO_m01_all_cases.append(IFNO_m01_0)
        DSM_m01_all_cases.append(DSM_m01_0)
        
        IUFNO_m05_all_cases.append(IUFNO_m05_0)
        F_IUFNO_m05_all_cases.append(F_IUFNO_m05_0)
        F_IFNO_m05_all_cases.append(F_IFNO_m05_0)
        IFNO_m05_all_cases.append(IFNO_m05_0)
        DSM_m05_all_cases.append(DSM_m05_0)        
        
        IUFNO_m1_all_cases.append(IUFNO_m1_0)
        F_IUFNO_m1_all_cases.append(F_IUFNO_m1_0)
        F_IFNO_m1_all_cases.append(F_IFNO_m1_0)
        IFNO_m1_all_cases.append(IFNO_m1_0)
        DSM_m1_all_cases.append(DSM_m1_0)        
        
        IUFNO_m2_all_cases.append(IUFNO_m2_0)
        F_IUFNO_m2_all_cases.append(F_IUFNO_m2_0)
        F_IFNO_m2_all_cases.append(F_IFNO_m2_0)
        IFNO_m2_all_cases.append(IFNO_m2_0)
        DSM_m2_all_cases.append(DSM_m2_0)
        
        IUFNO_m5_all_cases.append(IUFNO_m5_0)
        F_IUFNO_m5_all_cases.append(F_IUFNO_m5_0)
        F_IFNO_m5_all_cases.append(F_IFNO_m5_0)
        IFNO_m5_all_cases.append(IFNO_m5_0)
        DSM_m5_all_cases.append(DSM_m5_0)        
        
        IUFNO_m10_all_cases.append(IUFNO_m10_0)
        F_IUFNO_m10_all_cases.append(F_IUFNO_m10_0)
        F_IFNO_m10_all_cases.append(F_IFNO_m10_0)
        IFNO_m10_all_cases.append(IFNO_m10_0)
        DSM_m10_all_cases.append(DSM_m10_0)          
        


    fDNS = np.vstack(fDNS_all_cases)    
    IUFNO = np.vstack(IUFNO_all_cases)                 
    F_IUFNO = np.vstack(F_IUFNO_all_cases)     
    F_IFNO = np.vstack(F_IFNO_all_cases)  
    IFNO = np.vstack(IFNO_all_cases)  
    DSM = np.vstack(DSM_all_cases)  

    IUFNO_m01 = np.vstack(IUFNO_m01_all_cases)                 
    F_IUFNO_m01 = np.vstack(F_IUFNO_m01_all_cases)     
    F_IFNO_m01 = np.vstack(F_IFNO_m01_all_cases)  
    IFNO_m01 = np.vstack(IFNO_m01_all_cases)  
    DSM_m01 = np.vstack(DSM_m01_all_cases)  

    IUFNO_m05 = np.vstack(IUFNO_m05_all_cases)                 
    F_IUFNO_m05 = np.vstack(F_IUFNO_m05_all_cases)     
    F_IFNO_m05 = np.vstack(F_IFNO_m05_all_cases)  
    IFNO_m05 = np.vstack(IFNO_m05_all_cases)  
    DSM_m05 = np.vstack(DSM_m05_all_cases)  

    IUFNO_m1 = np.vstack(IUFNO_m1_all_cases)                 
    F_IUFNO_m1 = np.vstack(F_IUFNO_m1_all_cases)     
    F_IFNO_m1 = np.vstack(F_IFNO_m1_all_cases)  
    IFNO_m1 = np.vstack(IFNO_m1_all_cases)  
    DSM_m1 = np.vstack(DSM_m1_all_cases)  

    IUFNO_m2 = np.vstack(IUFNO_m2_all_cases)                 
    F_IUFNO_m2 = np.vstack(F_IUFNO_m2_all_cases)     
    F_IFNO_m2 = np.vstack(F_IFNO_m2_all_cases)  
    IFNO_m2 = np.vstack(IFNO_m2_all_cases)  
    DSM_m2 = np.vstack(DSM_m2_all_cases)  

    IUFNO_m5 = np.vstack(IUFNO_m5_all_cases)                 
    F_IUFNO_m5 = np.vstack(F_IUFNO_m5_all_cases)     
    F_IFNO_m5 = np.vstack(F_IFNO_m5_all_cases)  
    IFNO_m5 = np.vstack(IFNO_m5_all_cases)  
    DSM_m5 = np.vstack(DSM_m5_all_cases)  

    IUFNO_m10 = np.vstack(IUFNO_m10_all_cases)                 
    F_IUFNO_m10 = np.vstack(F_IUFNO_m10_all_cases)     
    F_IFNO_m10 = np.vstack(F_IFNO_m10_all_cases)  
    IFNO_m10 = np.vstack(IFNO_m10_all_cases)  
    DSM_m10 = np.vstack(DSM_m10_all_cases)   

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

    y_F_IFNO=[]
    y_F_IUFNO=[]
    y_IUFNO=[]
    y_IFNO=[]
    y_DSM=[]

    y_F_IFNO_m01=[]
    y_F_IUFNO_m01=[]
    y_IUFNO_m01=[]
    y_IFNO_m01=[]
    y_DSM_m01=[]
    
    y_F_IFNO_m05=[]
    y_F_IUFNO_m05=[]
    y_IUFNO_m05=[]
    y_IFNO_m05=[]
    y_DSM_m05=[]    
    
    y_F_IFNO_m1=[]
    y_F_IUFNO_m1=[]
    y_IUFNO_m1=[]
    y_IFNO_m1=[]
    y_DSM_m1=[]    
    
    y_F_IFNO_m2=[]
    y_F_IUFNO_m2=[]
    y_IUFNO_m2=[]
    y_IFNO_m2=[]
    y_DSM_m2=[]    
    
    y_F_IFNO_m5=[]
    y_F_IUFNO_m5=[]
    y_IUFNO_m5=[]
    y_IFNO_m5=[]
    y_DSM_m5=[]    
    
    y_F_IFNO_m10=[]
    y_F_IUFNO_m10=[]
    y_IUFNO_m10=[]
    y_IFNO_m10=[]
    y_DSM_m10=[]

    for i in range(case_number*time_steps):
        fDNS1=0
        F_IFNO1=0
        F_IUFNO1=0
        IUFNO1=0
        IFNO1=0
        DSM1=0

        F_IFNO1_m01=0
        F_IUFNO1_m01=0
        IUFNO1_m01=0
        IFNO1_m01=0
        DSM1_m01=0          
        
        F_IFNO1_m05=0
        F_IUFNO1_m05=0
        IUFNO1_m05=0
        IFNO1_m05=0
        DSM1_m05=0 
        
        F_IFNO1_m1=0
        F_IUFNO1_m1=0
        IUFNO1_m1=0
        IFNO1_m1=0
        DSM1_m1=0        
        
        F_IFNO1_m2=0
        F_IUFNO1_m2=0
        IUFNO1_m2=0
        IFNO1_m2=0
        DSM1_m2=0

        F_IFNO1_m5=0
        F_IUFNO1_m5=0
        IUFNO1_m5=0
        IFNO1_m5=0
        DSM1_m5=0

        F_IFNO1_m10=0
        F_IUFNO1_m10=0
        IUFNO1_m10=0
        IFNO1_m10=0
        DSM1_m10=0
        
        for j in range(period):
            fDNS1=(fDNS[j+period*i, 1]-fDNS_time_avg[j, 1])
            F_IFNO1=(F_IFNO[j+period*i, 1]-fDNS_time_avg[j, 1])
            F_IUFNO1=(F_IUFNO[j+period*i, 1]-fDNS_time_avg[j, 1])
            IUFNO1=(IUFNO[j+period*i, 1]-fDNS_time_avg[j, 1])
            IFNO1=(IFNO[j+period*i, 1]-fDNS_time_avg[j, 1])
            DSM1=(DSM[j+period*i, 1]-fDNS_time_avg[j, 1])            
               
            F_IFNO1_m01=(F_IFNO_m01[j+period*i, 1]-fDNS_time_avg[j, 1])
            F_IUFNO1_m01=(F_IUFNO_m01[j+period*i, 1]-fDNS_time_avg[j, 1])
            IUFNO1_m01=(IUFNO_m01[j+period*i, 1]-fDNS_time_avg[j, 1])
            IFNO1_m01=(IFNO_m01[j+period*i, 1]-fDNS_time_avg[j, 1])
            DSM1_m01=(DSM_m01[j+period*i, 1]-fDNS_time_avg[j, 1])

            F_IFNO1_m05=(F_IFNO_m05[j+period*i, 1]-fDNS_time_avg[j, 1])
            F_IUFNO1_m05=(F_IUFNO_m05[j+period*i, 1]-fDNS_time_avg[j, 1])
            IUFNO1_m05=(IUFNO_m05[j+period*i, 1]-fDNS_time_avg[j, 1])
            IFNO1_m05=(IFNO_m05[j+period*i, 1]-fDNS_time_avg[j, 1])
            DSM1_m05=(DSM_m05[j+period*i, 1]-fDNS_time_avg[j, 1])

            F_IFNO1_m1=(F_IFNO_m1[j+period*i, 1]-fDNS_time_avg[j, 1])
            F_IUFNO1_m1=(F_IUFNO_m1[j+period*i, 1]-fDNS_time_avg[j, 1])
            IUFNO1_m1=(IUFNO_m1[j+period*i, 1]-fDNS_time_avg[j, 1])
            IFNO1_m1=(IFNO_m1[j+period*i, 1]-fDNS_time_avg[j, 1])
            DSM1_m1=(DSM_m1[j+period*i, 1]-fDNS_time_avg[j, 1])

            F_IFNO1_m2=(F_IFNO_m2[j+period*i, 1]-fDNS_time_avg[j, 1])
            F_IUFNO1_m2=(F_IUFNO_m2[j+period*i, 1]-fDNS_time_avg[j, 1])
            IUFNO1_m2=(IUFNO_m2[j+period*i, 1]-fDNS_time_avg[j, 1])
            IFNO1_m2=(IFNO_m2[j+period*i, 1]-fDNS_time_avg[j, 1])
            DSM1_m2=(DSM_m2[j+period*i, 1]-fDNS_time_avg[j, 1])

            F_IFNO1_m5=(F_IFNO_m5[j+period*i, 1]-fDNS_time_avg[j, 1])
            F_IUFNO1_m5=(F_IUFNO_m5[j+period*i, 1]-fDNS_time_avg[j, 1])
            IUFNO1_m5=(IUFNO_m5[j+period*i, 1]-fDNS_time_avg[j, 1])
            IFNO1_m5=(IFNO_m5[j+period*i, 1]-fDNS_time_avg[j, 1])
            DSM1_m5=(DSM_m5[j+period*i, 1]-fDNS_time_avg[j, 1])

            F_IFNO1_m10=(F_IFNO_m10[j+period*i, 1]-fDNS_time_avg[j, 1])
            F_IUFNO1_m10=(F_IUFNO_m10[j+period*i, 1]-fDNS_time_avg[j, 1])
            IUFNO1_m10=(IUFNO_m10[j+period*i, 1]-fDNS_time_avg[j, 1])
            IFNO1_m10=(IFNO_m10[j+period*i, 1]-fDNS_time_avg[j, 1])
            DSM1_m10=(DSM_m10[j+period*i, 1]-fDNS_time_avg[j, 1])

            
            y_F_IFNO.append(F_IFNO1)  
            y_F_IUFNO.append(F_IUFNO1)
            y_IUFNO.append(IUFNO1)
            y_IFNO.append(IFNO1)
            y_DSM.append(DSM1)
            y_fDNS1.append(fDNS1)

            y_F_IFNO_m01.append(F_IFNO1_m01)  
            y_F_IUFNO_m01.append(F_IUFNO1_m01)
            y_IUFNO_m01.append(IUFNO1_m01)
            y_IFNO_m01.append(IFNO1_m01)
            y_DSM_m01.append(DSM1_m01)
            
            y_F_IFNO_m05.append(F_IFNO1_m05)  
            y_F_IUFNO_m05.append(F_IUFNO1_m05)
            y_IUFNO_m05.append(IUFNO1_m05)
            y_IFNO_m05.append(IFNO1_m05)
            y_DSM_m05.append(DSM1_m05)            
            
            y_F_IFNO_m1.append(F_IFNO1_m1)  
            y_F_IUFNO_m1.append(F_IUFNO1_m1)
            y_IUFNO_m1.append(IUFNO1_m1)
            y_IFNO_m1.append(IFNO1_m1)
            y_DSM_m1.append(DSM1_m1)           

            y_F_IFNO_m2.append(F_IFNO1_m2)  
            y_F_IUFNO_m2.append(F_IUFNO1_m2)
            y_IUFNO_m2.append(IUFNO1_m2)
            y_IFNO_m2.append(IFNO1_m2)
            y_DSM_m2.append(DSM1_m2)
            
            y_F_IFNO_m5.append(F_IFNO1_m5)  
            y_F_IUFNO_m5.append(F_IUFNO1_m5)
            y_IUFNO_m5.append(IUFNO1_m5)
            y_IFNO_m5.append(IFNO1_m5)
            y_DSM_m5.append(DSM1_m5)            
            
            y_F_IFNO_m10.append(F_IFNO1_m10)  
            y_F_IUFNO_m10.append(F_IUFNO1_m10)
            y_IUFNO_m10.append(IUFNO1_m10)
            y_IFNO_m10.append(IFNO1_m10)
            y_DSM_m10.append(DSM1_m10)             
            
            
    #####savefiles###########
    step = np.arange(1, period*time_steps + 1)
    step = np.tile(step, case_number)  # 生成一维数组
    print(f"Shape of step: {step.shape}")
    y_F_IFNO = np.array(y_F_IFNO)
    print(f"Shape of y_F_IFNO: {y_F_IFNO.shape}")
    data1 = np.column_stack((step, y_fDNS1))    
    data2 = np.column_stack((step, y_F_IFNO))
    data3 = np.column_stack((step, y_F_IUFNO))
    data4 = np.column_stack((step, y_IUFNO))
    data5 = np.column_stack((step, y_IFNO))
    data6 = np.column_stack((step, y_DSM))
   
    data7 = np.column_stack((step, y_F_IFNO_m01))
    data8 = np.column_stack((step, y_F_IUFNO_m01))
    data9 = np.column_stack((step, y_IUFNO_m01))
    data10 = np.column_stack((step, y_IFNO_m01))
    data11 = np.column_stack((step, y_DSM_m01))
   
    data12 = np.column_stack((step, y_F_IFNO_m05))
    data13 = np.column_stack((step, y_F_IUFNO_m05))
    data14 = np.column_stack((step, y_IUFNO_m05))
    data15 = np.column_stack((step, y_IFNO_m05))
    data16 = np.column_stack((step, y_DSM_m05))
  
    data17 = np.column_stack((step, y_F_IFNO_m1))
    data18 = np.column_stack((step, y_F_IUFNO_m1))
    data19 = np.column_stack((step, y_IUFNO_m1))
    data20 = np.column_stack((step, y_IFNO_m1))
    data21 = np.column_stack((step, y_DSM_m1))

    data22 = np.column_stack((step, y_F_IFNO_m2))
    data23 = np.column_stack((step, y_F_IUFNO_m2))
    data24 = np.column_stack((step, y_IUFNO_m2))
    data25 = np.column_stack((step, y_IFNO_m2))
    data26 = np.column_stack((step, y_DSM_m2))

    data27 = np.column_stack((step, y_F_IFNO_m5))
    data28 = np.column_stack((step, y_F_IUFNO_m5))
    data29 = np.column_stack((step, y_IUFNO_m5))
    data30 = np.column_stack((step, y_IFNO_m5))
    data31 = np.column_stack((step, y_DSM_m5))

    data32 = np.column_stack((step, y_F_IFNO_m10))
    data33 = np.column_stack((step, y_F_IUFNO_m10))
    data34 = np.column_stack((step, y_IUFNO_m10))
    data35 = np.column_stack((step, y_IFNO_m10))
    data36 = np.column_stack((step, y_DSM_m10)) 
  
    # 将数据保存到 .dat 文件中
    np.savetxt('./result/{}cases/error_with_time_fDNS.dat'.format(case_number), data1, fmt='%d %.16f')
    np.savetxt('./result/{}cases/error_with_time_F_IFNO.dat'.format(case_number), data2, fmt='%d %.16f')
    np.savetxt('./result/{}cases/error_with_time_F_IUFNO.dat'.format(case_number), data3, fmt='%d %.16f')
    np.savetxt('./result/{}cases/error_with_time_IUFNO.dat'.format(case_number), data4, fmt='%d %.16f')
    np.savetxt('./result/{}cases/error_with_time_IFNO.dat'.format(case_number), data5, fmt='%d %.16f')
    np.savetxt('./result/{}cases/error_with_time_DSM.dat'.format(case_number), data6, fmt='%d %.16f')
 
    np.savetxt('./result/{}cases/error_with_time_F_IFNO_m01.dat'.format(case_number), data7, fmt='%d %.16f')
    np.savetxt('./result/{}cases/error_with_time_F_IUFNO_m01.dat'.format(case_number), data8, fmt='%d %.16f')
    np.savetxt('./result/{}cases/error_with_time_IUFNO_m01.dat'.format(case_number), data9, fmt='%d %.16f')
    np.savetxt('./result/{}cases/error_with_time_IFNO_m01.dat'.format(case_number), data10, fmt='%d %.16f')
    np.savetxt('./result/{}cases/error_with_time_DSM_m01.dat'.format(case_number), data11, fmt='%d %.16f')    

    np.savetxt('./result/{}cases/error_with_time_F_IFNO_m05.dat'.format(case_number), data12, fmt='%d %.16f')
    np.savetxt('./result/{}cases/error_with_time_F_IUFNO_m05.dat'.format(case_number), data13, fmt='%d %.16f')
    np.savetxt('./result/{}cases/error_with_time_IUFNO_m05.dat'.format(case_number), data14, fmt='%d %.16f')
    np.savetxt('./result/{}cases/error_with_time_IFNO_m05.dat'.format(case_number), data15, fmt='%d %.16f')
    np.savetxt('./result/{}cases/error_with_time_DSM_m05.dat'.format(case_number), data16, fmt='%d %.16f')

    np.savetxt('./result/{}cases/error_with_time_F_IFNO_m1.dat'.format(case_number), data17, fmt='%d %.16f')
    np.savetxt('./result/{}cases/error_with_time_F_IUFNO_m1.dat'.format(case_number), data18, fmt='%d %.16f')
    np.savetxt('./result/{}cases/error_with_time_IUFNO_m1.dat'.format(case_number), data19, fmt='%d %.16f')
    np.savetxt('./result/{}cases/error_with_time_IFNO_m1.dat'.format(case_number), data20, fmt='%d %.16f')
    np.savetxt('./result/{}cases/error_with_time_DSM_m1.dat'.format(case_number), data21, fmt='%d %.16f')
 
    np.savetxt('./result/{}cases/error_with_time_F_IFNO_m2.dat'.format(case_number), data22, fmt='%d %.16f')
    np.savetxt('./result/{}cases/error_with_time_F_IUFNO_m2.dat'.format(case_number), data23, fmt='%d %.16f')
    np.savetxt('./result/{}cases/error_with_time_IUFNO_m2.dat'.format(case_number), data24, fmt='%d %.16f')
    np.savetxt('./result/{}cases/error_with_time_IFNO_m2.dat'.format(case_number), data25, fmt='%d %.16f')
    np.savetxt('./result/{}cases/error_with_time_DSM_m2.dat'.format(case_number), data26, fmt='%d %.16f')    

    np.savetxt('./result/{}cases/error_with_time_F_IFNO_m5.dat'.format(case_number), data27, fmt='%d %.16f')
    np.savetxt('./result/{}cases/error_with_time_F_IUFNO_m5.dat'.format(case_number), data28, fmt='%d %.16f')
    np.savetxt('./result/{}cases/error_with_time_IUFNO_m5.dat'.format(case_number), data29, fmt='%d %.16f')
    np.savetxt('./result/{}cases/error_with_time_IFNO_m5.dat'.format(case_number), data30, fmt='%d %.16f')
    np.savetxt('./result/{}cases/error_with_time_DSM_m5.dat'.format(case_number), data31, fmt='%d %.16f')

    np.savetxt('./result/{}cases/error_with_time_F_IFNO_m10.dat'.format(case_number), data32, fmt='%d %.16f')
    np.savetxt('./result/{}cases/error_with_time_F_IUFNO_m10.dat'.format(case_number), data33, fmt='%d %.16f')
    np.savetxt('./result/{}cases/error_with_time_IUFNO_m10.dat'.format(case_number), data34, fmt='%d %.16f')
    np.savetxt('./result/{}cases/error_with_time_IFNO_m10.dat'.format(case_number), data35, fmt='%d %.16f')
    np.savetxt('./result/{}cases/error_with_time_DSM_m10.dat'.format(case_number), data36, fmt='%d %.16f')




