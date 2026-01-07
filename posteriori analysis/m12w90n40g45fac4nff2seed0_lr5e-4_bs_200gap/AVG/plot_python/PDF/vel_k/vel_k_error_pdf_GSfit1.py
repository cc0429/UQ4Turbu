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
from scipy.stats import norm
from scipy.optimize import curve_fit
from scipy.stats import skewnorm
from scipy.stats import kstest
from sklearn.mixture import GaussianMixture
import scipy.stats as stats
from scipy.stats import ks_2samp
from scipy.stats import truncnorm, kstest
import statsmodels.api as sm
plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.serif'] = ['Times', 'Times', 'STIXGeneral']

case_number_list =[30]
vel_k_list = [1,2,3,4,5,6,7,8,9,10]
vel_k_list = [5]

  
for kk, case_number in enumerate(case_number_list):
    for k, vel_k in enumerate(vel_k_list):

    #-------------------------------------------------------------读入数据，
        if vel_k in [1,2]:
            fDNS = np.round(np.loadtxt("./result/{}cases/error_with_time_fDNS_k={}.dat".format(case_number, vel_k), dtype=float), 1)
            DSM = np.round(np.loadtxt("./result/{}cases/error_with_time_DSM_k={}.dat".format(case_number, vel_k), dtype=float), 1)        
            #IUFNO_40ep = np.round(np.loadtxt("./result/{}cases/error_with_time_IUFNO_k={}.dat".format(case_number, vel_k), dtype=float), 1)
            #F_IUFNO_40ep = np.round(np.loadtxt("./result/{}cases/error_with_time_F_IUFNO_k={}.dat".format(case_number, vel_k), dtype=float), 1)
            #F_IFNO_40ep = np.round(np.loadtxt("./result/{}cases/error_with_time_F_IFNO_k={}.dat".format(case_number, vel_k), dtype=float), 1)
            #IFNO = np.round(np.loadtxt("./result/{}cases/error_with_time_IFNO_k={}.dat".format(case_number, vel_k), dtype=float), 1)
            IUFNO_40ep = np.loadtxt("./result/{}cases/error_with_time_IUFNO_k={}.dat".format(case_number, vel_k), dtype=float)
            F_IUFNO_40ep = np.loadtxt("./result/{}cases/error_with_time_F_IUFNO_k={}.dat".format(case_number, vel_k), dtype=float)
            F_IFNO_40ep = np.loadtxt("./result/{}cases/error_with_time_F_IFNO_k={}.dat".format(case_number, vel_k), dtype=float)
            IFNO = np.loadtxt("./result/{}cases/error_with_time_IFNO_k={}.dat".format(case_number, vel_k), dtype=float)         
        else:

            fDNS = np.loadtxt("./result/{}cases/error_with_time_fDNS_k={}.dat".format(case_number, vel_k), dtype=float)
            IUFNO_40ep = np.loadtxt("./result/{}cases/error_with_time_IUFNO_k={}.dat".format(case_number, vel_k), dtype=float)
            F_IUFNO_40ep = np.loadtxt("./result/{}cases/error_with_time_F_IUFNO_k={}.dat".format(case_number, vel_k), dtype=float)
            F_IFNO_40ep = np.loadtxt("./result/{}cases/error_with_time_F_IFNO_k={}.dat".format(case_number, vel_k), dtype=float)
            DSM = np.loadtxt("./result/{}cases/error_with_time_DSM_k={}.dat".format(case_number, vel_k), dtype=float)
            IFNO = np.loadtxt("./result/{}cases/error_with_time_IFNO_k={}.dat".format(case_number, vel_k), dtype=float)            
        #-------------------------输入参数
        # time_advance=[20]  #挑推进时间画图
        # time_advance=[40]  #挑推进时间画图
        #time_advance=[1,2,3,10,15,20,25,30,40,50,60,70,80,90,100,110,120,130,140,150,160,170,180,190,200,210,220,230,240,250]  #挑推进时间画图
        data1=fDNS[:,1]
        data2=F_IUFNO_40ep[:,1]
        data3=F_IFNO_40ep[:,1]
        data4=DSM[:,1]
        data5=IUFNO_40ep[:,1]
        data6=IFNO[:,1]        
        print("Size of data1:", len(data1))
        print("data1:",data1)
   
        colors = ['#A52A2A','#ff7f0e','#ffd700','green','#1f77b4','purple']
        # 绘制 PDF
       
        
        #3
        plt.figure(figsize=(14, 10.5), facecolor='none')  # 设置图形大小
        plt.rcParams['text.color'] = 'black'  # 字体颜色
        
       # 直方图数据
        hist, bin_edges = np.histogram(data3, bins=50, density=True)
        bin_centers = (bin_edges[:-1] + bin_edges[1:]) / 2
        
        # 使用 skewnorm.fit() 进行偏态正态分布的拟合
        alpha_fit, mu_fit, sigma_fit = skewnorm.fit(data3) 
        # 绘制拟合结果的概率密度函数图
        x = np.linspace(min(data3), max(data3), 2000)
        pdf= skewnorm.pdf(x, a=alpha_fit, loc=mu_fit, scale=sigma_fit)    
        #plot
        plt.plot(x, pdf, 'k-',linewidth=4, zorder=2,label=f'Fit: $\\alpha={alpha_fit:.4f}$, $\\mu={mu_fit:.4f}$, $\\sigma={sigma_fit:.4f}$')
        #绘制原始频率密度曲线（虚线）
        plt.plot(bin_centers, hist, linestyle="--", color=colors[0], label='Data density', linewidth=4,zorder=1)
        # 绘制直方圖结果
        plt.hist(data3, bins=50, density=True,alpha=0.4,color=colors[0], label='Data histogram',zorder=0)
        plt.rcParams['mathtext.fontset'] = 'cm'
        plt.title(r'Skew normal distribution fit for E(k={}) error: F-IFNO'.format(vel_k), fontsize=40, pad=10) 
        plt.xlabel('Error', fontsize=40)  # x 轴标签
        plt.ylabel('Density', fontsize=40)  # y 轴标签
        plt.xticks(fontsize=40)  # x 轴刻度字体大小
        plt.yticks(fontsize=40)  # y 轴刻度字体大小
        plt.gca().xaxis.set_tick_params(pad=15)    
        plt.legend(loc='upper right', fontsize=40)  # 添加图例并设置位置
        # 设置边框颜色
        plt.gca().spines['top'].set_color('black')
        plt.gca().spines['right'].set_color('black')
        plt.gca().spines['left'].set_color('black')
        plt.gca().spines['bottom'].set_color('black')
        # 设置 x 轴和 y 轴的间隔
        x_ticks = np.arange(start=0, stop=max(data3), step=0.5)  # 根据需要设置间隔
        y_ticks = np.arange(start=0, stop=1.1, step=0.1)  # 根据需要设置间隔
        # 设置 x,y 轴刻度格式
        plt.gca().xaxis.set_major_formatter(ticker.FormatStrFormatter('%.2f'))
        plt.gca().yaxis.set_major_formatter(ticker.FormatStrFormatter('%.1f'))
        handles, labels = plt.gca().get_legend_handles_labels()    
        handles = [handles[1], handles[0], handles[2]]
        labels = [labels[1], labels[0], labels[2]]      
        plt.ylim(0, 13)
            
        # 显示图例
        plt.legend(handles=handles,labels=labels,loc='upper center',bbox_to_anchor=(0.45, -0.18),fontsize=40, ncol=2,columnspacing=-9)
        # 去除网格线
        plt.grid(False)
        #plt.ylim(0, 10) 
        plt.subplots_adjust(bottom=0.31)
        plt.savefig('./GSfit/{}cases/k={}/GSfit_F-IFNO_k={}.png'.format(case_number,vel_k,vel_k), dpi=300)  

        plt.close()  # 关闭当前图像，释放内存









 