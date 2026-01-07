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
case_number_list =[30,1,10,20]
vel_k_list = [1,2,3,4,5,6,7,8,9,10]

for kk, case_number in enumerate(case_number_list):
    for k, vel_k in enumerate(vel_k_list):
        #-------------------------------------------------------------读入数据，
        ###小數點后3位###

        if vel_k in [1,2]:
            fDNS = np.round(np.loadtxt("./result/{}cases/error_with_time_fDNS_k={}.dat".format(case_number, vel_k), dtype=float), 3)
            DSM = np.round(np.loadtxt("./result/{}cases/error_with_time_DSM_k={}.dat".format(case_number, vel_k), dtype=float), 3)        
            IUFNO_40ep = np.round(np.loadtxt("./result/{}cases/error_with_time_IUFNO_k={}.dat".format(case_number, vel_k), dtype=float), 1)
            F_IUFNO_40ep = np.round(np.loadtxt("./result/{}cases/error_with_time_F_IUFNO_k={}.dat".format(case_number, vel_k), dtype=float), 1)
            F_IFNO_40ep = np.round(np.loadtxt("./result/{}cases/error_with_time_F_IFNO_k={}.dat".format(case_number, vel_k), dtype=float), 1)
            IFNO = np.round(np.loadtxt("./result/{}cases/error_with_time_IFNO_k={}.dat".format(case_number, vel_k), dtype=float), 1)       
            #IUFNO_40ep = np.loadtxt("./result/{}cases/error_with_time_IUFNO_k={}.dat".format(case_number, vel_k), dtype=float)
            #F_IUFNO_40ep = np.loadtxt("./result/{}cases/error_with_time_F_IUFNO_k={}.dat".format(case_number, vel_k), dtype=float)
            #F_IFNO_40ep = np.loadtxt("./result/{}cases/error_with_time_F_IFNO_k={}.dat".format(case_number, vel_k), dtype=float)
            #IFNO = np.loadtxt("./result/{}cases/error_with_time_IFNO_k={}.dat".format(case_number, vel_k), dtype=float)        
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
        colors = [
            '#FF0000', '#00FF00', '#0000FF', '#FFFF00', '#00FFFF',   # 原有5种颜色
            '#FF00FF', '#FFA500', '#800080', '#A52A2A', '#808080',
            '#000000', '#ADD8E6', '#90EE90', '#FFC0CB', '#FFD700', 
            '#EE82EE', '#008080', '#FF1493', '#4682B4', '#D3D3D3',
            '#00008B', '#C0C0C0', '#708090', '#DDA0DD', '#FF8C00',
            '#4682B4', '#FAEBD7', '#7CFC00', '#FF007F', '#B0C4DE',   # 新增
            '#FF6347', '#2E8B57', '#DAA520', '#B8860B', '#87CEFA',
            '#6495ED', '#BDB76B', '#F08080', '#FF4500', '#32CD32',
            '#8A2BE2', '#FF69B4', '#6A5ACD', '#FFDAB9', '#FFE4B5',
            '#BA55D3', '#00FA9A', '#F4A460', '#FFB6C1', '#00CED1', 
            '#DC143C', '#4169E1', '#4682B4', '#008000'                         # 新增颜色至50种
        ]
        
        # 绘制 PDF
        #1
        plt.figure(figsize=(9.5, 6), facecolor='none')  # 设置图形大小
        plt.rcParams['text.color'] = 'black'  # 字体颜色
        # 绘制直方图
        sns.distplot(data1, bins=50, hist=True, kde=False, hist_kws={'color':colors[0]}, norm_hist=True,label='Histogram')
        # 绘制核密度估计
        sns.distplot(data1, hist=False, kde=True, kde_kws={'color':colors[0], 'linestyle':'-'}, norm_hist=True,label='Kernel Density Estimate')
        # 图标题
        plt.title(r'Probability density function (PDF) of E(k={}) error: fDNS'.format(vel_k), fontsize=18)  
        plt.xlabel('Error', fontsize=18)  # x 轴标签
        plt.ylabel('Density', fontsize=18)  # y 轴标签
        plt.xticks(fontsize=20)  # x 轴刻度字体大小
        plt.yticks(fontsize=20)  # y 轴刻度字体大小
        plt.legend(loc='upper right', fontsize=18)  # 添加图例并设置位置
        # 设置边框颜色
        plt.gca().spines['top'].set_color('black')
        plt.gca().spines['right'].set_color('black')
        plt.gca().spines['left'].set_color('black')
        plt.gca().spines['bottom'].set_color('black')
        # 设置 x 轴和 y 轴的间隔
        x_ticks = np.arange(start=0, stop=max(data1), step=0.5)  # 根据需要设置间隔
        y_ticks = np.arange(start=0, stop=1.1, step=0.1)  # 根据需要设置间隔
        # 设置 x,y 轴刻度格式
        plt.gca().xaxis.set_major_formatter(ticker.FormatStrFormatter('%.3f'))
        plt.gca().yaxis.set_major_formatter(ticker.FormatStrFormatter('%.3f'))
        # 显示图例
        plt.legend(fontsize=16)
        # 去除网格线
        plt.grid(False)
        plt.savefig('./pdf/{}cases/pdf_fDNS_k={}.png'.format(case_number,vel_k), dpi=300)  

        plt.close()  # 关闭当前图像，释放内存


        #2
        plt.figure(figsize=(9.5, 6), facecolor='none')  # 设置图形大小
        plt.rcParams['text.color'] = 'black'  # 字体颜色
        # 绘制直方图
        sns.distplot(data2, bins=50, hist=True, kde=False, hist_kws={'color':colors[14]}, norm_hist=True,label='Histogram')
        # 绘制核密度估计
        sns.distplot(data2, hist=False, kde=True, kde_kws={'color':colors[14], 'linestyle':'-'}, norm_hist=True,label='Kernel Density Estimate')
        # 图标题
        plt.title(r'Probability density function (PDF) of E(k={}) error: IUFNO'.format(vel_k), fontsize=18)  
        plt.xlabel('Error', fontsize=18)  # x 轴标签
        plt.ylabel('Density', fontsize=18)  # y 轴标签
        plt.xticks(fontsize=20)  # x 轴刻度字体大小
        plt.yticks(fontsize=20)  # y 轴刻度字体大小
        plt.legend(loc='upper right', fontsize=18)  # 添加图例并设置位置
        # 设置边框颜色
        plt.gca().spines['top'].set_color('black')
        plt.gca().spines['right'].set_color('black')
        plt.gca().spines['left'].set_color('black')
        plt.gca().spines['bottom'].set_color('black')
        # 设置 x 轴和 y 轴的间隔
        x_ticks = np.arange(start=0, stop=max(data2), step=0.5)  # 根据需要设置间隔
        y_ticks = np.arange(start=0, stop=1.1, step=0.1)  # 根据需要设置间隔
        # 设置 x,y 轴刻度格式
        plt.gca().xaxis.set_major_formatter(ticker.FormatStrFormatter('%.3f'))
        plt.gca().yaxis.set_major_formatter(ticker.FormatStrFormatter('%.3f'))
        # 显示图例
        plt.legend(fontsize=16)
        # 去除网格线
        plt.grid(False)
        plt.savefig('./pdf/{}cases/pdf_IUFNO_k={}.png'.format(case_number,vel_k), dpi=300)

        plt.close()  # 关闭当前图像，释放内存

        #3
        plt.figure(figsize=(9.5, 6), facecolor='none')  # 设置图形大小
        plt.rcParams['text.color'] = 'black'  # 字体颜色
        # 绘制直方图
        sns.distplot(data3, bins=50, hist=True, kde=False, hist_kws={'color':colors[39]}, norm_hist=True,label='Histogram')
        # 绘制核密度估计
        sns.distplot(data3, hist=False, kde=True, kde_kws={'color':colors[39], 'linestyle':'-'}, norm_hist=True,label='Kernel Density Estimate')
        # 图标题
        plt.title(r'Probability density function (PDF) of E(k={}) error: F-IUFNO'.format(vel_k), fontsize=18)  
        plt.xlabel('Error', fontsize=18)  # x 轴标签
        plt.ylabel('Density', fontsize=18)  # y 轴标签
        plt.xticks(fontsize=20)  # x 轴刻度字体大小
        plt.yticks(fontsize=20)  # y 轴刻度字体大小
        plt.legend(loc='upper right', fontsize=18)  # 添加图例并设置位置
        # 设置边框颜色
        plt.gca().spines['top'].set_color('black')
        plt.gca().spines['right'].set_color('black')
        plt.gca().spines['left'].set_color('black')
        plt.gca().spines['bottom'].set_color('black')
        # 设置 x 轴和 y 轴的间隔
        x_ticks = np.arange(start=0, stop=max(data3), step=0.5)  # 根据需要设置间隔
        y_ticks = np.arange(start=0, stop=1.1, step=0.1)  # 根据需要设置间隔
        # 设置 x,y 轴刻度格式
        plt.gca().xaxis.set_major_formatter(ticker.FormatStrFormatter('%.3f'))
        plt.gca().yaxis.set_major_formatter(ticker.FormatStrFormatter('%.3f'))
        # 显示图例
        plt.legend(fontsize=16)
        # 去除网格线
        plt.grid(False)
        plt.savefig('./pdf/{}cases/pdf_F-IUFNO_k={}.png'.format(case_number,vel_k), dpi=300)

        plt.close()  # 关闭当前图像，释放内存
        #4
        plt.figure(figsize=(9.5, 6), facecolor='none')  # 设置图形大小
        plt.rcParams['text.color'] = 'black'  # 字体颜色
        # 绘制直方图
        sns.distplot(data4, bins=50, hist=True, kde=False, hist_kws={'color':colors[2]}, norm_hist=True,label='Histogram')
        # 绘制核密度估计
        sns.distplot(data4, hist=False, kde=True, kde_kws={'color':colors[2], 'linestyle':'-'}, norm_hist=True,label='Kernel Density Estimate')
        # 图标题
        plt.title(r'Probability density function (PDF) of E(k={}) error: F-IFNO'.format(vel_k), fontsize=18)  
        plt.xlabel('Error', fontsize=18)  # x 轴标签
        plt.ylabel('Density', fontsize=18)  # y 轴标签
        plt.xticks(fontsize=20)  # x 轴刻度字体大小
        plt.yticks(fontsize=20)  # y 轴刻度字体大小
        plt.legend(loc='upper right', fontsize=18)  # 添加图例并设置位置
        # 设置边框颜色
        plt.gca().spines['top'].set_color('black')
        plt.gca().spines['right'].set_color('black')
        plt.gca().spines['left'].set_color('black')
        plt.gca().spines['bottom'].set_color('black')
        # 设置 x 轴和 y 轴的间隔
        x_ticks = np.arange(start=0, stop=max(data4), step=0.5)  # 根据需要设置间隔
        y_ticks = np.arange(start=0, stop=1.1, step=0.1)  # 根据需要设置间隔
        # 设置 x,y 轴刻度格式
        plt.gca().xaxis.set_major_formatter(ticker.FormatStrFormatter('%.3f'))
        plt.gca().yaxis.set_major_formatter(ticker.FormatStrFormatter('%.3f'))
        # 显示图例
        plt.legend(fontsize=16)
        # 去除网格线
        plt.grid(False)
        plt.savefig('./pdf/{}cases/pdf_F-IFNO_k={}.png'.format(case_number,vel_k), dpi=300)

        plt.close()  # 关闭当前图像，释放内存  
        #5
        plt.figure(figsize=(9.5, 6), facecolor='none')  # 设置图形大小
        plt.rcParams['text.color'] = 'black'  # 字体颜色
        # 绘制直方图
        sns.distplot(data5, bins=50, hist=True, kde=False, hist_kws={'color':colors[28]}, norm_hist=True,label='Histogram')
        # 绘制核密度估计
        sns.distplot(data5, hist=False, kde=True, kde_kws={'color':colors[28], 'linestyle':'-'}, norm_hist=True,label='Kernel Density Estimate')
        # 图标题
        plt.title(r'Probability density function (PDF) of E(k={}) error: IFNO'.format(vel_k), fontsize=18)  
        plt.xlabel('Error', fontsize=18)  # x 轴标签
        plt.ylabel('Density', fontsize=18)  # y 轴标签
        plt.xticks(fontsize=20)  # x 轴刻度字体大小
        plt.yticks(fontsize=20)  # y 轴刻度字体大小
        plt.legend(loc='upper right', fontsize=18)  # 添加图例并设置位置
        # 设置边框颜色
        plt.gca().spines['top'].set_color('black')
        plt.gca().spines['right'].set_color('black')
        plt.gca().spines['left'].set_color('black')
        plt.gca().spines['bottom'].set_color('black')
        # 设置 x 轴和 y 轴的间隔
        x_ticks = np.arange(start=0, stop=max(data5), step=0.5)  # 根据需要设置间隔
        y_ticks = np.arange(start=0, stop=1.1, step=0.1)  # 根据需要设置间隔
        # 设置 x,y 轴刻度格式
        plt.gca().xaxis.set_major_formatter(ticker.FormatStrFormatter('%.3f'))
        plt.gca().yaxis.set_major_formatter(ticker.FormatStrFormatter('%.3f'))
        # 显示图例
        plt.legend(fontsize=16)
        # 去除网格线
        plt.grid(False)
        plt.savefig('./pdf/{}cases/pdf_IFNO_k={}.png'.format(case_number,vel_k), dpi=300)

        plt.close()  # 关闭当前图像，释放内存
        #6
        plt.figure(figsize=(9.5, 6), facecolor='none')  # 设置图形大小
        plt.rcParams['text.color'] = 'black'  # 字体颜色
        # 绘制直方图
        sns.distplot(data6, bins=50, hist=True, kde=False, hist_kws={'color':colors[7]}, norm_hist=True,label='Histogram')
        # 绘制核密度估计
        sns.distplot(data6, hist=False, kde=True, kde_kws={'color':colors[7], 'linestyle':'-'}, norm_hist=True,label='Kernel Density Estimate')
        # 图标题
        plt.title(r'Probability density function (PDF) of E(k={}) error: DSM'.format(vel_k), fontsize=18)  
        plt.xlabel('Error', fontsize=18)  # x 轴标签
        plt.ylabel('Density', fontsize=18)  # y 轴标签
        plt.xticks(fontsize=20)  # x 轴刻度字体大小
        plt.yticks(fontsize=20)  # y 轴刻度字体大小
        plt.legend(loc='upper right', fontsize=18)  # 添加图例并设置位置
        # 设置边框颜色
        plt.gca().spines['top'].set_color('black')
        plt.gca().spines['right'].set_color('black')
        plt.gca().spines['left'].set_color('black')
        plt.gca().spines['bottom'].set_color('black')
        # 设置 x 轴和 y 轴的间隔
        x_ticks = np.arange(start=0, stop=max(data6), step=0.5)  # 根据需要设置间隔
        y_ticks = np.arange(start=0, stop=1.1, step=0.1)  # 根据需要设置间隔
        # 设置 x,y 轴刻度格式
        plt.gca().xaxis.set_major_formatter(ticker.FormatStrFormatter('%.3f'))
        plt.gca().yaxis.set_major_formatter(ticker.FormatStrFormatter('%.3f'))
        # 显示图例
        plt.legend(fontsize=16)
        # 去除网格线
        plt.grid(False)
        plt.savefig('./pdf/{}cases/pdf_DSM_k={}.png'.format(case_number,vel_k), dpi=300)

        plt.close()  # 关闭当前图像，释放内存