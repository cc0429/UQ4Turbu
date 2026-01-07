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

for k, case_number in enumerate(case_number_list):

    #-------------------------------------------------------------读入数据，


    fDNS = np.loadtxt("./result/{}cases/error_with_time_fDNS.dat".format(case_number), dtype=float)
    IUFNO_40ep = np.loadtxt("./result/{}cases/error_with_time_IUFNO.dat".format(case_number), dtype=float)
    F_IUFNO_40ep = np.loadtxt("./result/{}cases/error_with_time_F_IUFNO.dat".format(case_number), dtype=float)
    F_IFNO_40ep = np.loadtxt("./result/{}cases/error_with_time_F_IFNO.dat".format(case_number), dtype=float)
    IFNO = np.loadtxt("./result/{}cases/error_with_time_IFNO.dat".format(case_number), dtype=float)
    DSM = np.loadtxt("./result/{}cases/error_with_time_DSM.dat".format(case_number), dtype=float)
    

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

    avg_results = []
    avg_error = []
    variance_error = []

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



    ######----------------------------x=model----------------------------########
    # 图形参数设置
    dpi = 600
    width, height = 10, 6
    fontSize = 25
    lineWidth = 2
    boxWidth = 2.5
    Lmajor, Lminor = 7, 4
    xlabPad, ylabPad = 10, 10
    xlabel = r"$\mathdefault{Model}$"
    ylabel = r"$\mathdefault{Errorbar \ for \ E_k}$"
    ylimit = [-12,12]
    legend1 = ["F-IFNO", "F-IUFNO", "IUFNO", "IFNO","DSM","fDNS"]

    fig = plt.figure(figsize=(width, height), dpi=dpi)
    plt.rcParams["font.size"] = fontSize
    plt.rcParams["axes.linewidth"] = lineWidth
    ax = fig.add_axes([0, 0, 1, 1])

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
    #ax.set_ylim(ylimit[0], ylimit[1]) 
   

    # Matplotlib 配置
    mpl.rc('font', family='STIXGeneral')
    mpl.rc('text', usetex=False)
    mpl.rcParams['xtick.direction'] = 'in'
    mpl.rcParams['ytick.direction'] = 'in'
    plt.rcParams["mathtext.fontset"] = "cm"

    x1 = ["F-IFNO", "F-IUFNO","IUFNO","IFNO","DSM","fDNS"]
    mean1_F_IFNO = [avg_error[0]]
    std1_F_IFNO = [variance_error[0]]

    mean1_F_IUFNO = [avg_error[1]]
    std1_F_IUFNO = [variance_error[1]]

    mean1_IUFNO = [avg_error[2]]
    std1_IUFNO = [variance_error[2]]

    mean1_IFNO = [avg_error[3]]
    std1_IFNO = [variance_error[3]]

    mean1_DSM = [avg_error[4]]
    std1_DSM = [variance_error[4]]

    mean1_fDSN = [avg_error[5]]
    std1_fDSN = [variance_error[5]]


    x2 = ["F-IFNO", "F-IUFNO","IUFNO","IFNO","DSM","fDNS"]
    y2= [avg_error[0], avg_error[1], avg_error[2], avg_error[3], avg_error[4], avg_error[5]]
    plt.plot(x2, y2, color='black', alpha=0.3,  linewidth=2*lineWidth, linestyle='--', zorder=2)


    plt.plot([x1[0]], [mean1_F_IFNO[0]], color="#1f77b4", alpha=0.3, linewidth=2*lineWidth, linestyle='--',zorder=2)
    plt.errorbar([x1[0]], [mean1_F_IFNO[0]], yerr=[std1_F_IFNO[0]], fmt='o', color="#1f77b4", ecolor="#1f77b4", capsize=8, elinewidth=4, markeredgewidth=4)

    plt.plot([x1[1]], [mean1_F_IUFNO[0]], color="#ff7f0e", alpha=0.3, linewidth=2*lineWidth, linestyle='--', zorder=1)
    plt.errorbar([x1[1]], [mean1_F_IUFNO[0]], yerr=[std1_F_IUFNO[0]], fmt='o', color="#ff7f0e", ecolor="#ff7f0e", capsize=8, elinewidth=4, markeredgewidth=4)

    plt.plot([x1[2]], [mean1_IUFNO[0]], color='gold', alpha=0.3, linewidth=2*lineWidth, linestyle='--', zorder=0)
    plt.errorbar([x1[2]], [mean1_IUFNO[0]], yerr=[std1_IUFNO[0]], fmt='o', color='gold', ecolor='gold', capsize=8, elinewidth=4, markeredgewidth=4)

    plt.plot([x1[3]], [mean1_IFNO[0]], color='pink', alpha=0.3, linewidth=2*lineWidth, linestyle='--', zorder=0)
    plt.errorbar([x1[3]], [mean1_IFNO[0]], yerr=[std1_IFNO[0]], fmt='o', color='pink', ecolor='pink', capsize=8, elinewidth=4, markeredgewidth=4)

    plt.plot([x1[4]], [mean1_DSM[0]], color="green", alpha=0.3, linewidth=2*lineWidth, linestyle='--', zorder=2)
    plt.errorbar([x1[4]], [mean1_DSM[0]], yerr=[std1_DSM[0]], fmt='o', color="green", ecolor="green", capsize=8, elinewidth=4, markeredgewidth=4)

    plt.plot([x1[5]], [mean1_fDSN[0]], color='purple', alpha=0.3, linewidth=2*lineWidth, linestyle='--', zorder=2)
    plt.errorbar([x1[5]], [mean1_fDSN[0]], yerr=[std1_fDSN[0]], fmt='o', color='purple', ecolor='purple', capsize=8, elinewidth=4, markeredgewidth=4)

    # Matplotlib 配置 - 全局字体设置为 STIXGeneral
    mpl.rc('font', family='STIXGeneral')
    # 创建图例
    #plt.title(r"Errorbar for Ek", fontsize=25, color='black', loc='center', pad=15)

    # 显示网格
    #plt.grid()
    figPath1 = os.path.abspath("./Ek_errorbar/{}cases".format(case_number))
    gfile1 = "Errorbar for Ek_model_6.png"
    gpath1 = os.path.join(figPath1, gfile1)
    # 保存图形
    plt.savefig(gpath1, bbox_inches='tight')
    plt.close()
    
    
    ######----------------------------x=model----------------------------########
    # 图形参数设置
    dpi = 600
    width, height = 10, 6
    fontSize = 25
    lineWidth = 2
    boxWidth = 2.5
    Lmajor, Lminor = 7, 4
    xlabPad, ylabPad = 10, 10
    xlabel = r"$\mathdefault{Model}$"
    ylabel = r"$\mathdefault{Errorbar \ for \ E_k}$"
    ylimit = [-2.4,0.2]
    legend1 = ["F-IFNO", "F-IUFNO","DSM","fDNS"]

    fig = plt.figure(figsize=(width, height), dpi=dpi)
    plt.rcParams["font.size"] = fontSize
    plt.rcParams["axes.linewidth"] = lineWidth
    ax = fig.add_axes([0, 0, 1, 1])

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
    #ax.set_ylim(ylimit[0], ylimit[1]) 
   

    # Matplotlib 配置
    mpl.rc('font', family='STIXGeneral')
    mpl.rc('text', usetex=False)
    mpl.rcParams['xtick.direction'] = 'in'
    mpl.rcParams['ytick.direction'] = 'in'
    plt.rcParams["mathtext.fontset"] = "cm"

    x1 = ["F-IFNO", "F-IUFNO","DSM","fDNS"]
    mean1_F_IFNO = [avg_error[0]]
    std1_F_IFNO = [variance_error[0]]

    mean1_F_IUFNO = [avg_error[1]]
    std1_F_IUFNO = [variance_error[1]]

    mean1_DSM = [avg_error[4]]
    std1_DSM = [variance_error[4]]

    mean1_fDSN = [avg_error[5]]
    std1_fDSN = [variance_error[5]]


    x2 = ["F-IFNO", "F-IUFNO","DSM","fDNS"]
    y2= [avg_error[0], avg_error[1], avg_error[4], avg_error[5]]
    plt.plot(x2, y2, color='black', alpha=0.3,  linewidth=2*lineWidth, linestyle='--', zorder=2)


    plt.plot([x1[0]], [mean1_F_IFNO[0]], color="#1f77b4", alpha=0.3, linewidth=2*lineWidth, linestyle='--',zorder=2)
    plt.errorbar([x1[0]], [mean1_F_IFNO[0]], yerr=[std1_F_IFNO[0]], fmt='o', color="#1f77b4", ecolor="#1f77b4", capsize=8, elinewidth=4, markeredgewidth=4)

    plt.plot([x1[1]], [mean1_F_IUFNO[0]], color="#ff7f0e", alpha=0.3, linewidth=2*lineWidth, linestyle='--', zorder=1)
    plt.errorbar([x1[1]], [mean1_F_IUFNO[0]], yerr=[std1_F_IUFNO[0]], fmt='o', color="#ff7f0e", ecolor="#ff7f0e", capsize=8, elinewidth=4, markeredgewidth=4)

    plt.plot([x1[2]], [mean1_DSM[0]], color="green", alpha=0.3, linewidth=2*lineWidth, linestyle='--', zorder=2)
    plt.errorbar([x1[2]], [mean1_DSM[0]], yerr=[std1_DSM[0]], fmt='o', color="green", ecolor="green", capsize=8, elinewidth=4, markeredgewidth=4)

    plt.plot([x1[3]], [mean1_fDSN[0]], color='purple', alpha=0.3, linewidth=2*lineWidth, linestyle='--', zorder=2)
    plt.errorbar([x1[3]], [mean1_fDSN[0]], yerr=[std1_fDSN[0]], fmt='o', color='purple', ecolor='purple', capsize=8, elinewidth=4, markeredgewidth=4)

    # Matplotlib 配置 - 全局字体设置为 STIXGeneral
    mpl.rc('font', family='STIXGeneral')
    # 创建图例
    #plt.title(r"Errorbar for Ek", fontsize=25, color='black', loc='center', pad=15)

    # 显示网格
    #plt.grid()
    figPath1 = os.path.abspath("./Ek_errorbar/{}cases".format(case_number))
    gfile1 = "Errorbar for Ek_model_4.png"
    gpath1 = os.path.join(figPath1, gfile1)
    # 保存图形
    plt.savefig(gpath1, bbox_inches='tight')
    plt.close()
    ######----------------------------x=model----------------------------########
    # 图形参数设置
    dpi = 600
    width, height = 10, 6
    fontSize = 25
    lineWidth = 2
    boxWidth = 2.5
    Lmajor, Lminor = 7, 4
    xlabPad, ylabPad = 10, 10
    xlabel = r"$\mathdefault{Model}$"
    ylabel = r"$\mathdefault{Errorbar \ for \ E_k}$"
    ylimit = [-12,12]
    legend1 = ["F-IFNO", "F-IUFNO", "IUFNO", "IFNO","DSM","fDNS"]

    fig = plt.figure(figsize=(width, height), dpi=dpi)
    plt.rcParams["font.size"] = fontSize
    plt.rcParams["axes.linewidth"] = lineWidth
    ax = fig.add_axes([0, 0, 1, 1])

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
    #ax.set_ylim(ylimit[0], ylimit[1]) 
   

    # Matplotlib 配置
    mpl.rc('font', family='STIXGeneral')
    mpl.rc('text', usetex=False)
    mpl.rcParams['xtick.direction'] = 'in'
    mpl.rcParams['ytick.direction'] = 'in'
    plt.rcParams["mathtext.fontset"] = "cm"

    x1 = ["F-IFNO", "F-IUFNO","IUFNO","IFNO","DSM","fDNS"]
    mean1_F_IFNO = [avg_error[0]]
    std1_F_IFNO = [variance_error[0]]

    mean1_F_IUFNO = [avg_error[1]]
    std1_F_IUFNO = [variance_error[1]]

    mean1_IUFNO = [avg_error[2]]
    std1_IUFNO = [variance_error[2]]

    mean1_IFNO = [avg_error[3]]
    std1_IFNO = [variance_error[3]]

    mean1_DSM = [avg_error[4]]
    std1_DSM = [variance_error[4]]

    mean1_fDSN = [avg_error[5]]
    std1_fDSN = [variance_error[5]]


    x2 = ["IUFNO","IFNO","DSM","fDNS"]
    y2= [avg_error[2], avg_error[3], avg_error[4], avg_error[5]]
    plt.plot(x2, y2, color='black', alpha=0.3,  linewidth=2*lineWidth, linestyle='--', zorder=2)

    plt.plot([x1[2]], [mean1_IUFNO[0]], color='gold', alpha=0.3, linewidth=2*lineWidth, linestyle='--', zorder=0)
    plt.errorbar([x1[2]], [mean1_IUFNO[0]], yerr=[std1_IUFNO[0]], fmt='o', color='gold', ecolor='gold', capsize=8, elinewidth=4, markeredgewidth=4)

    plt.plot([x1[3]], [mean1_IFNO[0]], color='pink', alpha=0.3, linewidth=2*lineWidth, linestyle='--', zorder=0)
    plt.errorbar([x1[3]], [mean1_IFNO[0]], yerr=[std1_IFNO[0]], fmt='o', color='pink', ecolor='pink', capsize=8, elinewidth=4, markeredgewidth=4)

    plt.plot([x1[4]], [mean1_DSM[0]], color="green", alpha=0.3, linewidth=2*lineWidth, linestyle='--', zorder=2)
    plt.errorbar([x1[4]], [mean1_DSM[0]], yerr=[std1_DSM[0]], fmt='o', color="green", ecolor="green", capsize=8, elinewidth=4, markeredgewidth=4)

    plt.plot([x1[5]], [mean1_fDSN[0]], color='purple', alpha=0.3, linewidth=2*lineWidth, linestyle='--', zorder=2)
    plt.errorbar([x1[5]], [mean1_fDSN[0]], yerr=[std1_fDSN[0]], fmt='o', color='purple', ecolor='purple', capsize=8, elinewidth=4, markeredgewidth=4)

    # Matplotlib 配置 - 全局字体设置为 STIXGeneral
    mpl.rc('font', family='STIXGeneral')
    # 创建图例
    #plt.title(r"Errorbar for Ek", fontsize=25, color='black', loc='center', pad=15)

    # 显示网格
    #plt.grid()
    figPath1 = os.path.abspath("./Ek_errorbar/{}cases".format(case_number))
    gfile1 = "Errorbar for Ek_model_4-.png"
    gpath1 = os.path.join(figPath1, gfile1)
    # 保存图形
    plt.savefig(gpath1, bbox_inches='tight')
    plt.close()

