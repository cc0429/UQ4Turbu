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


        
        ######----------------------------x=model----------------------------########
        # 图形参数设置
        dpi = 600
        width, height = 18, 6
        fontSize = 30
        lineWidth = 2
        boxWidth = 2.5
        Lmajor, Lminor = 7, 4
        xlabPad, ylabPad = 10, 10
        xlabel = r"$\mathdefault{Model}$"
        ylabel = r"$\mathdefault{{Error \ distribution \ for \ E(k={})}}$".format(vel_k)
        #ylimit = [-0.8, 0.4]
        legend1 = ["F-IFNO", "F-IUFNO", "IUFNO","IFNO","DSM","fDNS"]

        fig = plt.figure(figsize=(width, height), dpi=dpi)
        plt.rcParams["font.size"] = fontSize
        plt.rcParams["axes.linewidth"] = lineWidth
        ax = fig.add_axes([0, 0, 1, 1])

        ax.yaxis.set_major_locator(ticker.MaxNLocator(nbins=6, min_n_ticks=5))

        # 让次刻度为主刻度的 1/5
        plt.gca().yaxis.set_minor_locator(ticker.AutoMinorLocator(n=5))

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

        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
       

        # Matplotlib 配置
        mpl.rc('font', family='STIXGeneral')
        mpl.rc('text', usetex=False)
        mpl.rcParams['xtick.direction'] = 'in'
        mpl.rcParams['ytick.direction'] = 'in'
        plt.rcParams["mathtext.fontset"] = "cm"

        x1 = ["F-IFNO", "F-IUFNO", "IUFNO","IFNO","DSM","fDNS"]

        box = plt.boxplot([data1,data2,data3,data4,data5,data6],
            labels=x1,
            patch_artist=True,  # 让箱子填充颜色
            boxprops=dict(linewidth=2),  # 调整箱子线条粗细
            whiskerprops=dict(linewidth=2),  # 调整须（whiskers）线条粗细
            capprops=dict(linewidth=2),  # 调整顶部和底部横线（caps）粗细
            medianprops=dict(linewidth=2,color="red")  # 调整中位数线条粗细
        )

        # Matplotlib 配置 - 全局字体设置为 STIXGeneral
        mpl.rc('font', family='STIXGeneral')
        # 创建图例ror Distribu
        #plt.title("Error Distribution for E[k={}]".format(vel_k), fontsize=25, color='black', loc='center', pad=15)

        # 显示网格
        #plt.grid()
        figPath1 = os.path.abspath("./vel_k_errorbar/{}cases/k={}".format(case_number,vel_k))
        gfile1 = "Errorbarbox for E[k={}]_model.png".format(vel_k)
        gpath1 = os.path.join(figPath1, gfile1)
        # 保存图形
        plt.savefig(gpath1, bbox_inches='tight')
        plt.close()
            
