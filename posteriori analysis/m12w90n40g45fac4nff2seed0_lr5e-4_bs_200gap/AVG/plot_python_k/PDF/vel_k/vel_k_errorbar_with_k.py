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
period = 10 #10个波数

for kk, case_number in enumerate(case_number_list):

    avg_results = []
    avg_error = []
    variance_error = []
    
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


        print(len(avg_error))#340


    ######----------------------------x=k----------------------------########

    x1 = [1,2,3,4,5,6,7,8,9,10]
    h=1
    mean1_F_IFNO = [avg_error[(h-1)+6*0], avg_error[(h-1)+6*1], avg_error[(h-1)+6*2], avg_error[(h-1)+6*3], avg_error[(h-1)+6*4], avg_error[(h-1)+6*5], avg_error[(h-1)+6*6], avg_error[(h-1)+6*7], avg_error[(h-1)+6*8], avg_error[(h-1)+6*9]]
    std1_F_IFNO = [variance_error[(h-1)+6*0],variance_error[(h-1)+6*1],variance_error[(h-1)+6*2],variance_error[(h-1)+6*3],variance_error[(h-1)+6*4],variance_error[(h-1)+6*5],variance_error[(h-1)+6*6],variance_error[(h-1)+6*7],variance_error[(h-1)+6*8],variance_error[(h-1)+6*9]]

    h=2
    mean1_F_IUFNO_40ep = [avg_error[(h-1)+6*0], avg_error[(h-1)+6*1], avg_error[(h-1)+6*2], avg_error[(h-1)+6*3], avg_error[(h-1)+6*4], avg_error[(h-1)+6*5], avg_error[(h-1)+6*6], avg_error[(h-1)+6*7], avg_error[(h-1)+6*8], avg_error[(h-1)+6*9]]
    std1_F_IUFNO_40ep = [variance_error[(h-1)+6*0],variance_error[(h-1)+6*1],variance_error[(h-1)+6*2],variance_error[(h-1)+6*3],variance_error[(h-1)+6*4],variance_error[(h-1)+6*5],variance_error[(h-1)+6*6],variance_error[(h-1)+6*7],variance_error[(h-1)+6*8],variance_error[(h-1)+6*9]]

    h=3
    mean1_IUFNO_40ep = [avg_error[(h-1)+6*0], avg_error[(h-1)+6*1], avg_error[(h-1)+6*2], avg_error[(h-1)+6*3], avg_error[(h-1)+6*4], avg_error[(h-1)+6*5], avg_error[(h-1)+6*6], avg_error[(h-1)+6*7], avg_error[(h-1)+6*8], avg_error[(h-1)+6*9]]
    std1_IUFNO_40ep = [variance_error[(h-1)+6*0],variance_error[(h-1)+6*1],variance_error[(h-1)+6*2],variance_error[(h-1)+6*3],variance_error[(h-1)+6*4],variance_error[(h-1)+6*5],variance_error[(h-1)+6*6],variance_error[(h-1)+6*7],variance_error[(h-1)+6*8],variance_error[(h-1)+6*9]]

    h=4
    mean1_IFNO = [avg_error[(h-1)+6*0], avg_error[(h-1)+6*1], avg_error[(h-1)+6*2], avg_error[(h-1)+6*3], avg_error[(h-1)+6*4], avg_error[(h-1)+6*5], avg_error[(h-1)+6*6], avg_error[(h-1)+6*7], avg_error[(h-1)+6*8], avg_error[(h-1)+6*9]]
    std1_IFNO = [variance_error[(h-1)+6*0],variance_error[(h-1)+6*1],variance_error[(h-1)+6*2],variance_error[(h-1)+6*3],variance_error[(h-1)+6*4],variance_error[(h-1)+6*5],variance_error[(h-1)+6*6],variance_error[(h-1)+6*7],variance_error[(h-1)+6*8],variance_error[(h-1)+6*9]]

    h=5
    mean1_DSM = [avg_error[(h-1)+6*0], avg_error[(h-1)+6*1], avg_error[(h-1)+6*2], avg_error[(h-1)+6*3], avg_error[(h-1)+6*4], avg_error[(h-1)+6*5], avg_error[(h-1)+6*6], avg_error[(h-1)+6*7], avg_error[(h-1)+6*8], avg_error[(h-1)+6*9]]
    std1_DSM = [variance_error[(h-1)+6*0],variance_error[(h-1)+6*1],variance_error[(h-1)+6*2],variance_error[(h-1)+6*3],variance_error[(h-1)+6*4],variance_error[(h-1)+6*5],variance_error[(h-1)+6*6],variance_error[(h-1)+6*7],variance_error[(h-1)+6*8],variance_error[(h-1)+6*9]]
    
    h=6
    mean1_fDSN = [avg_error[(h-1)+6*0], avg_error[(h-1)+6*1], avg_error[(h-1)+6*2], avg_error[(h-1)+6*3], avg_error[(h-1)+6*4], avg_error[(h-1)+6*5], avg_error[(h-1)+6*6], avg_error[(h-1)+6*7], avg_error[(h-1)+6*8], avg_error[(h-1)+6*9]]
    std1_fDSN = [variance_error[(h-1)+6*0],variance_error[(h-1)+6*1],variance_error[(h-1)+6*2],variance_error[(h-1)+6*3],variance_error[(h-1)+6*4],variance_error[(h-1)+6*5],variance_error[(h-1)+6*6],variance_error[(h-1)+6*7],variance_error[(h-1)+6*8],variance_error[(h-1)+6*9]]


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
    legend1 = ["F-IFNO", "F-IUFNO","IUFNO","IFNO","DSM","fDNS"]


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

    plt.plot(x1, mean1_F_IFNO, color="#1f77b4", alpha=0.3, linewidth=2*lineWidth, linestyle='--',zorder=3)
    plt.errorbar(x1, mean1_F_IFNO, yerr=std1_F_IFNO, fmt='o', color="#1f77b4", ecolor="#1f77b4", capsize=8, elinewidth=4, markeredgewidth=4, label=legend1[0],zorder=3)

    plt.plot(x1, mean1_DSM, color="green", alpha=0.3, linewidth=2*lineWidth, linestyle='--',zorder=2)
    plt.errorbar(x1, mean1_DSM, yerr=std1_DSM, fmt='o', color="green", ecolor="green", capsize=8, elinewidth=4, markeredgewidth=4, label=legend1[4],zorder=2)

    plt.plot(x1, mean1_fDSN, color='purple', alpha=0.3, linewidth=3*lineWidth, linestyle='--',zorder=1)
    plt.errorbar(x1, mean1_fDSN, yerr=std1_fDSN, fmt='o', color='purple', ecolor='purple', capsize=8, elinewidth=4, markeredgewidth=4, label=legend1[5],zorder=1)

    # Matplotlib 配置 - 全局字体设置为 STIXGeneral
    mpl.rc('font', family='STIXGeneral')
    # 创建图例
    lgd = plt.legend(loc='lower right', fontsize=40, frameon=True, framealpha=0, edgecolor='black', shadow=False)
    #plt.title("spectrum errorbar".format(vel_k), fontsize=40, color='black', loc='center', pad=15)

    # 显示网格
    #plt.grid()
    figPath1 = os.path.abspath("./vel_k_errorbar_with_k/{}cases".format(case_number))
    gfile1 = "spectrum errorbar for F-IFNO.png"
    gpath1 = os.path.join(figPath1, gfile1)
    # 保存图形
    plt.savefig(gpath1, bbox_extra_artists=(lgd,), bbox_inches='tight')
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
    legend1 = ["F-IFNO", "F-IUFNO","IUFNO","IFNO","DSM","fDNS"]

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


    plt.plot(x1, mean1_F_IUFNO_40ep, color="#ff7f0e", alpha=0.3, linewidth=2*lineWidth, linestyle='--',zorder=3)
    plt.errorbar(x1, mean1_F_IUFNO_40ep, yerr=std1_F_IUFNO_40ep, fmt='o', color="#ff7f0e", ecolor="#ff7f0e", capsize=8, elinewidth=4, markeredgewidth=4, label=legend1[1],zorder=3)
    
    plt.plot(x1, mean1_DSM, color="green", alpha=0.3, linewidth=2*lineWidth, linestyle='--',zorder=2)
    plt.errorbar(x1, mean1_DSM, yerr=std1_DSM, fmt='o', color="green", ecolor="green", capsize=8, elinewidth=4, markeredgewidth=4, label=legend1[4],zorder=2)

    plt.plot(x1, mean1_fDSN, color='purple', alpha=0.3, linewidth=3*lineWidth, linestyle='--',zorder=1)
    plt.errorbar(x1, mean1_fDSN, yerr=std1_fDSN, fmt='o', color='purple', ecolor='purple', capsize=8, elinewidth=4, markeredgewidth=4, label=legend1[5],zorder=1)

    # Matplotlib 配置 - 全局字体设置为 STIXGeneral
    mpl.rc('font', family='STIXGeneral')
    # 创建图例
    lgd = plt.legend(loc='lower right', fontsize=40, frameon=True, framealpha=0, edgecolor='black', shadow=False)
    #plt.title("spectrum errorbar".format(vel_k), fontsize=40, color='black', loc='center', pad=15)

    # 显示网格
    #plt.grid()
    figPath1 = os.path.abspath("./vel_k_errorbar_with_k/{}cases".format(case_number))
    gfile1 = "spectrum errorbar for F-IUFNO.png"
    gpath1 = os.path.join(figPath1, gfile1)
    # 保存图形
    plt.savefig(gpath1, bbox_extra_artists=(lgd,), bbox_inches='tight')
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
    legend1 = ["F-IFNO", "F-IUFNO","IUFNO","IFNO","DSM","fDNS"]

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

    plt.plot(x1, mean1_IUFNO_40ep, color='gold', alpha=0.3, linewidth=2*lineWidth, linestyle='--',zorder=3)
    plt.errorbar(x1, mean1_IUFNO_40ep, yerr=std1_IUFNO_40ep, fmt='o', color='gold', ecolor='gold', capsize=8, elinewidth=4, markeredgewidth=4, label=legend1[2],zorder=3)

    plt.plot(x1, mean1_DSM, color="green", alpha=0.3, linewidth=2*lineWidth, linestyle='--',zorder=2)
    plt.errorbar(x1, mean1_DSM, yerr=std1_DSM, fmt='o', color="green", ecolor="green", capsize=8, elinewidth=4, markeredgewidth=4, label=legend1[4],zorder=2)

    plt.plot(x1, mean1_fDSN, color='purple', alpha=0.3, linewidth=3*lineWidth, linestyle='--',zorder=1)
    plt.errorbar(x1, mean1_fDSN, yerr=std1_fDSN, fmt='o', color='purple', ecolor='purple', capsize=8, elinewidth=4, markeredgewidth=4, label=legend1[5],zorder=1)

    # Matplotlib 配置 - 全局字体设置为 STIXGeneral
    mpl.rc('font', family='STIXGeneral')
    # 创建图例
    lgd = plt.legend(loc='lower right', fontsize=40, frameon=True, framealpha=0, edgecolor='black', shadow=False)
    #plt.title("spectrum errorbar".format(vel_k), fontsize=40, color='black', loc='center', pad=15)

    # 显示网格
    #plt.grid()
    figPath1 = os.path.abspath("./vel_k_errorbar_with_k/{}cases".format(case_number))
    gfile1 = "spectrum errorbar for IUFNO.png"
    gpath1 = os.path.join(figPath1, gfile1)
    # 保存图形
    plt.savefig(gpath1, bbox_extra_artists=(lgd,), bbox_inches='tight')
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
    legend1 = ["F-IFNO", "F-IUFNO","IUFNO","IFNO","DSM","fDNS"]

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


    plt.plot(x1, mean1_IFNO, color='pink', alpha=0.3, linewidth=2*lineWidth, linestyle='--',zorder=3)
    plt.errorbar(x1, mean1_IFNO, yerr=std1_IFNO, fmt='o', color='pink', ecolor='pink', capsize=8, elinewidth=4, markeredgewidth=4, label=legend1[3],zorder=3)

    plt.plot(x1, mean1_DSM, color="green", alpha=0.3, linewidth=2*lineWidth, linestyle='--',zorder=2)
    plt.errorbar(x1, mean1_DSM, yerr=std1_DSM, fmt='o', color="green", ecolor="green", capsize=8, elinewidth=4, markeredgewidth=4, label=legend1[4],zorder=2)

    plt.plot(x1, mean1_fDSN, color='purple', alpha=0.3, linewidth=3*lineWidth, linestyle='--',zorder=1)
    plt.errorbar(x1, mean1_fDSN, yerr=std1_fDSN, fmt='o', color='purple', ecolor='purple', capsize=8, elinewidth=4, markeredgewidth=4, label=legend1[5],zorder=1)
    
    # Matplotlib 配置 - 全局字体设置为 STIXGeneral
    mpl.rc('font', family='STIXGeneral')
    # 创建图例
    lgd = plt.legend(loc='lower right', fontsize=40, frameon=True, framealpha=0, edgecolor='black', shadow=False)
    #plt.title("spectrum errorbar".format(vel_k), fontsize=40, color='black', loc='center', pad=15)

    # 显示网格
    #plt.grid()
    figPath1 = os.path.abspath("./vel_k_errorbar_with_k/{}cases".format(case_number))
    gfile1 = "spectrum errorbar for IFNO.png"
    gpath1 = os.path.join(figPath1, gfile1)
    # 保存图形
    plt.savefig(gpath1, bbox_extra_artists=(lgd,), bbox_inches='tight')
    plt.close()


