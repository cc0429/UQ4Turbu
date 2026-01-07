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

case_number_list =[30,1,10,20]

for k, case_number in enumerate(case_number_list):

    #-------------------------------------------------------------读入数据，


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
    file_path1 = './Ek_error_variance/{}cases/RMS.dat'.format(case_number)
    # 写入文件，第一行是标题
    header1 = ["F_IFNO_rms", "F_IUFNO_rms", "IUFNO_rms", "IFNO_rms", "DSM_rms", "F_IFNO_mag0.1_rms", "F_IUFNO_mag0.1_rms", "IUFNO_mag0.1_rms", "IFNO_mag0.1_rms", "DSM_mag0.1_rms", "F_IFNO_mag0.5_rms", "F_IUFNO_mag0.5_rms", "IUFNO_mag0.5_rms", "IFNO_mag0.5_rms", "DSM_mag0.5_rms", "F_IFNO_mag1_rms", "F_IUFNO_mag1_rms", "IUFNO_mag1_rms", "IFNO_mag1_rms", "DSM_mag1_rms", "F_IFNO_mag2_rms", "F_IUFNO_mag2_rms", "IUFNO_mag2_rms", "IFNO_mag2_rms", "DSM_mag2_rms", "F_IFNO_mag5_rms", "F_IUFNO_mag5_rms", "IUFNO_mag5_rms", "IFNO_mag5_rms", "DSM_mag5_rms", "F_IFNO_mag10_rms", "F_IUFNO_mag10_rms", "IUFNO_mag10_rms", "IFNO_mag10_rms", "DSM_mag10_rms", "fDNS_rms"]


    combined_data1 = np.column_stack((header1, rms_results_array.astype(str)))
    with open(file_path1, 'w') as f:
        for row in combined_data1:
            f.write(f'{row[0]}    {row[1]}\n')  # 标题和数值列用空格分隔

    print(f"数据已成功保存到 {file_path1}")
    
    #####savefiles###########
    file_path2 = './Ek_error_variance/{}cases/AVG.dat'.format(case_number)
    header2 = ["F_IFNO_avg", "F_IUFNO_avg", "IUFNO_avg", "IFNO_avg", "DSM_avg", "F_IFNO_mag0.1_avg", "F_IUFNO_mag0.1_avg", "IUFNO_mag0.1_avg", "IFNO_mag0.1_avg", "DSM_mag0.1_avg", "F_IFNO_mag0.5_avg", "F_IUFNO_mag0.5_avg", "IUFNO_mag0.5_avg", "IFNO_mag0.5_avg", "DSM_mag0.5_avg", "F_IFNO_mag1_avg", "F_IUFNO_mag1_avg", "IUFNO_mag1_avg", "IFNO_mag1_avg", "DSM_mag1_avg", "F_IFNO_mag2_avg", "F_IUFNO_mag2_avg", "IUFNO_mag2_avg", "IFNO_mag2_avg", "DSM_mag2_avg", "F_IFNO_mag5_avg", "F_IUFNO_mag5_avg", "IUFNO_mag5_avg", "IFNO_mag5_avg", "DSM_mag5_avg", "F_IFNO_mag10_avg", "F_IUFNO_mag10_avg", "IUFNO_mag10_avg", "IFNO_mag10_avg", "DSM_mag10_avg", "fDNS_avg"]


    combined_data2 = np.column_stack((header2, avg_results_array.astype(str)))
    with open(file_path2, 'w') as f:
        for row in combined_data2:
            f.write(f'{row[0]}    {row[1]}\n')  # 标题和数值列用空格分隔

    print(f"数据已成功保存到 {file_path2}")      
    
    