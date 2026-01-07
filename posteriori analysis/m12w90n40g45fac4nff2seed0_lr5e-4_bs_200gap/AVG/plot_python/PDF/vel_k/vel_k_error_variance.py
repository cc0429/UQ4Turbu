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

time_steps = 600
case_number_list =[30,1,10,20]
vel_k_list = [1,2,3,4,5,6,7,8,9,10]

for kk, case_number in enumerate(case_number_list):
    for k, vel_k in enumerate(vel_k_list):
        #-------------------------------------------------------------读入数据，
        ###小數點后3位###

        fDNS = np.loadtxt("./result/{}cases/error_with_time_fDNS_k={}.dat".format(case_number, vel_k), dtype=float)
        IUFNO_40ep = np.loadtxt("./result/{}cases/error_with_time_IUFNO_k={}.dat".format(case_number, vel_k), dtype=float)
        F_IUFNO_40ep = np.loadtxt("./result/{}cases/error_with_time_F_IUFNO_k={}.dat".format(case_number, vel_k), dtype=float)
        F_IFNO_40ep = np.loadtxt("./result/{}cases/error_with_time_F_IFNO_k={}.dat".format(case_number, vel_k), dtype=float)
        IFNO = np.loadtxt("./result/{}cases/error_with_time_IFNO_k={}.dat".format(case_number, vel_k), dtype=float)
        DSM = np.loadtxt("./result/{}cases/error_with_time_DSM_k={}.dat".format(case_number, vel_k), dtype=float)
        
        #-------------------------输入参数
        period = 10 #10个波数
    

        #-------------------------输入参数
        # time_advance=[20]  #挑推进时间画图
        # time_advance=[40]  #挑推进时间画图
        #time_advance=[1,2,3,10,15,20,25,30,40,50,60,70,80,90,100,110,120,130,140,150,160,170,180,190,200,210,220,230,240,250]  #挑推进时间画图
        data1=F_IFNO_40ep[:,1]
        data2=F_IUFNO_40ep[:,1]
        data3=IUFNO_40ep[:,1]
        data4=IFNO[:,1]
        data5=DSM[:,1]
        
        data6=fDNS[:,1]

        data_list = [data1, data2, data3, data4, data5, data6]

        rms_results = []
        avg_results = []

        # 遍历每个数据集计算 RMS、平均值和方差
        for i, data in enumerate(data_list, start=1):
            # 计算 RMS 误差
            rms_error = np.sqrt(np.mean(np.square(data)))
            avg_error = np.mean(data)
            
            # 计算误差的方差
            variance_error = np.var(data)
            
            # 以 "RMS ± 方差" 和 "AVG ± 方差" 形式存储结果
            rms_result = f"{rms_error:.8f} ± {variance_error:.8f}"
            avg_result = f"{avg_error:.8f} ± {variance_error:.8f}"
            
            rms_results.append(rms_result)
            avg_results.append(avg_result)

        rms_results_array = np.array(rms_results).reshape(-1, 1)
        avg_results_array = np.array(avg_results).reshape(-1, 1)
        #####savefiles###########
        file_path1 = './vel_k_error_variance/{}cases/RMS_k={}.dat'.format(case_number,vel_k)
        # 写入文件，第一行是标题
        header1 = ["F_IFNO_rms", "F_IUFNO_rms", "IUFNO_rms", "IFNO_rms", "DSM_rms", "fDNS_rms"]


        combined_data1 = np.column_stack((header1, rms_results_array.astype(str)))
        with open(file_path1, 'w') as f:
            for row in combined_data1:
                f.write(f'{row[0]}    {row[1]}\n')  # 标题和数值列用空格分隔

        print(f"数据已成功保存到 {file_path1}")
        
        #####savefiles###########
        file_path2 = './vel_k_error_variance/{}cases/AVG_k={}.dat'.format(case_number,vel_k)
        header2 = [
            "F_IFNO_avg", "F_IUFNO_avg", "IUFNO_avg",
             "IFNO_avg", "DSM_avg","fDNS_avg"
        ]


        combined_data2 = np.column_stack((header2, avg_results_array.astype(str)))
        with open(file_path2, 'w') as f:
            for row in combined_data2:
                f.write(f'{row[0]}    {row[1]}\n')  # 标题和数值列用空格分隔

        print(f"数据已成功保存到 {file_path2}")      
        
        