"""
@author: admin
"""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import os
import matplotlib as mpl
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker  
import numpy as np
plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.serif'] = ['Times', 'Times', 'STIXGeneral']
case_number_list =[30,1,10,20]
vel_k_list = [1,2,3,4,5,6,7,8,9,10]

for kk, case_number in enumerate(case_number_list):


    avg_results = []
    avg_error = []
    variance_error = []
        
        
    for k, vel_k in enumerate(vel_k_list):
        #-------------------------------------------------------------读入数据，
        ###小數點后3位###
        fDNS = np.loadtxt("./result/{}cases/error_with_time_fDNS_k={}.dat".format(case_number, vel_k), dtype=float)
        IUFNO = np.loadtxt("./result/{}cases/error_with_time_IUFNO_k={}.dat".format(case_number, vel_k), dtype=float)
        F_IUFNO = np.loadtxt("./result/{}cases/error_with_time_F_IUFNO_k={}.dat".format(case_number, vel_k), dtype=float)
        F_IFNO = np.loadtxt("./result/{}cases/error_with_time_F_IFNO_k={}.dat".format(case_number, vel_k), dtype=float)
        IFNO = np.loadtxt("./result/{}cases/error_with_time_IFNO_k={}.dat".format(case_number, vel_k), dtype=float)
        DSM = np.loadtxt("./result/{}cases/error_with_time_DSM_k={}.dat".format(case_number, vel_k), dtype=float)

        IUFNO_m01 = np.loadtxt("./result/{}cases/error_with_time_IUFNO_m01_k={}.dat".format(case_number, vel_k), dtype=float)
        F_IUFNO_m01 = np.loadtxt("./result/{}cases/error_with_time_F_IUFNO_m01_k={}.dat".format(case_number, vel_k), dtype=float)
        F_IFNO_m01 = np.loadtxt("./result/{}cases/error_with_time_F_IFNO_m01_k={}.dat".format(case_number, vel_k), dtype=float)
        IFNO_m01 = np.loadtxt("./result/{}cases/error_with_time_IFNO_m01_k={}.dat".format(case_number, vel_k), dtype=float)
        DSM_m01 = np.loadtxt("./result/{}cases/error_with_time_DSM_m01_k={}.dat".format(case_number, vel_k), dtype=float)       

        IUFNO_m05 = np.loadtxt("./result/{}cases/error_with_time_IUFNO_m05_k={}.dat".format(case_number, vel_k), dtype=float)
        F_IUFNO_m05 = np.loadtxt("./result/{}cases/error_with_time_F_IUFNO_m05_k={}.dat".format(case_number, vel_k), dtype=float)
        F_IFNO_m05 = np.loadtxt("./result/{}cases/error_with_time_F_IFNO_m05_k={}.dat".format(case_number, vel_k), dtype=float)
        IFNO_m05 = np.loadtxt("./result/{}cases/error_with_time_IFNO_m05_k={}.dat".format(case_number, vel_k), dtype=float)
        DSM_m05 = np.loadtxt("./result/{}cases/error_with_time_DSM_m05_k={}.dat".format(case_number, vel_k), dtype=float)           

        IUFNO_m1 = np.loadtxt("./result/{}cases/error_with_time_IUFNO_m1_k={}.dat".format(case_number, vel_k), dtype=float)
        F_IUFNO_m1 = np.loadtxt("./result/{}cases/error_with_time_F_IUFNO_m1_k={}.dat".format(case_number, vel_k), dtype=float)
        F_IFNO_m1 = np.loadtxt("./result/{}cases/error_with_time_F_IFNO_m1_k={}.dat".format(case_number, vel_k), dtype=float)
        IFNO_m1 = np.loadtxt("./result/{}cases/error_with_time_IFNO_m1_k={}.dat".format(case_number, vel_k), dtype=float)
        DSM_m1 = np.loadtxt("./result/{}cases/error_with_time_DSM_m1_k={}.dat".format(case_number, vel_k), dtype=float)           

        IUFNO_m2 = np.loadtxt("./result/{}cases/error_with_time_IUFNO_m2_k={}.dat".format(case_number, vel_k), dtype=float)
        F_IUFNO_m2 = np.loadtxt("./result/{}cases/error_with_time_F_IUFNO_m2_k={}.dat".format(case_number, vel_k), dtype=float)
        F_IFNO_m2 = np.loadtxt("./result/{}cases/error_with_time_F_IFNO_m2_k={}.dat".format(case_number, vel_k), dtype=float)
        IFNO_m2 = np.loadtxt("./result/{}cases/error_with_time_IFNO_m2_k={}.dat".format(case_number, vel_k), dtype=float)
        DSM_m2 = np.loadtxt("./result/{}cases/error_with_time_DSM_m2_k={}.dat".format(case_number, vel_k), dtype=float)       

        IUFNO_m5 = np.loadtxt("./result/{}cases/error_with_time_IUFNO_m5_k={}.dat".format(case_number, vel_k), dtype=float)
        F_IUFNO_m5 = np.loadtxt("./result/{}cases/error_with_time_F_IUFNO_m5_k={}.dat".format(case_number, vel_k), dtype=float)
        F_IFNO_m5 = np.loadtxt("./result/{}cases/error_with_time_F_IFNO_m5_k={}.dat".format(case_number, vel_k), dtype=float)
        IFNO_m5 = np.loadtxt("./result/{}cases/error_with_time_IFNO_m5_k={}.dat".format(case_number, vel_k), dtype=float)
        DSM_m5 = np.loadtxt("./result/{}cases/error_with_time_DSM_m5_k={}.dat".format(case_number, vel_k), dtype=float)           

        IUFNO_m10 = np.loadtxt("./result/{}cases/error_with_time_IUFNO_m10_k={}.dat".format(case_number, vel_k), dtype=float)
        F_IUFNO_m10 = np.loadtxt("./result/{}cases/error_with_time_F_IUFNO_m10_k={}.dat".format(case_number, vel_k), dtype=float)
        F_IFNO_m10 = np.loadtxt("./result/{}cases/error_with_time_F_IFNO_m10_k={}.dat".format(case_number, vel_k), dtype=float)
        IFNO_m10 = np.loadtxt("./result/{}cases/error_with_time_IFNO_m10_k={}.dat".format(case_number, vel_k), dtype=float)
        DSM_m10 = np.loadtxt("./result/{}cases/error_with_time_DSM_m10_k={}.dat".format(case_number, vel_k), dtype=float)   
        
        #-------------------------输入参数
        period = 10 #10个波数    
    

        #-------------------------输入参数
        # time_advance=[20]  #挑推进时间画图
        # time_advance=[40]  #挑推进时间画图
        #time_advance=[1,2,3,10,15,20,25,30,40,50,60,70,80,90,100,110,120,130,140,150,160,170,180,190,200,210,220,230,240,250]  #挑推进时间画图
        data1=F_IFNO[:,1]
        data2=F_IUFNO[:,1]
        data3=IUFNO[:,1]
        data4=IFNO[:,1]
        data5=DSM[:,1]
        
        data6=F_IFNO_m01[:,1]
        data7=F_IUFNO_m01[:,1]
        data8=IUFNO_m01[:,1]
        data9=IFNO_m01[:,1]
        data10=DSM_m01[:,1]

        data11=F_IFNO_m05[:,1]
        data12=F_IUFNO_m05[:,1]
        data13=IUFNO_m05[:,1]
        data14=IFNO_m05[:,1]
        data15=DSM_m05[:,1]

        data16=F_IFNO_m1[:,1]
        data17=F_IUFNO_m1[:,1]
        data18=IUFNO_m1[:,1]
        data19=IFNO_m1[:,1]
        data20=DSM_m1[:,1]

        data21=F_IFNO_m2[:,1]
        data22=F_IUFNO_m2[:,1]
        data23=IUFNO_m2[:,1]
        data24=IFNO_m2[:,1]
        data25=DSM_m2[:,1]

        data26=F_IFNO_m5[:,1]
        data27=F_IUFNO_m5[:,1]
        data28=IUFNO_m5[:,1]
        data29=IFNO_m5[:,1]
        data30=DSM_m5[:,1]

        data31=F_IFNO_m10[:,1]
        data32=F_IUFNO_m10[:,1]
        data33=IUFNO_m10[:,1]
        data34=IFNO_m10[:,1]
        data35=DSM_m10[:,1]

        data36=fDNS[:,1]

        data_list = [data1, data2, data3, data4, data5, data6, data7, data8,
                     data9, data10, data11, data12, data13, data14, data15, data16,
                     data17, data18, data19, data20, data21, data22, data23, data24,
                     data25, data26, data27, data28, data29, data30, data31, data32,
                     data33, data34,data35, data36]


        # 遍历每个数据集计算 RMS、平均值和方差
        for i, data in enumerate(data_list, start=1):
            # 计算 RMS 误差
            avg_error1 = np.mean(data)
            
            # 计算误差的方差
            variance_error1 = np.var(data)
            
            avg_result = f"{avg_error1:.8f} ± {variance_error1:.8f}"
            
            avg_error.append(avg_error1)
            variance_error.append(variance_error1)
            avg_results.append(avg_result)


        print(len(avg_error))#360

    ######----------------------------x=k----------------------------########

    x1 = [1,2,3,4,5,6,7,8,9,10]
    h=1
    mean1_F_IFNO = [avg_error[(h-1)+36*0], avg_error[(h-1)+36*1], avg_error[(h-1)+36*2], avg_error[(h-1)+36*3], avg_error[(h-1)+36*4], avg_error[(h-1)+36*5], avg_error[(h-1)+36*6], avg_error[(h-1)+36*7], avg_error[(h-1)+36*8], avg_error[(h-1)+36*9]]
    std1_F_IFNO = [variance_error[(h-1)+36*0],variance_error[(h-1)+36*1],variance_error[(h-1)+36*2],variance_error[(h-1)+36*3],variance_error[(h-1)+36*4],variance_error[(h-1)+36*5],variance_error[(h-1)+36*6],variance_error[(h-1)+36*7],variance_error[(h-1)+36*8],variance_error[(h-1)+36*9]]

    h=2
    mean1_F_IUFNO = [avg_error[(h-1)+36*0], avg_error[(h-1)+36*1], avg_error[(h-1)+36*2], avg_error[(h-1)+36*3], avg_error[(h-1)+36*4], avg_error[(h-1)+36*5], avg_error[(h-1)+36*6], avg_error[(h-1)+36*7], avg_error[(h-1)+36*8], avg_error[(h-1)+36*9]]
    std1_F_IUFNO = [variance_error[(h-1)+36*0],variance_error[(h-1)+36*1],variance_error[(h-1)+36*2],variance_error[(h-1)+36*3],variance_error[(h-1)+36*4],variance_error[(h-1)+36*5],variance_error[(h-1)+36*6],variance_error[(h-1)+36*7],variance_error[(h-1)+36*8],variance_error[(h-1)+36*9]]
    
    h=3
    mean1_IUFNO = [avg_error[(h-1)+36*0], avg_error[(h-1)+36*1], avg_error[(h-1)+36*2], avg_error[(h-1)+36*3], avg_error[(h-1)+36*4], avg_error[(h-1)+36*5], avg_error[(h-1)+36*6], avg_error[(h-1)+36*7], avg_error[(h-1)+36*8], avg_error[(h-1)+36*9]]
    std1_IUFNO = [variance_error[(h-1)+36*0],variance_error[(h-1)+36*1],variance_error[(h-1)+36*2],variance_error[(h-1)+36*3],variance_error[(h-1)+36*4],variance_error[(h-1)+36*5],variance_error[(h-1)+36*6],variance_error[(h-1)+36*7],variance_error[(h-1)+36*8],variance_error[(h-1)+36*9]]
    
    h=4
    mean1_IFNO = [avg_error[(h-1)+36*0], avg_error[(h-1)+36*1], avg_error[(h-1)+36*2], avg_error[(h-1)+36*3], avg_error[(h-1)+36*4], avg_error[(h-1)+36*5], avg_error[(h-1)+36*6], avg_error[(h-1)+36*7], avg_error[(h-1)+36*8], avg_error[(h-1)+36*9]]
    std1_IFNO = [variance_error[(h-1)+36*0],variance_error[(h-1)+36*1],variance_error[(h-1)+36*2],variance_error[(h-1)+36*3],variance_error[(h-1)+36*4],variance_error[(h-1)+36*5],variance_error[(h-1)+36*6],variance_error[(h-1)+36*7],variance_error[(h-1)+36*8],variance_error[(h-1)+36*9]]
    
    h=5
    mean1_DSM = [avg_error[(h-1)+36*0], avg_error[(h-1)+36*1], avg_error[(h-1)+36*2], avg_error[(h-1)+36*3], avg_error[(h-1)+36*4], avg_error[(h-1)+36*5], avg_error[(h-1)+36*6], avg_error[(h-1)+36*7], avg_error[(h-1)+36*8], avg_error[(h-1)+36*9]]
    std1_DSM = [variance_error[(h-1)+36*0],variance_error[(h-1)+36*1],variance_error[(h-1)+36*2],variance_error[(h-1)+36*3],variance_error[(h-1)+36*4],variance_error[(h-1)+36*5],variance_error[(h-1)+36*6],variance_error[(h-1)+36*7],variance_error[(h-1)+36*8],variance_error[(h-1)+36*9]]

    h=6
    mean1_F_IFNO_m01 = [avg_error[(h-1)+36*0], avg_error[(h-1)+36*1], avg_error[(h-1)+36*2], avg_error[(h-1)+36*3], avg_error[(h-1)+36*4], avg_error[(h-1)+36*5], avg_error[(h-1)+36*6], avg_error[(h-1)+36*7], avg_error[(h-1)+36*8], avg_error[(h-1)+36*9]]
    std1_F_IFNO_m01 = [variance_error[(h-1)+36*0],variance_error[(h-1)+36*1],variance_error[(h-1)+36*2],variance_error[(h-1)+36*3],variance_error[(h-1)+36*4],variance_error[(h-1)+36*5],variance_error[(h-1)+36*6],variance_error[(h-1)+36*7],variance_error[(h-1)+36*8],variance_error[(h-1)+36*9]]

    h=7
    mean1_F_IUFNO_m01 = [avg_error[(h-1)+36*0], avg_error[(h-1)+36*1], avg_error[(h-1)+36*2], avg_error[(h-1)+36*3], avg_error[(h-1)+36*4], avg_error[(h-1)+36*5], avg_error[(h-1)+36*6], avg_error[(h-1)+36*7], avg_error[(h-1)+36*8], avg_error[(h-1)+36*9]]
    std1_F_IUFNO_m01 = [variance_error[(h-1)+36*0],variance_error[(h-1)+36*1],variance_error[(h-1)+36*2],variance_error[(h-1)+36*3],variance_error[(h-1)+36*4],variance_error[(h-1)+36*5],variance_error[(h-1)+36*6],variance_error[(h-1)+36*7],variance_error[(h-1)+36*8],variance_error[(h-1)+36*9]]
    
    h=8
    mean1_IUFNO_m01 = [avg_error[(h-1)+36*0], avg_error[(h-1)+36*1], avg_error[(h-1)+36*2], avg_error[(h-1)+36*3], avg_error[(h-1)+36*4], avg_error[(h-1)+36*5], avg_error[(h-1)+36*6], avg_error[(h-1)+36*7], avg_error[(h-1)+36*8], avg_error[(h-1)+36*9]]
    std1_IUFNO_m01 = [variance_error[(h-1)+36*0],variance_error[(h-1)+36*1],variance_error[(h-1)+36*2],variance_error[(h-1)+36*3],variance_error[(h-1)+36*4],variance_error[(h-1)+36*5],variance_error[(h-1)+36*6],variance_error[(h-1)+36*7],variance_error[(h-1)+36*8],variance_error[(h-1)+36*9]]
    
    h=9
    mean1_IFNO_m01 = [avg_error[(h-1)+36*0], avg_error[(h-1)+36*1], avg_error[(h-1)+36*2], avg_error[(h-1)+36*3], avg_error[(h-1)+36*4], avg_error[(h-1)+36*5], avg_error[(h-1)+36*6], avg_error[(h-1)+36*7], avg_error[(h-1)+36*8], avg_error[(h-1)+36*9]]
    std1_IFNO_m01 = [variance_error[(h-1)+36*0],variance_error[(h-1)+36*1],variance_error[(h-1)+36*2],variance_error[(h-1)+36*3],variance_error[(h-1)+36*4],variance_error[(h-1)+36*5],variance_error[(h-1)+36*6],variance_error[(h-1)+36*7],variance_error[(h-1)+36*8],variance_error[(h-1)+36*9]]
    
    h=10
    mean1_DSM_m01 = [avg_error[(h-1)+36*0], avg_error[(h-1)+36*1], avg_error[(h-1)+36*2], avg_error[(h-1)+36*3], avg_error[(h-1)+36*4], avg_error[(h-1)+36*5], avg_error[(h-1)+36*6], avg_error[(h-1)+36*7], avg_error[(h-1)+36*8], avg_error[(h-1)+36*9]]
    std1_DSM_m01 = [variance_error[(h-1)+36*0],variance_error[(h-1)+36*1],variance_error[(h-1)+36*2],variance_error[(h-1)+36*3],variance_error[(h-1)+36*4],variance_error[(h-1)+36*5],variance_error[(h-1)+36*6],variance_error[(h-1)+36*7],variance_error[(h-1)+36*8],variance_error[(h-1)+36*9]]

    h=11
    mean1_F_IFNO_m05 = [avg_error[(h-1)+36*0], avg_error[(h-1)+36*1], avg_error[(h-1)+36*2], avg_error[(h-1)+36*3], avg_error[(h-1)+36*4], avg_error[(h-1)+36*5], avg_error[(h-1)+36*6], avg_error[(h-1)+36*7], avg_error[(h-1)+36*8], avg_error[(h-1)+36*9]]
    std1_F_IFNO_m05 = [variance_error[(h-1)+36*0],variance_error[(h-1)+36*1],variance_error[(h-1)+36*2],variance_error[(h-1)+36*3],variance_error[(h-1)+36*4],variance_error[(h-1)+36*5],variance_error[(h-1)+36*6],variance_error[(h-1)+36*7],variance_error[(h-1)+36*8],variance_error[(h-1)+36*9]]

    h=12
    mean1_F_IUFNO_m05 = [avg_error[(h-1)+36*0], avg_error[(h-1)+36*1], avg_error[(h-1)+36*2], avg_error[(h-1)+36*3], avg_error[(h-1)+36*4], avg_error[(h-1)+36*5], avg_error[(h-1)+36*6], avg_error[(h-1)+36*7], avg_error[(h-1)+36*8], avg_error[(h-1)+36*9]]
    std1_F_IUFNO_m05 = [variance_error[(h-1)+36*0],variance_error[(h-1)+36*1],variance_error[(h-1)+36*2],variance_error[(h-1)+36*3],variance_error[(h-1)+36*4],variance_error[(h-1)+36*5],variance_error[(h-1)+36*6],variance_error[(h-1)+36*7],variance_error[(h-1)+36*8],variance_error[(h-1)+36*9]]
    
    h=13
    mean1_IUFNO_m05 = [avg_error[(h-1)+36*0], avg_error[(h-1)+36*1], avg_error[(h-1)+36*2], avg_error[(h-1)+36*3], avg_error[(h-1)+36*4], avg_error[(h-1)+36*5], avg_error[(h-1)+36*6], avg_error[(h-1)+36*7], avg_error[(h-1)+36*8], avg_error[(h-1)+36*9]]
    std1_IUFNO_m05 = [variance_error[(h-1)+36*0],variance_error[(h-1)+36*1],variance_error[(h-1)+36*2],variance_error[(h-1)+36*3],variance_error[(h-1)+36*4],variance_error[(h-1)+36*5],variance_error[(h-1)+36*6],variance_error[(h-1)+36*7],variance_error[(h-1)+36*8],variance_error[(h-1)+36*9]]
    
    h=14
    mean1_IFNO_m05 = [avg_error[(h-1)+36*0], avg_error[(h-1)+36*1], avg_error[(h-1)+36*2], avg_error[(h-1)+36*3], avg_error[(h-1)+36*4], avg_error[(h-1)+36*5], avg_error[(h-1)+36*6], avg_error[(h-1)+36*7], avg_error[(h-1)+36*8], avg_error[(h-1)+36*9]]
    std1_IFNO_m05 = [variance_error[(h-1)+36*0],variance_error[(h-1)+36*1],variance_error[(h-1)+36*2],variance_error[(h-1)+36*3],variance_error[(h-1)+36*4],variance_error[(h-1)+36*5],variance_error[(h-1)+36*6],variance_error[(h-1)+36*7],variance_error[(h-1)+36*8],variance_error[(h-1)+36*9]]
    
    h=15
    mean1_DSM_m05 = [avg_error[(h-1)+36*0], avg_error[(h-1)+36*1], avg_error[(h-1)+36*2], avg_error[(h-1)+36*3], avg_error[(h-1)+36*4], avg_error[(h-1)+36*5], avg_error[(h-1)+36*6], avg_error[(h-1)+36*7], avg_error[(h-1)+36*8], avg_error[(h-1)+36*9]]
    std1_DSM_m05 = [variance_error[(h-1)+36*0],variance_error[(h-1)+36*1],variance_error[(h-1)+36*2],variance_error[(h-1)+36*3],variance_error[(h-1)+36*4],variance_error[(h-1)+36*5],variance_error[(h-1)+36*6],variance_error[(h-1)+36*7],variance_error[(h-1)+36*8],variance_error[(h-1)+36*9]]

    h=16
    mean1_F_IFNO_m1 = [avg_error[(h-1)+36*0], avg_error[(h-1)+36*1], avg_error[(h-1)+36*2], avg_error[(h-1)+36*3], avg_error[(h-1)+36*4], avg_error[(h-1)+36*5], avg_error[(h-1)+36*6], avg_error[(h-1)+36*7], avg_error[(h-1)+36*8], avg_error[(h-1)+36*9]]
    std1_F_IFNO_m1 = [variance_error[(h-1)+36*0],variance_error[(h-1)+36*1],variance_error[(h-1)+36*2],variance_error[(h-1)+36*3],variance_error[(h-1)+36*4],variance_error[(h-1)+36*5],variance_error[(h-1)+36*6],variance_error[(h-1)+36*7],variance_error[(h-1)+36*8],variance_error[(h-1)+36*9]]

    h=17
    mean1_F_IUFNO_m1 = [avg_error[(h-1)+36*0], avg_error[(h-1)+36*1], avg_error[(h-1)+36*2], avg_error[(h-1)+36*3], avg_error[(h-1)+36*4], avg_error[(h-1)+36*5], avg_error[(h-1)+36*6], avg_error[(h-1)+36*7], avg_error[(h-1)+36*8], avg_error[(h-1)+36*9]]
    std1_F_IUFNO_m1 = [variance_error[(h-1)+36*0],variance_error[(h-1)+36*1],variance_error[(h-1)+36*2],variance_error[(h-1)+36*3],variance_error[(h-1)+36*4],variance_error[(h-1)+36*5],variance_error[(h-1)+36*6],variance_error[(h-1)+36*7],variance_error[(h-1)+36*8],variance_error[(h-1)+36*9]]
    
    h=18
    mean1_IUFNO_m1 = [avg_error[(h-1)+36*0], avg_error[(h-1)+36*1], avg_error[(h-1)+36*2], avg_error[(h-1)+36*3], avg_error[(h-1)+36*4], avg_error[(h-1)+36*5], avg_error[(h-1)+36*6], avg_error[(h-1)+36*7], avg_error[(h-1)+36*8], avg_error[(h-1)+36*9]]
    std1_IUFNO_m1 = [variance_error[(h-1)+36*0],variance_error[(h-1)+36*1],variance_error[(h-1)+36*2],variance_error[(h-1)+36*3],variance_error[(h-1)+36*4],variance_error[(h-1)+36*5],variance_error[(h-1)+36*6],variance_error[(h-1)+36*7],variance_error[(h-1)+36*8],variance_error[(h-1)+36*9]]
    
    h=19
    mean1_IFNO_m1 = [avg_error[(h-1)+36*0], avg_error[(h-1)+36*1], avg_error[(h-1)+36*2], avg_error[(h-1)+36*3], avg_error[(h-1)+36*4], avg_error[(h-1)+36*5], avg_error[(h-1)+36*6], avg_error[(h-1)+36*7], avg_error[(h-1)+36*8], avg_error[(h-1)+36*9]]
    std1_IFNO_m1 = [variance_error[(h-1)+36*0],variance_error[(h-1)+36*1],variance_error[(h-1)+36*2],variance_error[(h-1)+36*3],variance_error[(h-1)+36*4],variance_error[(h-1)+36*5],variance_error[(h-1)+36*6],variance_error[(h-1)+36*7],variance_error[(h-1)+36*8],variance_error[(h-1)+36*9]]
    
    h=20
    mean1_DSM_m1 = [avg_error[(h-1)+36*0], avg_error[(h-1)+36*1], avg_error[(h-1)+36*2], avg_error[(h-1)+36*3], avg_error[(h-1)+36*4], avg_error[(h-1)+36*5], avg_error[(h-1)+36*6], avg_error[(h-1)+36*7], avg_error[(h-1)+36*8], avg_error[(h-1)+36*9]]
    std1_DSM_m1 = [variance_error[(h-1)+36*0],variance_error[(h-1)+36*1],variance_error[(h-1)+36*2],variance_error[(h-1)+36*3],variance_error[(h-1)+36*4],variance_error[(h-1)+36*5],variance_error[(h-1)+36*6],variance_error[(h-1)+36*7],variance_error[(h-1)+36*8],variance_error[(h-1)+36*9]]

    h=21
    mean1_F_IFNO_m2 = [avg_error[(h-1)+36*0], avg_error[(h-1)+36*1], avg_error[(h-1)+36*2], avg_error[(h-1)+36*3], avg_error[(h-1)+36*4], avg_error[(h-1)+36*5], avg_error[(h-1)+36*6], avg_error[(h-1)+36*7], avg_error[(h-1)+36*8], avg_error[(h-1)+36*9]]
    std1_F_IFNO_m2 = [variance_error[(h-1)+36*0],variance_error[(h-1)+36*1],variance_error[(h-1)+36*2],variance_error[(h-1)+36*3],variance_error[(h-1)+36*4],variance_error[(h-1)+36*5],variance_error[(h-1)+36*6],variance_error[(h-1)+36*7],variance_error[(h-1)+36*8],variance_error[(h-1)+36*9]]

    h=22
    mean1_F_IUFNO_m2 = [avg_error[(h-1)+36*0], avg_error[(h-1)+36*1], avg_error[(h-1)+36*2], avg_error[(h-1)+36*3], avg_error[(h-1)+36*4], avg_error[(h-1)+36*5], avg_error[(h-1)+36*6], avg_error[(h-1)+36*7], avg_error[(h-1)+36*8], avg_error[(h-1)+36*9]]
    std1_F_IUFNO_m2 = [variance_error[(h-1)+36*0],variance_error[(h-1)+36*1],variance_error[(h-1)+36*2],variance_error[(h-1)+36*3],variance_error[(h-1)+36*4],variance_error[(h-1)+36*5],variance_error[(h-1)+36*6],variance_error[(h-1)+36*7],variance_error[(h-1)+36*8],variance_error[(h-1)+36*9]]
    
    h=23
    mean1_IUFNO_m2 = [avg_error[(h-1)+36*0], avg_error[(h-1)+36*1], avg_error[(h-1)+36*2], avg_error[(h-1)+36*3], avg_error[(h-1)+36*4], avg_error[(h-1)+36*5], avg_error[(h-1)+36*6], avg_error[(h-1)+36*7], avg_error[(h-1)+36*8], avg_error[(h-1)+36*9]]
    std1_IUFNO_m2 = [variance_error[(h-1)+36*0],variance_error[(h-1)+36*1],variance_error[(h-1)+36*2],variance_error[(h-1)+36*3],variance_error[(h-1)+36*4],variance_error[(h-1)+36*5],variance_error[(h-1)+36*6],variance_error[(h-1)+36*7],variance_error[(h-1)+36*8],variance_error[(h-1)+36*9]]
    
    h=24
    mean1_IFNO_m2 = [avg_error[(h-1)+36*0], avg_error[(h-1)+36*1], avg_error[(h-1)+36*2], avg_error[(h-1)+36*3], avg_error[(h-1)+36*4], avg_error[(h-1)+36*5], avg_error[(h-1)+36*6], avg_error[(h-1)+36*7], avg_error[(h-1)+36*8], avg_error[(h-1)+36*9]]
    std1_IFNO_m2 = [variance_error[(h-1)+36*0],variance_error[(h-1)+36*1],variance_error[(h-1)+36*2],variance_error[(h-1)+36*3],variance_error[(h-1)+36*4],variance_error[(h-1)+36*5],variance_error[(h-1)+36*6],variance_error[(h-1)+36*7],variance_error[(h-1)+36*8],variance_error[(h-1)+36*9]]
    
    h=25
    mean1_DSM_m2 = [avg_error[(h-1)+36*0], avg_error[(h-1)+36*1], avg_error[(h-1)+36*2], avg_error[(h-1)+36*3], avg_error[(h-1)+36*4], avg_error[(h-1)+36*5], avg_error[(h-1)+36*6], avg_error[(h-1)+36*7], avg_error[(h-1)+36*8], avg_error[(h-1)+36*9]]
    std1_DSM_m2 = [variance_error[(h-1)+36*0],variance_error[(h-1)+36*1],variance_error[(h-1)+36*2],variance_error[(h-1)+36*3],variance_error[(h-1)+36*4],variance_error[(h-1)+36*5],variance_error[(h-1)+36*6],variance_error[(h-1)+36*7],variance_error[(h-1)+36*8],variance_error[(h-1)+36*9]]

    h=26
    mean1_F_IFNO_m5 = [avg_error[(h-1)+36*0], avg_error[(h-1)+36*1], avg_error[(h-1)+36*2], avg_error[(h-1)+36*3], avg_error[(h-1)+36*4], avg_error[(h-1)+36*5], avg_error[(h-1)+36*6], avg_error[(h-1)+36*7], avg_error[(h-1)+36*8], avg_error[(h-1)+36*9]]
    std1_F_IFNO_m5 = [variance_error[(h-1)+36*0],variance_error[(h-1)+36*1],variance_error[(h-1)+36*2],variance_error[(h-1)+36*3],variance_error[(h-1)+36*4],variance_error[(h-1)+36*5],variance_error[(h-1)+36*6],variance_error[(h-1)+36*7],variance_error[(h-1)+36*8],variance_error[(h-1)+36*9]]

    h=27
    mean1_F_IUFNO_m5 = [avg_error[(h-1)+36*0], avg_error[(h-1)+36*1], avg_error[(h-1)+36*2], avg_error[(h-1)+36*3], avg_error[(h-1)+36*4], avg_error[(h-1)+36*5], avg_error[(h-1)+36*6], avg_error[(h-1)+36*7], avg_error[(h-1)+36*8], avg_error[(h-1)+36*9]]
    std1_F_IUFNO_m5 = [variance_error[(h-1)+36*0],variance_error[(h-1)+36*1],variance_error[(h-1)+36*2],variance_error[(h-1)+36*3],variance_error[(h-1)+36*4],variance_error[(h-1)+36*5],variance_error[(h-1)+36*6],variance_error[(h-1)+36*7],variance_error[(h-1)+36*8],variance_error[(h-1)+36*9]]
    
    h=28
    mean1_IUFNO_m5 = [avg_error[(h-1)+36*0], avg_error[(h-1)+36*1], avg_error[(h-1)+36*2], avg_error[(h-1)+36*3], avg_error[(h-1)+36*4], avg_error[(h-1)+36*5], avg_error[(h-1)+36*6], avg_error[(h-1)+36*7], avg_error[(h-1)+36*8], avg_error[(h-1)+36*9]]
    std1_IUFNO_m5 = [variance_error[(h-1)+36*0],variance_error[(h-1)+36*1],variance_error[(h-1)+36*2],variance_error[(h-1)+36*3],variance_error[(h-1)+36*4],variance_error[(h-1)+36*5],variance_error[(h-1)+36*6],variance_error[(h-1)+36*7],variance_error[(h-1)+36*8],variance_error[(h-1)+36*9]]
    
    h=29
    mean1_IFNO_m5 = [avg_error[(h-1)+36*0], avg_error[(h-1)+36*1], avg_error[(h-1)+36*2], avg_error[(h-1)+36*3], avg_error[(h-1)+36*4], avg_error[(h-1)+36*5], avg_error[(h-1)+36*6], avg_error[(h-1)+36*7], avg_error[(h-1)+36*8], avg_error[(h-1)+36*9]]
    std1_IFNO_m5 = [variance_error[(h-1)+36*0],variance_error[(h-1)+36*1],variance_error[(h-1)+36*2],variance_error[(h-1)+36*3],variance_error[(h-1)+36*4],variance_error[(h-1)+36*5],variance_error[(h-1)+36*6],variance_error[(h-1)+36*7],variance_error[(h-1)+36*8],variance_error[(h-1)+36*9]]
    
    h=30
    mean1_DSM_m5 = [avg_error[(h-1)+36*0], avg_error[(h-1)+36*1], avg_error[(h-1)+36*2], avg_error[(h-1)+36*3], avg_error[(h-1)+36*4], avg_error[(h-1)+36*5], avg_error[(h-1)+36*6], avg_error[(h-1)+36*7], avg_error[(h-1)+36*8], avg_error[(h-1)+36*9]]
    std1_DSM_m5 = [variance_error[(h-1)+36*0],variance_error[(h-1)+36*1],variance_error[(h-1)+36*2],variance_error[(h-1)+36*3],variance_error[(h-1)+36*4],variance_error[(h-1)+36*5],variance_error[(h-1)+36*6],variance_error[(h-1)+36*7],variance_error[(h-1)+36*8],variance_error[(h-1)+36*9]]

    h=31
    mean1_F_IFNO_m10 = [avg_error[(h-1)+36*0], avg_error[(h-1)+36*1], avg_error[(h-1)+36*2], avg_error[(h-1)+36*3], avg_error[(h-1)+36*4], avg_error[(h-1)+36*5], avg_error[(h-1)+36*6], avg_error[(h-1)+36*7], avg_error[(h-1)+36*8], avg_error[(h-1)+36*9]]
    std1_F_IFNO_m10 = [variance_error[(h-1)+36*0],variance_error[(h-1)+36*1],variance_error[(h-1)+36*2],variance_error[(h-1)+36*3],variance_error[(h-1)+36*4],variance_error[(h-1)+36*5],variance_error[(h-1)+36*6],variance_error[(h-1)+36*7],variance_error[(h-1)+36*8],variance_error[(h-1)+36*9]]

    h=32
    mean1_F_IUFNO_m10 = [avg_error[(h-1)+36*0], avg_error[(h-1)+36*1], avg_error[(h-1)+36*2], avg_error[(h-1)+36*3], avg_error[(h-1)+36*4], avg_error[(h-1)+36*5], avg_error[(h-1)+36*6], avg_error[(h-1)+36*7], avg_error[(h-1)+36*8], avg_error[(h-1)+36*9]]
    std1_F_IUFNO_m10 = [variance_error[(h-1)+36*0],variance_error[(h-1)+36*1],variance_error[(h-1)+36*2],variance_error[(h-1)+36*3],variance_error[(h-1)+36*4],variance_error[(h-1)+36*5],variance_error[(h-1)+36*6],variance_error[(h-1)+36*7],variance_error[(h-1)+36*8],variance_error[(h-1)+36*9]]
    
    h=33
    mean1_IUFNO_m10 = [avg_error[(h-1)+36*0], avg_error[(h-1)+36*1], avg_error[(h-1)+36*2], avg_error[(h-1)+36*3], avg_error[(h-1)+36*4], avg_error[(h-1)+36*5], avg_error[(h-1)+36*6], avg_error[(h-1)+36*7], avg_error[(h-1)+36*8], avg_error[(h-1)+36*9]]
    std1_IUFNO_m10 = [variance_error[(h-1)+36*0],variance_error[(h-1)+36*1],variance_error[(h-1)+36*2],variance_error[(h-1)+36*3],variance_error[(h-1)+36*4],variance_error[(h-1)+36*5],variance_error[(h-1)+36*6],variance_error[(h-1)+36*7],variance_error[(h-1)+36*8],variance_error[(h-1)+36*9]]
    
    h=34
    mean1_IFNO_m10 = [avg_error[(h-1)+36*0], avg_error[(h-1)+36*1], avg_error[(h-1)+36*2], avg_error[(h-1)+36*3], avg_error[(h-1)+36*4], avg_error[(h-1)+36*5], avg_error[(h-1)+36*6], avg_error[(h-1)+36*7], avg_error[(h-1)+36*8], avg_error[(h-1)+36*9]]
    std1_IFNO_m10 = [variance_error[(h-1)+36*0],variance_error[(h-1)+36*1],variance_error[(h-1)+36*2],variance_error[(h-1)+36*3],variance_error[(h-1)+36*4],variance_error[(h-1)+36*5],variance_error[(h-1)+36*6],variance_error[(h-1)+36*7],variance_error[(h-1)+36*8],variance_error[(h-1)+36*9]]
    
    h=35
    mean1_DSM_m10 = [avg_error[(h-1)+36*0], avg_error[(h-1)+36*1], avg_error[(h-1)+36*2], avg_error[(h-1)+36*3], avg_error[(h-1)+36*4], avg_error[(h-1)+36*5], avg_error[(h-1)+36*6], avg_error[(h-1)+36*7], avg_error[(h-1)+36*8], avg_error[(h-1)+36*9]]
    std1_DSM_m10 = [variance_error[(h-1)+36*0],variance_error[(h-1)+36*1],variance_error[(h-1)+36*2],variance_error[(h-1)+36*3],variance_error[(h-1)+36*4],variance_error[(h-1)+36*5],variance_error[(h-1)+36*6],variance_error[(h-1)+36*7],variance_error[(h-1)+36*8],variance_error[(h-1)+36*9]]
    
    h=36
    mean1_fDNS = [avg_error[(h-1)+36*0], avg_error[(h-1)+36*1], avg_error[(h-1)+36*2], avg_error[(h-1)+36*3], avg_error[(h-1)+36*4], avg_error[(h-1)+36*5], avg_error[(h-1)+36*6], avg_error[(h-1)+36*7], avg_error[(h-1)+36*8], avg_error[(h-1)+36*9]]
    std1_fDNS = [variance_error[(h-1)+36*0],variance_error[(h-1)+36*1],variance_error[(h-1)+36*2],variance_error[(h-1)+36*3],variance_error[(h-1)+36*4],variance_error[(h-1)+36*5],variance_error[(h-1)+36*6],variance_error[(h-1)+36*7],variance_error[(h-1)+36*8],variance_error[(h-1)+36*9]]

    #########################################
    # 图形参数设置
    dpi = 600
    width, height = 15, 9
    fontSize = 40
    lineWidth = 2
    boxWidth = 2.5
    Lmajor, Lminor = 7, 4
    xlabPad, ylabPad = 10, 10
    xlabel = r"$\mathdefault{k}$"
    ylabel = r"$\mathdefault{Error}$"
    xlimit = [1, 10]
    #ylimit = [-1.6, 1.6]
    legend1 = ["F-IFNO", "F-IFNO_mag0.1","F-IFNO_mag0.5", "F-IFNO_mag1","F-IFNO_mag2", "F-IFNO_mag5","F-IFNO_mag10","fDNS"]
    colors = ['#A52A2A','#ff7f0e','gold','green','#1f77b4','#008080','purple','black','pink','#00FFFF','#FF00FF']

    fig = plt.figure(figsize=(width, height), dpi=dpi)
    plt.rcParams["font.size"] = fontSize
    plt.rcParams["axes.linewidth"] = lineWidth
    ax = fig.add_axes([0, 0, 1, 1])

    # X 轴设置
    ax.xaxis.set_minor_locator(mpl.ticker.MultipleLocator(1))        
    ax.xaxis.set_major_locator(mpl.ticker.MultipleLocator(1)) 
    ax.xaxis.set_major_formatter(mpl.ticker.FormatStrFormatter('%1.0f'))
    # Y 轴设置       
    # 自动设置主刻度和次刻度
    plt.yscale("linear")
    ax.yaxis.set_major_locator(ticker.MaxNLocator(nbins=6, min_n_ticks=5))  # Automatically set major ticks
    ax.yaxis.set_minor_locator(ticker.AutoMinorLocator(5))  # Automatically set minor ticks to be 5 times finer than major ticks
    ax.autoscale(enable=True, axis='y', tight=False)
    # formatter = mpl.ticker.LogFormatterSciNotation()
    ax.yaxis.set_major_formatter(mpl.ticker.ScalarFormatter())
    ax.yaxis.set_minor_formatter(mpl.ticker.NullFormatter())

    # 坐标轴和刻度设置
    ax.spines['right'].set_visible(True)
    ax.spines['top'].set_visible(True)
    ax.spines['bottom'].set_linewidth(boxWidth)
    ax.spines['left'].set_linewidth(boxWidth)
    ax.spines['top'].set_linewidth(boxWidth)
    ax.spines['right'].set_linewidth(boxWidth)

    ax.xaxis.set_tick_params(which='major', size=Lmajor, width=boxWidth, direction='in', pad=xlabPad, top=False)
    ax.xaxis.set_tick_params(which='minor', size=Lminor, width=boxWidth, direction='in', pad=xlabPad, top=False)
    ax.yaxis.set_tick_params(which='major', size=Lmajor, width=boxWidth, direction='in', pad=ylabPad, right=False)
    ax.yaxis.set_tick_params(which='minor', size=Lminor, width=boxWidth, direction='in', pad=ylabPad, right=False)

    plt.xlabel(xlabel, fontsize=40)
    plt.ylabel(ylabel, fontsize=40)
    #ax.set_ylim(ylimit[0], ylimit[1]) 
    plt.xticks(fontsize=40)
    plt.yticks(fontsize=40)  

    # Matplotlib 配置
    mpl.rc('font', family='STIXGeneral')
    mpl.rc('text', usetex=False)
    mpl.rcParams['xtick.direction'] = 'in'
    mpl.rcParams['ytick.direction'] = 'in'
    plt.rcParams["mathtext.fontset"] = "cm"

    plt.plot(x1[2:], mean1_F_IFNO[2:], color=colors[0], alpha=0.3, linewidth=2*lineWidth, linestyle='--',zorder=6)
    plt.errorbar(x1[2:], mean1_F_IFNO[2:], yerr=std1_F_IFNO[2:], fmt='o', color=colors[0], ecolor=colors[0], capsize=8, elinewidth=4, markeredgewidth=4, label=legend1[0],zorder=6)

    plt.plot(x1[2:], mean1_F_IFNO_m01[2:], color=colors[1], alpha=0.3, linewidth=2*lineWidth, linestyle='--',zorder=5)
    plt.errorbar(x1[2:], mean1_F_IFNO_m01[2:], yerr=std1_F_IFNO_m01[2:], fmt='o', color=colors[1], ecolor=colors[1], capsize=8, elinewidth=4, markeredgewidth=4, label=legend1[1],zorder=5)

    plt.plot(x1[2:], mean1_F_IFNO_m05[2:], color=colors[2], alpha=0.3, linewidth=2*lineWidth, linestyle='--',zorder=4)
    plt.errorbar(x1[2:], mean1_F_IFNO_m05[2:], yerr=std1_F_IFNO_m05[2:], fmt='o', color=colors[2], ecolor=colors[2], capsize=8, elinewidth=4, markeredgewidth=4, label=legend1[2],zorder=4)

    plt.plot(x1[2:], mean1_F_IFNO_m1[2:], color=colors[3], alpha=0.3, linewidth=2*lineWidth, linestyle='--',zorder=3)
    plt.errorbar(x1[2:], mean1_F_IFNO_m1[2:], yerr=std1_F_IFNO_m1[2:], fmt='o', color=colors[3], ecolor=colors[3], capsize=8, elinewidth=4, markeredgewidth=4, label=legend1[3],zorder=3)

    plt.plot(x1[2:], mean1_F_IFNO_m2[2:], color=colors[4], alpha=0.3, linewidth=2*lineWidth, linestyle='--',zorder=2)
    plt.errorbar(x1[2:], mean1_F_IFNO_m2[2:], yerr=std1_F_IFNO_m2[2:], fmt='o', color=colors[4], ecolor=colors[4], capsize=8, elinewidth=4, markeredgewidth=4, label=legend1[4],zorder=2)

    plt.plot(x1[2:], mean1_F_IFNO_m5[2:], color=colors[5], alpha=0.3, linewidth=2*lineWidth, linestyle='--',zorder=1)
    plt.errorbar(x1[2:], mean1_F_IFNO_m5[2:], yerr=std1_F_IFNO_m5[2:], fmt='o', color=colors[5], ecolor=colors[5], capsize=8, elinewidth=4, markeredgewidth=4, label=legend1[5],zorder=1)

    plt.plot(x1[2:], mean1_F_IFNO_m10[2:], color=colors[6], alpha=0.3, linewidth=2*lineWidth, linestyle='--',zorder=0)
    plt.errorbar(x1[2:], mean1_F_IFNO_m10[2:], yerr=std1_F_IFNO_m10[2:], fmt='o', color=colors[6], ecolor=colors[6], capsize=8, elinewidth=4, markeredgewidth=4, label=legend1[6],zorder=0)

    plt.plot(x1[2:], mean1_fDNS[2:], color=colors[7], alpha=0.3, linewidth=3*lineWidth, linestyle='--',zorder=7)
    plt.errorbar(x1[2:], mean1_fDNS[2:], yerr=std1_fDNS[2:], fmt='o', color=colors[7], ecolor=colors[7], capsize=8, elinewidth=4, markeredgewidth=4, label=legend1[7],zorder=7)

    # Matplotlib 配置 - 全局字体设置为 STIXGeneral
    mpl.rc('font', family='STIXGeneral')
    # 创建图例
    #lgd = plt.legend(loc='upper right', fontsize=30, frameon=True, framealpha=0, edgecolor='black', shadow=False)
    #plt.title("spectrum errorbar".format(vel_k), fontsize=40, color='black', loc='center', pad=15)

    # 显示网格
    #plt.grid()
    figPath1 = os.path.abspath("./vel_k_errorbar_with_mag_with_k/{}cases".format(case_number))
    gfile1 = "spectrum errorbar for F-IFNO_k=3-10_label.png"
    gpath1 = os.path.join(figPath1, gfile1)
    # 保存图形
    plt.savefig(gpath1, bbox_inches='tight')
    plt.close()

    #########################################
    # 图形参数设置
    dpi = 600
    width, height = 15, 9
    fontSize = 40
    lineWidth = 2
    boxWidth = 2.5
    Lmajor, Lminor = 7, 4
    xlabPad, ylabPad = 10, 10
    xlabel = r"$\mathdefault{k}$"
    ylabel = r"$\mathdefault{Error}$"
    xlimit = [1, 10]
    #ylimit = [-1.6, 1.6]
    legend1 = ["F-IUFNO", "F-IUFNO_mag0.1","F-IUFNO_mag0.5", "F-IUFNO_mag1","F-IUFNO_mag2", "F-IUFNO_mag5","F-IUFNO_mag10","fDNS"]
    colors = ['#A52A2A','#ff7f0e','gold','green','#1f77b4','#008080','purple','black','pink','#00FFFF','#FF00FF']

    fig = plt.figure(figsize=(width, height), dpi=dpi)
    plt.rcParams["font.size"] = fontSize
    plt.rcParams["axes.linewidth"] = lineWidth
    ax = fig.add_axes([0, 0, 1, 1])

    # X 轴设置
    ax.xaxis.set_minor_locator(mpl.ticker.MultipleLocator(1))        
    ax.xaxis.set_major_locator(mpl.ticker.MultipleLocator(1)) 
    ax.xaxis.set_major_formatter(mpl.ticker.FormatStrFormatter('%1.0f'))
    # Y 轴设置       
    # 自动设置主刻度和次刻度
    plt.yscale("linear")
    ax.yaxis.set_major_locator(ticker.MaxNLocator(nbins=6, min_n_ticks=5))  # Automatically set major ticks
    ax.yaxis.set_minor_locator(ticker.AutoMinorLocator(5))  # Automatically set minor ticks to be 5 times finer than major ticks
    ax.autoscale(enable=True, axis='y', tight=False)
    # formatter = mpl.ticker.LogFormatterSciNotation()
    ax.yaxis.set_major_formatter(mpl.ticker.ScalarFormatter())
    ax.yaxis.set_minor_formatter(mpl.ticker.NullFormatter())

    # 坐标轴和刻度设置
    ax.spines['right'].set_visible(True)
    ax.spines['top'].set_visible(True)
    ax.spines['bottom'].set_linewidth(boxWidth)
    ax.spines['left'].set_linewidth(boxWidth)
    ax.spines['top'].set_linewidth(boxWidth)
    ax.spines['right'].set_linewidth(boxWidth)

    ax.xaxis.set_tick_params(which='major', size=Lmajor, width=boxWidth, direction='in', pad=xlabPad, top=False)
    ax.xaxis.set_tick_params(which='minor', size=Lminor, width=boxWidth, direction='in', pad=xlabPad, top=False)
    ax.yaxis.set_tick_params(which='major', size=Lmajor, width=boxWidth, direction='in', pad=ylabPad, right=False)
    ax.yaxis.set_tick_params(which='minor', size=Lminor, width=boxWidth, direction='in', pad=ylabPad, right=False)

    plt.xlabel(xlabel, fontsize=40)
    plt.ylabel(ylabel, fontsize=40)
    #ax.set_ylim(ylimit[0], ylimit[1]) 
    plt.xticks(fontsize=40)
    plt.yticks(fontsize=40)  

    # Matplotlib 配置
    mpl.rc('font', family='STIXGeneral')
    mpl.rc('text', usetex=False)
    mpl.rcParams['xtick.direction'] = 'in'
    mpl.rcParams['ytick.direction'] = 'in'
    plt.rcParams["mathtext.fontset"] = "cm"

    plt.plot(x1[2:], mean1_F_IUFNO[2:], color=colors[0], alpha=0.3, linewidth=2*lineWidth, linestyle='--',zorder=6)
    plt.errorbar(x1[2:], mean1_F_IUFNO[2:], yerr=std1_F_IUFNO[2:], fmt='o', color=colors[0], ecolor=colors[0], capsize=8, elinewidth=4, markeredgewidth=4, label=legend1[0],zorder=6)

    plt.plot(x1[2:], mean1_F_IUFNO_m01[2:], color=colors[1], alpha=0.3, linewidth=2*lineWidth, linestyle='--',zorder=5)
    plt.errorbar(x1[2:], mean1_F_IUFNO_m01[2:], yerr=std1_F_IUFNO_m01[2:], fmt='o', color=colors[1], ecolor=colors[1], capsize=8, elinewidth=4, markeredgewidth=4, label=legend1[1],zorder=5)

    plt.plot(x1[2:], mean1_F_IUFNO_m05[2:], color=colors[2], alpha=0.3, linewidth=2*lineWidth, linestyle='--',zorder=4)
    plt.errorbar(x1[2:], mean1_F_IUFNO_m05[2:], yerr=std1_F_IUFNO_m05[2:], fmt='o', color=colors[2], ecolor=colors[2], capsize=8, elinewidth=4, markeredgewidth=4, label=legend1[2],zorder=4)

    plt.plot(x1[2:], mean1_F_IUFNO_m1[2:], color=colors[3], alpha=0.3, linewidth=2*lineWidth, linestyle='--',zorder=3)
    plt.errorbar(x1[2:], mean1_F_IUFNO_m1[2:], yerr=std1_F_IUFNO_m1[2:], fmt='o', color=colors[3], ecolor=colors[3], capsize=8, elinewidth=4, markeredgewidth=4, label=legend1[3],zorder=3)

    plt.plot(x1[2:], mean1_F_IUFNO_m2[2:], color=colors[4], alpha=0.3, linewidth=2*lineWidth, linestyle='--',zorder=2)
    plt.errorbar(x1[2:], mean1_F_IUFNO_m2[2:], yerr=std1_F_IUFNO_m2[2:], fmt='o', color=colors[4], ecolor=colors[4], capsize=8, elinewidth=4, markeredgewidth=4, label=legend1[4],zorder=2)

    plt.plot(x1[2:], mean1_F_IUFNO_m5[2:], color=colors[5], alpha=0.3, linewidth=2*lineWidth, linestyle='--',zorder=1)
    plt.errorbar(x1[2:], mean1_F_IUFNO_m5[2:], yerr=std1_F_IUFNO_m5[2:], fmt='o', color=colors[5], ecolor=colors[5], capsize=8, elinewidth=4, markeredgewidth=4, label=legend1[5],zorder=1)

    plt.plot(x1[2:], mean1_F_IUFNO_m10[2:], color=colors[6], alpha=0.3, linewidth=2*lineWidth, linestyle='--',zorder=0)
    plt.errorbar(x1[2:], mean1_F_IUFNO_m10[2:], yerr=std1_F_IUFNO_m10[2:], fmt='o', color=colors[6], ecolor=colors[6], capsize=8, elinewidth=4, markeredgewidth=4, label=legend1[6],zorder=0)

    plt.plot(x1[2:], mean1_fDNS[2:], color=colors[7], alpha=0.3, linewidth=3*lineWidth, linestyle='--',zorder=7)
    plt.errorbar(x1[2:], mean1_fDNS[2:], yerr=std1_fDNS[2:], fmt='o', color=colors[7], ecolor=colors[7], capsize=8, elinewidth=4, markeredgewidth=4, label=legend1[7],zorder=7)

    # Matplotlib 配置 - 全局字体设置为 STIXGeneral
    mpl.rc('font', family='STIXGeneral')
    # 创建图例
    #lgd = plt.legend(loc='lower right', fontsize=30, frameon=True, framealpha=0, edgecolor='black', shadow=False)
    #plt.title("spectrum errorbar".format(vel_k), fontsize=40, color='black', loc='center', pad=15)

    # 显示网格
    #plt.grid()
    figPath1 = os.path.abspath("./vel_k_errorbar_with_mag_with_k/{}cases".format(case_number))
    gfile1 = "spectrum errorbar for F-IUFNO_k=3-10_label.png"
    gpath1 = os.path.join(figPath1, gfile1)
    # 保存图形
    plt.savefig(gpath1, bbox_inches='tight')
    plt.close()

    #########################################
    # 图形参数设置
    dpi = 600
    width, height = 15, 9
    fontSize = 40
    lineWidth = 2
    boxWidth = 2.5
    Lmajor, Lminor = 7, 4
    xlabPad, ylabPad = 10, 10
    xlabel = r"$\mathdefault{k}$"
    ylabel = r"$\mathdefault{Error}$"
    xlimit = [1, 10]
    #ylimit = [-1.6, 1.6]
    legend1 = ["IUFNO", "IUFNO_mag0.1","IUFNO_mag0.5", "IUFNO_mag1","IUFNO_mag2", "IUFNO_mag5","IUFNO_mag10","fDNS"]
    colors = ['#A52A2A','#ff7f0e','gold','green','#1f77b4','#008080','purple','black','pink','#00FFFF','#FF00FF']

    fig = plt.figure(figsize=(width, height), dpi=dpi)
    plt.rcParams["font.size"] = fontSize
    plt.rcParams["axes.linewidth"] = lineWidth
    ax = fig.add_axes([0, 0, 1, 1])

    # X 轴设置
    ax.xaxis.set_minor_locator(mpl.ticker.MultipleLocator(1))        
    ax.xaxis.set_major_locator(mpl.ticker.MultipleLocator(1)) 
    ax.xaxis.set_major_formatter(mpl.ticker.FormatStrFormatter('%1.0f'))
    # Y 轴设置       
    # 自动设置主刻度和次刻度
    plt.yscale("linear")
    ax.yaxis.set_major_locator(ticker.MaxNLocator(nbins=6, min_n_ticks=5))  # Automatically set major ticks
    ax.yaxis.set_minor_locator(ticker.AutoMinorLocator(5))  # Automatically set minor ticks to be 5 times finer than major ticks
    ax.autoscale(enable=True, axis='y', tight=False)
    # formatter = mpl.ticker.LogFormatterSciNotation()
    ax.yaxis.set_major_formatter(mpl.ticker.ScalarFormatter())
    ax.yaxis.set_minor_formatter(mpl.ticker.NullFormatter())

    # 坐标轴和刻度设置
    ax.spines['right'].set_visible(True)
    ax.spines['top'].set_visible(True)
    ax.spines['bottom'].set_linewidth(boxWidth)
    ax.spines['left'].set_linewidth(boxWidth)
    ax.spines['top'].set_linewidth(boxWidth)
    ax.spines['right'].set_linewidth(boxWidth)

    ax.xaxis.set_tick_params(which='major', size=Lmajor, width=boxWidth, direction='in', pad=xlabPad, top=False)
    ax.xaxis.set_tick_params(which='minor', size=Lminor, width=boxWidth, direction='in', pad=xlabPad, top=False)
    ax.yaxis.set_tick_params(which='major', size=Lmajor, width=boxWidth, direction='in', pad=ylabPad, right=False)
    ax.yaxis.set_tick_params(which='minor', size=Lminor, width=boxWidth, direction='in', pad=ylabPad, right=False)

    plt.xlabel(xlabel, fontsize=40)
    plt.ylabel(ylabel, fontsize=40)
    #ax.set_ylim(ylimit[0], ylimit[1]) 
    plt.xticks(fontsize=40)
    plt.yticks(fontsize=40)  

    # Matplotlib 配置
    mpl.rc('font', family='STIXGeneral')
    mpl.rc('text', usetex=False)
    mpl.rcParams['xtick.direction'] = 'in'
    mpl.rcParams['ytick.direction'] = 'in'
    plt.rcParams["mathtext.fontset"] = "cm"

    plt.plot(x1[2:], mean1_IUFNO[2:], color=colors[0], alpha=0.3, linewidth=2*lineWidth, linestyle='--',zorder=6)
    plt.errorbar(x1[2:], mean1_IUFNO[2:], yerr=std1_IUFNO[2:], fmt='o', color=colors[0], ecolor=colors[0], capsize=8, elinewidth=4, markeredgewidth=4, label=legend1[0],zorder=6)

    plt.plot(x1[2:], mean1_IUFNO_m01[2:], color=colors[1], alpha=0.3, linewidth=2*lineWidth, linestyle='--',zorder=5)
    plt.errorbar(x1[2:], mean1_IUFNO_m01[2:], yerr=std1_IUFNO_m01[2:], fmt='o', color=colors[1], ecolor=colors[1], capsize=8, elinewidth=4, markeredgewidth=4, label=legend1[1],zorder=5)

    plt.plot(x1[2:], mean1_IUFNO_m05[2:], color=colors[2], alpha=0.3, linewidth=2*lineWidth, linestyle='--',zorder=4)
    plt.errorbar(x1[2:], mean1_IUFNO_m05[2:], yerr=std1_IUFNO_m05[2:], fmt='o', color=colors[2], ecolor=colors[2], capsize=8, elinewidth=4, markeredgewidth=4, label=legend1[2],zorder=4)

    plt.plot(x1[2:], mean1_IUFNO_m1[2:], color=colors[3], alpha=0.3, linewidth=2*lineWidth, linestyle='--',zorder=3)
    plt.errorbar(x1[2:], mean1_IUFNO_m1[2:], yerr=std1_IUFNO_m1[2:], fmt='o', color=colors[3], ecolor=colors[3], capsize=8, elinewidth=4, markeredgewidth=4, label=legend1[3],zorder=3)

    plt.plot(x1[2:], mean1_IUFNO_m2[2:], color=colors[4], alpha=0.3, linewidth=2*lineWidth, linestyle='--',zorder=2)
    plt.errorbar(x1[2:], mean1_IUFNO_m2[2:], yerr=std1_IUFNO_m2[2:], fmt='o', color=colors[4], ecolor=colors[4], capsize=8, elinewidth=4, markeredgewidth=4, label=legend1[4],zorder=2)

    plt.plot(x1[2:], mean1_IUFNO_m5[2:], color=colors[5], alpha=0.3, linewidth=2*lineWidth, linestyle='--',zorder=1)
    plt.errorbar(x1[2:], mean1_IUFNO_m5[2:], yerr=std1_IUFNO_m5[2:], fmt='o', color=colors[5], ecolor=colors[5], capsize=8, elinewidth=4, markeredgewidth=4, label=legend1[5],zorder=1)

    plt.plot(x1[2:], mean1_IUFNO_m10[2:], color=colors[6], alpha=0.3, linewidth=2*lineWidth, linestyle='--',zorder=0)
    plt.errorbar(x1[2:], mean1_IUFNO_m10[2:], yerr=std1_IUFNO_m10[2:], fmt='o', color=colors[6], ecolor=colors[6], capsize=8, elinewidth=4, markeredgewidth=4, label=legend1[6],zorder=0)

    plt.plot(x1[2:], mean1_fDNS[2:], color=colors[7], alpha=0.3, linewidth=3*lineWidth, linestyle='--',zorder=7)
    plt.errorbar(x1[2:], mean1_fDNS[2:], yerr=std1_fDNS[2:], fmt='o', color=colors[7], ecolor=colors[7], capsize=8, elinewidth=4, markeredgewidth=4, label=legend1[7],zorder=7)

    # Matplotlib 配置 - 全局字体设置为 STIXGeneral
    mpl.rc('font', family='STIXGeneral')
    # 创建图例
    #lgd = plt.legend(loc='upper right', fontsize=30, frameon=True, framealpha=0, edgecolor='black', shadow=False)
    #plt.title("spectrum errorbar".format(vel_k), fontsize=40, color='black', loc='center', pad=15)

    # 显示网格
    #plt.grid()
    figPath1 = os.path.abspath("./vel_k_errorbar_with_mag_with_k/{}cases".format(case_number))
    gfile1 = "spectrum errorbar for IUFNO_k=3-10_label.png"
    gpath1 = os.path.join(figPath1, gfile1)
    # 保存图形
    plt.savefig(gpath1, bbox_inches='tight')
    plt.close()

    #########################################
    # 图形参数设置
    dpi = 600
    width, height = 15, 9
    fontSize = 40
    lineWidth = 2
    boxWidth = 2.5
    Lmajor, Lminor = 7, 4
    xlabPad, ylabPad = 10, 10
    xlabel = r"$\mathdefault{k}$"
    ylabel = r"$\mathdefault{Error}$"
    xlimit = [1, 10]
    #ylimit = [-1.6, 1.6]
    legend1 = ["IFNO", "IFNO_mag0.1","IFNO_mag0.5", "IFNO_mag1","IFNO_mag2", "IFNO_mag5","IFNO_mag10","fDNS"]
    colors = ['#A52A2A','#ff7f0e','gold','green','#1f77b4','#008080','purple','black','pink','#00FFFF','#FF00FF']

    fig = plt.figure(figsize=(width, height), dpi=dpi)
    plt.rcParams["font.size"] = fontSize
    plt.rcParams["axes.linewidth"] = lineWidth
    ax = fig.add_axes([0, 0, 1, 1])

    # X 轴设置
    ax.xaxis.set_minor_locator(mpl.ticker.MultipleLocator(1))        
    ax.xaxis.set_major_locator(mpl.ticker.MultipleLocator(1)) 
    ax.xaxis.set_major_formatter(mpl.ticker.FormatStrFormatter('%1.0f'))
    # Y 轴设置       
    # 自动设置主刻度和次刻度
    plt.yscale("linear")
    ax.yaxis.set_major_locator(ticker.MaxNLocator(nbins=6, min_n_ticks=5))  # Automatically set major ticks
    ax.yaxis.set_minor_locator(ticker.AutoMinorLocator(5))  # Automatically set minor ticks to be 5 times finer than major ticks
    ax.autoscale(enable=True, axis='y', tight=False)
    # formatter = mpl.ticker.LogFormatterSciNotation()
    ax.yaxis.set_major_formatter(mpl.ticker.ScalarFormatter())
    ax.yaxis.set_minor_formatter(mpl.ticker.NullFormatter())

    # 坐标轴和刻度设置
    ax.spines['right'].set_visible(True)
    ax.spines['top'].set_visible(True)
    ax.spines['bottom'].set_linewidth(boxWidth)
    ax.spines['left'].set_linewidth(boxWidth)
    ax.spines['top'].set_linewidth(boxWidth)
    ax.spines['right'].set_linewidth(boxWidth)

    ax.xaxis.set_tick_params(which='major', size=Lmajor, width=boxWidth, direction='in', pad=xlabPad, top=False)
    ax.xaxis.set_tick_params(which='minor', size=Lminor, width=boxWidth, direction='in', pad=xlabPad, top=False)
    ax.yaxis.set_tick_params(which='major', size=Lmajor, width=boxWidth, direction='in', pad=ylabPad, right=False)
    ax.yaxis.set_tick_params(which='minor', size=Lminor, width=boxWidth, direction='in', pad=ylabPad, right=False)

    plt.xlabel(xlabel, fontsize=40)
    plt.ylabel(ylabel, fontsize=40)
    #ax.set_ylim(ylimit[0], ylimit[1]) 
    plt.xticks(fontsize=40)
    plt.yticks(fontsize=40)  

    # Matplotlib 配置
    mpl.rc('font', family='STIXGeneral')
    mpl.rc('text', usetex=False)
    mpl.rcParams['xtick.direction'] = 'in'
    mpl.rcParams['ytick.direction'] = 'in'
    plt.rcParams["mathtext.fontset"] = "cm"

    plt.plot(x1[2:], mean1_IFNO[2:], color=colors[0], alpha=0.3, linewidth=2*lineWidth, linestyle='--',zorder=6)
    plt.errorbar(x1[2:], mean1_IFNO[2:], yerr=std1_IFNO[2:], fmt='o', color=colors[0], ecolor=colors[0], capsize=8, elinewidth=4, markeredgewidth=4, label=legend1[0],zorder=6)

    plt.plot(x1[2:], mean1_IFNO_m01[2:], color=colors[1], alpha=0.3, linewidth=2*lineWidth, linestyle='--',zorder=5)
    plt.errorbar(x1[2:], mean1_IFNO_m01[2:], yerr=std1_IFNO_m01[2:], fmt='o', color=colors[1], ecolor=colors[1], capsize=8, elinewidth=4, markeredgewidth=4, label=legend1[1],zorder=5)

    plt.plot(x1[2:], mean1_IFNO_m05[2:], color=colors[2], alpha=0.3, linewidth=2*lineWidth, linestyle='--',zorder=4)
    plt.errorbar(x1[2:], mean1_IFNO_m05[2:], yerr=std1_IFNO_m05[2:], fmt='o', color=colors[2], ecolor=colors[2], capsize=8, elinewidth=4, markeredgewidth=4, label=legend1[2],zorder=4)

    plt.plot(x1[2:], mean1_IFNO_m1[2:], color=colors[3], alpha=0.3, linewidth=2*lineWidth, linestyle='--',zorder=3)
    plt.errorbar(x1[2:], mean1_IFNO_m1[2:], yerr=std1_IFNO_m1[2:], fmt='o', color=colors[3], ecolor=colors[3], capsize=8, elinewidth=4, markeredgewidth=4, label=legend1[3],zorder=3)

    plt.plot(x1[2:], mean1_IFNO_m2[2:], color=colors[4], alpha=0.3, linewidth=2*lineWidth, linestyle='--',zorder=2)
    plt.errorbar(x1[2:], mean1_IFNO_m2[2:], yerr=std1_IFNO_m2[2:], fmt='o', color=colors[4], ecolor=colors[4], capsize=8, elinewidth=4, markeredgewidth=4, label=legend1[4],zorder=2)

    plt.plot(x1[2:], mean1_IFNO_m5[2:], color=colors[5], alpha=0.3, linewidth=2*lineWidth, linestyle='--',zorder=1)
    plt.errorbar(x1[2:], mean1_IFNO_m5[2:], yerr=std1_IFNO_m5[2:], fmt='o', color=colors[5], ecolor=colors[5], capsize=8, elinewidth=4, markeredgewidth=4, label=legend1[5],zorder=1)

    plt.plot(x1[2:], mean1_IFNO_m10[2:], color=colors[6], alpha=0.3, linewidth=2*lineWidth, linestyle='--',zorder=0)
    plt.errorbar(x1[2:], mean1_IFNO_m10[2:], yerr=std1_IFNO_m10[2:], fmt='o', color=colors[6], ecolor=colors[6], capsize=8, elinewidth=4, markeredgewidth=4, label=legend1[6],zorder=0)

    plt.plot(x1[2:], mean1_fDNS[2:], color=colors[7], alpha=0.3, linewidth=3*lineWidth, linestyle='--',zorder=7)
    plt.errorbar(x1[2:], mean1_fDNS[2:], yerr=std1_fDNS[2:], fmt='o', color=colors[7], ecolor=colors[7], capsize=8, elinewidth=4, markeredgewidth=4, label=legend1[7],zorder=7)

    # Matplotlib 配置 - 全局字体设置为 STIXGeneral
    mpl.rc('font', family='STIXGeneral')
    # 创建图例
    #lgd = plt.legend(loc='upper right', fontsize=30, frameon=True, framealpha=0, edgecolor='black', shadow=False)
    #plt.title("spectrum errorbar".format(vel_k), fontsize=40, color='black', loc='center', pad=15)

    # 显示网格
    #plt.grid()
    figPath1 = os.path.abspath("./vel_k_errorbar_with_mag_with_k/{}cases".format(case_number))
    gfile1 = "spectrum errorbar for IFNO_k=3-10_label.png"
    gpath1 = os.path.join(figPath1, gfile1)
    # 保存图形
    plt.savefig(gpath1, bbox_inches='tight')
    plt.close()


    #########################################
    # 图形参数设置
    dpi = 600
    width, height = 15, 9
    fontSize = 40
    lineWidth = 2
    boxWidth = 2.5
    Lmajor, Lminor = 7, 4
    xlabPad, ylabPad = 10, 10
    xlabel = r"$\mathdefault{k}$"
    ylabel = r"$\mathdefault{Error}$"
    xlimit = [1, 10]
    #ylimit = [-1.6, 1.6]
    legend1 = ["DSM", "DSM_mag0.1","DSM_mag0.5", "DSM_mag1","DSM_mag2", "DSM_mag5","DSM_mag10","fDNS"]
    colors = ['#A52A2A','#ff7f0e','gold','green','#1f77b4','#008080','purple','black','pink','#00FFFF','#FF00FF']

    fig = plt.figure(figsize=(width, height), dpi=dpi)
    plt.rcParams["font.size"] = fontSize
    plt.rcParams["axes.linewidth"] = lineWidth
    ax = fig.add_axes([0, 0, 1, 1])

    # X 轴设置
    ax.xaxis.set_minor_locator(mpl.ticker.MultipleLocator(1))        
    ax.xaxis.set_major_locator(mpl.ticker.MultipleLocator(1)) 
    ax.xaxis.set_major_formatter(mpl.ticker.FormatStrFormatter('%1.0f'))
    # Y 轴设置       
    # 自动设置主刻度和次刻度
    plt.yscale("linear")
    ax.yaxis.set_major_locator(ticker.MaxNLocator(nbins=6, min_n_ticks=5))  # Automatically set major ticks
    ax.yaxis.set_minor_locator(ticker.AutoMinorLocator(5))  # Automatically set minor ticks to be 5 times finer than major ticks
    ax.autoscale(enable=True, axis='y', tight=False)
    # formatter = mpl.ticker.LogFormatterSciNotation()
    ax.yaxis.set_major_formatter(mpl.ticker.ScalarFormatter())
    ax.yaxis.set_minor_formatter(mpl.ticker.NullFormatter())

    # 坐标轴和刻度设置
    ax.spines['right'].set_visible(True)
    ax.spines['top'].set_visible(True)
    ax.spines['bottom'].set_linewidth(boxWidth)
    ax.spines['left'].set_linewidth(boxWidth)
    ax.spines['top'].set_linewidth(boxWidth)
    ax.spines['right'].set_linewidth(boxWidth)

    ax.xaxis.set_tick_params(which='major', size=Lmajor, width=boxWidth, direction='in', pad=xlabPad, top=False)
    ax.xaxis.set_tick_params(which='minor', size=Lminor, width=boxWidth, direction='in', pad=xlabPad, top=False)
    ax.yaxis.set_tick_params(which='major', size=Lmajor, width=boxWidth, direction='in', pad=ylabPad, right=False)
    ax.yaxis.set_tick_params(which='minor', size=Lminor, width=boxWidth, direction='in', pad=ylabPad, right=False)

    plt.xlabel(xlabel, fontsize=40)
    plt.ylabel(ylabel, fontsize=40)
    #ax.set_ylim(ylimit[0], ylimit[1]) 
    plt.xticks(fontsize=40)
    plt.yticks(fontsize=40)  

    # Matplotlib 配置
    mpl.rc('font', family='STIXGeneral')
    mpl.rc('text', usetex=False)
    mpl.rcParams['xtick.direction'] = 'in'
    mpl.rcParams['ytick.direction'] = 'in'
    plt.rcParams["mathtext.fontset"] = "cm"

    plt.plot(x1[2:], mean1_DSM[2:], color=colors[0], alpha=0.3, linewidth=2*lineWidth, linestyle='--',zorder=4)
    plt.errorbar(x1[2:], mean1_DSM[2:], yerr=std1_DSM[2:], fmt='o', color=colors[0], ecolor=colors[0], capsize=8, elinewidth=4, markeredgewidth=4, label=legend1[0],zorder=4)

    plt.plot(x1[2:], mean1_DSM_m01[2:], color=colors[1], alpha=0.3, linewidth=2*lineWidth, linestyle='--',zorder=3)
    plt.errorbar(x1[2:], mean1_DSM_m01[2:], yerr=std1_DSM_m01[2:], fmt='o', color=colors[1], ecolor=colors[1], capsize=8, elinewidth=4, markeredgewidth=4, label=legend1[1],zorder=3)

    plt.plot(x1[2:], mean1_DSM_m05[2:], color=colors[2], alpha=0.3, linewidth=2*lineWidth, linestyle='--',zorder=2)
    plt.errorbar(x1[2:], mean1_DSM_m05[2:], yerr=std1_DSM_m05[2:], fmt='o', color=colors[2], ecolor=colors[2], capsize=8, elinewidth=4, markeredgewidth=4, label=legend1[2],zorder=2)

    plt.plot(x1[2:], mean1_DSM_m1[2:], color=colors[3], alpha=0.3, linewidth=2*lineWidth, linestyle='--',zorder=1)
    plt.errorbar(x1[2:], mean1_DSM_m1[2:], yerr=std1_DSM_m1[2:], fmt='o', color=colors[3], ecolor=colors[3], capsize=8, elinewidth=4, markeredgewidth=4, label=legend1[3],zorder=1)

    plt.plot(x1[2:], mean1_DSM_m2[2:], color=colors[4], alpha=0.3, linewidth=2*lineWidth, linestyle='--',zorder=0)
    plt.errorbar(x1[2:], mean1_DSM_m2[2:], yerr=std1_DSM_m2[2:], fmt='o', color=colors[4], ecolor=colors[4], capsize=8, elinewidth=4, markeredgewidth=4, label=legend1[4],zorder=0)

    plt.plot(x1[2:], mean1_fDNS[2:], color=colors[7], alpha=0.3, linewidth=3*lineWidth, linestyle='--',zorder=5)
    plt.errorbar(x1[2:], mean1_fDNS[2:], yerr=std1_fDNS[2:], fmt='o', color=colors[7], ecolor=colors[7], capsize=8, elinewidth=4, markeredgewidth=4, label=legend1[7],zorder=5)

    # Matplotlib 配置 - 全局字体设置为 STIXGeneral
    mpl.rc('font', family='STIXGeneral')
    # 创建图例
    #lgd = plt.legend(loc='lower right', fontsize=30, frameon=True, framealpha=0, edgecolor='black', shadow=False)
    #plt.title("spectrum errorbar".format(vel_k), fontsize=40, color='black', loc='center', pad=15)

    # 显示网格
    #plt.grid()
    figPath1 = os.path.abspath("./vel_k_errorbar_with_mag_with_k/{}cases".format(case_number))
    gfile1 = "spectrum errorbar for DSM_k=3-10_label.png"
    gpath1 = os.path.join(figPath1, gfile1)
    # 保存图形
    plt.savefig(gpath1, bbox_inches='tight')
    plt.close()
































