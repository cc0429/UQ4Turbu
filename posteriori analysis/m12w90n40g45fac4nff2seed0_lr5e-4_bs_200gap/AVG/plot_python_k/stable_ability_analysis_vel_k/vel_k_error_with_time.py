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


        fDNS = np.loadtxt("./result/{}cases/error_with_time_fDNS.dat".format(case_number), dtype=float)
        IUFNO = np.loadtxt("./result/{}cases/error_with_time_IUFNO.dat".format(case_number), dtype=float)
        F_IUFNO = np.loadtxt("./result/{}cases/error_with_time_F_IUFNO.dat".format(case_number), dtype=float)
        F_IFNO = np.loadtxt("./result/{}cases/error_with_time_F_IFNO.dat".format(case_number), dtype=float)
        IFNO = np.loadtxt("./result/{}cases/error_with_time_IFNO.dat".format(case_number), dtype=float)
        DSM = np.loadtxt("./result/{}cases/error_with_time_DSM.dat".format(case_number), dtype=float)
        
        IUFNO_m01 = np.loadtxt("./result/{}cases/error_with_time_IUFNO_m01.dat".format(case_number), dtype=float)
        F_IUFNO_m01 = np.loadtxt("./result/{}cases/error_with_time_F_IUFNO_m01.dat".format(case_number), dtype=float)
        F_IFNO_m01 = np.loadtxt("./result/{}cases/error_with_time_F_IFNO_m01.dat".format(case_number), dtype=float)
        IFNO_m01 = np.loadtxt("./result/{}cases/error_with_time_IFNO_m01.dat".format(case_number), dtype=float)
        DSM_m01 = np.loadtxt("./result/{}cases/error_with_time_DSM_m01.dat".format(case_number), dtype=float)
        
        IUFNO_m05 = np.loadtxt("./result/{}cases/error_with_time_IUFNO_m05.dat".format(case_number), dtype=float)
        F_IUFNO_m05 = np.loadtxt("./result/{}cases/error_with_time_F_IUFNO_m05.dat".format(case_number), dtype=float)
        F_IFNO_m05 = np.loadtxt("./result/{}cases/error_with_time_F_IFNO_m05.dat".format(case_number), dtype=float)
        IFNO_m05 = np.loadtxt("./result/{}cases/error_with_time_IFNO_m05.dat".format(case_number), dtype=float)
        DSM_m05 = np.loadtxt("./result/{}cases/error_with_time_DSM_m05.dat".format(case_number), dtype=float)    
        
        IUFNO_m1 = np.loadtxt("./result/{}cases/error_with_time_IUFNO_m1.dat".format(case_number), dtype=float)
        F_IUFNO_m1 = np.loadtxt("./result/{}cases/error_with_time_F_IUFNO_m1.dat".format(case_number), dtype=float)
        F_IFNO_m1 = np.loadtxt("./result/{}cases/error_with_time_F_IFNO_m1.dat".format(case_number), dtype=float)
        IFNO_m1 = np.loadtxt("./result/{}cases/error_with_time_IFNO_m1.dat".format(case_number), dtype=float)
        DSM_m1 = np.loadtxt("./result/{}cases/error_with_time_DSM_m1.dat".format(case_number), dtype=float)    
        
        IUFNO_m2 = np.loadtxt("./result/{}cases/error_with_time_IUFNO_m2.dat".format(case_number), dtype=float)
        F_IUFNO_m2 = np.loadtxt("./result/{}cases/error_with_time_F_IUFNO_m2.dat".format(case_number), dtype=float)
        F_IFNO_m2 = np.loadtxt("./result/{}cases/error_with_time_F_IFNO_m2.dat".format(case_number), dtype=float)
        IFNO_m2 = np.loadtxt("./result/{}cases/error_with_time_IFNO_m2.dat".format(case_number), dtype=float)
        DSM_m2 = np.loadtxt("./result/{}cases/error_with_time_DSM_m2.dat".format(case_number), dtype=float)    
        
        IUFNO_m5 = np.loadtxt("./result/{}cases/error_with_time_IUFNO_m5.dat".format(case_number), dtype=float)
        F_IUFNO_m5 = np.loadtxt("./result/{}cases/error_with_time_F_IUFNO_m5.dat".format(case_number), dtype=float)
        F_IFNO_m5 = np.loadtxt("./result/{}cases/error_with_time_F_IFNO_m5.dat".format(case_number), dtype=float)
        IFNO_m5 = np.loadtxt("./result/{}cases/error_with_time_IFNO_m5.dat".format(case_number), dtype=float)
        DSM_m5 = np.loadtxt("./result/{}cases/error_with_time_DSM_m5.dat".format(case_number), dtype=float)    
        
        IUFNO_m10 = np.loadtxt("./result/{}cases/error_with_time_IUFNO_m10.dat".format(case_number), dtype=float)
        F_IUFNO_m10 = np.loadtxt("./result/{}cases/error_with_time_F_IUFNO_m10.dat".format(case_number), dtype=float)
        F_IFNO_m10 = np.loadtxt("./result/{}cases/error_with_time_F_IFNO_m10.dat".format(case_number), dtype=float)
        IFNO_m10 = np.loadtxt("./result/{}cases/error_with_time_IFNO_m10.dat".format(case_number), dtype=float)
        DSM_m10 = np.loadtxt("./result/{}cases/error_with_time_DSM_m10.dat".format(case_number), dtype=float)  
        #-------------------------输入参数
        period = 10 #10个波数

        #--------------------------
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
            
            for j in range(1):

                F_IFNO1=(F_IFNO[vel_k-1+period*i, 1])
                F_IUFNO1=(F_IUFNO[vel_k-1+period*i, 1])
                IUFNO1=(IUFNO[vel_k-1+period*i, 1])
                IFNO1=(IFNO[vel_k-1+period*i, 1])
                DSM1=(DSM[vel_k-1+period*i, 1])
                fDNS1=(fDNS[vel_k-1+period*i, 1])

                F_IFNO1_m01=(F_IFNO_m01[vel_k-1+period*i, 1])
                F_IUFNO1_m01=(F_IUFNO_m01[vel_k-1+period*i, 1])
                IUFNO1_m01=(IUFNO_m01[vel_k-1+period*i, 1])
                IFNO1_m01=(IFNO_m01[vel_k-1+period*i, 1])
                DSM1_m01=(DSM_m01[vel_k-1+period*i, 1])

                F_IFNO1_m05=(F_IFNO_m05[vel_k-1+period*i, 1])
                F_IUFNO1_m05=(F_IUFNO_m05[vel_k-1+period*i, 1])
                IUFNO1_m05=(IUFNO_m05[vel_k-1+period*i, 1])
                IFNO1_m05=(IFNO_m05[vel_k-1+period*i, 1])
                DSM1_m05=(DSM_m05[vel_k-1+period*i, 1])

                F_IFNO1_m1=(F_IFNO_m1[vel_k-1+period*i, 1])
                F_IUFNO1_m1=(F_IUFNO_m1[vel_k-1+period*i, 1])
                IUFNO1_m1=(IUFNO_m1[vel_k-1+period*i, 1])
                IFNO1_m1=(IFNO_m1[vel_k-1+period*i, 1])
                DSM1_m1=(DSM_m1[vel_k-1+period*i, 1])

                F_IFNO1_m2=(F_IFNO_m2[vel_k-1+period*i, 1])
                F_IUFNO1_m2=(F_IUFNO_m2[vel_k-1+period*i, 1])
                IUFNO1_m2=(IUFNO_m2[vel_k-1+period*i, 1])
                IFNO1_m2=(IFNO_m2[vel_k-1+period*i, 1])
                DSM1_m2=(DSM_m2[vel_k-1+period*i, 1])
                
                F_IFNO1_m5=(F_IFNO_m5[vel_k-1+period*i, 1])
                F_IUFNO1_m5=(F_IUFNO_m5[vel_k-1+period*i, 1])
                IUFNO1_m5=(IUFNO_m5[vel_k-1+period*i, 1])
                IFNO1_m5=(IFNO_m5[vel_k-1+period*i, 1])
                DSM1_m5=(DSM_m5[vel_k-1+period*i, 1])
                
                F_IFNO1_m10=(F_IFNO_m10[vel_k-1+period*i, 1])
                F_IUFNO1_m10=(F_IUFNO_m10[vel_k-1+period*i, 1])
                IUFNO1_m10=(IUFNO_m10[vel_k-1+period*i, 1])
                IFNO1_m10=(IFNO_m10[vel_k-1+period*i, 1])
                DSM1_m10=(DSM_m10[vel_k-1+period*i, 1])
                
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
        step = np.arange(1, time_steps + 1)
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
        np.savetxt('./result/{}cases/error_with_time_fDNS_k={}.dat'.format(case_number,vel_k), data1, fmt='%d %.16f')
        np.savetxt('./result/{}cases/error_with_time_F_IFNO_k={}.dat'.format(case_number,vel_k), data2, fmt='%d %.16f')
        np.savetxt('./result/{}cases/error_with_time_F_IUFNO_k={}.dat'.format(case_number,vel_k), data3, fmt='%d %.16f')
        np.savetxt('./result/{}cases/error_with_time_IUFNO_k={}.dat'.format(case_number,vel_k), data4, fmt='%d %.16f')
        np.savetxt('./result/{}cases/error_with_time_IFNO_k={}.dat'.format(case_number,vel_k), data5, fmt='%d %.16f')
        np.savetxt('./result/{}cases/error_with_time_DSM_k={}.dat'.format(case_number,vel_k), data6, fmt='%d %.16f')
     
        np.savetxt('./result/{}cases/error_with_time_F_IFNO_m01_k={}.dat'.format(case_number,vel_k), data7, fmt='%d %.16f')
        np.savetxt('./result/{}cases/error_with_time_F_IUFNO_m01_k={}.dat'.format(case_number,vel_k), data8, fmt='%d %.16f')
        np.savetxt('./result/{}cases/error_with_time_IUFNO_m01_k={}.dat'.format(case_number,vel_k), data9, fmt='%d %.16f')
        np.savetxt('./result/{}cases/error_with_time_IFNO_m01_k={}.dat'.format(case_number,vel_k), data10, fmt='%d %.16f')
        np.savetxt('./result/{}cases/error_with_time_DSM_m01_k={}.dat'.format(case_number,vel_k), data11, fmt='%d %.16f')    

        np.savetxt('./result/{}cases/error_with_time_F_IFNO_m05_k={}.dat'.format(case_number,vel_k), data12, fmt='%d %.16f')
        np.savetxt('./result/{}cases/error_with_time_F_IUFNO_m05_k={}.dat'.format(case_number,vel_k), data13, fmt='%d %.16f')
        np.savetxt('./result/{}cases/error_with_time_IUFNO_m05_k={}.dat'.format(case_number,vel_k), data14, fmt='%d %.16f')
        np.savetxt('./result/{}cases/error_with_time_IFNO_m05_k={}.dat'.format(case_number,vel_k), data15, fmt='%d %.16f')
        np.savetxt('./result/{}cases/error_with_time_DSM_m05_k={}.dat'.format(case_number,vel_k), data16, fmt='%d %.16f')

        np.savetxt('./result/{}cases/error_with_time_F_IFNO_m1_k={}.dat'.format(case_number,vel_k), data17, fmt='%d %.16f')
        np.savetxt('./result/{}cases/error_with_time_F_IUFNO_m1_k={}.dat'.format(case_number,vel_k), data18, fmt='%d %.16f')
        np.savetxt('./result/{}cases/error_with_time_IUFNO_m1_k={}.dat'.format(case_number,vel_k), data19, fmt='%d %.16f')
        np.savetxt('./result/{}cases/error_with_time_IFNO_m1_k={}.dat'.format(case_number,vel_k), data20, fmt='%d %.16f')
        np.savetxt('./result/{}cases/error_with_time_DSM_m1_k={}.dat'.format(case_number,vel_k), data21, fmt='%d %.16f')
     
        np.savetxt('./result/{}cases/error_with_time_F_IFNO_m2_k={}.dat'.format(case_number,vel_k), data22, fmt='%d %.16f')
        np.savetxt('./result/{}cases/error_with_time_F_IUFNO_m2_k={}.dat'.format(case_number,vel_k), data23, fmt='%d %.16f')
        np.savetxt('./result/{}cases/error_with_time_IUFNO_m2_k={}.dat'.format(case_number,vel_k), data24, fmt='%d %.16f')
        np.savetxt('./result/{}cases/error_with_time_IFNO_m2_k={}.dat'.format(case_number,vel_k), data25, fmt='%d %.16f')
        np.savetxt('./result/{}cases/error_with_time_DSM_m2_k={}.dat'.format(case_number,vel_k), data26, fmt='%d %.16f')    

        np.savetxt('./result/{}cases/error_with_time_F_IFNO_m5_k={}.dat'.format(case_number,vel_k), data27, fmt='%d %.16f')
        np.savetxt('./result/{}cases/error_with_time_F_IUFNO_m5_k={}.dat'.format(case_number,vel_k), data28, fmt='%d %.16f')
        np.savetxt('./result/{}cases/error_with_time_IUFNO_m5_k={}.dat'.format(case_number,vel_k), data29, fmt='%d %.16f')
        np.savetxt('./result/{}cases/error_with_time_IFNO_m5_k={}.dat'.format(case_number,vel_k), data30, fmt='%d %.16f')
        np.savetxt('./result/{}cases/error_with_time_DSM_m5_k={}.dat'.format(case_number,vel_k), data31, fmt='%d %.16f')

        np.savetxt('./result/{}cases/error_with_time_F_IFNO_m10_k={}.dat'.format(case_number,vel_k), data32, fmt='%d %.16f')
        np.savetxt('./result/{}cases/error_with_time_F_IUFNO_m10_k={}.dat'.format(case_number,vel_k), data33, fmt='%d %.16f')
        np.savetxt('./result/{}cases/error_with_time_IUFNO_m10_k={}.dat'.format(case_number,vel_k), data34, fmt='%d %.16f')
        np.savetxt('./result/{}cases/error_with_time_IFNO_m10_k={}.dat'.format(case_number,vel_k), data35, fmt='%d %.16f')
        np.savetxt('./result/{}cases/error_with_time_DSM_m10_k={}.dat'.format(case_number,vel_k), data36, fmt='%d %.16f')




