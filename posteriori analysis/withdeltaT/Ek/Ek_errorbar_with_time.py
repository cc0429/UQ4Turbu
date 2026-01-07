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
case_number_list =[30]
time_steps=600
for k, case_number in enumerate(case_number_list):

    #-------------------------------------------------------------读入数据，


    fDNS_20 = np.loadtxt("../../m12w90n40g45fac4nff2seed0_lr5e-4_bs5_200gap_4_20gap/AVG/plot_python/PDF/Ek/result/{}cases/error_with_time_fDNS.dat".format(case_number), dtype=float)
    IUFNO_20 = np.loadtxt("../../m12w90n40g45fac4nff2seed0_lr5e-4_bs5_200gap_4_20gap/AVG/plot_python/PDF/Ek/result/{}cases/error_with_time_IUFNO.dat".format(case_number), dtype=float)
    F_IUFNO_20 = np.loadtxt("../../m12w90n40g45fac4nff2seed0_lr5e-4_bs5_200gap_4_20gap/AVG/plot_python/PDF/Ek/result/{}cases/error_with_time_F_IUFNO.dat".format(case_number), dtype=float)
    F_IFNO_20 = np.loadtxt("../../m12w90n40g45fac4nff2seed0_lr5e-4_bs5_200gap_4_20gap/AVG/plot_python/PDF/Ek/result/{}cases/error_with_time_F_IFNO.dat".format(case_number), dtype=float)
    IFNO_20 = np.loadtxt("../../m12w90n40g45fac4nff2seed0_lr5e-4_bs5_200gap_4_20gap/AVG/plot_python/PDF/Ek/result/{}cases/error_with_time_IFNO.dat".format(case_number), dtype=float)
    DSM_20 = np.loadtxt("../../m12w90n40g45fac4nff2seed0_lr5e-4_bs5_200gap_4_20gap/AVG/plot_python/PDF/Ek/result/{}cases/error_with_time_DSM.dat".format(case_number), dtype=float)
    
    fDNS_40 = np.loadtxt("../../m12w90n40g45fac4nff2seed0_lr5e-4_bs5_40gap/AVG/plot_python/PDF/Ek/result/{}cases/error_with_time_fDNS.dat".format(case_number), dtype=float)
    IUFNO_40 = np.loadtxt("../../m12w90n40g45fac4nff2seed0_lr5e-4_bs5_40gap/AVG/plot_python/PDF/Ek/result/{}cases/error_with_time_IUFNO.dat".format(case_number), dtype=float)
    F_IUFNO_40 = np.loadtxt("../../m12w90n40g45fac4nff2seed0_lr5e-4_bs5_40gap/AVG/plot_python/PDF/Ek/result/{}cases/error_with_time_F_IUFNO.dat".format(case_number), dtype=float)
    F_IFNO_40 = np.loadtxt("../../m12w90n40g45fac4nff2seed0_lr5e-4_bs5_40gap/AVG/plot_python/PDF/Ek/result/{}cases/error_with_time_F_IFNO.dat".format(case_number), dtype=float)
    IFNO_40 = np.loadtxt("../../m12w90n40g45fac4nff2seed0_lr5e-4_bs5_40gap/AVG/plot_python/PDF/Ek/result/{}cases/error_with_time_IFNO.dat".format(case_number), dtype=float)
    DSM_40 = np.loadtxt("../../m12w90n40g45fac4nff2seed0_lr5e-4_bs5_40gap/AVG/plot_python/PDF/Ek/result/{}cases/error_with_time_DSM.dat".format(case_number), dtype=float)
    
    fDNS_100 = np.loadtxt("../../m12w90n40g45fac4nff2seed0_lr5e-4_bs5_100gap/AVG/plot_python/PDF/Ek/result/{}cases/error_with_time_fDNS.dat".format(case_number), dtype=float)
    IUFNO_100 = np.loadtxt("../../m12w90n40g45fac4nff2seed0_lr5e-4_bs5_100gap/AVG/plot_python/PDF/Ek/result/{}cases/error_with_time_IUFNO.dat".format(case_number), dtype=float)
    F_IUFNO_100 = np.loadtxt("../../m12w90n40g45fac4nff2seed0_lr5e-4_bs5_100gap/AVG/plot_python/PDF/Ek/result/{}cases/error_with_time_F_IUFNO.dat".format(case_number), dtype=float)
    F_IFNO_100 = np.loadtxt("../../m12w90n40g45fac4nff2seed0_lr5e-4_bs5_100gap/AVG/plot_python/PDF/Ek/result/{}cases/error_with_time_F_IFNO.dat".format(case_number), dtype=float)
    IFNO_100 = np.loadtxt("../../m12w90n40g45fac4nff2seed0_lr5e-4_bs5_100gap/AVG/plot_python/PDF/Ek/result/{}cases/error_with_time_IFNO.dat".format(case_number), dtype=float)
    DSM_100 = np.loadtxt("../../m12w90n40g45fac4nff2seed0_lr5e-4_bs5_100gap/AVG/plot_python/PDF/Ek/result/{}cases/error_with_time_DSM.dat".format(case_number), dtype=float)    
    
    fDNS_200 = np.loadtxt("../../m12w90n40g45fac4nff2seed0_lr5e-4_bs5/AVG/plot_python_new/PDF/Ek/result/{}cases/error_with_time_fDNS.dat".format(case_number), dtype=float)
    IUFNO_200 = np.loadtxt("../../m12w90n40g45fac4nff2seed0_lr5e-4_bs5/AVG/plot_python_new/PDF/Ek/result/{}cases/error_with_time_IUFNO.dat".format(case_number), dtype=float)
    F_IUFNO_200 = np.loadtxt("../../m12w90n40g45fac4nff2seed0_lr5e-4_bs5/AVG/plot_python_new/PDF/Ek/result/{}cases/error_with_time_F_IUFNO.dat".format(case_number), dtype=float)
    F_IFNO_200 = np.loadtxt("../../m12w90n40g45fac4nff2seed0_lr5e-4_bs5/AVG/plot_python_new/PDF/Ek/result/{}cases/error_with_time_F_IFNO.dat".format(case_number), dtype=float)
    IFNO_200 = np.loadtxt("../../m12w90n40g45fac4nff2seed0_lr5e-4_bs5/AVG/plot_python_new/PDF/Ek/result/{}cases/error_with_time_IFNO.dat".format(case_number), dtype=float)
    DSM_200 = np.loadtxt("../../m12w90n40g45fac4nff2seed0_lr5e-4_bs5/AVG/plot_python_new/PDF/Ek/result/{}cases/error_with_time_DSM.dat".format(case_number), dtype=float)    

    fDNS_300 = np.loadtxt("../../m12w90n40g45fac4nff2seed0_lr5e-4_bs5_300gap/AVG/plot_python/PDF/Ek/result/{}cases/error_with_time_fDNS.dat".format(case_number), dtype=float)
    IUFNO_300 = np.loadtxt("../../m12w90n40g45fac4nff2seed0_lr5e-4_bs5_300gap/AVG/plot_python/PDF/Ek/result/{}cases/error_with_time_IUFNO.dat".format(case_number), dtype=float)
    F_IUFNO_300 = np.loadtxt("../../m12w90n40g45fac4nff2seed0_lr5e-4_bs5_300gap/AVG/plot_python/PDF/Ek/result/{}cases/error_with_time_F_IUFNO.dat".format(case_number), dtype=float)
    F_IFNO_300 = np.loadtxt("../../m12w90n40g45fac4nff2seed0_lr5e-4_bs5_300gap/AVG/plot_python/PDF/Ek/result/{}cases/error_with_time_F_IFNO.dat".format(case_number), dtype=float)
    IFNO_300 = np.loadtxt("../../m12w90n40g45fac4nff2seed0_lr5e-4_bs5_300gap/AVG/plot_python/PDF/Ek/result/{}cases/error_with_time_IFNO.dat".format(case_number), dtype=float)
    DSM_300 = np.loadtxt("../../m12w90n40g45fac4nff2seed0_lr5e-4_bs5_300gap/AVG/plot_python/PDF/Ek/result/{}cases/error_with_time_DSM.dat".format(case_number), dtype=float)    
        
    fDNS_400 = np.loadtxt("../../m12w90n40g45fac4nff2seed0_lr5e-4_bs5_400gap/AVG/plot_python/PDF/Ek/result/{}cases/error_with_time_fDNS.dat".format(case_number), dtype=float)
    IUFNO_400 = np.loadtxt("../../m12w90n40g45fac4nff2seed0_lr5e-4_bs5_400gap/AVG/plot_python/PDF/Ek/result/{}cases/error_with_time_IUFNO.dat".format(case_number), dtype=float)
    F_IUFNO_400 = np.loadtxt("../../m12w90n40g45fac4nff2seed0_lr5e-4_bs5_400gap/AVG/plot_python/PDF/Ek/result/{}cases/error_with_time_F_IUFNO.dat".format(case_number), dtype=float)
    F_IFNO_400 = np.loadtxt("../../m12w90n40g45fac4nff2seed0_lr5e-4_bs5_400gap/AVG/plot_python/PDF/Ek/result/{}cases/error_with_time_F_IFNO.dat".format(case_number), dtype=float)
    IFNO_400 = np.loadtxt("../../m12w90n40g45fac4nff2seed0_lr5e-4_bs5_400gap/AVG/plot_python/PDF/Ek/result/{}cases/error_with_time_IFNO.dat".format(case_number), dtype=float)
    DSM_400 = np.loadtxt("../../m12w90n40g45fac4nff2seed0_lr5e-4_bs5_400gap/AVG/plot_python/PDF/Ek/result/{}cases/error_with_time_DSM.dat".format(case_number), dtype=float)    
        
    IUFNO_20_k = np.loadtxt("../../m12w90n40g45fac4nff2seed0_lr5e-4_bs5_200gap_4_20gap/AVG/plot_python_k/PDF/Ek/result/{}cases/error_with_time_IUFNO.dat".format(case_number), dtype=float)
    F_IUFNO_20_k = np.loadtxt("../../m12w90n40g45fac4nff2seed0_lr5e-4_bs5_200gap_4_20gap/AVG/plot_python_k/PDF/Ek/result/{}cases/error_with_time_F_IUFNO.dat".format(case_number), dtype=float)
    F_IFNO_20_k = np.loadtxt("../../m12w90n40g45fac4nff2seed0_lr5e-4_bs5_200gap_4_20gap/AVG/plot_python_k/PDF/Ek/result/{}cases/error_with_time_F_IFNO.dat".format(case_number), dtype=float)
    IFNO_20_k = np.loadtxt("../../m12w90n40g45fac4nff2seed0_lr5e-4_bs5_200gap_4_20gap/AVG/plot_python_k/PDF/Ek/result/{}cases/error_with_time_IFNO.dat".format(case_number), dtype=float)
    
    IUFNO_40_k = np.loadtxt("../../m12w90n40g45fac4nff2seed0_lr5e-4_bs5_40gap/AVG/plot_python_k/PDF/Ek/result/{}cases/error_with_time_IUFNO.dat".format(case_number), dtype=float)
    F_IUFNO_40_k = np.loadtxt("../../m12w90n40g45fac4nff2seed0_lr5e-4_bs5_40gap/AVG/plot_python_k/PDF/Ek/result/{}cases/error_with_time_F_IUFNO.dat".format(case_number), dtype=float)
    F_IFNO_40_k = np.loadtxt("../../m12w90n40g45fac4nff2seed0_lr5e-4_bs5_40gap/AVG/plot_python_k/PDF/Ek/result/{}cases/error_with_time_F_IFNO.dat".format(case_number), dtype=float)
    IFNO_40_k = np.loadtxt("../../m12w90n40g45fac4nff2seed0_lr5e-4_bs5_40gap/AVG/plot_python_k/PDF/Ek/result/{}cases/error_with_time_IFNO.dat".format(case_number), dtype=float)
    
    IUFNO_100_k = np.loadtxt("../../m12w90n40g45fac4nff2seed0_lr5e-4_bs5_100gap/AVG/plot_python_k/PDF/Ek/result/{}cases/error_with_time_IUFNO.dat".format(case_number), dtype=float)
    F_IUFNO_100_k = np.loadtxt("../../m12w90n40g45fac4nff2seed0_lr5e-4_bs5_100gap/AVG/plot_python_k/PDF/Ek/result/{}cases/error_with_time_F_IUFNO.dat".format(case_number), dtype=float)
    F_IFNO_100_k = np.loadtxt("../../m12w90n40g45fac4nff2seed0_lr5e-4_bs5_100gap/AVG/plot_python_k/PDF/Ek/result/{}cases/error_with_time_F_IFNO.dat".format(case_number), dtype=float)
    IFNO_100_k = np.loadtxt("../../m12w90n40g45fac4nff2seed0_lr5e-4_bs5_100gap/AVG/plot_python_k/PDF/Ek/result/{}cases/error_with_time_IFNO.dat".format(case_number), dtype=float)    
    
    IUFNO_200_k = np.loadtxt("../../m12w90n40g45fac4nff2seed0_lr5e-4_bs5/AVG/plot_python_k/PDF/Ek/result/{}cases/error_with_time_IUFNO.dat".format(case_number), dtype=float)
    F_IUFNO_200_k = np.loadtxt("../../m12w90n40g45fac4nff2seed0_lr5e-4_bs5/AVG/plot_python_k/PDF/Ek/result/{}cases/error_with_time_F_IUFNO.dat".format(case_number), dtype=float)
    F_IFNO_200_k = np.loadtxt("../../m12w90n40g45fac4nff2seed0_lr5e-4_bs5/AVG/plot_python_k/PDF/Ek/result/{}cases/error_with_time_F_IFNO.dat".format(case_number), dtype=float)
    IFNO_200_k = np.loadtxt("../../m12w90n40g45fac4nff2seed0_lr5e-4_bs5/AVG/plot_python_k/PDF/Ek/result/{}cases/error_with_time_IFNO.dat".format(case_number), dtype=float)    

    IUFNO_300_k = np.loadtxt("../../m12w90n40g45fac4nff2seed0_lr5e-4_bs5_300gap/AVG/plot_python_k/PDF/Ek/result/{}cases/error_with_time_IUFNO.dat".format(case_number), dtype=float)
    F_IUFNO_300_k = np.loadtxt("../../m12w90n40g45fac4nff2seed0_lr5e-4_bs5_300gap/AVG/plot_python_k/PDF/Ek/result/{}cases/error_with_time_F_IUFNO.dat".format(case_number), dtype=float)
    F_IFNO_300_k = np.loadtxt("../../m12w90n40g45fac4nff2seed0_lr5e-4_bs5_300gap/AVG/plot_python_k/PDF/Ek/result/{}cases/error_with_time_F_IFNO.dat".format(case_number), dtype=float)
    IFNO_300_k = np.loadtxt("../../m12w90n40g45fac4nff2seed0_lr5e-4_bs5_300gap/AVG/plot_python_k/PDF/Ek/result/{}cases/error_with_time_IFNO.dat".format(case_number), dtype=float)  
 
    IUFNO_400_k = np.loadtxt("../../m12w90n40g45fac4nff2seed0_lr5e-4_bs5_400gap/AVG/plot_python_k/PDF/Ek/result/{}cases/error_with_time_IUFNO.dat".format(case_number), dtype=float)
    F_IUFNO_400_k = np.loadtxt("../../m12w90n40g45fac4nff2seed0_lr5e-4_bs5_400gap/AVG/plot_python_k/PDF/Ek/result/{}cases/error_with_time_F_IUFNO.dat".format(case_number), dtype=float)
    F_IFNO_400_k = np.loadtxt("../../m12w90n40g45fac4nff2seed0_lr5e-4_bs5_400gap/AVG/plot_python_k/PDF/Ek/result/{}cases/error_with_time_F_IFNO.dat".format(case_number), dtype=float)
    IFNO_400_k = np.loadtxt("../../m12w90n40g45fac4nff2seed0_lr5e-4_bs5_400gap/AVG/plot_python_k/PDF/Ek/result/{}cases/error_with_time_IFNO.dat".format(case_number), dtype=float)  

    
    #-------------------------输入参数
    # time_advance=[20]  #挑推进时间画图
    # time_advance=[40]  #挑推进时间画图
    #time_advance=[1,2,3,10,15,20,25,30,40,50,60,70,80,90,100,110,120,130,140,150,160,170,180,190,200,210,220,230,240,250]  #挑推进时间画图
    data1=F_IFNO_20_k[:,1]
    data2=F_IUFNO_20_k[:,1]
    data3=IUFNO_20_k[:,1]
    data4=IFNO_20_k[:,1]
    data5=F_IFNO_20[:,1]
    data6=F_IUFNO_20[:,1]
    data7=IUFNO_20[:,1]
    data8=IFNO_20[:,1]       
    data9=DSM_20[:,1]
    data10=fDNS_20[:,1]

    data11=F_IFNO_40_k[:,1]
    data12=F_IUFNO_40_k[:,1]
    data13=IUFNO_40_k[:,1]
    data14=IFNO_40_k[:,1]
    data15=F_IFNO_40[:,1]
    data16=F_IUFNO_40[:,1]
    data17=IUFNO_40[:,1]
    data18=IFNO_40[:,1]       
    data19=DSM_40[:,1]
    data20=fDNS_40[:,1]

    data21=F_IFNO_100_k[:,1]
    data22=F_IUFNO_100_k[:,1]
    data23=IUFNO_100_k[:,1]
    data24=IFNO_100_k[:,1]
    data25=F_IFNO_100[:,1]
    data26=F_IUFNO_100[:,1]
    data27=IUFNO_100[:,1]
    data28=IFNO_100[:,1]       
    data29=DSM_100[:,1]
    data30=fDNS_100[:,1]

    data31=F_IFNO_200_k[:,1]
    data32=F_IUFNO_200_k[:,1]
    data33=IUFNO_200_k[:,1]
    data34=IFNO_200_k[:,1]
    data35=F_IFNO_200[:,1]
    data36=F_IUFNO_200[:,1]
    data37=IUFNO_200[:,1]
    data38=IFNO_200[:,1]       
    data39=DSM_200[:,1]
    data40=fDNS_200[:,1]

    data41=F_IFNO_300_k[:,1]
    data42=F_IUFNO_300_k[:,1]
    data43=IUFNO_300_k[:,1]
    data44=IFNO_300_k[:,1]
    data45=F_IFNO_300[:,1]
    data46=F_IUFNO_300[:,1]
    data47=IUFNO_300[:,1]
    data48=IFNO_300[:,1]       
    data49=DSM_300[:,1]
    data50=fDNS_300[:,1]

    data51=F_IFNO_400_k[:,1]
    data52=F_IUFNO_400_k[:,1]
    data53=IUFNO_400_k[:,1]
    data54=IFNO_400_k[:,1]
    data55=F_IFNO_400[:,1]
    data56=F_IUFNO_400[:,1]
    data57=IUFNO_400[:,1]
    data58=IFNO_400[:,1]       
    data59=DSM_400[:,1]
    data60=fDNS_400[:,1]


    data_list = [globals()[f"data{i}"] for i in range(1, 61)]
    data_list = [np.array(d).reshape(case_number, time_steps) for d in data_list]
    mean_list = []
    std_list = []

    for data in data_list:
        mean_i = np.mean(data, axis=0)  # 沿着 case 轴求每个 time_step 的均值
        std_i = np.var(data, axis=0)
        mean_list.append(mean_i)
        std_list.append(std_i)


    mean_array = np.array(mean_list)
    std_array = np.array(std_list)

    lower_list = mean_array - std_array
    upper_list = mean_array + std_array

    lower_array = np.array(lower_list)

    print(lower_array.shape)
    print(mean_array.shape)
    iii=0
    mean1_F_IFNO_k = [mean_list[iii+0],mean_list[iii+10],mean_list[iii+20],mean_list[iii+30],mean_list[iii+40],mean_list[iii+50]]
    upper1_F_IFNO_k = [upper_list[iii+0],upper_list[iii+10],upper_list[iii+20],upper_list[iii+30],upper_list[iii+40],upper_list[iii+50]]    
    lower1_F_IFNO_k = [lower_list[iii+0],lower_list[iii+10],lower_list[iii+20],lower_list[iii+30],lower_list[iii+40],lower_list[iii+50]]

    iii=1
    mean1_F_IUFNO_k = [mean_list[iii+0],mean_list[iii+10],mean_list[iii+20],mean_list[iii+30],mean_list[iii+40],mean_list[iii+50]]
    upper1_F_IUFNO_k = [upper_list[iii+0],upper_list[iii+10],upper_list[iii+20],upper_list[iii+30],upper_list[iii+40],upper_list[iii+50]]    
    lower1_F_IUFNO_k = [lower_list[iii+0],lower_list[iii+10],lower_list[iii+20],lower_list[iii+30],lower_list[iii+40],lower_list[iii+50]]

    iii=2
    mean1_IUFNO_k = [mean_list[iii+0],mean_list[iii+10],mean_list[iii+20],mean_list[iii+30],mean_list[iii+40],mean_list[iii+50]]
    upper1_IUFNO_k = [upper_list[iii+0],upper_list[iii+10],upper_list[iii+20],upper_list[iii+30],upper_list[iii+40],upper_list[iii+50]]    
    lower1_IUFNO_k = [lower_list[iii+0],lower_list[iii+10],lower_list[iii+20],lower_list[iii+30],lower_list[iii+40],lower_list[iii+50]]

    iii=3
    mean1_IFNO_k = [mean_list[iii+0],mean_list[iii+10],mean_list[iii+20],mean_list[iii+30],mean_list[iii+40],mean_list[iii+50]]
    upper1_IFNO_k = [upper_list[iii+0],upper_list[iii+10],upper_list[iii+20],upper_list[iii+30],upper_list[iii+40],upper_list[iii+50]]    
    lower1_IFNO_k = [lower_list[iii+0],lower_list[iii+10],lower_list[iii+20],lower_list[iii+30],lower_list[iii+40],lower_list[iii+50]]

    iii=4
    mean1_F_IFNO = [mean_list[iii+0],mean_list[iii+10],mean_list[iii+20],mean_list[iii+30],mean_list[iii+40],mean_list[iii+50]]
    upper1_F_IFNO = [upper_list[iii+0],upper_list[iii+10],upper_list[iii+20],upper_list[iii+30],upper_list[iii+40],upper_list[iii+50]]    
    lower1_F_IFNO = [lower_list[iii+0],lower_list[iii+10],lower_list[iii+20],lower_list[iii+30],lower_list[iii+40],lower_list[iii+50]]

    iii=5
    mean1_F_IUFNO = [mean_list[iii+0],mean_list[iii+10],mean_list[iii+20],mean_list[iii+30],mean_list[iii+40],mean_list[iii+50]]
    upper1_F_IUFNO = [upper_list[iii+0],upper_list[iii+10],upper_list[iii+20],upper_list[iii+30],upper_list[iii+40],upper_list[iii+50]]    
    lower1_F_IUFNO = [lower_list[iii+0],lower_list[iii+10],lower_list[iii+20],lower_list[iii+30],lower_list[iii+40],lower_list[iii+50]]

    iii=6
    mean1_IUFNO = [mean_list[iii+0],mean_list[iii+10],mean_list[iii+20],mean_list[iii+30],mean_list[iii+40],mean_list[iii+50]]
    upper1_IUFNO = [upper_list[iii+0],upper_list[iii+10],upper_list[iii+20],upper_list[iii+30],upper_list[iii+40],upper_list[iii+50]]    
    lower1_IUFNO = [lower_list[iii+0],lower_list[iii+10],lower_list[iii+20],lower_list[iii+30],lower_list[iii+40],lower_list[iii+50]]

    iii=7
    mean1_IFNO = [mean_list[iii+0],mean_list[iii+10],mean_list[iii+20],mean_list[iii+30],mean_list[iii+40],mean_list[iii+50]]
    upper1_IFNO = [upper_list[iii+0],upper_list[iii+10],upper_list[iii+20],upper_list[iii+30],upper_list[iii+40],upper_list[iii+50]]    
    lower1_IFNO = [lower_list[iii+0],lower_list[iii+10],lower_list[iii+20],lower_list[iii+30],lower_list[iii+40],lower_list[iii+50]]

    iii=8
    mean1_DSM = [mean_list[iii+0],mean_list[iii+10],mean_list[iii+20],mean_list[iii+30],mean_list[iii+40],mean_list[iii+50]]
    upper1_DSM = [upper_list[iii+0],upper_list[iii+10],upper_list[iii+20],upper_list[iii+30],upper_list[iii+40],upper_list[iii+50]]    
    lower1_DSM = [lower_list[iii+0],lower_list[iii+10],lower_list[iii+20],lower_list[iii+30],lower_list[iii+40],lower_list[iii+50]]

    iii=9
    mean1_fDNS = [mean_list[iii+0],mean_list[iii+10],mean_list[iii+20],mean_list[iii+30],mean_list[iii+40],mean_list[iii+50]]
    upper1_fDNS = [upper_list[iii+0],upper_list[iii+10],upper_list[iii+20],upper_list[iii+30],upper_list[iii+40],upper_list[iii+50]]    
    lower1_fDNS = [lower_list[iii+0],lower_list[iii+10],lower_list[iii+20],lower_list[iii+30],lower_list[iii+40],lower_list[iii+50]]

 

    ######----------------------------x=model----------------------------########
    # 图形参数设置
    dpi = 600
    width, height = 8, 6
    fontsize =40
    lineWidth = 1.5
    boxWidth = 2.5
    Lmajor, Lminor = 7, 4
    xlabPad, ylabPad = 10, 10
    xlabel = r"$\mathdefault{t/\tau}$" 
    ylabel = r"$\mathdefault{Mean \pm Std \ error \ of \ E_k}$"
    xlimit=[1,121]
    #ylimit = [-0.18,0.04]
    legend1 = ["F-IFNO","F-IUFNO", "IUFNO", "IFNO","DSM","fDNS"]
    legend2 =[r'$\mathdefault{{\Delta T = 0.02   \tau}}$',r'$\mathdefault{{\Delta T = 0.04  \tau}}$',r'$\mathdefault{{\Delta T = 0.1  \tau}}$',r'$\mathdefault{{\Delta T = 0.2   \tau}}$',r'$\mathdefault{{\Delta T = 0.3   \tau}}$',r'$\mathdefault{{\Delta T = 0.4   \tau}}$']
  
    colors = ['#A52A2A','#ff7f0e','#ffd700','green','#1f77b4','purple']

    
    fig = plt.figure(figsize=(width, height), dpi=dpi)
    plt.rcParams["font.size"] = fontsize
    plt.rcParams["axes.linewidth"] = lineWidth
    ax = fig.add_axes([0, 0, 1, 1])
    # X 轴设置
    plt.xscale("linear")                                     #画linear
    ax.xaxis.set_major_locator(mpl.ticker.MultipleLocator(20)) #次刻度
    ax.xaxis.set_minor_locator(mpl.ticker.MultipleLocator(2))  #次刻度  #主刻度格式
    ax.xaxis.set_major_formatter(mpl.ticker.ScalarFormatter())               #应用主刻度格式
    ax.xaxis.set_minor_formatter(mpl.ticker.NullFormatter()) #次刻度
    # Y 轴设置
    plt.yscale("linear")
    ax.yaxis.set_major_locator(ticker.MaxNLocator(nbins=6, min_n_ticks=5))  # Automatically set major ticks
    ax.yaxis.set_minor_locator(ticker.AutoMinorLocator(5))  # Automatically set minor ticks to be 5 times finer than major ticks
    ax.autoscale(enable=True, axis='y', tight=False)
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

    plt.xlabel(xlabel, fontsize =40)
    plt.ylabel(ylabel, fontsize =40)
    ax.set_xlim(xlimit[0], xlimit[1]) 
    plt.xticks(fontsize =40)
    plt.yticks(fontsize =40)   

    # Matplotlib 配置
    mpl.rc('font', family='STIXGeneral')
    mpl.rc('text', usetex=False)
    mpl.rcParams['xtick.direction'] = 'in'
    mpl.rcParams['ytick.direction'] = 'in'
    plt.rcParams["mathtext.fontset"] = "cm"
    
    x1 = np.arange(0.2, time_steps*0.2+0.2,0.2)
    x2 = np.arange(0.3, time_steps*0.3+0.3,0.3)
    x3 = np.arange(0.4, time_steps*0.4+0.4,0.4)
    u_true=np.zeros(time_steps)
    ##plt.plot(x3, u_true, 'k-', label='Ground Truth',linewidth=2*lineWidth)
    op=0
    plt.plot(x1, mean1_F_IFNO_k[op], color=colors[0],linewidth=2*lineWidth, linestyle='-', label=legend2[0],zorder=5)
    plt.fill_between(x1, lower1_F_IFNO_k[op], upper1_F_IFNO_k[op], color=colors[0], alpha=0.2)
    op=1
    plt.plot(x1, mean1_F_IFNO_k[op], color=colors[1],linewidth=2*lineWidth, linestyle='-', label=legend2[1],zorder=4)
    plt.fill_between(x1, lower1_F_IFNO_k[op], upper1_F_IFNO_k[op], color=colors[1], alpha=0.2)      
    op=2
    plt.plot(x1, mean1_F_IFNO_k[op], color=colors[2],linewidth=2*lineWidth, linestyle='-', label=legend2[2],zorder=3)
    plt.fill_between(x1, lower1_F_IFNO_k[op], upper1_F_IFNO_k[op], color=colors[2], alpha=0.2)
    op=3
    plt.plot(x1, mean1_F_IFNO_k[op], color=colors[3],linewidth=2*lineWidth, linestyle='-', label=legend2[3],zorder=2)
    plt.fill_between(x1, lower1_F_IFNO_k[op], upper1_F_IFNO_k[op], color=colors[3], alpha=0.2)
    op=4
    plt.plot(x2, mean1_F_IFNO_k[op], color=colors[4],linewidth=2*lineWidth, linestyle='-', label=legend2[4],zorder=1)
    plt.fill_between(x2, lower1_F_IFNO_k[op], upper1_F_IFNO_k[op], color=colors[4], alpha=0.2)      
    op=5
    plt.plot(x3, mean1_F_IFNO_k[op], color=colors[5],linewidth=2*lineWidth, linestyle='-', label=legend2[5],zorder=6)
    plt.fill_between(x3, lower1_F_IFNO_k[op], upper1_F_IFNO_k[op], color=colors[5], alpha=0.2)    
    
    plt.ylim(-0.8, 0.05)
    # Matplotlib 配置 - 全局字体设置为 STIXGeneral
    mpl.rc('font', family='STIXGeneral')
    # 创建图例
    #plt.title(r"Mean prediction with 95% confidence interval", fontsize =40, color='black', loc='center', pad=15)
    lgd = plt.legend(
        loc='lower right',              # 基准位置
        bbox_to_anchor=(1.0, 0.0),      # x=1.0表示图右边缘，y=0.0表示图下边缘
        fontsize =30,
        ncol=2,                         # 2 列，自动变成 3 行（如果有 6 个标签）
        frameon=True,
        framealpha=0,
        edgecolor='black',
        shadow=False
    )

    figPath1 = os.path.abspath("./Errorbar_with_time")
    gfile1 = "F-IFNO with_1.png"
    gpath1 = os.path.join(figPath1, gfile1)
    # 保存图形
    plt.savefig(gpath1, bbox_inches='tight')
    plt.close() 
 
  
 
 
 
    ######----------------------------x=model----------------------------########
    # 图形参数设置
    dpi = 600
    width, height = 8, 6
    fontsize =40
    lineWidth = 1.5
    boxWidth = 2.5
    Lmajor, Lminor = 7, 4
    xlabPad, ylabPad = 10, 10
    xlabel = r"$\mathdefault{t/\tau}$" 
    ylabel = r"$\mathdefault{Mean \pm Std \ error \ of \ E_k}$"
    xlimit=[1,121]
    #ylimit = [-0.18,0.04]
    legend1 = ["F-IFNO","F-IUFNO", "IUFNO", "IFNO","DSM","fDNS"]
    legend2 =[r'$\mathdefault{{\Delta T = 0.02   \tau}}$',r'$\mathdefault{{\Delta T = 0.04  \tau}}$',r'$\mathdefault{{\Delta T = 0.1  \tau}}$',r'$\mathdefault{{\Delta T = 0.2   \tau}}$',r'$\mathdefault{{\Delta T = 0.3   \tau}}$',r'$\mathdefault{{\Delta T = 0.4   \tau}}$']
  
    colors = ['#A52A2A','#ff7f0e','#ffd700','green','#1f77b4','purple']

    
    fig = plt.figure(figsize=(width, height), dpi=dpi)
    plt.rcParams["font.size"] = fontsize
    plt.rcParams["axes.linewidth"] = lineWidth
    ax = fig.add_axes([0, 0, 1, 1])
    # X 轴设置
    plt.xscale("linear")                                     #画linear
    ax.xaxis.set_major_locator(mpl.ticker.MultipleLocator(20)) #次刻度
    ax.xaxis.set_minor_locator(mpl.ticker.MultipleLocator(2))  #次刻度  #主刻度格式
    ax.xaxis.set_major_formatter(mpl.ticker.ScalarFormatter())               #应用主刻度格式
    ax.xaxis.set_minor_formatter(mpl.ticker.NullFormatter()) #次刻度
    # Y 轴设置
    plt.yscale("linear")
    ax.yaxis.set_major_locator(ticker.MaxNLocator(nbins=6, min_n_ticks=5))  # Automatically set major ticks
    ax.yaxis.set_minor_locator(ticker.AutoMinorLocator(5))  # Automatically set minor ticks to be 5 times finer than major ticks
    ax.autoscale(enable=True, axis='y', tight=False)
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

    plt.xlabel(xlabel, fontsize =40)
    plt.ylabel(ylabel, fontsize =40)
    ax.set_xlim(xlimit[0], xlimit[1]) 
    plt.xticks(fontsize =40)
    plt.yticks(fontsize =40)   

    # Matplotlib 配置
    mpl.rc('font', family='STIXGeneral')
    mpl.rc('text', usetex=False)
    mpl.rcParams['xtick.direction'] = 'in'
    mpl.rcParams['ytick.direction'] = 'in'
    plt.rcParams["mathtext.fontset"] = "cm"
    
    x1 = np.arange(0.2, time_steps*0.2+0.2,0.2)
    x2 = np.arange(0.3, time_steps*0.3+0.3,0.3)
    x3 = np.arange(0.4, time_steps*0.4+0.4,0.4)
    u_true=np.zeros(time_steps)
    #plt.plot(x3, u_true, 'k-', label='Ground Truth',linewidth=2*lineWidth)
    op=0
    plt.plot(x1, mean1_F_IUFNO_k[op], color=colors[0],linewidth=2*lineWidth, linestyle='-', label=legend2[0],zorder=5)
    plt.fill_between(x1, lower1_F_IUFNO_k[op], upper1_F_IUFNO_k[op], color=colors[0], alpha=0.2)
    op=1
    plt.plot(x1, mean1_F_IUFNO_k[op], color=colors[1],linewidth=2*lineWidth, linestyle='-', label=legend2[1],zorder=4)
    plt.fill_between(x1, lower1_F_IUFNO_k[op], upper1_F_IUFNO_k[op], color=colors[1], alpha=0.2)      
    op=2
    plt.plot(x1, mean1_F_IUFNO_k[op], color=colors[2],linewidth=2*lineWidth, linestyle='-', label=legend2[2],zorder=3)
    plt.fill_between(x1, lower1_F_IUFNO_k[op], upper1_F_IUFNO_k[op], color=colors[2], alpha=0.2)
    op=3
    plt.plot(x1, mean1_F_IUFNO_k[op], color=colors[3],linewidth=2*lineWidth, linestyle='-', label=legend2[3],zorder=2)
    plt.fill_between(x1, lower1_F_IUFNO_k[op], upper1_F_IUFNO_k[op], color=colors[3], alpha=0.2)
    op=4
    plt.plot(x2, mean1_F_IUFNO_k[op], color=colors[4],linewidth=2*lineWidth, linestyle='-', label=legend2[4],zorder=1)
    plt.fill_between(x2, lower1_F_IUFNO_k[op], upper1_F_IUFNO_k[op], color=colors[4], alpha=0.2)      
    op=5
    plt.plot(x3, mean1_F_IUFNO_k[op], color=colors[5],linewidth=2*lineWidth, linestyle='-', label=legend2[5],zorder=6)
    plt.fill_between(x3, lower1_F_IUFNO_k[op], upper1_F_IUFNO_k[op], color=colors[5], alpha=0.2)    

    # Matplotlib 配置 - 全局字体设置为 STIXGeneral
    mpl.rc('font', family='STIXGeneral')
    # 创建图例
    #plt.title(r"Mean prediction with 95% confidence interval", fontsize =40, color='black', loc='center', pad=15)
    lgd = plt.legend(
        loc='lower right',
        #bbox_to_anchor=(1, 0),  # (x, y)，x=1.0是图右边界，y=1.0是图上边界
        fontsize =40,
        frameon=True,
        framealpha=0,
        edgecolor='black',
        shadow=False
    )

    figPath1 = os.path.abspath("./Errorbar_with_time")
    gfile1 = "F-IUFNO with_1.png"
    gpath1 = os.path.join(figPath1, gfile1)
    # 保存图形
    plt.savefig(gpath1, bbox_inches='tight')
    plt.close() 
 
 
 
 
 
 
    ######----------------------------x=model----------------------------########
    # 图形参数设置
    dpi = 600
    width, height = 8, 6
    fontsize =40
    lineWidth = 1.5
    boxWidth = 2.5
    Lmajor, Lminor = 7, 4
    xlabPad, ylabPad = 10, 10
    xlabel = r"$\mathdefault{t/\tau}$" 
    ylabel = r"$\mathdefault{Mean \pm Std \ error \ of \ E_k}$"
    xlimit=[1,121]
    #ylimit = [-0.18,0.04]
    legend1 = ["F-IFNO","F-IUFNO", "IUFNO", "IFNO","DSM","fDNS"]
    legend2 =[r'$\mathdefault{{\Delta T = 0.02   \tau}}$',r'$\mathdefault{{\Delta T = 0.04  \tau}}$',r'$\mathdefault{{\Delta T = 0.1  \tau}}$',r'$\mathdefault{{\Delta T = 0.2   \tau}}$',r'$\mathdefault{{\Delta T = 0.3   \tau}}$',r'$\mathdefault{{\Delta T = 0.4   \tau}}$']
  
    colors = ['#A52A2A','#ff7f0e','#ffd700','green','#1f77b4','purple']

    
    fig = plt.figure(figsize=(width, height), dpi=dpi)
    plt.rcParams["font.size"] = fontsize
    plt.rcParams["axes.linewidth"] = lineWidth
    ax = fig.add_axes([0, 0, 1, 1])
    # X 轴设置
    plt.xscale("linear")                                     #画linear
    ax.xaxis.set_major_locator(mpl.ticker.MultipleLocator(20)) #次刻度
    ax.xaxis.set_minor_locator(mpl.ticker.MultipleLocator(2))  #次刻度  #主刻度格式
    ax.xaxis.set_major_formatter(mpl.ticker.ScalarFormatter())               #应用主刻度格式
    ax.xaxis.set_minor_formatter(mpl.ticker.NullFormatter()) #次刻度
    # Y 轴设置
    plt.yscale("linear")
    ax.yaxis.set_major_locator(ticker.MaxNLocator(nbins=6, min_n_ticks=5))  # Automatically set major ticks
    ax.yaxis.set_minor_locator(ticker.AutoMinorLocator(5))  # Automatically set minor ticks to be 5 times finer than major ticks
    ax.autoscale(enable=True, axis='y', tight=False)
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

    plt.xlabel(xlabel, fontsize =40)
    plt.ylabel(ylabel, fontsize =40)
    ax.set_xlim(xlimit[0], xlimit[1]) 
    plt.xticks(fontsize =40)
    plt.yticks(fontsize =40)   

    # Matplotlib 配置
    mpl.rc('font', family='STIXGeneral')
    mpl.rc('text', usetex=False)
    mpl.rcParams['xtick.direction'] = 'in'
    mpl.rcParams['ytick.direction'] = 'in'
    plt.rcParams["mathtext.fontset"] = "cm"
    
    x1 = np.arange(0.2, time_steps*0.2+0.2,0.2)
    x2 = np.arange(0.3, time_steps*0.3+0.3,0.3)
    x3 = np.arange(0.4, time_steps*0.4+0.4,0.4)
    u_true=np.zeros(time_steps)
    ##plt.plot(x3, u_true, 'k-', label='Ground Truth',linewidth=2*lineWidth)
    op=0
    plt.plot(x1, mean1_IUFNO_k[op], color=colors[0],linewidth=2*lineWidth, linestyle='-', label=legend2[0],zorder=5)
    plt.fill_between(x1, lower1_IUFNO_k[op], upper1_IUFNO_k[op], color=colors[0], alpha=0.2)
    op=1
    plt.plot(x1, mean1_IUFNO_k[op], color=colors[1],linewidth=2*lineWidth, linestyle='-', label=legend2[1],zorder=4)
    plt.fill_between(x1, lower1_IUFNO_k[op], upper1_IUFNO_k[op], color=colors[1], alpha=0.2)      
    op=2
    plt.plot(x1, mean1_IUFNO_k[op], color=colors[2],linewidth=2*lineWidth, linestyle='-', label=legend2[2],zorder=3)
    plt.fill_between(x1, lower1_IUFNO_k[op], upper1_IUFNO_k[op], color=colors[2], alpha=0.2)
    op=3
    plt.plot(x1, mean1_IUFNO_k[op], color=colors[3],linewidth=2*lineWidth, linestyle='-', label=legend2[3],zorder=2)
    plt.fill_between(x1, lower1_IUFNO_k[op], upper1_IUFNO_k[op], color=colors[3], alpha=0.2)
    op=4
    plt.plot(x2, mean1_IUFNO_k[op], color=colors[4],linewidth=2*lineWidth, linestyle='-', label=legend2[4],zorder=1)
    plt.fill_between(x2, lower1_IUFNO_k[op], upper1_IUFNO_k[op], color=colors[4], alpha=0.2)      
    op=5
    plt.plot(x3, mean1_IUFNO_k[op], color=colors[5],linewidth=2*lineWidth, linestyle='-', label=legend2[5],zorder=6)
    plt.fill_between(x3, lower1_IUFNO_k[op], upper1_IUFNO_k[op], color=colors[5], alpha=0.2)    

    # Matplotlib 配置 - 全局字体设置为 STIXGeneral
    mpl.rc('font', family='STIXGeneral')
    # 创建图例
    #plt.title(r"Mean prediction with 95% confidence interval", fontsize =40, color='black', loc='center', pad=15)
    lgd = plt.legend(
        loc='upper right',
        #bbox_to_anchor=(1, 0),  # (x, y)，x=1.0是图右边界，y=1.0是图上边界
        fontsize =40,
        frameon=True,
        framealpha=0,
        edgecolor='black',
        shadow=False
    )

    figPath1 = os.path.abspath("./Errorbar_with_time")
    gfile1 = "IUFNO with_1.png"
    gpath1 = os.path.join(figPath1, gfile1)
    # 保存图形
    plt.savefig(gpath1, bbox_inches='tight')
    plt.close()  
 
 
 

 
    ######----------------------------x=model----------------------------########
    # 图形参数设置
    dpi = 600
    width, height = 8, 6
    fontsize =40
    lineWidth = 1.5
    boxWidth = 2.5
    Lmajor, Lminor = 7, 4
    xlabPad, ylabPad = 10, 10
    xlabel = r"$\mathdefault{t/\tau}$" 
    ylabel = r"$\mathdefault{Mean \pm Std \ error \ of \ E_k}$"
    xlimit=[1,121]
    #ylimit = [-0.18,0.04]
    legend1 = ["F-IFNO","F-IUFNO", "IUFNO", "IFNO","DSM","fDNS"]
    legend2 =[r'$\mathdefault{{\Delta T = 0.02   \tau}}$',r'$\mathdefault{{\Delta T = 0.04  \tau}}$',r'$\mathdefault{{\Delta T = 0.1  \tau}}$',r'$\mathdefault{{\Delta T = 0.2   \tau}}$',r'$\mathdefault{{\Delta T = 0.3   \tau}}$',r'$\mathdefault{{\Delta T = 0.4   \tau}}$']
  
    colors = ['#A52A2A','#ff7f0e','#ffd700','green','#1f77b4','purple']

    
    fig = plt.figure(figsize=(width, height), dpi=dpi)
    plt.rcParams["font.size"] = fontsize
    plt.rcParams["axes.linewidth"] = lineWidth
    ax = fig.add_axes([0, 0, 1, 1])
    # X 轴设置
    plt.xscale("linear")                                     #画linear
    ax.xaxis.set_major_locator(mpl.ticker.MultipleLocator(20)) #次刻度
    ax.xaxis.set_minor_locator(mpl.ticker.MultipleLocator(2))  #次刻度  #主刻度格式
    ax.xaxis.set_major_formatter(mpl.ticker.ScalarFormatter())               #应用主刻度格式
    ax.xaxis.set_minor_formatter(mpl.ticker.NullFormatter()) #次刻度
    # Y 轴设置
    plt.yscale("linear")
    ax.yaxis.set_major_locator(ticker.MaxNLocator(nbins=6, min_n_ticks=5))  # Automatically set major ticks
    ax.yaxis.set_minor_locator(ticker.AutoMinorLocator(5))  # Automatically set minor ticks to be 5 times finer than major ticks
    ax.autoscale(enable=True, axis='y', tight=False)
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

    plt.xlabel(xlabel, fontsize =40)
    plt.ylabel(ylabel, fontsize =40)
    ax.set_xlim(xlimit[0], xlimit[1]) 
    plt.xticks(fontsize =40)
    plt.yticks(fontsize =40)   

    # Matplotlib 配置
    mpl.rc('font', family='STIXGeneral')
    mpl.rc('text', usetex=False)
    mpl.rcParams['xtick.direction'] = 'in'
    mpl.rcParams['ytick.direction'] = 'in'
    plt.rcParams["mathtext.fontset"] = "cm"
    
    x1 = np.arange(0.2, time_steps*0.2+0.2,0.2)
    x2 = np.arange(0.3, time_steps*0.3+0.3,0.3)
    x3 = np.arange(0.4, time_steps*0.4+0.4,0.4)
    u_true=np.zeros(time_steps)
    #plt.plot(x3, u_true, 'k-', label='Ground Truth',linewidth=2*lineWidth)
    op=0
    plt.plot(x1, mean1_IFNO_k[op], color=colors[0],linewidth=2*lineWidth, linestyle='-', label=legend2[0],zorder=5)
    plt.fill_between(x1, lower1_IFNO_k[op], upper1_IFNO_k[op], color=colors[0], alpha=0.2)
    op=1
    plt.plot(x1, mean1_IFNO_k[op], color=colors[1],linewidth=2*lineWidth, linestyle='-', label=legend2[1],zorder=4)
    plt.fill_between(x1, lower1_IFNO_k[op], upper1_IFNO_k[op], color=colors[1], alpha=0.2)      
    op=2
    plt.plot(x1, mean1_IFNO_k[op], color=colors[2],linewidth=2*lineWidth, linestyle='-', label=legend2[2],zorder=3)
    plt.fill_between(x1, lower1_IFNO_k[op], upper1_IFNO_k[op], color=colors[2], alpha=0.2)
    op=3
    plt.plot(x1, mean1_IFNO_k[op], color=colors[3],linewidth=2*lineWidth, linestyle='-', label=legend2[3],zorder=2)
    plt.fill_between(x1, lower1_IFNO_k[op], upper1_IFNO_k[op], color=colors[3], alpha=0.2)
    op=4
    plt.plot(x2, mean1_IFNO_k[op], color=colors[4],linewidth=2*lineWidth, linestyle='-', label=legend2[4],zorder=1)
    plt.fill_between(x2, lower1_IFNO_k[op], upper1_IFNO_k[op], color=colors[4], alpha=0.2)      
    op=5
    plt.plot(x3, mean1_IFNO_k[op], color=colors[5],linewidth=2*lineWidth, linestyle='-', label=legend2[5],zorder=6)
    plt.fill_between(x3, lower1_IFNO_k[op], upper1_IFNO_k[op], color=colors[5], alpha=0.2)    

    # Matplotlib 配置 - 全局字体设置为 STIXGeneral
    mpl.rc('font', family='STIXGeneral')
    # 创建图例
    #plt.title(r"Mean prediction with 95% confidence interval", fontsize =40, color='black', loc='center', pad=15)
    lgd = plt.legend(
        loc='upper right',
        #bbox_to_anchor=(1, 0),  # (x, y)，x=1.0是图右边界，y=1.0是图上边界
        fontsize =40,
        frameon=True,
        framealpha=0,
        edgecolor='black',
        shadow=False
    )

    figPath1 = os.path.abspath("./Errorbar_with_time")
    gfile1 = "IFNO with_1.png"
    gpath1 = os.path.join(figPath1, gfile1)
    # 保存图形
    plt.savefig(gpath1, bbox_inches='tight')
    plt.close()   
 



    ######----------------------------x=model----------------------------########
    # 图形参数设置
    dpi = 600
    width, height = 8, 6
    fontsize =40
    lineWidth = 1.5
    boxWidth = 2.5
    Lmajor, Lminor = 7, 4
    xlabPad, ylabPad = 10, 10
    xlabel = r"$\mathdefault{t/\tau}$" 
    ylabel = r"$\mathdefault{Mean \pm Std \ error \ of \ E_k}$"
    xlimit=[1,121]
    #ylimit = [-0.18,0.04]
    legend1 = ["F-IFNO","F-IUFNO", "IUFNO", "IFNO","DSM","fDNS"]
    legend2 =[r'$\mathdefault{{\Delta T = 0.02   \tau}}$',r'$\mathdefault{{\Delta T = 0.04  \tau}}$',r'$\mathdefault{{\Delta T = 0.1  \tau}}$',r'$\mathdefault{{\Delta T = 0.2   \tau}}$',r'$\mathdefault{{\Delta T = 0.3   \tau}}$',r'$\mathdefault{{\Delta T = 0.4   \tau}}$']
  
    colors = ['#A52A2A','#ff7f0e','#ffd700','green','#1f77b4','purple']

    
    fig = plt.figure(figsize=(width, height), dpi=dpi)
    plt.rcParams["font.size"] = fontsize
    plt.rcParams["axes.linewidth"] = lineWidth
    ax = fig.add_axes([0, 0, 1, 1])
    # X 轴设置
    plt.xscale("linear")                                     #画linear
    ax.xaxis.set_major_locator(mpl.ticker.MultipleLocator(20)) #次刻度
    ax.xaxis.set_minor_locator(mpl.ticker.MultipleLocator(2))  #次刻度  #主刻度格式
    ax.xaxis.set_major_formatter(mpl.ticker.ScalarFormatter())               #应用主刻度格式
    ax.xaxis.set_minor_formatter(mpl.ticker.NullFormatter()) #次刻度
    # Y 轴设置
    plt.yscale("linear")
    ax.yaxis.set_major_locator(ticker.MaxNLocator(nbins=6, min_n_ticks=5))  # Automatically set major ticks
    ax.yaxis.set_minor_locator(ticker.AutoMinorLocator(5))  # Automatically set minor ticks to be 5 times finer than major ticks
    ax.autoscale(enable=True, axis='y', tight=False)
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

    plt.xlabel(xlabel, fontsize =40)
    plt.ylabel(ylabel, fontsize =40)
    ax.set_xlim(xlimit[0], xlimit[1]) 
    plt.xticks(fontsize =40)
    plt.yticks(fontsize =40)   

    # Matplotlib 配置
    mpl.rc('font', family='STIXGeneral')
    mpl.rc('text', usetex=False)
    mpl.rcParams['xtick.direction'] = 'in'
    mpl.rcParams['ytick.direction'] = 'in'
    plt.rcParams["mathtext.fontset"] = "cm"
    
    x1 = np.arange(0.2, time_steps*0.2+0.2,0.2)
    x2 = np.arange(0.3, time_steps*0.3+0.3,0.3)
    x3 = np.arange(0.4, time_steps*0.4+0.4,0.4)
    u_true=np.zeros(time_steps)
    #plt.plot(x3, u_true, 'k-', label='Ground Truth',linewidth=2*lineWidth)
    op=0
    plt.plot(x1, mean1_F_IFNO[op], color=colors[0],linewidth=2*lineWidth, linestyle='-', label=legend2[0],zorder=5)
    plt.fill_between(x1, lower1_F_IFNO[op], upper1_F_IFNO[op], color=colors[0], alpha=0.2)
    op=1
    plt.plot(x1, mean1_F_IFNO[op], color=colors[1],linewidth=2*lineWidth, linestyle='-', label=legend2[1],zorder=4)
    plt.fill_between(x1, lower1_F_IFNO[op], upper1_F_IFNO[op], color=colors[1], alpha=0.2)      
    op=2
    plt.plot(x1, mean1_F_IFNO[op], color=colors[2],linewidth=2*lineWidth, linestyle='-', label=legend2[2],zorder=3)
    plt.fill_between(x1, lower1_F_IFNO[op], upper1_F_IFNO[op], color=colors[2], alpha=0.2)
    op=3
    plt.plot(x1, mean1_F_IFNO[op], color=colors[3],linewidth=2*lineWidth, linestyle='-', label=legend2[3],zorder=2)
    plt.fill_between(x1, lower1_F_IFNO[op], upper1_F_IFNO[op], color=colors[3], alpha=0.2)
    op=4
    plt.plot(x2, mean1_F_IFNO[op], color=colors[4],linewidth=2*lineWidth, linestyle='-', label=legend2[4],zorder=1)
    plt.fill_between(x2, lower1_F_IFNO[op], upper1_F_IFNO[op], color=colors[4], alpha=0.2)      
    op=5
    plt.plot(x3, mean1_F_IFNO[op], color=colors[5],linewidth=2*lineWidth, linestyle='-', label=legend2[5],zorder=6)
    plt.fill_between(x3, lower1_F_IFNO[op], upper1_F_IFNO[op], color=colors[5], alpha=0.2)    

    # Matplotlib 配置 - 全局字体设置为 STIXGeneral
    mpl.rc('font', family='STIXGeneral')
    # 创建图例
    #plt.title(r"Mean prediction with 95% confidence interval", fontsize =40, color='black', loc='center', pad=15)
    lgd = plt.legend(
        loc='lower right',
        #bbox_to_anchor=(1, 0),  # (x, y)，x=1.0是图右边界，y=1.0是图上边界
        fontsize =40,
        frameon=True,
        framealpha=0,
        edgecolor='black',
        shadow=False
    )

    figPath1 = os.path.abspath("./Errorbar_with_time")
    gfile1 = "F-IFNO without_1.png"
    gpath1 = os.path.join(figPath1, gfile1)
    # 保存图形
    plt.savefig(gpath1, bbox_inches='tight')
    plt.close() 
 
  
 
 
 
    ######----------------------------x=model----------------------------########
    # 图形参数设置
    dpi = 600
    width, height = 8, 6
    fontsize =40
    lineWidth = 1.5
    boxWidth = 2.5
    Lmajor, Lminor = 7, 4
    xlabPad, ylabPad = 10, 10
    xlabel = r"$\mathdefault{t/\tau}$" 
    ylabel = r"$\mathdefault{Mean \pm Std \ error \ of \ E_k}$"
    xlimit=[1,121]
    #ylimit = [-0.18,0.04]
    legend1 = ["F-IFNO","F-IUFNO", "IUFNO", "IFNO","DSM","fDNS"]
    legend2 =[r'$\mathdefault{{\Delta T = 0.02   \tau}}$',r'$\mathdefault{{\Delta T = 0.04  \tau}}$',r'$\mathdefault{{\Delta T = 0.1  \tau}}$',r'$\mathdefault{{\Delta T = 0.2   \tau}}$',r'$\mathdefault{{\Delta T = 0.3   \tau}}$',r'$\mathdefault{{\Delta T = 0.4   \tau}}$']
  
    colors = ['#A52A2A','#ff7f0e','#ffd700','green','#1f77b4','purple']

    
    fig = plt.figure(figsize=(width, height), dpi=dpi)
    plt.rcParams["font.size"] = fontsize
    plt.rcParams["axes.linewidth"] = lineWidth
    ax = fig.add_axes([0, 0, 1, 1])
    # X 轴设置
    plt.xscale("linear")                                     #画linear
    ax.xaxis.set_major_locator(mpl.ticker.MultipleLocator(20)) #次刻度
    ax.xaxis.set_minor_locator(mpl.ticker.MultipleLocator(2))  #次刻度  #主刻度格式
    ax.xaxis.set_major_formatter(mpl.ticker.ScalarFormatter())               #应用主刻度格式
    ax.xaxis.set_minor_formatter(mpl.ticker.NullFormatter()) #次刻度
    # Y 轴设置
    plt.yscale("linear")
    ax.yaxis.set_major_locator(ticker.MaxNLocator(nbins=6, min_n_ticks=5))  # Automatically set major ticks
    ax.yaxis.set_minor_locator(ticker.AutoMinorLocator(5))  # Automatically set minor ticks to be 5 times finer than major ticks
    ax.autoscale(enable=True, axis='y', tight=False)
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

    plt.xlabel(xlabel, fontsize =40)
    plt.ylabel(ylabel, fontsize =40)
    ax.set_xlim(xlimit[0], xlimit[1]) 
    plt.xticks(fontsize =40)
    plt.yticks(fontsize =40)   

    # Matplotlib 配置
    mpl.rc('font', family='STIXGeneral')
    mpl.rc('text', usetex=False)
    mpl.rcParams['xtick.direction'] = 'in'
    mpl.rcParams['ytick.direction'] = 'in'
    plt.rcParams["mathtext.fontset"] = "cm"
    
    x1 = np.arange(0.2, time_steps*0.2+0.2,0.2)
    x2 = np.arange(0.3, time_steps*0.3+0.3,0.3)
    x3 = np.arange(0.4, time_steps*0.4+0.4,0.4)
    u_true=np.zeros(time_steps)
    #plt.plot(x3, u_true, 'k-', label='Ground Truth',linewidth=2*lineWidth)
    op=0
    plt.plot(x1, mean1_F_IUFNO[op], color=colors[0],linewidth=2*lineWidth, linestyle='-', label=legend2[0],zorder=5)
    plt.fill_between(x1, lower1_F_IUFNO[op], upper1_F_IUFNO[op], color=colors[0], alpha=0.2)
    op=1
    plt.plot(x1, mean1_F_IUFNO[op], color=colors[1],linewidth=2*lineWidth, linestyle='-', label=legend2[1],zorder=4)
    plt.fill_between(x1, lower1_F_IUFNO[op], upper1_F_IUFNO[op], color=colors[1], alpha=0.2)      
    op=2
    plt.plot(x1, mean1_F_IUFNO[op], color=colors[2],linewidth=2*lineWidth, linestyle='-', label=legend2[2],zorder=3)
    plt.fill_between(x1, lower1_F_IUFNO[op], upper1_F_IUFNO[op], color=colors[2], alpha=0.2)
    op=3
    plt.plot(x1, mean1_F_IUFNO[op], color=colors[3],linewidth=2*lineWidth, linestyle='-', label=legend2[3],zorder=2)
    plt.fill_between(x1, lower1_F_IUFNO[op], upper1_F_IUFNO[op], color=colors[3], alpha=0.2)
    op=4
    plt.plot(x2, mean1_F_IUFNO[op], color=colors[4],linewidth=2*lineWidth, linestyle='-', label=legend2[4],zorder=1)
    plt.fill_between(x2, lower1_F_IUFNO[op], upper1_F_IUFNO[op], color=colors[4], alpha=0.2)      
    op=5
    plt.plot(x3, mean1_F_IUFNO[op], color=colors[5],linewidth=2*lineWidth, linestyle='-', label=legend2[5],zorder=6)
    plt.fill_between(x3, lower1_F_IUFNO[op], upper1_F_IUFNO[op], color=colors[5], alpha=0.2)    

    # Matplotlib 配置 - 全局字体设置为 STIXGeneral
    mpl.rc('font', family='STIXGeneral')
    # 创建图例
    #plt.title(r"Mean prediction with 95% confidence interval", fontsize =40, color='black', loc='center', pad=15)
    lgd = plt.legend(
        loc='lower right',
        #bbox_to_anchor=(1, 0),  # (x, y)，x=1.0是图右边界，y=1.0是图上边界
        fontsize =40,
        frameon=True,
        framealpha=0,
        edgecolor='black',
        shadow=False
    )

    figPath1 = os.path.abspath("./Errorbar_with_time")
    gfile1 = "F-IUFNO without_1.png"
    gpath1 = os.path.join(figPath1, gfile1)
    # 保存图形
    plt.savefig(gpath1, bbox_inches='tight')
    plt.close() 
 
 
 
 
 
 
    ######----------------------------x=model----------------------------########
    # 图形参数设置
    dpi = 600
    width, height = 8, 6
    fontsize =40
    lineWidth = 1.5
    boxWidth = 2.5
    Lmajor, Lminor = 7, 4
    xlabPad, ylabPad = 10, 10
    xlabel = r"$\mathdefault{t/\tau}$" 
    ylabel = r"$\mathdefault{Mean \pm Std \ error \ of \ E_k}$"
    xlimit=[1,121]
    #ylimit = [-0.18,0.04]
    legend1 = ["F-IFNO","F-IUFNO", "IUFNO", "IFNO","DSM","fDNS"]
    legend2 =[r'$\mathdefault{{\Delta T = 0.02   \tau}}$',r'$\mathdefault{{\Delta T = 0.04  \tau}}$',r'$\mathdefault{{\Delta T = 0.1  \tau}}$',r'$\mathdefault{{\Delta T = 0.2   \tau}}$',r'$\mathdefault{{\Delta T = 0.3   \tau}}$',r'$\mathdefault{{\Delta T = 0.4   \tau}}$']
  
    colors = ['#A52A2A','#ff7f0e','#ffd700','green','#1f77b4','purple']

    
    fig = plt.figure(figsize=(width, height), dpi=dpi)
    plt.rcParams["font.size"] = fontsize
    plt.rcParams["axes.linewidth"] = lineWidth
    ax = fig.add_axes([0, 0, 1, 1])
    # X 轴设置
    plt.xscale("linear")                                     #画linear
    ax.xaxis.set_major_locator(mpl.ticker.MultipleLocator(20)) #次刻度
    ax.xaxis.set_minor_locator(mpl.ticker.MultipleLocator(2))  #次刻度  #主刻度格式
    ax.xaxis.set_major_formatter(mpl.ticker.ScalarFormatter())               #应用主刻度格式
    ax.xaxis.set_minor_formatter(mpl.ticker.NullFormatter()) #次刻度
    # Y 轴设置
    plt.yscale("linear")
    ax.yaxis.set_major_locator(ticker.MaxNLocator(nbins=6, min_n_ticks=5))  # Automatically set major ticks
    ax.yaxis.set_minor_locator(ticker.AutoMinorLocator(5))  # Automatically set minor ticks to be 5 times finer than major ticks
    ax.autoscale(enable=True, axis='y', tight=False)
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

    plt.xlabel(xlabel, fontsize =40)
    plt.ylabel(ylabel, fontsize =40)
    ax.set_xlim(xlimit[0], xlimit[1]) 
    plt.xticks(fontsize =40)
    plt.yticks(fontsize =40)   

    # Matplotlib 配置
    mpl.rc('font', family='STIXGeneral')
    mpl.rc('text', usetex=False)
    mpl.rcParams['xtick.direction'] = 'in'
    mpl.rcParams['ytick.direction'] = 'in'
    plt.rcParams["mathtext.fontset"] = "cm"
    
    x1 = np.arange(0.2, time_steps*0.2+0.2,0.2)
    x2 = np.arange(0.3, time_steps*0.3+0.3,0.3)
    x3 = np.arange(0.4, time_steps*0.4+0.4,0.4)
    u_true=np.zeros(time_steps)
    #plt.plot(x3, u_true, 'k-', label='Ground Truth',linewidth=2*lineWidth)
    op=0
    plt.plot(x1, mean1_IUFNO[op], color=colors[0],linewidth=2*lineWidth, linestyle='-', label=legend2[0],zorder=5)
    plt.fill_between(x1, lower1_IUFNO[op], upper1_IUFNO[op], color=colors[0], alpha=0.2)
    op=1
    plt.plot(x1, mean1_IUFNO[op], color=colors[1],linewidth=2*lineWidth, linestyle='-', label=legend2[1],zorder=4)
    plt.fill_between(x1, lower1_IUFNO[op], upper1_IUFNO[op], color=colors[1], alpha=0.2)      
    op=2
    plt.plot(x1, mean1_IUFNO[op], color=colors[2],linewidth=2*lineWidth, linestyle='-', label=legend2[2],zorder=3)
    plt.fill_between(x1, lower1_IUFNO[op], upper1_IUFNO[op], color=colors[2], alpha=0.2)
    op=3
    plt.plot(x1, mean1_IUFNO[op], color=colors[3],linewidth=2*lineWidth, linestyle='-', label=legend2[3],zorder=2)
    plt.fill_between(x1, lower1_IUFNO[op], upper1_IUFNO[op], color=colors[3], alpha=0.2)
    op=4
    plt.plot(x2, mean1_IUFNO[op], color=colors[4],linewidth=2*lineWidth, linestyle='-', label=legend2[4],zorder=1)
    plt.fill_between(x2, lower1_IUFNO[op], upper1_IUFNO[op], color=colors[4], alpha=0.2)      
    op=5
    plt.plot(x3, mean1_IUFNO[op], color=colors[5],linewidth=2*lineWidth, linestyle='-', label=legend2[5],zorder=6)
    plt.fill_between(x3, lower1_IUFNO[op], upper1_IUFNO[op], color=colors[5], alpha=0.2)    

    # Matplotlib 配置 - 全局字体设置为 STIXGeneral
    mpl.rc('font', family='STIXGeneral')
    # 创建图例
    #plt.title(r"Mean prediction with 95% confidence interval", fontsize =40, color='black', loc='center', pad=15)
    lgd = plt.legend(
        loc='upper right',
        #bbox_to_anchor=(1, 0),  # (x, y)，x=1.0是图右边界，y=1.0是图上边界
        fontsize =40,
        frameon=True,
        framealpha=0,
        edgecolor='black',
        shadow=False
    )

    figPath1 = os.path.abspath("./Errorbar_with_time")
    gfile1 = "IUFNO without_1.png"
    gpath1 = os.path.join(figPath1, gfile1)
    # 保存图形
    plt.savefig(gpath1, bbox_inches='tight')
    plt.close()  
 
 
 

 
    ######----------------------------x=model----------------------------########
    # 图形参数设置
    dpi = 600
    width, height = 8, 6
    fontsize =40
    lineWidth = 1.5
    boxWidth = 2.5
    Lmajor, Lminor = 7, 4
    xlabPad, ylabPad = 10, 10
    xlabel = r"$\mathdefault{t/\tau}$" 
    ylabel = r"$\mathdefault{Mean \pm Std \ error \ of \ E_k}$"
    xlimit=[1,121]
    #ylimit = [-0.18,0.04]
    legend1 = ["F-IFNO","F-IUFNO", "IUFNO", "IFNO","DSM","fDNS"]
    legend2 =[r'$\mathdefault{{\Delta T = 0.02   \tau}}$',r'$\mathdefault{{\Delta T = 0.04  \tau}}$',r'$\mathdefault{{\Delta T = 0.1  \tau}}$',r'$\mathdefault{{\Delta T = 0.2   \tau}}$',r'$\mathdefault{{\Delta T = 0.3   \tau}}$',r'$\mathdefault{{\Delta T = 0.4   \tau}}$']
  
    colors = ['#A52A2A','#ff7f0e','#ffd700','green','#1f77b4','purple']

    
    fig = plt.figure(figsize=(width, height), dpi=dpi)
    plt.rcParams["font.size"] = fontsize
    plt.rcParams["axes.linewidth"] = lineWidth
    ax = fig.add_axes([0, 0, 1, 1])
    # X 轴设置
    plt.xscale("linear")                                     #画linear
    ax.xaxis.set_major_locator(mpl.ticker.MultipleLocator(20)) #次刻度
    ax.xaxis.set_minor_locator(mpl.ticker.MultipleLocator(2))  #次刻度  #主刻度格式
    ax.xaxis.set_major_formatter(mpl.ticker.ScalarFormatter())               #应用主刻度格式
    ax.xaxis.set_minor_formatter(mpl.ticker.NullFormatter()) #次刻度
    # Y 轴设置
    plt.yscale("linear")
    ax.yaxis.set_major_locator(ticker.MaxNLocator(nbins=6, min_n_ticks=5))  # Automatically set major ticks
    ax.yaxis.set_minor_locator(ticker.AutoMinorLocator(5))  # Automatically set minor ticks to be 5 times finer than major ticks
    ax.autoscale(enable=True, axis='y', tight=False)
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

    plt.xlabel(xlabel, fontsize =40)
    plt.ylabel(ylabel, fontsize =40)
    ax.set_xlim(xlimit[0], xlimit[1]) 
    plt.xticks(fontsize =40)
    plt.yticks(fontsize =40)   

    # Matplotlib 配置
    mpl.rc('font', family='STIXGeneral')
    mpl.rc('text', usetex=False)
    mpl.rcParams['xtick.direction'] = 'in'
    mpl.rcParams['ytick.direction'] = 'in'
    plt.rcParams["mathtext.fontset"] = "cm"
    
    x1 = np.arange(0.2, time_steps*0.2+0.2,0.2)
    x2 = np.arange(0.3, time_steps*0.3+0.3,0.3)
    x3 = np.arange(0.4, time_steps*0.4+0.4,0.4)
    u_true=np.zeros(time_steps)
    #plt.plot(x3, u_true, 'k-', label='Ground Truth',linewidth=2*lineWidth)
    op=0
    plt.plot(x1, mean1_IFNO[op], color=colors[0],linewidth=2*lineWidth, linestyle='-', label=legend2[0],zorder=5)
    plt.fill_between(x1, lower1_IFNO[op], upper1_IFNO[op], color=colors[0], alpha=0.2)
    op=1
    plt.plot(x1, mean1_IFNO[op], color=colors[1],linewidth=2*lineWidth, linestyle='-', label=legend2[1],zorder=4)
    plt.fill_between(x1, lower1_IFNO[op], upper1_IFNO[op], color=colors[1], alpha=0.2)      
    op=2
    plt.plot(x1, mean1_IFNO[op], color=colors[2],linewidth=2*lineWidth, linestyle='-', label=legend2[2],zorder=3)
    plt.fill_between(x1, lower1_IFNO[op], upper1_IFNO[op], color=colors[2], alpha=0.2)
    op=3
    plt.plot(x1, mean1_IFNO[op], color=colors[3],linewidth=2*lineWidth, linestyle='-', label=legend2[3],zorder=2)
    plt.fill_between(x1, lower1_IFNO[op], upper1_IFNO[op], color=colors[3], alpha=0.2)
    op=4
    plt.plot(x2, mean1_IFNO[op], color=colors[4],linewidth=2*lineWidth, linestyle='-', label=legend2[4],zorder=1)
    plt.fill_between(x2, lower1_IFNO[op], upper1_IFNO[op], color=colors[4], alpha=0.2)      
    op=5
    plt.plot(x3, mean1_IFNO[op], color=colors[5],linewidth=2*lineWidth, linestyle='-', label=legend2[5],zorder=6)
    plt.fill_between(x3, lower1_IFNO[op], upper1_IFNO[op], color=colors[5], alpha=0.2)    

    # Matplotlib 配置 - 全局字体设置为 STIXGeneral
    mpl.rc('font', family='STIXGeneral')
    # 创建图例
    #plt.title(r"Mean prediction with 95% confidence interval", fontsize =40, color='black', loc='center', pad=15)
    lgd = plt.legend(
        loc='upper right',
        #bbox_to_anchor=(1, 0),  # (x, y)，x=1.0是图右边界，y=1.0是图上边界
        fontsize =40,
        frameon=True,
        framealpha=0,
        edgecolor='black',
        shadow=False
    )

    figPath1 = os.path.abspath("./Errorbar_with_time")
    gfile1 = "IFNO without_1.png"
    gpath1 = os.path.join(figPath1, gfile1)
    # 保存图形
    plt.savefig(gpath1, bbox_inches='tight')
    plt.close() 
 
 

    ######----------------------------x=model----------------------------########
    # 图形参数设置
    dpi = 600
    width, height = 8, 6
    fontsize =40
    lineWidth = 1.5
    boxWidth = 2.5
    Lmajor, Lminor = 7, 4
    xlabPad, ylabPad = 10, 10
    xlabel = r"$\mathdefault{t/\tau}$" 
    ylabel = r"$\mathdefault{Mean \pm Std \ error \ of \ E_k}$"
    xlimit=[1,121]
    #ylimit = [-0.18,0.04]
    legend1 = ["F-IFNO","F-IUFNO", "IUFNO", "IFNO","DSM","fDNS"]
    legend2 =[r'$\mathdefault{{\Delta T = 0.02   \tau}}$',r'$\mathdefault{{\Delta T = 0.04  \tau}}$',r'$\mathdefault{{\Delta T = 0.1  \tau}}$',r'$\mathdefault{{\Delta T = 0.2   \tau}}$',r'$\mathdefault{{\Delta T = 0.3   \tau}}$',r'$\mathdefault{{\Delta T = 0.4   \tau}}$']
  
    colors = ['#A52A2A','#ff7f0e','#ffd700','green','#1f77b4','purple']

    
    fig = plt.figure(figsize=(width, height), dpi=dpi)
    plt.rcParams["font.size"] = fontsize
    plt.rcParams["axes.linewidth"] = lineWidth
    ax = fig.add_axes([0, 0, 1, 1])
    # X 轴设置
    plt.xscale("linear")                                     #画linear
    ax.xaxis.set_major_locator(mpl.ticker.MultipleLocator(20)) #次刻度
    ax.xaxis.set_minor_locator(mpl.ticker.MultipleLocator(2))  #次刻度  #主刻度格式
    ax.xaxis.set_major_formatter(mpl.ticker.ScalarFormatter())               #应用主刻度格式
    ax.xaxis.set_minor_formatter(mpl.ticker.NullFormatter()) #次刻度
    # Y 轴设置
    plt.yscale("linear")
    ax.yaxis.set_major_locator(ticker.MaxNLocator(nbins=6, min_n_ticks=5))  # Automatically set major ticks
    ax.yaxis.set_minor_locator(ticker.AutoMinorLocator(5))  # Automatically set minor ticks to be 5 times finer than major ticks
    ax.autoscale(enable=True, axis='y', tight=False)
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

    plt.xlabel(xlabel, fontsize =40)
    plt.ylabel(ylabel, fontsize =40)
    ax.set_xlim(xlimit[0], xlimit[1]) 
    plt.xticks(fontsize =40)
    plt.yticks(fontsize =40)   

    # Matplotlib 配置
    mpl.rc('font', family='STIXGeneral')
    mpl.rc('text', usetex=False)
    mpl.rcParams['xtick.direction'] = 'in'
    mpl.rcParams['ytick.direction'] = 'in'
    plt.rcParams["mathtext.fontset"] = "cm"
    
    x1 = np.arange(0.2, time_steps*0.2+0.2,0.2)
    x2 = np.arange(0.3, time_steps*0.3+0.3,0.3)
    x3 = np.arange(0.4, time_steps*0.4+0.4,0.4)
    u_true=np.zeros(time_steps)
    #plt.plot(x3, u_true, 'k-', label='Ground Truth',linewidth=2*lineWidth)
    op=0
    plt.plot(x1, mean1_DSM[op], color=colors[0],linewidth=2*lineWidth, linestyle='-', label=legend2[0],zorder=5)
    plt.fill_between(x1, lower1_DSM[op], upper1_DSM[op], color=colors[0], alpha=0.2)
    op=1
    plt.plot(x1, mean1_DSM[op], color=colors[1],linewidth=2*lineWidth, linestyle='-', label=legend2[1],zorder=4)
    plt.fill_between(x1, lower1_DSM[op], upper1_DSM[op], color=colors[1], alpha=0.2)      
    op=2
    plt.plot(x1, mean1_DSM[op], color=colors[2],linewidth=2*lineWidth, linestyle='-', label=legend2[2],zorder=3)
    plt.fill_between(x1, lower1_DSM[op], upper1_DSM[op], color=colors[2], alpha=0.2)
    op=3
    plt.plot(x1, mean1_DSM[op], color=colors[3],linewidth=2*lineWidth, linestyle='-', label=legend2[3],zorder=2)
    plt.fill_between(x1, lower1_DSM[op], upper1_DSM[op], color=colors[3], alpha=0.2)
    op=4
    plt.plot(x2, mean1_DSM[op], color=colors[4],linewidth=2*lineWidth, linestyle='-', label=legend2[4],zorder=1)
    plt.fill_between(x2, lower1_DSM[op], upper1_DSM[op], color=colors[4], alpha=0.2)      
    op=5
    plt.plot(x3, mean1_DSM[op], color=colors[5],linewidth=2*lineWidth, linestyle='-', label=legend2[5],zorder=6)
    plt.fill_between(x3, lower1_DSM[op], upper1_DSM[op], color=colors[5], alpha=0.2)    

    # Matplotlib 配置 - 全局字体设置为 STIXGeneral
    mpl.rc('font', family='STIXGeneral')
    # 创建图例
    #plt.title(r"Mean prediction with 95% confidence interval", fontsize =40, color='black', loc='center', pad=15)
    lgd = plt.legend(
        loc='upper right',
        #bbox_to_anchor=(1, 0),  # (x, y)，x=1.0是图右边界，y=1.0是图上边界
        fontsize =40,
        frameon=True,
        framealpha=0,
        edgecolor='black',
        shadow=False
    )

    figPath1 = os.path.abspath("./Errorbar_with_time")
    gfile1 = "DSM without_1.png"
    gpath1 = os.path.join(figPath1, gfile1)
    # 保存图形
    plt.savefig(gpath1, bbox_inches='tight')
    plt.close()  
 
 

    ######----------------------------x=model----------------------------########
    # 图形参数设置
    dpi = 600
    width, height = 8, 6
    fontsize =40
    lineWidth = 1.5
    boxWidth = 2.5
    Lmajor, Lminor = 7, 4
    xlabPad, ylabPad = 10, 10
    xlabel = r"$\mathdefault{t/\tau}$" 
    ylabel = r"$\mathdefault{Mean \pm Std \ fluctuation \ of \ E_k}$"
    xlimit=[1,121]
    #ylimit = [-0.18,0.04]
    legend1 = ["F-IFNO","F-IUFNO", "IUFNO", "IFNO","DSM","fDNS"]
    legend2 =[r'$\mathdefault{{\Delta T = 0.02   \tau}}$',r'$\mathdefault{{\Delta T = 0.04  \tau}}$',r'$\mathdefault{{\Delta T = 0.1  \tau}}$',r'$\mathdefault{{\Delta T = 0.2   \tau}}$',r'$\mathdefault{{\Delta T = 0.3   \tau}}$',r'$\mathdefault{{\Delta T = 0.4   \tau}}$']
  
    colors = ['#A52A2A','#ff7f0e','#ffd700','green','#1f77b4','purple']

    
    fig = plt.figure(figsize=(width, height), dpi=dpi)
    plt.rcParams["font.size"] = fontsize
    plt.rcParams["axes.linewidth"] = lineWidth
    ax = fig.add_axes([0, 0, 1, 1])
    # X 轴设置
    plt.xscale("linear")                                     #画linear
    ax.xaxis.set_major_locator(mpl.ticker.MultipleLocator(20)) #次刻度
    ax.xaxis.set_minor_locator(mpl.ticker.MultipleLocator(2))  #次刻度  #主刻度格式
    ax.xaxis.set_major_formatter(mpl.ticker.ScalarFormatter())               #应用主刻度格式
    ax.xaxis.set_minor_formatter(mpl.ticker.NullFormatter()) #次刻度
    # Y 轴设置
    plt.yscale("linear")
    ax.yaxis.set_major_locator(ticker.MaxNLocator(nbins=6, min_n_ticks=5))  # Automatically set major ticks
    ax.yaxis.set_minor_locator(ticker.AutoMinorLocator(5))  # Automatically set minor ticks to be 5 times finer than major ticks
    ax.autoscale(enable=True, axis='y', tight=False)
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

    plt.xlabel(xlabel, fontsize =40)
    plt.ylabel(ylabel, fontsize =40)
    ax.set_xlim(xlimit[0], xlimit[1]) 
    plt.xticks(fontsize =40)
    plt.yticks(fontsize =40)   

    # Matplotlib 配置
    mpl.rc('font', family='STIXGeneral')
    mpl.rc('text', usetex=False)
    mpl.rcParams['xtick.direction'] = 'in'
    mpl.rcParams['ytick.direction'] = 'in'
    plt.rcParams["mathtext.fontset"] = "cm"
    
    x1 = np.arange(0.2, time_steps*0.2+0.2,0.2)
    x2 = np.arange(0.3, time_steps*0.3+0.3,0.3)
    x3 = np.arange(0.4, time_steps*0.4+0.4,0.4)
    u_true=np.zeros(time_steps)
    #plt.plot(x3, u_true, 'k-', label='Ground Truth',linewidth=2*lineWidth)
    op=0
    plt.plot(x1, mean1_fDNS[op], color=colors[0],linewidth=2*lineWidth, linestyle='-', label=legend2[0],zorder=5)
    plt.fill_between(x1, lower1_fDNS[op], upper1_fDNS[op], color=colors[0], alpha=0.2)
    op=1
    plt.plot(x1, mean1_fDNS[op], color=colors[1],linewidth=2*lineWidth, linestyle='-', label=legend2[1],zorder=4)
    plt.fill_between(x1, lower1_fDNS[op], upper1_fDNS[op], color=colors[1], alpha=0.2)      
    op=2
    plt.plot(x1, mean1_fDNS[op], color=colors[2],linewidth=2*lineWidth, linestyle='-', label=legend2[2],zorder=3)
    plt.fill_between(x1, lower1_fDNS[op], upper1_fDNS[op], color=colors[2], alpha=0.2)
    op=3
    plt.plot(x1, mean1_fDNS[op], color=colors[3],linewidth=2*lineWidth, linestyle='-', label=legend2[3],zorder=2)
    plt.fill_between(x1, lower1_fDNS[op], upper1_fDNS[op], color=colors[3], alpha=0.2)
    op=4
    plt.plot(x2, mean1_fDNS[op], color=colors[4],linewidth=2*lineWidth, linestyle='-', label=legend2[4],zorder=1)
    plt.fill_between(x2, lower1_fDNS[op], upper1_fDNS[op], color=colors[4], alpha=0.2)      
    op=5
    plt.plot(x3, mean1_fDNS[op], color=colors[5],linewidth=2*lineWidth, linestyle='-', label=legend2[5],zorder=6)
    plt.fill_between(x3, lower1_fDNS[op], upper1_fDNS[op], color=colors[5], alpha=0.2)    

    # Matplotlib 配置 - 全局字体设置为 STIXGeneral
    mpl.rc('font', family='STIXGeneral')
    # 创建图例
    #plt.title(r"Mean prediction with 95% confidence interval", fontsize =40, color='black', loc='center', pad=15)
    lgd = plt.legend(
        loc='upper right',
        #bbox_to_anchor=(1, 0),  # (x, y)，x=1.0是图右边界，y=1.0是图上边界
        fontsize =40,
        frameon=True,
        framealpha=0,
        edgecolor='black',
        shadow=False
    )

    figPath1 = os.path.abspath("./Errorbar_with_time")
    gfile1 = "fDNS without_1.png"
    gpath1 = os.path.join(figPath1, gfile1)
    # 保存图形
    plt.savefig(gpath1, bbox_inches='tight')
    plt.close()   
 