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
plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.serif'] = ['Times', 'Times', 'STIXGeneral']
time_steps = 600
case_number_list =[30]
vel_k_list = [1,2,3,4,5,6,7,8,9,10]

for kk, case_number in enumerate(case_number_list):
    for k, vel_k in enumerate(vel_k_list):
        #-------------------------------------------------------------读入数据，
        ###小數點后3位###

        if vel_k in [1,2]:
            fDNS = np.round(np.loadtxt("./result/{}cases/error_with_time_fDNS_k={}.dat".format(case_number, vel_k), dtype=float), 3)
            DSM = np.round(np.loadtxt("./result/{}cases/error_with_time_DSM_k={}.dat".format(case_number, vel_k), dtype=float), 3)        
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
        period = 10 #10个波数
        # time_advance=[20]  #挑推进时间画图
        # time_advance=[40]  #挑推进时间画图
        #time_advance=[1,2,3,10,15,20,25,30,40,50,60,70,80,90,100,110,120,130,140,150,160,170,180,190,200,210,220,230,240,250]  #挑推进时间画图
        data1=fDNS[:,1]
        data2=IUFNO_40ep[:,1]
        data3=F_IUFNO_40ep[:,1]
        data4=F_IFNO_40ep[:,1]
        data5=IFNO[:,1]
        data6=DSM[:,1]
        print("Size of data1:", len(data1))
        print("data1:",data1)
        #--------------------------
        
        colors = ['#A52A2A','#ff7f0e','#ffd700','green','#1f77b4','purple','black']
        # 绘制 PDF
        #1
        plt.figure(figsize=(14,10.5), facecolor='none')  # 设置图形大小
        plt.rcParams['text.color'] = 'black'  # 字体颜色
        # 绘制直方图
        sns.distplot(data1, bins=50, hist=True, kde=False, hist_kws={'color':colors[5]}, norm_hist=True,label='Data histogram')
        # 绘制核密度估计
        sns.distplot(data1, hist=False, kde=True, kde_kws={'color':colors[5], 'linestyle':'--', 'linewidth':4}, norm_hist=True,label='Data density')
        # 图标题
        plt.title(r'Probability density function (PDF) of E(k={}) fluctuation: fDNS'.format(vel_k), fontsize=40, pad=15)  
        plt.xlabel('Fluctuation', fontsize=40)  # x 轴标签
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
        x_ticks = np.arange(start=0, stop=max(data1), step=0.5)  # 根据需要设置间隔
        y_ticks = np.arange(start=0, stop=1.1, step=0.1)  # 根据需要设置间隔
        # 设置 x,y 轴刻度格式
        plt.gca().xaxis.set_major_formatter(ticker.FormatStrFormatter('%.2f'))
        plt.gca().yaxis.set_major_formatter(ticker.FormatStrFormatter('%.1f'))
        # 显示图例
        plt.legend(loc='upper center',bbox_to_anchor=(0.5, -0.24),fontsize=40, ncol=2,columnspacing=1)
        # 去除网格线
        plt.grid(False)
        plt.subplots_adjust(bottom=0.31)
        plt.savefig('./pdf/{}cases/pdf_fDNS_k={}_1.png'.format(case_number,vel_k), dpi=300)   

        plt.close()  # 关闭当前图像，释放内存

        #2
        plt.figure(figsize=(14,10.5), facecolor='none')  # 设置图形大小
        plt.rcParams['text.color'] = 'black'  # 字体颜色
        # 绘制直方图
        sns.distplot(data2, bins=50, hist=True, kde=False, hist_kws={'color':colors[2]}, norm_hist=True,label='Data histogram')
        # 绘制核密度估计
        sns.distplot(data2, hist=False, kde=True, kde_kws={'color':colors[2], 'linestyle':'--', 'linewidth':4}, norm_hist=True,label='Data density')
        # 图标题
        plt.title(r'Probability density function (PDF) of E(k={}) error: IUFNO'.format(vel_k), fontsize=40, pad=15)  
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
        x_ticks = np.arange(start=0, stop=max(data2), step=0.5)  # 根据需要设置间隔
        y_ticks = np.arange(start=0, stop=1.1, step=0.1)  # 根据需要设置间隔
        # 设置 x,y 轴刻度格式
        plt.gca().xaxis.set_major_formatter(ticker.FormatStrFormatter('%.2f'))
        plt.gca().yaxis.set_major_formatter(ticker.FormatStrFormatter('%.1f'))
        # 显示图例
        plt.legend(loc='upper center',bbox_to_anchor=(0.5, -0.24),fontsize=40, ncol=2,columnspacing=1)
        # 去除网格线
        plt.grid(False)
        plt.subplots_adjust(bottom=0.31)
        plt.savefig('./pdf/{}cases/pdf_IUFNO_k={}_1.png'.format(case_number,vel_k), dpi=300)  

        plt.close()  # 关闭当前图像，释放内存
        
        #3
        plt.figure(figsize=(14,10.5), facecolor='none')  # 设置图形大小
        plt.rcParams['text.color'] = 'black'  # 字体颜色
        # 绘制直方图
        sns.distplot(data3, bins=50, hist=True, kde=False, hist_kws={'color':colors[1]}, norm_hist=True,label='Data histogram')
        # 绘制核密度估计
        sns.distplot(data3, hist=False, kde=True, kde_kws={'color':colors[1], 'linestyle':'--', 'linewidth':4}, norm_hist=True,label='Data density')
        # 图标题
        plt.title(r'Probability density function (PDF) of E(k={}) error: F-IUFNO'.format(vel_k), fontsize=40, pad=15)  
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
        # 显示图例
        plt.legend(loc='upper center',bbox_to_anchor=(0.5, -0.24),fontsize=40, ncol=2,columnspacing=1)
        # 去除网格线
        plt.grid(False)
        plt.subplots_adjust(bottom=0.31)
        plt.savefig('./pdf/{}cases/pdf_F-IUFNO_k={}_1.png'.format(case_number,vel_k), dpi=300)  

        plt.close()  # 关闭当前图像，释放内存
        
        #4
        plt.figure(figsize=(14,10.5), facecolor='none')  # 设置图形大小
        plt.rcParams['text.color'] = 'black'  # 字体颜色
        # 绘制直方图
        sns.distplot(data4, bins=50, hist=True, kde=False, hist_kws={'color':colors[0]}, norm_hist=True,label='Data histogram')
        # 绘制核密度估计
        sns.distplot(data4, hist=False, kde=True, kde_kws={'color':colors[0], 'linestyle':'--', 'linewidth':4}, norm_hist=True,label='Data density')
        # 图标题
        plt.title(r'Probability density function (PDF) of E(k={}) error: F-IFNO'.format(vel_k), fontsize=40, pad=15)  
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
        x_ticks = np.arange(start=0, stop=max(data4), step=0.5)  # 根据需要设置间隔
        y_ticks = np.arange(start=0, stop=1.1, step=0.1)  # 根据需要设置间隔
        # 设置 x,y 轴刻度格式
        plt.gca().xaxis.set_major_formatter(ticker.FormatStrFormatter('%.2f'))
        plt.gca().yaxis.set_major_formatter(ticker.FormatStrFormatter('%.1f'))
        # 显示图例
        plt.legend(loc='upper center',bbox_to_anchor=(0.5, -0.24),fontsize=40, ncol=2,columnspacing=1)
        # 去除网格线
        plt.grid(False)
        plt.subplots_adjust(bottom=0.31)
        plt.savefig('./pdf/{}cases/pdf_F-IFNO_k={}_1.png'.format(case_number,vel_k), dpi=300)

        plt.close()  # 关闭当前图像，释放内存  
        #5
        plt.figure(figsize=(14,10.5), facecolor='none')  # 设置图形大小
        plt.rcParams['text.color'] = 'black'  # 字体颜色
        # 绘制直方图
        sns.distplot(data5, bins=50, hist=True, kde=False, hist_kws={'color':colors[3]}, norm_hist=True,label='Data histogram')
        # 绘制核密度估计
        sns.distplot(data5, hist=False, kde=True, kde_kws={'color':colors[3], 'linestyle':'--', 'linewidth':4}, norm_hist=True,label='Data density')
        # 图标题
        plt.title(r'Probability density function (PDF) of E(k={}) error: IFNO'.format(vel_k), fontsize=40, pad=15)  
        plt.xlabel('Error', fontsize=40)  # x 轴标签
        plt.ylabel('Density', fontsize=40)  # y 轴标签

        plt.legend(loc='upper right', fontsize=40)  # 添加图例并设置位置
        # 设置边框颜色
        plt.gca().spines['top'].set_color('black')
        plt.gca().spines['right'].set_color('black')
        plt.gca().spines['left'].set_color('black')
        plt.gca().spines['bottom'].set_color('black')
        # 设置 x 轴和 y 轴的间隔
        x_ticks = np.arange(start=min(data5)+ 1, stop=max(data5)+ 1, step=3)  # 根据需要设置间隔
        y_ticks = np.arange(start=0, stop=0.9, step=0.2)  # 根据需要设置间隔
        plt.xticks(fontsize=40)  # x 轴刻度字体大小
        plt.yticks(fontsize=40)  # y 轴刻度字体大小
        plt.gca().xaxis.set_tick_params(pad=15)
        # 设置 x,y 轴刻度格式
        plt.gca().xaxis.set_major_formatter(ticker.FormatStrFormatter('%.2f'))
        plt.gca().yaxis.set_major_formatter(ticker.FormatStrFormatter('%.1f'))
        # 显示图例
        plt.legend(loc='upper center',bbox_to_anchor=(0.5, -0.24),fontsize=40, ncol=2,columnspacing=1)
        # 去除网格线
        plt.grid(False)
        plt.subplots_adjust(bottom=0.31)
        plt.savefig('./pdf/{}cases/pdf_IFNO_k={}_1.png'.format(case_number,vel_k), dpi=300)  

        plt.close()  # 关闭当前图像，释放内存
        #6
        plt.figure(figsize=(14,10.5), facecolor='none')  # 设置图形大小
        plt.rcParams['text.color'] = 'black'  # 字体颜色
        # 绘制直方图
        sns.distplot(data6, bins=50, hist=True, kde=False, hist_kws={'color':colors[4]}, norm_hist=True,label='Data histogram')
        # 绘制核密度估计
        sns.distplot(data6, hist=False, kde=True, kde_kws={'color':colors[4], 'linestyle':'--', 'linewidth':4}, norm_hist=True,label='Data density')
        # 图标题
        plt.title(r'Probability density function (PDF) of E(k={}) error: DSM'.format(vel_k), fontsize=40, pad=15)  
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
        x_ticks = np.arange(start=0, stop=max(data6), step=0.5)  # 根据需要设置间隔
        y_ticks = np.arange(start=0, stop=1.1, step=0.1)  # 根据需要设置间隔
        # 设置 x,y 轴刻度格式
        plt.gca().xaxis.set_major_formatter(ticker.FormatStrFormatter('%.2f'))
        plt.gca().yaxis.set_major_formatter(ticker.FormatStrFormatter('%.1f'))
        # 显示图例
        plt.legend(loc='upper center',bbox_to_anchor=(0.5, -0.24),fontsize=40, ncol=2,columnspacing=1)
        # 去除网格线
        plt.grid(False)
        plt.subplots_adjust(bottom=0.31)
        plt.savefig('./pdf/{}cases/pdf_DSM_k={}_1.png'.format(case_number,vel_k), dpi=300)  

        plt.close()  # 关闭当前图像，释放内存        
        
        
 