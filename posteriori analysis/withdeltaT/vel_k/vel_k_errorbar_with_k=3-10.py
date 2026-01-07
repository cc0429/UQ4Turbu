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
vel_k_list = [1,2,3,4,5,6,7,8,9,10]

for k, case_number in enumerate(case_number_list):


    avg_results = []
    avg_error = []
    variance_error = []

    for kk, vel_k in enumerate(vel_k_list):
    #-------------------------------------------------------------读入数据，


        fDNS_20 = np.loadtxt("../../m12w90n40g45fac4nff2seed0_lr5e-4_bs5_200gap_4_20gap/AVG/plot_python/PDF/vel_k/result/{}cases/error_with_time_fDNS_k={}.dat".format(case_number,vel_k), dtype=float)
        IUFNO_20 = np.loadtxt("../../m12w90n40g45fac4nff2seed0_lr5e-4_bs5_200gap_4_20gap/AVG/plot_python/PDF/vel_k/result/{}cases/error_with_time_IUFNO_k={}.dat".format(case_number,vel_k), dtype=float)
        F_IUFNO_20 = np.loadtxt("../../m12w90n40g45fac4nff2seed0_lr5e-4_bs5_200gap_4_20gap/AVG/plot_python/PDF/vel_k/result/{}cases/error_with_time_F_IUFNO_k={}.dat".format(case_number,vel_k), dtype=float)
        F_IFNO_20 = np.loadtxt("../../m12w90n40g45fac4nff2seed0_lr5e-4_bs5_200gap_4_20gap/AVG/plot_python/PDF/vel_k/result/{}cases/error_with_time_F_IFNO_k={}.dat".format(case_number,vel_k), dtype=float)
        IFNO_20 = np.loadtxt("../../m12w90n40g45fac4nff2seed0_lr5e-4_bs5_200gap_4_20gap/AVG/plot_python/PDF/vel_k/result/{}cases/error_with_time_IFNO_k={}.dat".format(case_number,vel_k), dtype=float)
        DSM_20 = np.loadtxt("../../m12w90n40g45fac4nff2seed0_lr5e-4_bs5_200gap_4_20gap/AVG/plot_python/PDF/vel_k/result/{}cases/error_with_time_DSM_k={}.dat".format(case_number,vel_k), dtype=float)
        
        fDNS_40 = np.loadtxt("../../m12w90n40g45fac4nff2seed0_lr5e-4_bs5_40gap/AVG/plot_python/PDF/vel_k/result/{}cases/error_with_time_fDNS_k={}.dat".format(case_number,vel_k), dtype=float)
        IUFNO_40 = np.loadtxt("../../m12w90n40g45fac4nff2seed0_lr5e-4_bs5_40gap/AVG/plot_python/PDF/vel_k/result/{}cases/error_with_time_IUFNO_k={}.dat".format(case_number,vel_k), dtype=float)
        F_IUFNO_40 = np.loadtxt("../../m12w90n40g45fac4nff2seed0_lr5e-4_bs5_40gap/AVG/plot_python/PDF/vel_k/result/{}cases/error_with_time_F_IUFNO_k={}.dat".format(case_number,vel_k), dtype=float)
        F_IFNO_40 = np.loadtxt("../../m12w90n40g45fac4nff2seed0_lr5e-4_bs5_40gap/AVG/plot_python/PDF/vel_k/result/{}cases/error_with_time_F_IFNO_k={}.dat".format(case_number,vel_k), dtype=float)
        IFNO_40 = np.loadtxt("../../m12w90n40g45fac4nff2seed0_lr5e-4_bs5_40gap/AVG/plot_python/PDF/vel_k/result/{}cases/error_with_time_IFNO_k={}.dat".format(case_number,vel_k), dtype=float)
        DSM_40 = np.loadtxt("../../m12w90n40g45fac4nff2seed0_lr5e-4_bs5_40gap/AVG/plot_python/PDF/vel_k/result/{}cases/error_with_time_DSM_k={}.dat".format(case_number,vel_k), dtype=float)
        
        fDNS_100 = np.loadtxt("../../m12w90n40g45fac4nff2seed0_lr5e-4_bs5_100gap/AVG/plot_python/PDF/vel_k/result/{}cases/error_with_time_fDNS_k={}.dat".format(case_number,vel_k), dtype=float)
        IUFNO_100 = np.loadtxt("../../m12w90n40g45fac4nff2seed0_lr5e-4_bs5_100gap/AVG/plot_python/PDF/vel_k/result/{}cases/error_with_time_IUFNO_k={}.dat".format(case_number,vel_k), dtype=float)
        F_IUFNO_100 = np.loadtxt("../../m12w90n40g45fac4nff2seed0_lr5e-4_bs5_100gap/AVG/plot_python/PDF/vel_k/result/{}cases/error_with_time_F_IUFNO_k={}.dat".format(case_number,vel_k), dtype=float)
        F_IFNO_100 = np.loadtxt("../../m12w90n40g45fac4nff2seed0_lr5e-4_bs5_100gap/AVG/plot_python/PDF/vel_k/result/{}cases/error_with_time_F_IFNO_k={}.dat".format(case_number,vel_k), dtype=float)
        IFNO_100 = np.loadtxt("../../m12w90n40g45fac4nff2seed0_lr5e-4_bs5_100gap/AVG/plot_python/PDF/vel_k/result/{}cases/error_with_time_IFNO_k={}.dat".format(case_number,vel_k), dtype=float)
        DSM_100 = np.loadtxt("../../m12w90n40g45fac4nff2seed0_lr5e-4_bs5_100gap/AVG/plot_python/PDF/vel_k/result/{}cases/error_with_time_DSM_k={}.dat".format(case_number,vel_k), dtype=float)    
        
        fDNS_200 = np.loadtxt("../../m12w90n40g45fac4nff2seed0_lr5e-4_bs5/AVG/plot_python_new/PDF/vel_k/result/{}cases/error_with_time_fDNS_k={}.dat".format(case_number,vel_k), dtype=float)
        IUFNO_200 = np.loadtxt("../../m12w90n40g45fac4nff2seed0_lr5e-4_bs5/AVG/plot_python_new/PDF/vel_k/result/{}cases/error_with_time_IUFNO_k={}.dat".format(case_number,vel_k), dtype=float)
        F_IUFNO_200 = np.loadtxt("../../m12w90n40g45fac4nff2seed0_lr5e-4_bs5/AVG/plot_python_new/PDF/vel_k/result/{}cases/error_with_time_F_IUFNO_k={}.dat".format(case_number,vel_k), dtype=float)
        F_IFNO_200 = np.loadtxt("../../m12w90n40g45fac4nff2seed0_lr5e-4_bs5/AVG/plot_python_new/PDF/vel_k/result/{}cases/error_with_time_F_IFNO_k={}.dat".format(case_number,vel_k), dtype=float)
        IFNO_200 = np.loadtxt("../../m12w90n40g45fac4nff2seed0_lr5e-4_bs5/AVG/plot_python_new/PDF/vel_k/result/{}cases/error_with_time_IFNO_k={}.dat".format(case_number,vel_k), dtype=float)
        DSM_200 = np.loadtxt("../../m12w90n40g45fac4nff2seed0_lr5e-4_bs5/AVG/plot_python_new/PDF/vel_k/result/{}cases/error_with_time_DSM_k={}.dat".format(case_number,vel_k), dtype=float)    

        fDNS_300 = np.loadtxt("../../m12w90n40g45fac4nff2seed0_lr5e-4_bs5_300gap/AVG/plot_python/PDF/vel_k/result/{}cases/error_with_time_fDNS_k={}.dat".format(case_number,vel_k), dtype=float)
        IUFNO_300 = np.loadtxt("../../m12w90n40g45fac4nff2seed0_lr5e-4_bs5_300gap/AVG/plot_python/PDF/vel_k/result/{}cases/error_with_time_IUFNO_k={}.dat".format(case_number,vel_k), dtype=float)
        F_IUFNO_300 = np.loadtxt("../../m12w90n40g45fac4nff2seed0_lr5e-4_bs5_300gap/AVG/plot_python/PDF/vel_k/result/{}cases/error_with_time_F_IUFNO_k={}.dat".format(case_number,vel_k), dtype=float)
        F_IFNO_300 = np.loadtxt("../../m12w90n40g45fac4nff2seed0_lr5e-4_bs5_300gap/AVG/plot_python/PDF/vel_k/result/{}cases/error_with_time_F_IFNO_k={}.dat".format(case_number,vel_k), dtype=float)
        IFNO_300 = np.loadtxt("../../m12w90n40g45fac4nff2seed0_lr5e-4_bs5_300gap/AVG/plot_python/PDF/vel_k/result/{}cases/error_with_time_IFNO_k={}.dat".format(case_number,vel_k), dtype=float)
        DSM_300 = np.loadtxt("../../m12w90n40g45fac4nff2seed0_lr5e-4_bs5_300gap/AVG/plot_python/PDF/vel_k/result/{}cases/error_with_time_DSM_k={}.dat".format(case_number,vel_k), dtype=float)    
            
        fDNS_400 = np.loadtxt("../../m12w90n40g45fac4nff2seed0_lr5e-4_bs5_400gap/AVG/plot_python/PDF/vel_k/result/{}cases/error_with_time_fDNS_k={}.dat".format(case_number,vel_k), dtype=float)
        IUFNO_400 = np.loadtxt("../../m12w90n40g45fac4nff2seed0_lr5e-4_bs5_400gap/AVG/plot_python/PDF/vel_k/result/{}cases/error_with_time_IUFNO_k={}.dat".format(case_number,vel_k), dtype=float)
        F_IUFNO_400 = np.loadtxt("../../m12w90n40g45fac4nff2seed0_lr5e-4_bs5_400gap/AVG/plot_python/PDF/vel_k/result/{}cases/error_with_time_F_IUFNO_k={}.dat".format(case_number,vel_k), dtype=float)
        F_IFNO_400 = np.loadtxt("../../m12w90n40g45fac4nff2seed0_lr5e-4_bs5_400gap/AVG/plot_python/PDF/vel_k/result/{}cases/error_with_time_F_IFNO_k={}.dat".format(case_number,vel_k), dtype=float)
        IFNO_400 = np.loadtxt("../../m12w90n40g45fac4nff2seed0_lr5e-4_bs5_400gap/AVG/plot_python/PDF/vel_k/result/{}cases/error_with_time_IFNO_k={}.dat".format(case_number,vel_k), dtype=float)
        DSM_400 = np.loadtxt("../../m12w90n40g45fac4nff2seed0_lr5e-4_bs5_400gap/AVG/plot_python/PDF/vel_k/result/{}cases/error_with_time_DSM_k={}.dat".format(case_number,vel_k), dtype=float)    
            
        IUFNO_20_k = np.loadtxt("../../m12w90n40g45fac4nff2seed0_lr5e-4_bs5_200gap_4_20gap/AVG/plot_python_k/PDF/vel_k/result/{}cases/error_with_time_IUFNO_k={}.dat".format(case_number,vel_k), dtype=float)
        F_IUFNO_20_k = np.loadtxt("../../m12w90n40g45fac4nff2seed0_lr5e-4_bs5_200gap_4_20gap/AVG/plot_python_k/PDF/vel_k/result/{}cases/error_with_time_F_IUFNO_k={}.dat".format(case_number,vel_k), dtype=float)
        F_IFNO_20_k = np.loadtxt("../../m12w90n40g45fac4nff2seed0_lr5e-4_bs5_200gap_4_20gap/AVG/plot_python_k/PDF/vel_k/result/{}cases/error_with_time_F_IFNO_k={}.dat".format(case_number,vel_k), dtype=float)
        IFNO_20_k = np.loadtxt("../../m12w90n40g45fac4nff2seed0_lr5e-4_bs5_200gap_4_20gap/AVG/plot_python_k/PDF/vel_k/result/{}cases/error_with_time_IFNO_k={}.dat".format(case_number,vel_k), dtype=float)
        
        IUFNO_40_k = np.loadtxt("../../m12w90n40g45fac4nff2seed0_lr5e-4_bs5_40gap/AVG/plot_python_k/PDF/vel_k/result/{}cases/error_with_time_IUFNO_k={}.dat".format(case_number,vel_k), dtype=float)
        F_IUFNO_40_k = np.loadtxt("../../m12w90n40g45fac4nff2seed0_lr5e-4_bs5_40gap/AVG/plot_python_k/PDF/vel_k/result/{}cases/error_with_time_F_IUFNO_k={}.dat".format(case_number,vel_k), dtype=float)
        F_IFNO_40_k = np.loadtxt("../../m12w90n40g45fac4nff2seed0_lr5e-4_bs5_40gap/AVG/plot_python_k/PDF/vel_k/result/{}cases/error_with_time_F_IFNO_k={}.dat".format(case_number,vel_k), dtype=float)
        IFNO_40_k = np.loadtxt("../../m12w90n40g45fac4nff2seed0_lr5e-4_bs5_40gap/AVG/plot_python_k/PDF/vel_k/result/{}cases/error_with_time_IFNO_k={}.dat".format(case_number,vel_k), dtype=float)
        
        IUFNO_100_k = np.loadtxt("../../m12w90n40g45fac4nff2seed0_lr5e-4_bs5_100gap/AVG/plot_python_k/PDF/vel_k/result/{}cases/error_with_time_IUFNO_k={}.dat".format(case_number,vel_k), dtype=float)
        F_IUFNO_100_k = np.loadtxt("../../m12w90n40g45fac4nff2seed0_lr5e-4_bs5_100gap/AVG/plot_python_k/PDF/vel_k/result/{}cases/error_with_time_F_IUFNO_k={}.dat".format(case_number,vel_k), dtype=float)
        F_IFNO_100_k = np.loadtxt("../../m12w90n40g45fac4nff2seed0_lr5e-4_bs5_100gap/AVG/plot_python_k/PDF/vel_k/result/{}cases/error_with_time_F_IFNO_k={}.dat".format(case_number,vel_k), dtype=float)
        IFNO_100_k = np.loadtxt("../../m12w90n40g45fac4nff2seed0_lr5e-4_bs5_100gap/AVG/plot_python_k/PDF/vel_k/result/{}cases/error_with_time_IFNO_k={}.dat".format(case_number,vel_k), dtype=float)    
        
        IUFNO_200_k = np.loadtxt("../../m12w90n40g45fac4nff2seed0_lr5e-4_bs5/AVG/plot_python_k/PDF/vel_k/result/{}cases/error_with_time_IUFNO_k={}.dat".format(case_number,vel_k), dtype=float)
        F_IUFNO_200_k = np.loadtxt("../../m12w90n40g45fac4nff2seed0_lr5e-4_bs5/AVG/plot_python_k/PDF/vel_k/result/{}cases/error_with_time_F_IUFNO_k={}.dat".format(case_number,vel_k), dtype=float)
        F_IFNO_200_k = np.loadtxt("../../m12w90n40g45fac4nff2seed0_lr5e-4_bs5/AVG/plot_python_k/PDF/vel_k/result/{}cases/error_with_time_F_IFNO_k={}.dat".format(case_number,vel_k), dtype=float)
        IFNO_200_k = np.loadtxt("../../m12w90n40g45fac4nff2seed0_lr5e-4_bs5/AVG/plot_python_k/PDF/vel_k/result/{}cases/error_with_time_IFNO_k={}.dat".format(case_number,vel_k), dtype=float)    

        IUFNO_300_k = np.loadtxt("../../m12w90n40g45fac4nff2seed0_lr5e-4_bs5_300gap/AVG/plot_python_k/PDF/vel_k/result/{}cases/error_with_time_IUFNO_k={}.dat".format(case_number,vel_k), dtype=float)
        F_IUFNO_300_k = np.loadtxt("../../m12w90n40g45fac4nff2seed0_lr5e-4_bs5_300gap/AVG/plot_python_k/PDF/vel_k/result/{}cases/error_with_time_F_IUFNO_k={}.dat".format(case_number,vel_k), dtype=float)
        F_IFNO_300_k = np.loadtxt("../../m12w90n40g45fac4nff2seed0_lr5e-4_bs5_300gap/AVG/plot_python_k/PDF/vel_k/result/{}cases/error_with_time_F_IFNO_k={}.dat".format(case_number,vel_k), dtype=float)
        IFNO_300_k = np.loadtxt("../../m12w90n40g45fac4nff2seed0_lr5e-4_bs5_300gap/AVG/plot_python_k/PDF/vel_k/result/{}cases/error_with_time_IFNO_k={}.dat".format(case_number,vel_k), dtype=float)  
     
        IUFNO_400_k = np.loadtxt("../../m12w90n40g45fac4nff2seed0_lr5e-4_bs5_400gap/AVG/plot_python_k/PDF/vel_k/result/{}cases/error_with_time_IUFNO_k={}.dat".format(case_number,vel_k), dtype=float)
        F_IUFNO_400_k = np.loadtxt("../../m12w90n40g45fac4nff2seed0_lr5e-4_bs5_400gap/AVG/plot_python_k/PDF/vel_k/result/{}cases/error_with_time_F_IUFNO_k={}.dat".format(case_number,vel_k), dtype=float)
        F_IFNO_400_k = np.loadtxt("../../m12w90n40g45fac4nff2seed0_lr5e-4_bs5_400gap/AVG/plot_python_k/PDF/vel_k/result/{}cases/error_with_time_F_IFNO_k={}.dat".format(case_number,vel_k), dtype=float)
        IFNO_400_k = np.loadtxt("../../m12w90n40g45fac4nff2seed0_lr5e-4_bs5_400gap/AVG/plot_python_k/PDF/vel_k/result/{}cases/error_with_time_IFNO_k={}.dat".format(case_number,vel_k), dtype=float)  

        
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

    print(len(avg_error))#600

    ######----------------------------x=model----------------------------########
    # 图形参数设置
    dpi = 600
    width, height = 10, 6
    fontSize = 30
    lineWidth = 2
    boxWidth = 2.5
    Lmajor, Lminor = 7, 4
    xlabPad, ylabPad = 10, 10
    xlabel = r"$\mathdefault{k}$"
    ylabel = r"$\mathdefault{Error}$"
    xlimit=[0,0.42]
    #ylimit = [-0.18,0.04]
    legend = ["F-IFNO_constraint", "F-IUFNO_constraint", "IUFNO_constraint", "IFNO_constraint","F-IFNO", "F-IUFNO", "IUFNO", "IFNO","DSM","fDNS"]
    legend1 = [r"$\mathdefault{\Delta T=0.02\tau}$", r"$\mathdefault{\Delta T=0.04\tau}$",r"$\mathdefault{\Delta T=0.1\tau}$",r"$\mathdefault{\Delta T=0.2\tau}$",r"$\mathdefault{\Delta T=0.3\tau}$",r"$\mathdefault{\Delta T=0.4\tau}$"]
    colors = ['#A52A2A','#ff7f0e','gold','green','#1f77b4','#008080','purple','pink','#00FFFF','#FF00FF']
    fig = plt.figure(figsize=(width, height), dpi=dpi)
    plt.rcParams["font.size"] = fontSize
    plt.rcParams["axes.linewidth"] = lineWidth
    ax = fig.add_axes([0, 0, 1, 1])
    # X 轴设置
    ax.xaxis.set_minor_locator(mpl.ticker.MultipleLocator(1))        
    ax.xaxis.set_major_locator(mpl.ticker.MultipleLocator(1)) 
    ax.xaxis.set_major_formatter(mpl.ticker.FormatStrFormatter('%1.0f'))
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

    plt.xlabel(xlabel, fontsize=30)
    plt.ylabel(ylabel, fontsize=30)

    plt.xticks(fontsize=30)
    plt.yticks(fontsize=30)   

    # Matplotlib 配置
    mpl.rc('font', family='STIXGeneral')
    mpl.rc('text', usetex=False)
    mpl.rcParams['xtick.direction'] = 'in'
    mpl.rcParams['ytick.direction'] = 'in'
    plt.rcParams["mathtext.fontset"] = "cm"

    x1 = [1,2,3,4,5,6,7,8,9,10]
    jj=0
    
    oo=10*0+0+jj
    mean1 = [avg_error[oo+60*0], avg_error[oo+60*1], avg_error[oo+60*2], avg_error[oo+60*3], avg_error[oo+60*4], avg_error[oo+60*5], avg_error[oo+60*6], avg_error[oo+60*7], avg_error[oo+60*8], avg_error[oo+60*9]]
    std1 = [variance_error[oo+60*0],variance_error[oo+60*1],variance_error[oo+60*2],variance_error[oo+60*3],variance_error[oo+60*4],variance_error[oo+60*5],variance_error[oo+60*6],variance_error[oo+60*7],variance_error[oo+60*8],variance_error[oo+60*9]]
    
    oo=10*1+0+jj 
    mean2 = [avg_error[oo+60*0], avg_error[oo+60*1], avg_error[oo+60*2], avg_error[oo+60*3], avg_error[oo+60*4], avg_error[oo+60*5], avg_error[oo+60*6], avg_error[oo+60*7], avg_error[oo+60*8], avg_error[oo+60*9]]
    std2 = [variance_error[oo+60*0],variance_error[oo+60*1],variance_error[oo+60*2],variance_error[oo+60*3],variance_error[oo+60*4],variance_error[oo+60*5],variance_error[oo+60*6],variance_error[oo+60*7],variance_error[oo+60*8],variance_error[oo+60*9]]

    oo=10*2+0+jj
    mean3 = [avg_error[oo+60*0], avg_error[oo+60*1], avg_error[oo+60*2], avg_error[oo+60*3], avg_error[oo+60*4], avg_error[oo+60*5], avg_error[oo+60*6], avg_error[oo+60*7], avg_error[oo+60*8], avg_error[oo+60*9]]
    std3 = [variance_error[oo+60*0],variance_error[oo+60*1],variance_error[oo+60*2],variance_error[oo+60*3],variance_error[oo+60*4],variance_error[oo+60*5],variance_error[oo+60*6],variance_error[oo+60*7],variance_error[oo+60*8],variance_error[oo+60*9]]

    oo=10*3+0+jj
    mean4 = [avg_error[oo+60*0], avg_error[oo+60*1], avg_error[oo+60*2], avg_error[oo+60*3], avg_error[oo+60*4], avg_error[oo+60*5], avg_error[oo+60*6], avg_error[oo+60*7], avg_error[oo+60*8], avg_error[oo+60*9]]
    std4 = [variance_error[oo+60*0],variance_error[oo+60*1],variance_error[oo+60*2],variance_error[oo+60*3],variance_error[oo+60*4],variance_error[oo+60*5],variance_error[oo+60*6],variance_error[oo+60*7],variance_error[oo+60*8],variance_error[oo+60*9]]

    oo=10*4+0+jj
    mean5 = [avg_error[oo+60*0], avg_error[oo+60*1], avg_error[oo+60*2], avg_error[oo+60*3], avg_error[oo+60*4], avg_error[oo+60*5], avg_error[oo+60*6], avg_error[oo+60*7], avg_error[oo+60*8], avg_error[oo+60*9]]
    std5 = [variance_error[oo+60*0],variance_error[oo+60*1],variance_error[oo+60*2],variance_error[oo+60*3],variance_error[oo+60*4],variance_error[oo+60*5],variance_error[oo+60*6],variance_error[oo+60*7],variance_error[oo+60*8],variance_error[oo+60*9]]

    oo=10*5+0+jj
    mean6 = [avg_error[oo+60*0], avg_error[oo+60*1], avg_error[oo+60*2], avg_error[oo+60*3], avg_error[oo+60*4], avg_error[oo+60*5], avg_error[oo+60*6], avg_error[oo+60*7], avg_error[oo+60*8], avg_error[oo+60*9]]
    std6 = [variance_error[oo+60*0],variance_error[oo+60*1],variance_error[oo+60*2],variance_error[oo+60*3],variance_error[oo+60*4],variance_error[oo+60*5],variance_error[oo+60*6],variance_error[oo+60*7],variance_error[oo+60*8],variance_error[oo+60*9]]


    yanse=colors[0]
    plt.plot(x1[2:], mean1[2:], color=yanse, alpha=0.3, linewidth=2*lineWidth, linestyle='--',zorder=2)
    plt.errorbar(x1[2:], mean1[2:], yerr=std1[2:], fmt='o', color=yanse, ecolor=yanse, capsize=8, elinewidth=4, markeredgewidth=4, label=legend1[0],zorder=2)

    yanse=colors[1]
    plt.plot(x1[2:], mean2[2:], color=yanse, alpha=0.3, linewidth=2*lineWidth, linestyle='--',zorder=2)
    plt.errorbar(x1[2:], mean2[2:], yerr=std2[2:], fmt='o', color=yanse, ecolor=yanse, capsize=8, elinewidth=4, markeredgewidth=4, label=legend1[1],zorder=2)

    yanse=colors[2]
    plt.plot(x1[2:], mean3[2:], color=yanse, alpha=0.3, linewidth=2*lineWidth, linestyle='--',zorder=2)
    plt.errorbar(x1[2:], mean3[2:], yerr=std3[2:], fmt='o', color=yanse, ecolor=yanse, capsize=8, elinewidth=4, markeredgewidth=4, label=legend1[2],zorder=2)

    yanse=colors[3]
    plt.plot(x1[2:], mean4[2:], color=yanse, alpha=0.3, linewidth=2*lineWidth, linestyle='--',zorder=2)
    plt.errorbar(x1[2:], mean4[2:], yerr=std4[2:], fmt='o', color=yanse, ecolor=yanse, capsize=8, elinewidth=4, markeredgewidth=4, label=legend1[3],zorder=2)

    yanse=colors[4]
    plt.plot(x1[2:], mean5[2:], color=yanse, alpha=0.3, linewidth=2*lineWidth, linestyle='--',zorder=2)
    plt.errorbar(x1[2:], mean5[2:], yerr=std5[2:], fmt='o', color=yanse, ecolor=yanse, capsize=8, elinewidth=4, markeredgewidth=4, label=legend1[4],zorder=2)
    
    yanse=colors[5]
    plt.plot(x1[2:], mean6[2:], color=yanse, alpha=0.3, linewidth=2*lineWidth, linestyle='--',zorder=2)
    plt.errorbar(x1[2:], mean6[2:], yerr=std6[2:], fmt='o', color=yanse, ecolor=yanse, capsize=8, elinewidth=4, markeredgewidth=4, label=legend1[5],zorder=2)   
    


    # Matplotlib 配置 - 全局字体设置为 STIXGeneral
    mpl.rc('font', family='STIXGeneral')
    # 创建图例
    #plt.title(r"Errorbar for Ek", fontsize=25, color='black', loc='center', pad=15)
    '''lgd = plt.legend(
        loc='upper right',       # 自动选择最优位置
        fontsize=25,
        frameon=True,
        framealpha=0,
        edgecolor='black',
        shadow=False
    )'''
    # 显示网格
    #plt.grid()
    figPath1 = os.path.abspath("./vel_k_errorbar_with_k/{}cases".format(case_number))
    gfile1 = "Errorbar for E(k=3-10) F-IFNO_k_label.png"
    gpath1 = os.path.join(figPath1, gfile1)
    # 保存图形
    plt.savefig(gpath1, bbox_inches='tight')
    plt.close()
    
    
    
    ######----------------------------x=model----------------------------########
    # 图形参数设置
    dpi = 600
    width, height = 10, 6
    fontSize = 30
    lineWidth = 2
    boxWidth = 2.5
    Lmajor, Lminor = 7, 4
    xlabPad, ylabPad = 10, 10
    xlabel = r"$\mathdefault{k}$"
    ylabel = r"$\mathdefault{Error}$"
    xlimit=[0,0.42]
    #ylimit = [-0.18,0.04]
    legend = ["F-IFNO_constraint", "F-IUFNO_constraint", "IUFNO_constraint", "IFNO_constraint","F-IFNO", "F-IUFNO", "IUFNO", "IFNO","DSM","fDNS"]
    legend1 = [r"$\mathdefault{\Delta T=0.02\tau}$", r"$\mathdefault{\Delta T=0.04\tau}$",r"$\mathdefault{\Delta T=0.1\tau}$",r"$\mathdefault{\Delta T=0.2\tau}$",r"$\mathdefault{\Delta T=0.3\tau}$",r"$\mathdefault{\Delta T=0.4\tau}$"]
    colors = ['#A52A2A','#ff7f0e','gold','green','#1f77b4','#008080','purple','pink','#00FFFF','#FF00FF']
    fig = plt.figure(figsize=(width, height), dpi=dpi)
    plt.rcParams["font.size"] = fontSize
    plt.rcParams["axes.linewidth"] = lineWidth
    ax = fig.add_axes([0, 0, 1, 1])
    # X 轴设置
    ax.xaxis.set_minor_locator(mpl.ticker.MultipleLocator(1))        
    ax.xaxis.set_major_locator(mpl.ticker.MultipleLocator(1)) 
    ax.xaxis.set_major_formatter(mpl.ticker.FormatStrFormatter('%1.0f'))
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

    plt.xlabel(xlabel, fontsize=30)
    plt.ylabel(ylabel, fontsize=30)

    plt.xticks(fontsize=30)
    plt.yticks(fontsize=30)   

    # Matplotlib 配置
    mpl.rc('font', family='STIXGeneral')
    mpl.rc('text', usetex=False)
    mpl.rcParams['xtick.direction'] = 'in'
    mpl.rcParams['ytick.direction'] = 'in'
    plt.rcParams["mathtext.fontset"] = "cm"

    x1 = [1,2,3,4,5,6,7,8,9,10]
    jj=1
    
    oo=10*0+0+jj
    mean1 = [avg_error[oo+60*0], avg_error[oo+60*1], avg_error[oo+60*2], avg_error[oo+60*3], avg_error[oo+60*4], avg_error[oo+60*5], avg_error[oo+60*6], avg_error[oo+60*7], avg_error[oo+60*8], avg_error[oo+60*9]]
    std1 = [variance_error[oo+60*0],variance_error[oo+60*1],variance_error[oo+60*2],variance_error[oo+60*3],variance_error[oo+60*4],variance_error[oo+60*5],variance_error[oo+60*6],variance_error[oo+60*7],variance_error[oo+60*8],variance_error[oo+60*9]]
    
    oo=10*1+0+jj 
    mean2 = [avg_error[oo+60*0], avg_error[oo+60*1], avg_error[oo+60*2], avg_error[oo+60*3], avg_error[oo+60*4], avg_error[oo+60*5], avg_error[oo+60*6], avg_error[oo+60*7], avg_error[oo+60*8], avg_error[oo+60*9]]
    std2 = [variance_error[oo+60*0],variance_error[oo+60*1],variance_error[oo+60*2],variance_error[oo+60*3],variance_error[oo+60*4],variance_error[oo+60*5],variance_error[oo+60*6],variance_error[oo+60*7],variance_error[oo+60*8],variance_error[oo+60*9]]

    oo=10*2+0+jj
    mean3 = [avg_error[oo+60*0], avg_error[oo+60*1], avg_error[oo+60*2], avg_error[oo+60*3], avg_error[oo+60*4], avg_error[oo+60*5], avg_error[oo+60*6], avg_error[oo+60*7], avg_error[oo+60*8], avg_error[oo+60*9]]
    std3 = [variance_error[oo+60*0],variance_error[oo+60*1],variance_error[oo+60*2],variance_error[oo+60*3],variance_error[oo+60*4],variance_error[oo+60*5],variance_error[oo+60*6],variance_error[oo+60*7],variance_error[oo+60*8],variance_error[oo+60*9]]

    oo=10*3+0+jj
    mean4 = [avg_error[oo+60*0], avg_error[oo+60*1], avg_error[oo+60*2], avg_error[oo+60*3], avg_error[oo+60*4], avg_error[oo+60*5], avg_error[oo+60*6], avg_error[oo+60*7], avg_error[oo+60*8], avg_error[oo+60*9]]
    std4 = [variance_error[oo+60*0],variance_error[oo+60*1],variance_error[oo+60*2],variance_error[oo+60*3],variance_error[oo+60*4],variance_error[oo+60*5],variance_error[oo+60*6],variance_error[oo+60*7],variance_error[oo+60*8],variance_error[oo+60*9]]

    oo=10*4+0+jj
    mean5 = [avg_error[oo+60*0], avg_error[oo+60*1], avg_error[oo+60*2], avg_error[oo+60*3], avg_error[oo+60*4], avg_error[oo+60*5], avg_error[oo+60*6], avg_error[oo+60*7], avg_error[oo+60*8], avg_error[oo+60*9]]
    std5 = [variance_error[oo+60*0],variance_error[oo+60*1],variance_error[oo+60*2],variance_error[oo+60*3],variance_error[oo+60*4],variance_error[oo+60*5],variance_error[oo+60*6],variance_error[oo+60*7],variance_error[oo+60*8],variance_error[oo+60*9]]

    oo=10*5+0+jj
    mean6 = [avg_error[oo+60*0], avg_error[oo+60*1], avg_error[oo+60*2], avg_error[oo+60*3], avg_error[oo+60*4], avg_error[oo+60*5], avg_error[oo+60*6], avg_error[oo+60*7], avg_error[oo+60*8], avg_error[oo+60*9]]
    std6 = [variance_error[oo+60*0],variance_error[oo+60*1],variance_error[oo+60*2],variance_error[oo+60*3],variance_error[oo+60*4],variance_error[oo+60*5],variance_error[oo+60*6],variance_error[oo+60*7],variance_error[oo+60*8],variance_error[oo+60*9]]


    yanse=colors[0]
    plt.plot(x1[2:], mean1[2:], color=yanse, alpha=0.3, linewidth=2*lineWidth, linestyle='--',zorder=2)
    plt.errorbar(x1[2:], mean1[2:], yerr=std1[2:], fmt='o', color=yanse, ecolor=yanse, capsize=8, elinewidth=4, markeredgewidth=4, label=legend1[0],zorder=2)

    yanse=colors[1]
    plt.plot(x1[2:], mean2[2:], color=yanse, alpha=0.3, linewidth=2*lineWidth, linestyle='--',zorder=2)
    plt.errorbar(x1[2:], mean2[2:], yerr=std2[2:], fmt='o', color=yanse, ecolor=yanse, capsize=8, elinewidth=4, markeredgewidth=4, label=legend1[1],zorder=2)

    yanse=colors[2]
    plt.plot(x1[2:], mean3[2:], color=yanse, alpha=0.3, linewidth=2*lineWidth, linestyle='--',zorder=2)
    plt.errorbar(x1[2:], mean3[2:], yerr=std3[2:], fmt='o', color=yanse, ecolor=yanse, capsize=8, elinewidth=4, markeredgewidth=4, label=legend1[2],zorder=2)

    yanse=colors[3]
    plt.plot(x1[2:], mean4[2:], color=yanse, alpha=0.3, linewidth=2*lineWidth, linestyle='--',zorder=2)
    plt.errorbar(x1[2:], mean4[2:], yerr=std4[2:], fmt='o', color=yanse, ecolor=yanse, capsize=8, elinewidth=4, markeredgewidth=4, label=legend1[3],zorder=2)

    yanse=colors[4]
    plt.plot(x1[2:], mean5[2:], color=yanse, alpha=0.3, linewidth=2*lineWidth, linestyle='--',zorder=2)
    plt.errorbar(x1[2:], mean5[2:], yerr=std5[2:], fmt='o', color=yanse, ecolor=yanse, capsize=8, elinewidth=4, markeredgewidth=4, label=legend1[4],zorder=2)
    
    yanse=colors[5]
    plt.plot(x1[2:], mean6[2:], color=yanse, alpha=0.3, linewidth=2*lineWidth, linestyle='--',zorder=2)
    plt.errorbar(x1[2:], mean6[2:], yerr=std6[2:], fmt='o', color=yanse, ecolor=yanse, capsize=8, elinewidth=4, markeredgewidth=4, label=legend1[5],zorder=2)   
    


    # Matplotlib 配置 - 全局字体设置为 STIXGeneral
    mpl.rc('font', family='STIXGeneral')
    # 创建图例
    #plt.title(r"Errorbar for Ek", fontsize=25, color='black', loc='center', pad=15)
    '''lgd = plt.legend(
        loc='upper right',       # 自动选择最优位置
        fontsize=25,
        frameon=True,
        framealpha=0,
        edgecolor='black',
        shadow=False
    )'''
    # 显示网格
    #plt.grid()
    figPath1 = os.path.abspath("./vel_k_errorbar_with_k/{}cases".format(case_number))
    gfile1 = "Errorbar for E(k=3-10) F-IUFNO_k_label.png"
    gpath1 = os.path.join(figPath1, gfile1)
    # 保存图形
    plt.savefig(gpath1, bbox_inches='tight')
    plt.close()    
    
    ######----------------------------x=model----------------------------########
    # 图形参数设置
    dpi = 600
    width, height = 10, 6
    fontSize = 30
    lineWidth = 2
    boxWidth = 2.5
    Lmajor, Lminor = 7, 4
    xlabPad, ylabPad = 10, 10
    xlabel = r"$\mathdefault{k}$"
    ylabel = r"$\mathdefault{Error}$"
    xlimit=[0,0.42]
    #ylimit = [-0.18,0.04]
    legend = ["F-IFNO_constraint", "F-IUFNO_constraint", "IUFNO_constraint", "IFNO_constraint","F-IFNO", "F-IUFNO", "IUFNO", "IFNO","DSM","fDNS"]
    legend1 = [r"$\mathdefault{\Delta T=0.02\tau}$", r"$\mathdefault{\Delta T=0.04\tau}$",r"$\mathdefault{\Delta T=0.1\tau}$",r"$\mathdefault{\Delta T=0.2\tau}$",r"$\mathdefault{\Delta T=0.3\tau}$",r"$\mathdefault{\Delta T=0.4\tau}$"]
    colors = ['#A52A2A','#ff7f0e','gold','green','#1f77b4','#008080','purple','pink','#00FFFF','#FF00FF']
    fig = plt.figure(figsize=(width, height), dpi=dpi)
    plt.rcParams["font.size"] = fontSize
    plt.rcParams["axes.linewidth"] = lineWidth
    ax = fig.add_axes([0, 0, 1, 1])
    # X 轴设置
    ax.xaxis.set_minor_locator(mpl.ticker.MultipleLocator(1))        
    ax.xaxis.set_major_locator(mpl.ticker.MultipleLocator(1)) 
    ax.xaxis.set_major_formatter(mpl.ticker.FormatStrFormatter('%1.0f'))
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

    plt.xlabel(xlabel, fontsize=30)
    plt.ylabel(ylabel, fontsize=30)

    plt.xticks(fontsize=30)
    plt.yticks(fontsize=30)   

    # Matplotlib 配置
    mpl.rc('font', family='STIXGeneral')
    mpl.rc('text', usetex=False)
    mpl.rcParams['xtick.direction'] = 'in'
    mpl.rcParams['ytick.direction'] = 'in'
    plt.rcParams["mathtext.fontset"] = "cm"

    x1 = [1,2,3,4,5,6,7,8,9,10]
    jj=2
    
    oo=10*0+0+jj
    mean1 = [avg_error[oo+60*0], avg_error[oo+60*1], avg_error[oo+60*2], avg_error[oo+60*3], avg_error[oo+60*4], avg_error[oo+60*5], avg_error[oo+60*6], avg_error[oo+60*7], avg_error[oo+60*8], avg_error[oo+60*9]]
    std1 = [variance_error[oo+60*0],variance_error[oo+60*1],variance_error[oo+60*2],variance_error[oo+60*3],variance_error[oo+60*4],variance_error[oo+60*5],variance_error[oo+60*6],variance_error[oo+60*7],variance_error[oo+60*8],variance_error[oo+60*9]]
    
    oo=10*1+0+jj 
    mean2 = [avg_error[oo+60*0], avg_error[oo+60*1], avg_error[oo+60*2], avg_error[oo+60*3], avg_error[oo+60*4], avg_error[oo+60*5], avg_error[oo+60*6], avg_error[oo+60*7], avg_error[oo+60*8], avg_error[oo+60*9]]
    std2 = [variance_error[oo+60*0],variance_error[oo+60*1],variance_error[oo+60*2],variance_error[oo+60*3],variance_error[oo+60*4],variance_error[oo+60*5],variance_error[oo+60*6],variance_error[oo+60*7],variance_error[oo+60*8],variance_error[oo+60*9]]

    oo=10*2+0+jj
    mean3 = [avg_error[oo+60*0], avg_error[oo+60*1], avg_error[oo+60*2], avg_error[oo+60*3], avg_error[oo+60*4], avg_error[oo+60*5], avg_error[oo+60*6], avg_error[oo+60*7], avg_error[oo+60*8], avg_error[oo+60*9]]
    std3 = [variance_error[oo+60*0],variance_error[oo+60*1],variance_error[oo+60*2],variance_error[oo+60*3],variance_error[oo+60*4],variance_error[oo+60*5],variance_error[oo+60*6],variance_error[oo+60*7],variance_error[oo+60*8],variance_error[oo+60*9]]

    oo=10*3+0+jj
    mean4 = [avg_error[oo+60*0], avg_error[oo+60*1], avg_error[oo+60*2], avg_error[oo+60*3], avg_error[oo+60*4], avg_error[oo+60*5], avg_error[oo+60*6], avg_error[oo+60*7], avg_error[oo+60*8], avg_error[oo+60*9]]
    std4 = [variance_error[oo+60*0],variance_error[oo+60*1],variance_error[oo+60*2],variance_error[oo+60*3],variance_error[oo+60*4],variance_error[oo+60*5],variance_error[oo+60*6],variance_error[oo+60*7],variance_error[oo+60*8],variance_error[oo+60*9]]

    oo=10*4+0+jj
    mean5 = [avg_error[oo+60*0], avg_error[oo+60*1], avg_error[oo+60*2], avg_error[oo+60*3], avg_error[oo+60*4], avg_error[oo+60*5], avg_error[oo+60*6], avg_error[oo+60*7], avg_error[oo+60*8], avg_error[oo+60*9]]
    std5 = [variance_error[oo+60*0],variance_error[oo+60*1],variance_error[oo+60*2],variance_error[oo+60*3],variance_error[oo+60*4],variance_error[oo+60*5],variance_error[oo+60*6],variance_error[oo+60*7],variance_error[oo+60*8],variance_error[oo+60*9]]

    oo=10*5+0+jj
    mean6 = [avg_error[oo+60*0], avg_error[oo+60*1], avg_error[oo+60*2], avg_error[oo+60*3], avg_error[oo+60*4], avg_error[oo+60*5], avg_error[oo+60*6], avg_error[oo+60*7], avg_error[oo+60*8], avg_error[oo+60*9]]
    std6 = [variance_error[oo+60*0],variance_error[oo+60*1],variance_error[oo+60*2],variance_error[oo+60*3],variance_error[oo+60*4],variance_error[oo+60*5],variance_error[oo+60*6],variance_error[oo+60*7],variance_error[oo+60*8],variance_error[oo+60*9]]


    yanse=colors[0]
    plt.plot(x1[2:], mean1[2:], color=yanse, alpha=0.3, linewidth=2*lineWidth, linestyle='--',zorder=2)
    plt.errorbar(x1[2:], mean1[2:], yerr=std1[2:], fmt='o', color=yanse, ecolor=yanse, capsize=8, elinewidth=4, markeredgewidth=4, label=legend1[0],zorder=2)

    yanse=colors[1]
    plt.plot(x1[2:], mean2[2:], color=yanse, alpha=0.3, linewidth=2*lineWidth, linestyle='--',zorder=2)
    plt.errorbar(x1[2:], mean2[2:], yerr=std2[2:], fmt='o', color=yanse, ecolor=yanse, capsize=8, elinewidth=4, markeredgewidth=4, label=legend1[1],zorder=2)

    yanse=colors[2]
    plt.plot(x1[2:], mean3[2:], color=yanse, alpha=0.3, linewidth=2*lineWidth, linestyle='--',zorder=2)
    plt.errorbar(x1[2:], mean3[2:], yerr=std3[2:], fmt='o', color=yanse, ecolor=yanse, capsize=8, elinewidth=4, markeredgewidth=4, label=legend1[2],zorder=2)

    yanse=colors[3]
    plt.plot(x1[2:], mean4[2:], color=yanse, alpha=0.3, linewidth=2*lineWidth, linestyle='--',zorder=2)
    plt.errorbar(x1[2:], mean4[2:], yerr=std4[2:], fmt='o', color=yanse, ecolor=yanse, capsize=8, elinewidth=4, markeredgewidth=4, label=legend1[3],zorder=2)

    yanse=colors[4]
    plt.plot(x1[2:], mean5[2:], color=yanse, alpha=0.3, linewidth=2*lineWidth, linestyle='--',zorder=2)
    plt.errorbar(x1[2:], mean5[2:], yerr=std5[2:], fmt='o', color=yanse, ecolor=yanse, capsize=8, elinewidth=4, markeredgewidth=4, label=legend1[4],zorder=2)
    
    yanse=colors[5]
    plt.plot(x1[2:], mean6[2:], color=yanse, alpha=0.3, linewidth=2*lineWidth, linestyle='--',zorder=2)
    plt.errorbar(x1[2:], mean6[2:], yerr=std6[2:], fmt='o', color=yanse, ecolor=yanse, capsize=8, elinewidth=4, markeredgewidth=4, label=legend1[5],zorder=2)   
    


    # Matplotlib 配置 - 全局字体设置为 STIXGeneral
    mpl.rc('font', family='STIXGeneral')
    # 创建图例
    #plt.title(r"Errorbar for Ek", fontsize=25, color='black', loc='center', pad=15)
    '''lgd = plt.legend(
        loc='upper right',       # 自动选择最优位置
        fontsize=25,
        frameon=True,
        framealpha=0,
        edgecolor='black',
        shadow=False
    )'''
    # 显示网格
    #plt.grid()
    figPath1 = os.path.abspath("./vel_k_errorbar_with_k/{}cases".format(case_number))
    gfile1 = "Errorbar for E(k=3-10) IUFNO_k_label.png"
    gpath1 = os.path.join(figPath1, gfile1)
    # 保存图形
    plt.savefig(gpath1, bbox_inches='tight')
    plt.close()    
    
    
    
    ######----------------------------x=model----------------------------########
    # 图形参数设置
    dpi = 600
    width, height = 10, 6
    fontSize = 30
    lineWidth = 2
    boxWidth = 2.5
    Lmajor, Lminor = 7, 4
    xlabPad, ylabPad = 10, 10
    xlabel = r"$\mathdefault{k}$"
    ylabel = r"$\mathdefault{Error}$"
    xlimit=[0,0.42]
    #ylimit = [-0.18,0.04]
    legend = ["F-IFNO_constraint", "F-IUFNO_constraint", "IUFNO_constraint", "IFNO_constraint","F-IFNO", "F-IUFNO", "IUFNO", "IFNO","DSM","fDNS"]
    legend1 = [r"$\mathdefault{\Delta T=0.02\tau}$", r"$\mathdefault{\Delta T=0.04\tau}$",r"$\mathdefault{\Delta T=0.1\tau}$",r"$\mathdefault{\Delta T=0.2\tau}$",r"$\mathdefault{\Delta T=0.3\tau}$",r"$\mathdefault{\Delta T=0.4\tau}$"]
    colors = ['#A52A2A','#ff7f0e','gold','green','#1f77b4','#008080','purple','pink','#00FFFF','#FF00FF']
    fig = plt.figure(figsize=(width, height), dpi=dpi)
    plt.rcParams["font.size"] = fontSize
    plt.rcParams["axes.linewidth"] = lineWidth
    ax = fig.add_axes([0, 0, 1, 1])
    # X 轴设置
    ax.xaxis.set_minor_locator(mpl.ticker.MultipleLocator(1))        
    ax.xaxis.set_major_locator(mpl.ticker.MultipleLocator(1)) 
    ax.xaxis.set_major_formatter(mpl.ticker.FormatStrFormatter('%1.0f'))
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

    plt.xlabel(xlabel, fontsize=30)
    plt.ylabel(ylabel, fontsize=30)

    plt.xticks(fontsize=30)
    plt.yticks(fontsize=30)   

    # Matplotlib 配置
    mpl.rc('font', family='STIXGeneral')
    mpl.rc('text', usetex=False)
    mpl.rcParams['xtick.direction'] = 'in'
    mpl.rcParams['ytick.direction'] = 'in'
    plt.rcParams["mathtext.fontset"] = "cm"

    x1 = [1,2,3,4,5,6,7,8,9,10]
    jj=3
    
    oo=10*0+0+jj
    mean1 = [avg_error[oo+60*0], avg_error[oo+60*1], avg_error[oo+60*2], avg_error[oo+60*3], avg_error[oo+60*4], avg_error[oo+60*5], avg_error[oo+60*6], avg_error[oo+60*7], avg_error[oo+60*8], avg_error[oo+60*9]]
    std1 = [variance_error[oo+60*0],variance_error[oo+60*1],variance_error[oo+60*2],variance_error[oo+60*3],variance_error[oo+60*4],variance_error[oo+60*5],variance_error[oo+60*6],variance_error[oo+60*7],variance_error[oo+60*8],variance_error[oo+60*9]]
    
    oo=10*1+0+jj 
    mean2 = [avg_error[oo+60*0], avg_error[oo+60*1], avg_error[oo+60*2], avg_error[oo+60*3], avg_error[oo+60*4], avg_error[oo+60*5], avg_error[oo+60*6], avg_error[oo+60*7], avg_error[oo+60*8], avg_error[oo+60*9]]
    std2 = [variance_error[oo+60*0],variance_error[oo+60*1],variance_error[oo+60*2],variance_error[oo+60*3],variance_error[oo+60*4],variance_error[oo+60*5],variance_error[oo+60*6],variance_error[oo+60*7],variance_error[oo+60*8],variance_error[oo+60*9]]

    oo=10*2+0+jj
    mean3 = [avg_error[oo+60*0], avg_error[oo+60*1], avg_error[oo+60*2], avg_error[oo+60*3], avg_error[oo+60*4], avg_error[oo+60*5], avg_error[oo+60*6], avg_error[oo+60*7], avg_error[oo+60*8], avg_error[oo+60*9]]
    std3 = [variance_error[oo+60*0],variance_error[oo+60*1],variance_error[oo+60*2],variance_error[oo+60*3],variance_error[oo+60*4],variance_error[oo+60*5],variance_error[oo+60*6],variance_error[oo+60*7],variance_error[oo+60*8],variance_error[oo+60*9]]

    oo=10*3+0+jj
    mean4 = [avg_error[oo+60*0], avg_error[oo+60*1], avg_error[oo+60*2], avg_error[oo+60*3], avg_error[oo+60*4], avg_error[oo+60*5], avg_error[oo+60*6], avg_error[oo+60*7], avg_error[oo+60*8], avg_error[oo+60*9]]
    std4 = [variance_error[oo+60*0],variance_error[oo+60*1],variance_error[oo+60*2],variance_error[oo+60*3],variance_error[oo+60*4],variance_error[oo+60*5],variance_error[oo+60*6],variance_error[oo+60*7],variance_error[oo+60*8],variance_error[oo+60*9]]

    oo=10*4+0+jj
    mean5 = [avg_error[oo+60*0], avg_error[oo+60*1], avg_error[oo+60*2], avg_error[oo+60*3], avg_error[oo+60*4], avg_error[oo+60*5], avg_error[oo+60*6], avg_error[oo+60*7], avg_error[oo+60*8], avg_error[oo+60*9]]
    std5 = [variance_error[oo+60*0],variance_error[oo+60*1],variance_error[oo+60*2],variance_error[oo+60*3],variance_error[oo+60*4],variance_error[oo+60*5],variance_error[oo+60*6],variance_error[oo+60*7],variance_error[oo+60*8],variance_error[oo+60*9]]

    oo=10*5+0+jj
    mean6 = [avg_error[oo+60*0], avg_error[oo+60*1], avg_error[oo+60*2], avg_error[oo+60*3], avg_error[oo+60*4], avg_error[oo+60*5], avg_error[oo+60*6], avg_error[oo+60*7], avg_error[oo+60*8], avg_error[oo+60*9]]
    std6 = [variance_error[oo+60*0],variance_error[oo+60*1],variance_error[oo+60*2],variance_error[oo+60*3],variance_error[oo+60*4],variance_error[oo+60*5],variance_error[oo+60*6],variance_error[oo+60*7],variance_error[oo+60*8],variance_error[oo+60*9]]


    yanse=colors[0]
    plt.plot(x1[2:], mean1[2:], color=yanse, alpha=0.3, linewidth=2*lineWidth, linestyle='--',zorder=2)
    plt.errorbar(x1[2:], mean1[2:], yerr=std1[2:], fmt='o', color=yanse, ecolor=yanse, capsize=8, elinewidth=4, markeredgewidth=4, label=legend1[0],zorder=2)

    yanse=colors[1]
    plt.plot(x1[2:], mean2[2:], color=yanse, alpha=0.3, linewidth=2*lineWidth, linestyle='--',zorder=2)
    plt.errorbar(x1[2:], mean2[2:], yerr=std2[2:], fmt='o', color=yanse, ecolor=yanse, capsize=8, elinewidth=4, markeredgewidth=4, label=legend1[1],zorder=2)

    yanse=colors[2]
    plt.plot(x1[2:], mean3[2:], color=yanse, alpha=0.3, linewidth=2*lineWidth, linestyle='--',zorder=2)
    plt.errorbar(x1[2:], mean3[2:], yerr=std3[2:], fmt='o', color=yanse, ecolor=yanse, capsize=8, elinewidth=4, markeredgewidth=4, label=legend1[2],zorder=2)

    yanse=colors[3]
    plt.plot(x1[2:], mean4[2:], color=yanse, alpha=0.3, linewidth=2*lineWidth, linestyle='--',zorder=2)
    plt.errorbar(x1[2:], mean4[2:], yerr=std4[2:], fmt='o', color=yanse, ecolor=yanse, capsize=8, elinewidth=4, markeredgewidth=4, label=legend1[3],zorder=2)

    yanse=colors[4]
    plt.plot(x1[2:], mean5[2:], color=yanse, alpha=0.3, linewidth=2*lineWidth, linestyle='--',zorder=2)
    plt.errorbar(x1[2:], mean5[2:], yerr=std5[2:], fmt='o', color=yanse, ecolor=yanse, capsize=8, elinewidth=4, markeredgewidth=4, label=legend1[4],zorder=2)
    
    yanse=colors[5]
    plt.plot(x1[2:], mean6[2:], color=yanse, alpha=0.3, linewidth=2*lineWidth, linestyle='--',zorder=2)
    plt.errorbar(x1[2:], mean6[2:], yerr=std6[2:], fmt='o', color=yanse, ecolor=yanse, capsize=8, elinewidth=4, markeredgewidth=4, label=legend1[5],zorder=2)   
    


    # Matplotlib 配置 - 全局字体设置为 STIXGeneral
    mpl.rc('font', family='STIXGeneral')
    # 创建图例
    #plt.title(r"Errorbar for Ek", fontsize=25, color='black', loc='center', pad=15)
    '''lgd = plt.legend(
        loc='upper right',       # 自动选择最优位置
        fontsize=25,
        frameon=True,
        framealpha=0,
        edgecolor='black',
        shadow=False
    )'''
    # 显示网格
    #plt.grid()
    figPath1 = os.path.abspath("./vel_k_errorbar_with_k/{}cases".format(case_number))
    gfile1 = "Errorbar for E(k=3-10) IFNO_k_label.png"
    gpath1 = os.path.join(figPath1, gfile1)
    # 保存图形
    plt.savefig(gpath1, bbox_inches='tight')
    plt.close()    
    
    
    ######----------------------------x=model----------------------------########
    # 图形参数设置
    dpi = 600
    width, height = 10, 6
    fontSize = 30
    lineWidth = 2
    boxWidth = 2.5
    Lmajor, Lminor = 7, 4
    xlabPad, ylabPad = 10, 10
    xlabel = r"$\mathdefault{k}$"
    ylabel = r"$\mathdefault{Error}$"
    xlimit=[0,0.42]
    #ylimit = [-0.18,0.04]
    legend = ["F-IFNO_constraint", "F-IUFNO_constraint", "IUFNO_constraint", "IFNO_constraint","F-IFNO", "F-IUFNO", "IUFNO", "IFNO","DSM","fDNS"]
    legend1 = [r"$\mathdefault{\Delta T=0.02\tau}$", r"$\mathdefault{\Delta T=0.04\tau}$",r"$\mathdefault{\Delta T=0.1\tau}$",r"$\mathdefault{\Delta T=0.2\tau}$",r"$\mathdefault{\Delta T=0.3\tau}$",r"$\mathdefault{\Delta T=0.4\tau}$"]
    colors = ['#A52A2A','#ff7f0e','gold','green','#1f77b4','#008080','purple','pink','#00FFFF','#FF00FF']
    fig = plt.figure(figsize=(width, height), dpi=dpi)
    plt.rcParams["font.size"] = fontSize
    plt.rcParams["axes.linewidth"] = lineWidth
    ax = fig.add_axes([0, 0, 1, 1])
    # X 轴设置
    ax.xaxis.set_minor_locator(mpl.ticker.MultipleLocator(1))        
    ax.xaxis.set_major_locator(mpl.ticker.MultipleLocator(1)) 
    ax.xaxis.set_major_formatter(mpl.ticker.FormatStrFormatter('%1.0f'))
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

    plt.xlabel(xlabel, fontsize=30)
    plt.ylabel(ylabel, fontsize=30)

    plt.xticks(fontsize=30)
    plt.yticks(fontsize=30)   

    # Matplotlib 配置
    mpl.rc('font', family='STIXGeneral')
    mpl.rc('text', usetex=False)
    mpl.rcParams['xtick.direction'] = 'in'
    mpl.rcParams['ytick.direction'] = 'in'
    plt.rcParams["mathtext.fontset"] = "cm"

    x1 = [1,2,3,4,5,6,7,8,9,10]
    jj=4
    
    oo=10*0+0+jj
    mean1 = [avg_error[oo+60*0], avg_error[oo+60*1], avg_error[oo+60*2], avg_error[oo+60*3], avg_error[oo+60*4], avg_error[oo+60*5], avg_error[oo+60*6], avg_error[oo+60*7], avg_error[oo+60*8], avg_error[oo+60*9]]
    std1 = [variance_error[oo+60*0],variance_error[oo+60*1],variance_error[oo+60*2],variance_error[oo+60*3],variance_error[oo+60*4],variance_error[oo+60*5],variance_error[oo+60*6],variance_error[oo+60*7],variance_error[oo+60*8],variance_error[oo+60*9]]
    
    oo=10*1+0+jj 
    mean2 = [avg_error[oo+60*0], avg_error[oo+60*1], avg_error[oo+60*2], avg_error[oo+60*3], avg_error[oo+60*4], avg_error[oo+60*5], avg_error[oo+60*6], avg_error[oo+60*7], avg_error[oo+60*8], avg_error[oo+60*9]]
    std2 = [variance_error[oo+60*0],variance_error[oo+60*1],variance_error[oo+60*2],variance_error[oo+60*3],variance_error[oo+60*4],variance_error[oo+60*5],variance_error[oo+60*6],variance_error[oo+60*7],variance_error[oo+60*8],variance_error[oo+60*9]]

    oo=10*2+0+jj
    mean3 = [avg_error[oo+60*0], avg_error[oo+60*1], avg_error[oo+60*2], avg_error[oo+60*3], avg_error[oo+60*4], avg_error[oo+60*5], avg_error[oo+60*6], avg_error[oo+60*7], avg_error[oo+60*8], avg_error[oo+60*9]]
    std3 = [variance_error[oo+60*0],variance_error[oo+60*1],variance_error[oo+60*2],variance_error[oo+60*3],variance_error[oo+60*4],variance_error[oo+60*5],variance_error[oo+60*6],variance_error[oo+60*7],variance_error[oo+60*8],variance_error[oo+60*9]]

    oo=10*3+0+jj
    mean4 = [avg_error[oo+60*0], avg_error[oo+60*1], avg_error[oo+60*2], avg_error[oo+60*3], avg_error[oo+60*4], avg_error[oo+60*5], avg_error[oo+60*6], avg_error[oo+60*7], avg_error[oo+60*8], avg_error[oo+60*9]]
    std4 = [variance_error[oo+60*0],variance_error[oo+60*1],variance_error[oo+60*2],variance_error[oo+60*3],variance_error[oo+60*4],variance_error[oo+60*5],variance_error[oo+60*6],variance_error[oo+60*7],variance_error[oo+60*8],variance_error[oo+60*9]]

    oo=10*4+0+jj
    mean5 = [avg_error[oo+60*0], avg_error[oo+60*1], avg_error[oo+60*2], avg_error[oo+60*3], avg_error[oo+60*4], avg_error[oo+60*5], avg_error[oo+60*6], avg_error[oo+60*7], avg_error[oo+60*8], avg_error[oo+60*9]]
    std5 = [variance_error[oo+60*0],variance_error[oo+60*1],variance_error[oo+60*2],variance_error[oo+60*3],variance_error[oo+60*4],variance_error[oo+60*5],variance_error[oo+60*6],variance_error[oo+60*7],variance_error[oo+60*8],variance_error[oo+60*9]]

    oo=10*5+0+jj
    mean6 = [avg_error[oo+60*0], avg_error[oo+60*1], avg_error[oo+60*2], avg_error[oo+60*3], avg_error[oo+60*4], avg_error[oo+60*5], avg_error[oo+60*6], avg_error[oo+60*7], avg_error[oo+60*8], avg_error[oo+60*9]]
    std6 = [variance_error[oo+60*0],variance_error[oo+60*1],variance_error[oo+60*2],variance_error[oo+60*3],variance_error[oo+60*4],variance_error[oo+60*5],variance_error[oo+60*6],variance_error[oo+60*7],variance_error[oo+60*8],variance_error[oo+60*9]]


    yanse=colors[0]
    plt.plot(x1[2:], mean1[2:], color=yanse, alpha=0.3, linewidth=2*lineWidth, linestyle='--',zorder=2)
    plt.errorbar(x1[2:], mean1[2:], yerr=std1[2:], fmt='o', color=yanse, ecolor=yanse, capsize=8, elinewidth=4, markeredgewidth=4, label=legend1[0],zorder=2)

    yanse=colors[1]
    plt.plot(x1[2:], mean2[2:], color=yanse, alpha=0.3, linewidth=2*lineWidth, linestyle='--',zorder=2)
    plt.errorbar(x1[2:], mean2[2:], yerr=std2[2:], fmt='o', color=yanse, ecolor=yanse, capsize=8, elinewidth=4, markeredgewidth=4, label=legend1[1],zorder=2)

    yanse=colors[2]
    plt.plot(x1[2:], mean3[2:], color=yanse, alpha=0.3, linewidth=2*lineWidth, linestyle='--',zorder=2)
    plt.errorbar(x1[2:], mean3[2:], yerr=std3[2:], fmt='o', color=yanse, ecolor=yanse, capsize=8, elinewidth=4, markeredgewidth=4, label=legend1[2],zorder=2)

    yanse=colors[3]
    plt.plot(x1[2:], mean4[2:], color=yanse, alpha=0.3, linewidth=2*lineWidth, linestyle='--',zorder=2)
    plt.errorbar(x1[2:], mean4[2:], yerr=std4[2:], fmt='o', color=yanse, ecolor=yanse, capsize=8, elinewidth=4, markeredgewidth=4, label=legend1[3],zorder=2)

    yanse=colors[4]
    plt.plot(x1[2:], mean5[2:], color=yanse, alpha=0.3, linewidth=2*lineWidth, linestyle='--',zorder=2)
    plt.errorbar(x1[2:], mean5[2:], yerr=std5[2:], fmt='o', color=yanse, ecolor=yanse, capsize=8, elinewidth=4, markeredgewidth=4, label=legend1[4],zorder=2)
    
    yanse=colors[5]
    plt.plot(x1[2:], mean6[2:], color=yanse, alpha=0.3, linewidth=2*lineWidth, linestyle='--',zorder=2)
    plt.errorbar(x1[2:], mean6[2:], yerr=std6[2:], fmt='o', color=yanse, ecolor=yanse, capsize=8, elinewidth=4, markeredgewidth=4, label=legend1[5],zorder=2)   
    


    # Matplotlib 配置 - 全局字体设置为 STIXGeneral
    mpl.rc('font', family='STIXGeneral')
    # 创建图例
    #plt.title(r"Errorbar for Ek", fontsize=25, color='black', loc='center', pad=15)
    '''lgd = plt.legend(
        loc='upper right',       # 自动选择最优位置
        fontsize=25,
        frameon=True,
        framealpha=0,
        edgecolor='black',
        shadow=False
    )'''
    # 显示网格
    #plt.grid()
    figPath1 = os.path.abspath("./vel_k_errorbar_with_k/{}cases".format(case_number))
    gfile1 = "Errorbar for E(k=3-10) F-IFNO_label.png"
    gpath1 = os.path.join(figPath1, gfile1)
    # 保存图形
    plt.savefig(gpath1, bbox_inches='tight')
    plt.close()  


    
    ######----------------------------x=model----------------------------########
    # 图形参数设置
    dpi = 600
    width, height = 10, 6
    fontSize = 30
    lineWidth = 2
    boxWidth = 2.5
    Lmajor, Lminor = 7, 4
    xlabPad, ylabPad = 10, 10
    xlabel = r"$\mathdefault{k}$"
    ylabel = r"$\mathdefault{Error}$"
    xlimit=[0,0.42]
    #ylimit = [-0.18,0.04]
    legend = ["F-IFNO_constraint", "F-IUFNO_constraint", "IUFNO_constraint", "IFNO_constraint","F-IFNO", "F-IUFNO", "IUFNO", "IFNO","DSM","fDNS"]
    legend1 = [r"$\mathdefault{\Delta T=0.02\tau}$", r"$\mathdefault{\Delta T=0.04\tau}$",r"$\mathdefault{\Delta T=0.1\tau}$",r"$\mathdefault{\Delta T=0.2\tau}$",r"$\mathdefault{\Delta T=0.3\tau}$",r"$\mathdefault{\Delta T=0.4\tau}$"]
    colors = ['#A52A2A','#ff7f0e','gold','green','#1f77b4','#008080','purple','pink','#00FFFF','#FF00FF']
    fig = plt.figure(figsize=(width, height), dpi=dpi)
    plt.rcParams["font.size"] = fontSize
    plt.rcParams["axes.linewidth"] = lineWidth
    ax = fig.add_axes([0, 0, 1, 1])
    # X 轴设置
    ax.xaxis.set_minor_locator(mpl.ticker.MultipleLocator(1))        
    ax.xaxis.set_major_locator(mpl.ticker.MultipleLocator(1)) 
    ax.xaxis.set_major_formatter(mpl.ticker.FormatStrFormatter('%1.0f'))
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

    plt.xlabel(xlabel, fontsize=30)
    plt.ylabel(ylabel, fontsize=30)

    plt.xticks(fontsize=30)
    plt.yticks(fontsize=30)   

    # Matplotlib 配置
    mpl.rc('font', family='STIXGeneral')
    mpl.rc('text', usetex=False)
    mpl.rcParams['xtick.direction'] = 'in'
    mpl.rcParams['ytick.direction'] = 'in'
    plt.rcParams["mathtext.fontset"] = "cm"

    x1 = [1,2,3,4,5,6,7,8,9,10]
    jj=5
    
    oo=10*0+0+jj
    mean1 = [avg_error[oo+60*0], avg_error[oo+60*1], avg_error[oo+60*2], avg_error[oo+60*3], avg_error[oo+60*4], avg_error[oo+60*5], avg_error[oo+60*6], avg_error[oo+60*7], avg_error[oo+60*8], avg_error[oo+60*9]]
    std1 = [variance_error[oo+60*0],variance_error[oo+60*1],variance_error[oo+60*2],variance_error[oo+60*3],variance_error[oo+60*4],variance_error[oo+60*5],variance_error[oo+60*6],variance_error[oo+60*7],variance_error[oo+60*8],variance_error[oo+60*9]]
    
    oo=10*1+0+jj 
    mean2 = [avg_error[oo+60*0], avg_error[oo+60*1], avg_error[oo+60*2], avg_error[oo+60*3], avg_error[oo+60*4], avg_error[oo+60*5], avg_error[oo+60*6], avg_error[oo+60*7], avg_error[oo+60*8], avg_error[oo+60*9]]
    std2 = [variance_error[oo+60*0],variance_error[oo+60*1],variance_error[oo+60*2],variance_error[oo+60*3],variance_error[oo+60*4],variance_error[oo+60*5],variance_error[oo+60*6],variance_error[oo+60*7],variance_error[oo+60*8],variance_error[oo+60*9]]

    oo=10*2+0+jj
    mean3 = [avg_error[oo+60*0], avg_error[oo+60*1], avg_error[oo+60*2], avg_error[oo+60*3], avg_error[oo+60*4], avg_error[oo+60*5], avg_error[oo+60*6], avg_error[oo+60*7], avg_error[oo+60*8], avg_error[oo+60*9]]
    std3 = [variance_error[oo+60*0],variance_error[oo+60*1],variance_error[oo+60*2],variance_error[oo+60*3],variance_error[oo+60*4],variance_error[oo+60*5],variance_error[oo+60*6],variance_error[oo+60*7],variance_error[oo+60*8],variance_error[oo+60*9]]

    oo=10*3+0+jj
    mean4 = [avg_error[oo+60*0], avg_error[oo+60*1], avg_error[oo+60*2], avg_error[oo+60*3], avg_error[oo+60*4], avg_error[oo+60*5], avg_error[oo+60*6], avg_error[oo+60*7], avg_error[oo+60*8], avg_error[oo+60*9]]
    std4 = [variance_error[oo+60*0],variance_error[oo+60*1],variance_error[oo+60*2],variance_error[oo+60*3],variance_error[oo+60*4],variance_error[oo+60*5],variance_error[oo+60*6],variance_error[oo+60*7],variance_error[oo+60*8],variance_error[oo+60*9]]

    oo=10*4+0+jj
    mean5 = [avg_error[oo+60*0], avg_error[oo+60*1], avg_error[oo+60*2], avg_error[oo+60*3], avg_error[oo+60*4], avg_error[oo+60*5], avg_error[oo+60*6], avg_error[oo+60*7], avg_error[oo+60*8], avg_error[oo+60*9]]
    std5 = [variance_error[oo+60*0],variance_error[oo+60*1],variance_error[oo+60*2],variance_error[oo+60*3],variance_error[oo+60*4],variance_error[oo+60*5],variance_error[oo+60*6],variance_error[oo+60*7],variance_error[oo+60*8],variance_error[oo+60*9]]

    oo=10*5+0+jj
    mean6 = [avg_error[oo+60*0], avg_error[oo+60*1], avg_error[oo+60*2], avg_error[oo+60*3], avg_error[oo+60*4], avg_error[oo+60*5], avg_error[oo+60*6], avg_error[oo+60*7], avg_error[oo+60*8], avg_error[oo+60*9]]
    std6 = [variance_error[oo+60*0],variance_error[oo+60*1],variance_error[oo+60*2],variance_error[oo+60*3],variance_error[oo+60*4],variance_error[oo+60*5],variance_error[oo+60*6],variance_error[oo+60*7],variance_error[oo+60*8],variance_error[oo+60*9]]


    yanse=colors[0]
    plt.plot(x1[2:], mean1[2:], color=yanse, alpha=0.3, linewidth=2*lineWidth, linestyle='--',zorder=2)
    plt.errorbar(x1[2:], mean1[2:], yerr=std1[2:], fmt='o', color=yanse, ecolor=yanse, capsize=8, elinewidth=4, markeredgewidth=4, label=legend1[0],zorder=2)

    yanse=colors[1]
    plt.plot(x1[2:], mean2[2:], color=yanse, alpha=0.3, linewidth=2*lineWidth, linestyle='--',zorder=2)
    plt.errorbar(x1[2:], mean2[2:], yerr=std2[2:], fmt='o', color=yanse, ecolor=yanse, capsize=8, elinewidth=4, markeredgewidth=4, label=legend1[1],zorder=2)

    yanse=colors[2]
    plt.plot(x1[2:], mean3[2:], color=yanse, alpha=0.3, linewidth=2*lineWidth, linestyle='--',zorder=2)
    plt.errorbar(x1[2:], mean3[2:], yerr=std3[2:], fmt='o', color=yanse, ecolor=yanse, capsize=8, elinewidth=4, markeredgewidth=4, label=legend1[2],zorder=2)

    yanse=colors[3]
    plt.plot(x1[2:], mean4[2:], color=yanse, alpha=0.3, linewidth=2*lineWidth, linestyle='--',zorder=2)
    plt.errorbar(x1[2:], mean4[2:], yerr=std4[2:], fmt='o', color=yanse, ecolor=yanse, capsize=8, elinewidth=4, markeredgewidth=4, label=legend1[3],zorder=2)

    yanse=colors[4]
    plt.plot(x1[2:], mean5[2:], color=yanse, alpha=0.3, linewidth=2*lineWidth, linestyle='--',zorder=2)
    plt.errorbar(x1[2:], mean5[2:], yerr=std5[2:], fmt='o', color=yanse, ecolor=yanse, capsize=8, elinewidth=4, markeredgewidth=4, label=legend1[4],zorder=2)
    
    yanse=colors[5]
    plt.plot(x1[2:], mean6[2:], color=yanse, alpha=0.3, linewidth=2*lineWidth, linestyle='--',zorder=2)
    plt.errorbar(x1[2:], mean6[2:], yerr=std6[2:], fmt='o', color=yanse, ecolor=yanse, capsize=8, elinewidth=4, markeredgewidth=4, label=legend1[5],zorder=2)   
    


    # Matplotlib 配置 - 全局字体设置为 STIXGeneral
    mpl.rc('font', family='STIXGeneral')
    # 创建图例
    #plt.title(r"Errorbar for Ek", fontsize=25, color='black', loc='center', pad=15)
    '''lgd = plt.legend(
        loc='upper right',       # 自动选择最优位置
        fontsize=25,
        frameon=True,
        framealpha=0,
        edgecolor='black',
        shadow=False
    )'''
    # 显示网格
    #plt.grid()
    figPath1 = os.path.abspath("./vel_k_errorbar_with_k/{}cases".format(case_number))
    gfile1 = "Errorbar for E(k=3-10) F-IUFNO_label.png"
    gpath1 = os.path.join(figPath1, gfile1)
    # 保存图形
    plt.savefig(gpath1, bbox_inches='tight')
    plt.close()  



    ######----------------------------x=model----------------------------########
    # 图形参数设置
    dpi = 600
    width, height = 10, 6
    fontSize = 30
    lineWidth = 2
    boxWidth = 2.5
    Lmajor, Lminor = 7, 4
    xlabPad, ylabPad = 10, 10
    xlabel = r"$\mathdefault{k}$"
    ylabel = r"$\mathdefault{Error}$"
    xlimit=[0,0.42]
    #ylimit = [-0.18,0.04]
    legend = ["F-IFNO_constraint", "F-IUFNO_constraint", "IUFNO_constraint", "IFNO_constraint","F-IFNO", "F-IUFNO", "IUFNO", "IFNO","DSM","fDNS"]
    legend1 = [r"$\mathdefault{\Delta T=0.02\tau}$", r"$\mathdefault{\Delta T=0.04\tau}$",r"$\mathdefault{\Delta T=0.1\tau}$",r"$\mathdefault{\Delta T=0.2\tau}$",r"$\mathdefault{\Delta T=0.3\tau}$",r"$\mathdefault{\Delta T=0.4\tau}$"]
    colors = ['#A52A2A','#ff7f0e','gold','green','#1f77b4','#008080','purple','pink','#00FFFF','#FF00FF']
    fig = plt.figure(figsize=(width, height), dpi=dpi)
    plt.rcParams["font.size"] = fontSize
    plt.rcParams["axes.linewidth"] = lineWidth
    ax = fig.add_axes([0, 0, 1, 1])
    # X 轴设置
    ax.xaxis.set_minor_locator(mpl.ticker.MultipleLocator(1))        
    ax.xaxis.set_major_locator(mpl.ticker.MultipleLocator(1)) 
    ax.xaxis.set_major_formatter(mpl.ticker.FormatStrFormatter('%1.0f'))
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

    plt.xlabel(xlabel, fontsize=30)
    plt.ylabel(ylabel, fontsize=30)

    plt.xticks(fontsize=30)
    plt.yticks(fontsize=30)   

    # Matplotlib 配置
    mpl.rc('font', family='STIXGeneral')
    mpl.rc('text', usetex=False)
    mpl.rcParams['xtick.direction'] = 'in'
    mpl.rcParams['ytick.direction'] = 'in'
    plt.rcParams["mathtext.fontset"] = "cm"

    x1 = [1,2,3,4,5,6,7,8,9,10]
    jj=6
    
    oo=10*0+0+jj
    mean1 = [avg_error[oo+60*0], avg_error[oo+60*1], avg_error[oo+60*2], avg_error[oo+60*3], avg_error[oo+60*4], avg_error[oo+60*5], avg_error[oo+60*6], avg_error[oo+60*7], avg_error[oo+60*8], avg_error[oo+60*9]]
    std1 = [variance_error[oo+60*0],variance_error[oo+60*1],variance_error[oo+60*2],variance_error[oo+60*3],variance_error[oo+60*4],variance_error[oo+60*5],variance_error[oo+60*6],variance_error[oo+60*7],variance_error[oo+60*8],variance_error[oo+60*9]]
    
    oo=10*1+0+jj 
    mean2 = [avg_error[oo+60*0], avg_error[oo+60*1], avg_error[oo+60*2], avg_error[oo+60*3], avg_error[oo+60*4], avg_error[oo+60*5], avg_error[oo+60*6], avg_error[oo+60*7], avg_error[oo+60*8], avg_error[oo+60*9]]
    std2 = [variance_error[oo+60*0],variance_error[oo+60*1],variance_error[oo+60*2],variance_error[oo+60*3],variance_error[oo+60*4],variance_error[oo+60*5],variance_error[oo+60*6],variance_error[oo+60*7],variance_error[oo+60*8],variance_error[oo+60*9]]

    oo=10*2+0+jj
    mean3 = [avg_error[oo+60*0], avg_error[oo+60*1], avg_error[oo+60*2], avg_error[oo+60*3], avg_error[oo+60*4], avg_error[oo+60*5], avg_error[oo+60*6], avg_error[oo+60*7], avg_error[oo+60*8], avg_error[oo+60*9]]
    std3 = [variance_error[oo+60*0],variance_error[oo+60*1],variance_error[oo+60*2],variance_error[oo+60*3],variance_error[oo+60*4],variance_error[oo+60*5],variance_error[oo+60*6],variance_error[oo+60*7],variance_error[oo+60*8],variance_error[oo+60*9]]

    oo=10*3+0+jj
    mean4 = [avg_error[oo+60*0], avg_error[oo+60*1], avg_error[oo+60*2], avg_error[oo+60*3], avg_error[oo+60*4], avg_error[oo+60*5], avg_error[oo+60*6], avg_error[oo+60*7], avg_error[oo+60*8], avg_error[oo+60*9]]
    std4 = [variance_error[oo+60*0],variance_error[oo+60*1],variance_error[oo+60*2],variance_error[oo+60*3],variance_error[oo+60*4],variance_error[oo+60*5],variance_error[oo+60*6],variance_error[oo+60*7],variance_error[oo+60*8],variance_error[oo+60*9]]

    oo=10*4+0+jj
    mean5 = [avg_error[oo+60*0], avg_error[oo+60*1], avg_error[oo+60*2], avg_error[oo+60*3], avg_error[oo+60*4], avg_error[oo+60*5], avg_error[oo+60*6], avg_error[oo+60*7], avg_error[oo+60*8], avg_error[oo+60*9]]
    std5 = [variance_error[oo+60*0],variance_error[oo+60*1],variance_error[oo+60*2],variance_error[oo+60*3],variance_error[oo+60*4],variance_error[oo+60*5],variance_error[oo+60*6],variance_error[oo+60*7],variance_error[oo+60*8],variance_error[oo+60*9]]

    oo=10*5+0+jj
    mean6 = [avg_error[oo+60*0], avg_error[oo+60*1], avg_error[oo+60*2], avg_error[oo+60*3], avg_error[oo+60*4], avg_error[oo+60*5], avg_error[oo+60*6], avg_error[oo+60*7], avg_error[oo+60*8], avg_error[oo+60*9]]
    std6 = [variance_error[oo+60*0],variance_error[oo+60*1],variance_error[oo+60*2],variance_error[oo+60*3],variance_error[oo+60*4],variance_error[oo+60*5],variance_error[oo+60*6],variance_error[oo+60*7],variance_error[oo+60*8],variance_error[oo+60*9]]


    yanse=colors[0]
    plt.plot(x1[2:], mean1[2:], color=yanse, alpha=0.3, linewidth=2*lineWidth, linestyle='--',zorder=2)
    plt.errorbar(x1[2:], mean1[2:], yerr=std1[2:], fmt='o', color=yanse, ecolor=yanse, capsize=8, elinewidth=4, markeredgewidth=4, label=legend1[0],zorder=2)

    yanse=colors[1]
    plt.plot(x1[2:], mean2[2:], color=yanse, alpha=0.3, linewidth=2*lineWidth, linestyle='--',zorder=2)
    plt.errorbar(x1[2:], mean2[2:], yerr=std2[2:], fmt='o', color=yanse, ecolor=yanse, capsize=8, elinewidth=4, markeredgewidth=4, label=legend1[1],zorder=2)

    yanse=colors[2]
    plt.plot(x1[2:], mean3[2:], color=yanse, alpha=0.3, linewidth=2*lineWidth, linestyle='--',zorder=2)
    plt.errorbar(x1[2:], mean3[2:], yerr=std3[2:], fmt='o', color=yanse, ecolor=yanse, capsize=8, elinewidth=4, markeredgewidth=4, label=legend1[2],zorder=2)

    yanse=colors[3]
    plt.plot(x1[2:], mean4[2:], color=yanse, alpha=0.3, linewidth=2*lineWidth, linestyle='--',zorder=2)
    plt.errorbar(x1[2:], mean4[2:], yerr=std4[2:], fmt='o', color=yanse, ecolor=yanse, capsize=8, elinewidth=4, markeredgewidth=4, label=legend1[3],zorder=2)

    yanse=colors[4]
    plt.plot(x1[2:], mean5[2:], color=yanse, alpha=0.3, linewidth=2*lineWidth, linestyle='--',zorder=2)
    plt.errorbar(x1[2:], mean5[2:], yerr=std5[2:], fmt='o', color=yanse, ecolor=yanse, capsize=8, elinewidth=4, markeredgewidth=4, label=legend1[4],zorder=2)
    
    yanse=colors[5]
    plt.plot(x1[2:], mean6[2:], color=yanse, alpha=0.3, linewidth=2*lineWidth, linestyle='--',zorder=2)
    plt.errorbar(x1[2:], mean6[2:], yerr=std6[2:], fmt='o', color=yanse, ecolor=yanse, capsize=8, elinewidth=4, markeredgewidth=4, label=legend1[5],zorder=2)   
    


    # Matplotlib 配置 - 全局字体设置为 STIXGeneral
    mpl.rc('font', family='STIXGeneral')
    # 创建图例
    #plt.title(r"Errorbar for Ek", fontsize=25, color='black', loc='center', pad=15)
    '''lgd = plt.legend(
        loc='upper right',       # 自动选择最优位置
        fontsize=25,
        frameon=True,
        framealpha=0,
        edgecolor='black',
        shadow=False
    )'''
    # 显示网格
    #plt.grid()
    figPath1 = os.path.abspath("./vel_k_errorbar_with_k/{}cases".format(case_number))
    gfile1 = "Errorbar for E(k=3-10) IUFNO_label.png"
    gpath1 = os.path.join(figPath1, gfile1)
    # 保存图形
    plt.savefig(gpath1, bbox_inches='tight')
    plt.close()


    ######----------------------------x=model----------------------------########
    # 图形参数设置
    dpi = 600
    width, height = 10, 6
    fontSize = 30
    lineWidth = 2
    boxWidth = 2.5
    Lmajor, Lminor = 7, 4
    xlabPad, ylabPad = 10, 10
    xlabel = r"$\mathdefault{k}$"
    ylabel = r"$\mathdefault{Error}$"
    xlimit=[0,0.42]
    #ylimit = [-0.18,0.04]
    legend = ["F-IFNO_constraint", "F-IUFNO_constraint", "IUFNO_constraint", "IFNO_constraint","F-IFNO", "F-IUFNO", "IUFNO", "IFNO","DSM","fDNS"]
    legend1 = [r"$\mathdefault{\Delta T=0.02\tau}$", r"$\mathdefault{\Delta T=0.04\tau}$",r"$\mathdefault{\Delta T=0.1\tau}$",r"$\mathdefault{\Delta T=0.2\tau}$",r"$\mathdefault{\Delta T=0.3\tau}$",r"$\mathdefault{\Delta T=0.4\tau}$"]
    colors = ['#A52A2A','#ff7f0e','gold','green','#1f77b4','#008080','purple','pink','#00FFFF','#FF00FF']
    fig = plt.figure(figsize=(width, height), dpi=dpi)
    plt.rcParams["font.size"] = fontSize
    plt.rcParams["axes.linewidth"] = lineWidth
    ax = fig.add_axes([0, 0, 1, 1])
    # X 轴设置
    ax.xaxis.set_minor_locator(mpl.ticker.MultipleLocator(1))        
    ax.xaxis.set_major_locator(mpl.ticker.MultipleLocator(1)) 
    ax.xaxis.set_major_formatter(mpl.ticker.FormatStrFormatter('%1.0f'))
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

    plt.xlabel(xlabel, fontsize=30)
    plt.ylabel(ylabel, fontsize=30)

    plt.xticks(fontsize=30)
    plt.yticks(fontsize=30)   

    # Matplotlib 配置
    mpl.rc('font', family='STIXGeneral')
    mpl.rc('text', usetex=False)
    mpl.rcParams['xtick.direction'] = 'in'
    mpl.rcParams['ytick.direction'] = 'in'
    plt.rcParams["mathtext.fontset"] = "cm"

    x1 = [1,2,3,4,5,6,7,8,9,10]
    jj=7
    
    oo=10*0+0+jj
    mean1 = [avg_error[oo+60*0], avg_error[oo+60*1], avg_error[oo+60*2], avg_error[oo+60*3], avg_error[oo+60*4], avg_error[oo+60*5], avg_error[oo+60*6], avg_error[oo+60*7], avg_error[oo+60*8], avg_error[oo+60*9]]
    std1 = [variance_error[oo+60*0],variance_error[oo+60*1],variance_error[oo+60*2],variance_error[oo+60*3],variance_error[oo+60*4],variance_error[oo+60*5],variance_error[oo+60*6],variance_error[oo+60*7],variance_error[oo+60*8],variance_error[oo+60*9]]
    
    oo=10*1+0+jj 
    mean2 = [avg_error[oo+60*0], avg_error[oo+60*1], avg_error[oo+60*2], avg_error[oo+60*3], avg_error[oo+60*4], avg_error[oo+60*5], avg_error[oo+60*6], avg_error[oo+60*7], avg_error[oo+60*8], avg_error[oo+60*9]]
    std2 = [variance_error[oo+60*0],variance_error[oo+60*1],variance_error[oo+60*2],variance_error[oo+60*3],variance_error[oo+60*4],variance_error[oo+60*5],variance_error[oo+60*6],variance_error[oo+60*7],variance_error[oo+60*8],variance_error[oo+60*9]]

    oo=10*2+0+jj
    mean3 = [avg_error[oo+60*0], avg_error[oo+60*1], avg_error[oo+60*2], avg_error[oo+60*3], avg_error[oo+60*4], avg_error[oo+60*5], avg_error[oo+60*6], avg_error[oo+60*7], avg_error[oo+60*8], avg_error[oo+60*9]]
    std3 = [variance_error[oo+60*0],variance_error[oo+60*1],variance_error[oo+60*2],variance_error[oo+60*3],variance_error[oo+60*4],variance_error[oo+60*5],variance_error[oo+60*6],variance_error[oo+60*7],variance_error[oo+60*8],variance_error[oo+60*9]]

    oo=10*3+0+jj
    mean4 = [avg_error[oo+60*0], avg_error[oo+60*1], avg_error[oo+60*2], avg_error[oo+60*3], avg_error[oo+60*4], avg_error[oo+60*5], avg_error[oo+60*6], avg_error[oo+60*7], avg_error[oo+60*8], avg_error[oo+60*9]]
    std4 = [variance_error[oo+60*0],variance_error[oo+60*1],variance_error[oo+60*2],variance_error[oo+60*3],variance_error[oo+60*4],variance_error[oo+60*5],variance_error[oo+60*6],variance_error[oo+60*7],variance_error[oo+60*8],variance_error[oo+60*9]]

    oo=10*4+0+jj
    mean5 = [avg_error[oo+60*0], avg_error[oo+60*1], avg_error[oo+60*2], avg_error[oo+60*3], avg_error[oo+60*4], avg_error[oo+60*5], avg_error[oo+60*6], avg_error[oo+60*7], avg_error[oo+60*8], avg_error[oo+60*9]]
    std5 = [variance_error[oo+60*0],variance_error[oo+60*1],variance_error[oo+60*2],variance_error[oo+60*3],variance_error[oo+60*4],variance_error[oo+60*5],variance_error[oo+60*6],variance_error[oo+60*7],variance_error[oo+60*8],variance_error[oo+60*9]]

    oo=10*5+0+jj
    mean6 = [avg_error[oo+60*0], avg_error[oo+60*1], avg_error[oo+60*2], avg_error[oo+60*3], avg_error[oo+60*4], avg_error[oo+60*5], avg_error[oo+60*6], avg_error[oo+60*7], avg_error[oo+60*8], avg_error[oo+60*9]]
    std6 = [variance_error[oo+60*0],variance_error[oo+60*1],variance_error[oo+60*2],variance_error[oo+60*3],variance_error[oo+60*4],variance_error[oo+60*5],variance_error[oo+60*6],variance_error[oo+60*7],variance_error[oo+60*8],variance_error[oo+60*9]]


    yanse=colors[0]
    plt.plot(x1[2:], mean1[2:], color=yanse, alpha=0.3, linewidth=2*lineWidth, linestyle='--',zorder=2)
    plt.errorbar(x1[2:], mean1[2:], yerr=std1[2:], fmt='o', color=yanse, ecolor=yanse, capsize=8, elinewidth=4, markeredgewidth=4, label=legend1[0],zorder=2)

    yanse=colors[1]
    plt.plot(x1[2:], mean2[2:], color=yanse, alpha=0.3, linewidth=2*lineWidth, linestyle='--',zorder=2)
    plt.errorbar(x1[2:], mean2[2:], yerr=std2[2:], fmt='o', color=yanse, ecolor=yanse, capsize=8, elinewidth=4, markeredgewidth=4, label=legend1[1],zorder=2)

    yanse=colors[2]
    plt.plot(x1[2:], mean3[2:], color=yanse, alpha=0.3, linewidth=2*lineWidth, linestyle='--',zorder=2)
    plt.errorbar(x1[2:], mean3[2:], yerr=std3[2:], fmt='o', color=yanse, ecolor=yanse, capsize=8, elinewidth=4, markeredgewidth=4, label=legend1[2],zorder=2)

    yanse=colors[3]
    plt.plot(x1[2:], mean4[2:], color=yanse, alpha=0.3, linewidth=2*lineWidth, linestyle='--',zorder=2)
    plt.errorbar(x1[2:], mean4[2:], yerr=std4[2:], fmt='o', color=yanse, ecolor=yanse, capsize=8, elinewidth=4, markeredgewidth=4, label=legend1[3],zorder=2)

    yanse=colors[4]
    plt.plot(x1[2:], mean5[2:], color=yanse, alpha=0.3, linewidth=2*lineWidth, linestyle='--',zorder=2)
    plt.errorbar(x1[2:], mean5[2:], yerr=std5[2:], fmt='o', color=yanse, ecolor=yanse, capsize=8, elinewidth=4, markeredgewidth=4, label=legend1[4],zorder=2)
    
    yanse=colors[5]
    plt.plot(x1[2:], mean6[2:], color=yanse, alpha=0.3, linewidth=2*lineWidth, linestyle='--',zorder=2)
    plt.errorbar(x1[2:], mean6[2:], yerr=std6[2:], fmt='o', color=yanse, ecolor=yanse, capsize=8, elinewidth=4, markeredgewidth=4, label=legend1[5],zorder=2)   
    


    # Matplotlib 配置 - 全局字体设置为 STIXGeneral
    mpl.rc('font', family='STIXGeneral')
    # 创建图例
    #plt.title(r"Errorbar for Ek", fontsize=25, color='black', loc='center', pad=15)
    '''lgd = plt.legend(
        loc='upper right',       # 自动选择最优位置
        fontsize=25,
        frameon=True,
        framealpha=0,
        edgecolor='black',
        shadow=False
    )'''
    # 显示网格
    #plt.grid()
    figPath1 = os.path.abspath("./vel_k_errorbar_with_k/{}cases".format(case_number))
    gfile1 = "Errorbar for E(k=3-10) IFNO_label.png"
    gpath1 = os.path.join(figPath1, gfile1)
    # 保存图形
    plt.savefig(gpath1, bbox_inches='tight')
    plt.close()


    ######----------------------------x=model----------------------------########
    # 图形参数设置
    dpi = 600
    width, height = 10, 6
    fontSize = 30
    lineWidth = 2
    boxWidth = 2.5
    Lmajor, Lminor = 7, 4
    xlabPad, ylabPad = 10, 10
    xlabel = r"$\mathdefault{k}$"
    ylabel = r"$\mathdefault{Error}$"
    xlimit=[0,0.42]
    #ylimit = [-0.18,0.04]
    legend = ["F-IFNO_constraint", "F-IUFNO_constraint", "IUFNO_constraint", "IFNO_constraint","F-IFNO", "F-IUFNO", "IUFNO", "IFNO","DSM","fDNS"]
    legend1 = [r"$\mathdefault{\Delta T=0.02\tau}$", r"$\mathdefault{\Delta T=0.04\tau}$",r"$\mathdefault{\Delta T=0.1\tau}$",r"$\mathdefault{\Delta T=0.2\tau}$",r"$\mathdefault{\Delta T=0.3\tau}$",r"$\mathdefault{\Delta T=0.4\tau}$"]
    colors = ['#A52A2A','#ff7f0e','gold','green','#1f77b4','#008080','purple','pink','#00FFFF','#FF00FF']
    fig = plt.figure(figsize=(width, height), dpi=dpi)
    plt.rcParams["font.size"] = fontSize
    plt.rcParams["axes.linewidth"] = lineWidth
    ax = fig.add_axes([0, 0, 1, 1])
    # X 轴设置
    ax.xaxis.set_minor_locator(mpl.ticker.MultipleLocator(1))        
    ax.xaxis.set_major_locator(mpl.ticker.MultipleLocator(1)) 
    ax.xaxis.set_major_formatter(mpl.ticker.FormatStrFormatter('%1.0f'))
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

    plt.xlabel(xlabel, fontsize=30)
    plt.ylabel(ylabel, fontsize=30)

    plt.xticks(fontsize=30)
    plt.yticks(fontsize=30)   

    # Matplotlib 配置
    mpl.rc('font', family='STIXGeneral')
    mpl.rc('text', usetex=False)
    mpl.rcParams['xtick.direction'] = 'in'
    mpl.rcParams['ytick.direction'] = 'in'
    plt.rcParams["mathtext.fontset"] = "cm"

    x1 = [1,2,3,4,5,6,7,8,9,10]
    jj=8
    
    oo=10*0+0+jj
    mean1 = [avg_error[oo+60*0], avg_error[oo+60*1], avg_error[oo+60*2], avg_error[oo+60*3], avg_error[oo+60*4], avg_error[oo+60*5], avg_error[oo+60*6], avg_error[oo+60*7], avg_error[oo+60*8], avg_error[oo+60*9]]
    std1 = [variance_error[oo+60*0],variance_error[oo+60*1],variance_error[oo+60*2],variance_error[oo+60*3],variance_error[oo+60*4],variance_error[oo+60*5],variance_error[oo+60*6],variance_error[oo+60*7],variance_error[oo+60*8],variance_error[oo+60*9]]
    
    oo=10*1+0+jj 
    mean2 = [avg_error[oo+60*0], avg_error[oo+60*1], avg_error[oo+60*2], avg_error[oo+60*3], avg_error[oo+60*4], avg_error[oo+60*5], avg_error[oo+60*6], avg_error[oo+60*7], avg_error[oo+60*8], avg_error[oo+60*9]]
    std2 = [variance_error[oo+60*0],variance_error[oo+60*1],variance_error[oo+60*2],variance_error[oo+60*3],variance_error[oo+60*4],variance_error[oo+60*5],variance_error[oo+60*6],variance_error[oo+60*7],variance_error[oo+60*8],variance_error[oo+60*9]]

    oo=10*2+0+jj
    mean3 = [avg_error[oo+60*0], avg_error[oo+60*1], avg_error[oo+60*2], avg_error[oo+60*3], avg_error[oo+60*4], avg_error[oo+60*5], avg_error[oo+60*6], avg_error[oo+60*7], avg_error[oo+60*8], avg_error[oo+60*9]]
    std3 = [variance_error[oo+60*0],variance_error[oo+60*1],variance_error[oo+60*2],variance_error[oo+60*3],variance_error[oo+60*4],variance_error[oo+60*5],variance_error[oo+60*6],variance_error[oo+60*7],variance_error[oo+60*8],variance_error[oo+60*9]]

    oo=10*3+0+jj
    mean4 = [avg_error[oo+60*0], avg_error[oo+60*1], avg_error[oo+60*2], avg_error[oo+60*3], avg_error[oo+60*4], avg_error[oo+60*5], avg_error[oo+60*6], avg_error[oo+60*7], avg_error[oo+60*8], avg_error[oo+60*9]]
    std4 = [variance_error[oo+60*0],variance_error[oo+60*1],variance_error[oo+60*2],variance_error[oo+60*3],variance_error[oo+60*4],variance_error[oo+60*5],variance_error[oo+60*6],variance_error[oo+60*7],variance_error[oo+60*8],variance_error[oo+60*9]]

    oo=10*4+0+jj
    mean5 = [avg_error[oo+60*0], avg_error[oo+60*1], avg_error[oo+60*2], avg_error[oo+60*3], avg_error[oo+60*4], avg_error[oo+60*5], avg_error[oo+60*6], avg_error[oo+60*7], avg_error[oo+60*8], avg_error[oo+60*9]]
    std5 = [variance_error[oo+60*0],variance_error[oo+60*1],variance_error[oo+60*2],variance_error[oo+60*3],variance_error[oo+60*4],variance_error[oo+60*5],variance_error[oo+60*6],variance_error[oo+60*7],variance_error[oo+60*8],variance_error[oo+60*9]]

    oo=10*5+0+jj
    mean6 = [avg_error[oo+60*0], avg_error[oo+60*1], avg_error[oo+60*2], avg_error[oo+60*3], avg_error[oo+60*4], avg_error[oo+60*5], avg_error[oo+60*6], avg_error[oo+60*7], avg_error[oo+60*8], avg_error[oo+60*9]]
    std6 = [variance_error[oo+60*0],variance_error[oo+60*1],variance_error[oo+60*2],variance_error[oo+60*3],variance_error[oo+60*4],variance_error[oo+60*5],variance_error[oo+60*6],variance_error[oo+60*7],variance_error[oo+60*8],variance_error[oo+60*9]]


    yanse=colors[0]
    plt.plot(x1[2:], mean1[2:], color=yanse, alpha=0.3, linewidth=2*lineWidth, linestyle='--',zorder=2)
    plt.errorbar(x1[2:], mean1[2:], yerr=std1[2:], fmt='o', color=yanse, ecolor=yanse, capsize=8, elinewidth=4, markeredgewidth=4, label=legend1[0],zorder=2)

    yanse=colors[1]
    plt.plot(x1[2:], mean2[2:], color=yanse, alpha=0.3, linewidth=2*lineWidth, linestyle='--',zorder=2)
    plt.errorbar(x1[2:], mean2[2:], yerr=std2[2:], fmt='o', color=yanse, ecolor=yanse, capsize=8, elinewidth=4, markeredgewidth=4, label=legend1[1],zorder=2)

    yanse=colors[2]
    plt.plot(x1[2:], mean3[2:], color=yanse, alpha=0.3, linewidth=2*lineWidth, linestyle='--',zorder=2)
    plt.errorbar(x1[2:], mean3[2:], yerr=std3[2:], fmt='o', color=yanse, ecolor=yanse, capsize=8, elinewidth=4, markeredgewidth=4, label=legend1[2],zorder=2)

    yanse=colors[3]
    plt.plot(x1[2:], mean4[2:], color=yanse, alpha=0.3, linewidth=2*lineWidth, linestyle='--',zorder=2)
    plt.errorbar(x1[2:], mean4[2:], yerr=std4[2:], fmt='o', color=yanse, ecolor=yanse, capsize=8, elinewidth=4, markeredgewidth=4, label=legend1[3],zorder=2)

    yanse=colors[4]
    plt.plot(x1[2:], mean5[2:], color=yanse, alpha=0.3, linewidth=2*lineWidth, linestyle='--',zorder=2)
    plt.errorbar(x1[2:], mean5[2:], yerr=std5[2:], fmt='o', color=yanse, ecolor=yanse, capsize=8, elinewidth=4, markeredgewidth=4, label=legend1[4],zorder=2)
    
    yanse=colors[5]
    plt.plot(x1[2:], mean6[2:], color=yanse, alpha=0.3, linewidth=2*lineWidth, linestyle='--',zorder=2)
    plt.errorbar(x1[2:], mean6[2:], yerr=std6[2:], fmt='o', color=yanse, ecolor=yanse, capsize=8, elinewidth=4, markeredgewidth=4, label=legend1[5],zorder=2)   
    


    # Matplotlib 配置 - 全局字体设置为 STIXGeneral
    mpl.rc('font', family='STIXGeneral')
    # 创建图例
    #plt.title(r"Errorbar for Ek", fontsize=25, color='black', loc='center', pad=15)
    '''lgd = plt.legend(
        loc='upper right',       # 自动选择最优位置
        fontsize=25,
        frameon=True,
        framealpha=0,
        edgecolor='black',
        shadow=False
    )'''
    # 显示网格
    #plt.grid()
    figPath1 = os.path.abspath("./vel_k_errorbar_with_k/{}cases".format(case_number))
    gfile1 = "Errorbar for E(k=3-10) DSM_label.png"
    gpath1 = os.path.join(figPath1, gfile1)
    # 保存图形
    plt.savefig(gpath1, bbox_inches='tight')
    plt.close()




    ######----------------------------x=model----------------------------########
    # 图形参数设置
    dpi = 600
    width, height = 10, 6
    fontSize = 30
    lineWidth = 2
    boxWidth = 2.5
    Lmajor, Lminor = 7, 4
    xlabPad, ylabPad = 10, 10
    xlabel = r"$\mathdefault{k}$"
    ylabel = r"$\mathdefault{Error}$"
    xlimit=[0,0.42]
    #ylimit = [-0.18,0.04]
    legend = ["F-IFNO_constraint", "F-IUFNO_constraint", "IUFNO_constraint", "IFNO_constraint","F-IFNO", "F-IUFNO", "IUFNO", "IFNO","DSM","fDNS"]
    legend1 = [r"$\mathdefault{\Delta T=0.02\tau}$", r"$\mathdefault{\Delta T=0.04\tau}$",r"$\mathdefault{\Delta T=0.1\tau}$",r"$\mathdefault{\Delta T=0.2\tau}$",r"$\mathdefault{\Delta T=0.3\tau}$",r"$\mathdefault{\Delta T=0.4\tau}$"]
    colors = ['#A52A2A','#ff7f0e','gold','green','#1f77b4','#008080','purple','pink','#00FFFF','#FF00FF']
    fig = plt.figure(figsize=(width, height), dpi=dpi)
    plt.rcParams["font.size"] = fontSize
    plt.rcParams["axes.linewidth"] = lineWidth
    ax = fig.add_axes([0, 0, 1, 1])
    # X 轴设置
    ax.xaxis.set_minor_locator(mpl.ticker.MultipleLocator(1))        
    ax.xaxis.set_major_locator(mpl.ticker.MultipleLocator(1)) 
    ax.xaxis.set_major_formatter(mpl.ticker.FormatStrFormatter('%1.0f'))
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

    plt.xlabel(xlabel, fontsize=30)
    plt.ylabel(ylabel, fontsize=30)

    plt.xticks(fontsize=30)
    plt.yticks(fontsize=30)   

    # Matplotlib 配置
    mpl.rc('font', family='STIXGeneral')
    mpl.rc('text', usetex=False)
    mpl.rcParams['xtick.direction'] = 'in'
    mpl.rcParams['ytick.direction'] = 'in'
    plt.rcParams["mathtext.fontset"] = "cm"

    x1 = [1,2,3,4,5,6,7,8,9,10]
    jj=9
    
    oo=10*0+0+jj
    mean1 = [avg_error[oo+60*0], avg_error[oo+60*1], avg_error[oo+60*2], avg_error[oo+60*3], avg_error[oo+60*4], avg_error[oo+60*5], avg_error[oo+60*6], avg_error[oo+60*7], avg_error[oo+60*8], avg_error[oo+60*9]]
    std1 = [variance_error[oo+60*0],variance_error[oo+60*1],variance_error[oo+60*2],variance_error[oo+60*3],variance_error[oo+60*4],variance_error[oo+60*5],variance_error[oo+60*6],variance_error[oo+60*7],variance_error[oo+60*8],variance_error[oo+60*9]]
    
    oo=10*1+0+jj 
    mean2 = [avg_error[oo+60*0], avg_error[oo+60*1], avg_error[oo+60*2], avg_error[oo+60*3], avg_error[oo+60*4], avg_error[oo+60*5], avg_error[oo+60*6], avg_error[oo+60*7], avg_error[oo+60*8], avg_error[oo+60*9]]
    std2 = [variance_error[oo+60*0],variance_error[oo+60*1],variance_error[oo+60*2],variance_error[oo+60*3],variance_error[oo+60*4],variance_error[oo+60*5],variance_error[oo+60*6],variance_error[oo+60*7],variance_error[oo+60*8],variance_error[oo+60*9]]

    oo=10*2+0+jj
    mean3 = [avg_error[oo+60*0], avg_error[oo+60*1], avg_error[oo+60*2], avg_error[oo+60*3], avg_error[oo+60*4], avg_error[oo+60*5], avg_error[oo+60*6], avg_error[oo+60*7], avg_error[oo+60*8], avg_error[oo+60*9]]
    std3 = [variance_error[oo+60*0],variance_error[oo+60*1],variance_error[oo+60*2],variance_error[oo+60*3],variance_error[oo+60*4],variance_error[oo+60*5],variance_error[oo+60*6],variance_error[oo+60*7],variance_error[oo+60*8],variance_error[oo+60*9]]

    oo=10*3+0+jj
    mean4 = [avg_error[oo+60*0], avg_error[oo+60*1], avg_error[oo+60*2], avg_error[oo+60*3], avg_error[oo+60*4], avg_error[oo+60*5], avg_error[oo+60*6], avg_error[oo+60*7], avg_error[oo+60*8], avg_error[oo+60*9]]
    std4 = [variance_error[oo+60*0],variance_error[oo+60*1],variance_error[oo+60*2],variance_error[oo+60*3],variance_error[oo+60*4],variance_error[oo+60*5],variance_error[oo+60*6],variance_error[oo+60*7],variance_error[oo+60*8],variance_error[oo+60*9]]

    oo=10*4+0+jj
    mean5 = [avg_error[oo+60*0], avg_error[oo+60*1], avg_error[oo+60*2], avg_error[oo+60*3], avg_error[oo+60*4], avg_error[oo+60*5], avg_error[oo+60*6], avg_error[oo+60*7], avg_error[oo+60*8], avg_error[oo+60*9]]
    std5 = [variance_error[oo+60*0],variance_error[oo+60*1],variance_error[oo+60*2],variance_error[oo+60*3],variance_error[oo+60*4],variance_error[oo+60*5],variance_error[oo+60*6],variance_error[oo+60*7],variance_error[oo+60*8],variance_error[oo+60*9]]

    oo=10*5+0+jj
    mean6 = [avg_error[oo+60*0], avg_error[oo+60*1], avg_error[oo+60*2], avg_error[oo+60*3], avg_error[oo+60*4], avg_error[oo+60*5], avg_error[oo+60*6], avg_error[oo+60*7], avg_error[oo+60*8], avg_error[oo+60*9]]
    std6 = [variance_error[oo+60*0],variance_error[oo+60*1],variance_error[oo+60*2],variance_error[oo+60*3],variance_error[oo+60*4],variance_error[oo+60*5],variance_error[oo+60*6],variance_error[oo+60*7],variance_error[oo+60*8],variance_error[oo+60*9]]


    yanse=colors[0]
    plt.plot(x1[2:], mean1[2:], color=yanse, alpha=0.3, linewidth=2*lineWidth, linestyle='--',zorder=2)
    plt.errorbar(x1[2:], mean1[2:], yerr=std1[2:], fmt='o', color=yanse, ecolor=yanse, capsize=8, elinewidth=4, markeredgewidth=4, label=legend1[0],zorder=2)

    yanse=colors[1]
    plt.plot(x1[2:], mean2[2:], color=yanse, alpha=0.3, linewidth=2*lineWidth, linestyle='--',zorder=2)
    plt.errorbar(x1[2:], mean2[2:], yerr=std2[2:], fmt='o', color=yanse, ecolor=yanse, capsize=8, elinewidth=4, markeredgewidth=4, label=legend1[1],zorder=2)

    yanse=colors[2]
    plt.plot(x1[2:], mean3[2:], color=yanse, alpha=0.3, linewidth=2*lineWidth, linestyle='--',zorder=2)
    plt.errorbar(x1[2:], mean3[2:], yerr=std3[2:], fmt='o', color=yanse, ecolor=yanse, capsize=8, elinewidth=4, markeredgewidth=4, label=legend1[2],zorder=2)

    yanse=colors[3]
    plt.plot(x1[2:], mean4[2:], color=yanse, alpha=0.3, linewidth=2*lineWidth, linestyle='--',zorder=2)
    plt.errorbar(x1[2:], mean4[2:], yerr=std4[2:], fmt='o', color=yanse, ecolor=yanse, capsize=8, elinewidth=4, markeredgewidth=4, label=legend1[3],zorder=2)

    yanse=colors[4]
    plt.plot(x1[2:], mean5[2:], color=yanse, alpha=0.3, linewidth=2*lineWidth, linestyle='--',zorder=2)
    plt.errorbar(x1[2:], mean5[2:], yerr=std5[2:], fmt='o', color=yanse, ecolor=yanse, capsize=8, elinewidth=4, markeredgewidth=4, label=legend1[4],zorder=2)
    
    yanse=colors[5]
    plt.plot(x1[2:], mean6[2:], color=yanse, alpha=0.3, linewidth=2*lineWidth, linestyle='--',zorder=2)
    plt.errorbar(x1[2:], mean6[2:], yerr=std6[2:], fmt='o', color=yanse, ecolor=yanse, capsize=8, elinewidth=4, markeredgewidth=4, label=legend1[5],zorder=2)   
    


    # Matplotlib 配置 - 全局字体设置为 STIXGeneral
    mpl.rc('font', family='STIXGeneral')
    # 创建图例
    #plt.title(r"Errorbar for Ek", fontsize=25, color='black', loc='center', pad=15)
    '''lgd = plt.legend(
        loc='upper right',       # 自动选择最优位置
        fontsize=25,
        frameon=True,
        framealpha=0,
        edgecolor='black',
        shadow=False
    )'''
    # 显示网格
    #plt.grid()
    figPath1 = os.path.abspath("./vel_k_errorbar_with_k/{}cases".format(case_number))
    gfile1 = "Errorbar for E(k=3-10) fDNS_label.png"
    gpath1 = os.path.join(figPath1, gfile1)
    # 保存图形
    plt.savefig(gpath1, bbox_inches='tight')
    plt.close()















  
    
    
    
    
 