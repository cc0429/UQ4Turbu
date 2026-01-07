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

case_number_list =[30,1,10,20]
# 定义高斯函数
def gaussian(x, amplitude, mean, std):
    return amplitude * np.exp(-0.5 * ((x - mean) / std) ** 2)
  
for k, case_number in enumerate(case_number_list):

    #-------------------------------------------------------------读入数据，


    fDNS = np.loadtxt("./result/{}cases/error_with_time_fDNS.dat".format(case_number), dtype=float)
    F_IUFNO_40ep = np.loadtxt("./result/{}cases/error_with_time_F_IUFNO.dat".format(case_number), dtype=float)
    F_IFNO_40ep = np.loadtxt("./result/{}cases/error_with_time_F_IFNO.dat".format(case_number), dtype=float)
    IUFNO_40ep = np.loadtxt("./result/{}cases/error_with_time_IUFNO.dat".format(case_number), dtype=float)    
    DSM = np.loadtxt("./result/{}cases/error_with_time_DSM.dat".format(case_number), dtype=float)
    IFNO = np.loadtxt("./result/{}cases/error_with_time_IFNO.dat".format(case_number), dtype=float)
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
        '#DC143C', '#4169E1', '#4682B4', '#008000'                      # 新增颜色至50种
    ]

    # 绘制 PDF
    #1
    plt.figure(figsize=(9.6, 6.5), facecolor='none')  # 设置图形大小
    plt.rcParams['text.color'] = 'black'  # 字体颜色
  
   # 直方图数据
    hist, bin_edges = np.histogram(data1, bins=50, density=True)
    bin_centers = (bin_edges[:-1] + bin_edges[1:]) / 2

    # 使用 scipy.stats.norm.fit 来拟合高斯分布
    mu, std = norm.fit(data1)

    #fit
    x = np.linspace(min(data1), max(data1),  2000)
    pdf = norm.pdf(x, mu, std)

    #plot
    plt.plot(x, pdf, 'k-', label=f"Fit: $\mu={mu:.4f}, \sigma={std:.4f}$", linewidth=2,zorder=2)
    #绘制原始频率密度曲线（虚线）
    plt.plot(bin_centers, hist, linestyle="--", color=colors[0], label='Data density', linewidth=2,zorder=1)
    # 绘制直方圖结果
    plt.hist(data1, bins=50, density=True,alpha=0.6,color=colors[0], label='Data histogram',zorder=0)
    plt.rcParams['mathtext.fontset'] = 'cm'
    plt.title(r'Normal distribution fit for $\mathrm{E_k}$ error: fDNS', fontsize=24) 
    plt.xlabel('Error', fontsize=24)  # x 轴标签
    plt.ylabel('Density', fontsize=24)  # y 轴标签
    plt.xticks(fontsize=24)  # x 轴刻度字体大小
    plt.yticks(fontsize=24)  # y 轴刻度字体大小
    plt.legend(loc='upper right', fontsize=24)  # 添加图例并设置位置
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
    plt.gca().yaxis.set_major_formatter(ticker.FormatStrFormatter('%.2f'))
    # 显示图例
    plt.legend(fontsize=24)
    # 去除网格线
    plt.grid(False)
    plt.savefig('./GSfit/{}cases/GSfit_fDNS.png'.format(case_number), dpi=300)  

    plt.close()  # 关闭当前图像，释放内存

        


    #2
    plt.figure(figsize=(9.6, 6.5), facecolor='none')  # 设置图形大小
    plt.rcParams['text.color'] = 'black'  # 字体颜色
  
   # 直方图数据
    hist, bin_edges = np.histogram(data2, bins=50, density=True)
    bin_centers = (bin_edges[:-1] + bin_edges[1:]) / 2
    
    # 使用 skewnorm.fit() 进行偏态正态分布的拟合
    alpha_fit, mu_fit, sigma_fit = skewnorm.fit(data2) 
    # 绘制拟合结果的概率密度函数图
    x = np.linspace(min(data2), max(data2), 2000)
    pdf= skewnorm.pdf(x, a=alpha_fit, loc=mu_fit, scale=sigma_fit)    
    #plot
    plt.plot(x, pdf, 'k-',linewidth=2, zorder=2,label=f'Fit: $\\alpha={alpha_fit:.4f}$, $\\mu={mu_fit:.4f}$, $\\sigma={sigma_fit:.4f}$')
    #绘制原始频率密度曲线（虚线）
    plt.plot(bin_centers, hist, linestyle="--", color=colors[39], label='Data density', linewidth=2,zorder=1)
    # 绘制直方圖结果
    plt.hist(data2, bins=50, density=True,alpha=0.6,color=colors[39], label='Data histogram',zorder=0)
    plt.rcParams['mathtext.fontset'] = 'cm'
    plt.title(r'Skew normal distribution fit for $\mathrm{E_k}$ error: F-IUFNO', fontsize=24) 
    plt.xlabel('Error', fontsize=24)  # x 轴标签
    plt.ylabel('Density', fontsize=24)  # y 轴标签
    plt.xticks(fontsize=24)  # x 轴刻度字体大小
    plt.yticks(fontsize=24)  # y 轴刻度字体大小
    plt.legend(loc='upper right', fontsize=24)  # 添加图例并设置位置
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
    plt.gca().yaxis.set_major_formatter(ticker.FormatStrFormatter('%.2f'))
    # 显示图例
    plt.legend(fontsize=24)
    # 去除网格线
    plt.grid(False)
    plt.savefig('./GSfit/{}cases/GSfit_F-IUFNO.png'.format(case_number), dpi=300)  

    plt.close()  # 关闭当前图像，释放内存
       
    
    #3
    plt.figure(figsize=(9.6, 6.5), facecolor='none')  # 设置图形大小
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
    plt.plot(x, pdf, 'k-',linewidth=2, zorder=2,label=f'Fit: $\\alpha={alpha_fit:.4f}$, $\\mu={mu_fit:.4f}$, $\\sigma={sigma_fit:.4f}$')
    #绘制原始频率密度曲线（虚线）
    plt.plot(bin_centers, hist, linestyle="--", color=colors[2], label='Data density', linewidth=2,zorder=1)
    # 绘制直方圖结果
    plt.hist(data3, bins=50, density=True,alpha=0.6,color=colors[2], label='Data histogram',zorder=0)
    plt.rcParams['mathtext.fontset'] = 'cm'
    plt.title(r'Skew normal distribution fit for $\mathrm{E_k}$ error: F-IFNO', fontsize=24) 
    plt.xlabel('Error', fontsize=24)  # x 轴标签
    plt.ylabel('Density', fontsize=24)  # y 轴标签
    plt.xticks(fontsize=24)  # x 轴刻度字体大小
    plt.yticks(fontsize=24)  # y 轴刻度字体大小
    plt.legend(loc='upper right', fontsize=24)  # 添加图例并设置位置
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
    plt.gca().yaxis.set_major_formatter(ticker.FormatStrFormatter('%.2f'))
    # 显示图例
    plt.legend(fontsize=24)
    # 去除网格线
    plt.grid(False)
    plt.savefig('./GSfit/{}cases/GSfit_F-IFNO.png'.format(case_number), dpi=300)  

    plt.close()  # 关闭当前图像，释放内存
    


    #4
    plt.figure(figsize=(9.6, 6.5), facecolor='none')  # 设置图形大小
    plt.rcParams['text.color'] = 'black'  # 字体颜色
  
   # 直方图数据
    hist, bin_edges = np.histogram(data4, bins=50, density=True)
    bin_centers = (bin_edges[:-1] + bin_edges[1:]) / 2

    # 使用 scipy.stats.norm.fit 来拟合高斯分布
    mu, std = norm.fit(data4)

    #fit
    x = np.linspace(min(data4), max(data4),  2000)
    pdf = norm.pdf(x, mu, std)

    #plot
    plt.plot(x, pdf, 'k-', label=f"Fit: $\mu={mu:.4f}, \sigma={std:.4f}$", linewidth=2,zorder=2)
    #绘制原始频率密度曲线（虚线）
    plt.plot(bin_centers, hist, linestyle="--", color=colors[7], label='Data density', linewidth=2,zorder=1)
    # 绘制直方圖结果
    plt.hist(data4, bins=50, density=True,alpha=0.6,color=colors[7], label='Data histogram',zorder=0)
    plt.rcParams['mathtext.fontset'] = 'cm'
    plt.title(r'Normal distribution fit for $\mathrm{E_k}$ error: DSM', fontsize=24) 
    plt.xlabel('Error', fontsize=24)  # x 轴标签
    plt.ylabel('Density', fontsize=24)  # y 轴标签
    plt.xticks(fontsize=24)  # x 轴刻度字体大小
    plt.yticks(fontsize=24)  # y 轴刻度字体大小
    plt.legend(loc='upper right', fontsize=24)  # 添加图例并设置位置
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
    plt.gca().yaxis.set_major_formatter(ticker.FormatStrFormatter('%.2f'))
    # 显示图例
    plt.legend(fontsize=24)
    # 去除网格线
    plt.grid(False)
    plt.savefig('./GSfit/{}cases/GSfit_DSM.png'.format(case_number), dpi=300)  

    plt.close()  # 关闭当前图像，释放内存
 
         
        
    #5
    plt.figure(figsize=(9.6, 6.5), facecolor='none')  # 设置图形大小
    plt.rcParams['text.color'] = 'black'  # 字体颜色
  
   # 直方图数据
    hist, bin_edges = np.histogram(data5, bins=50, density=True)
    bin_centers = (bin_edges[:-1] + bin_edges[1:]) / 2
    
    # 使用 skewnorm.fit() 进行偏态正态分布的拟合
    alpha_fit, mu_fit, sigma_fit = skewnorm.fit(data5) 
    # 绘制拟合结果的概率密度函数图
    x = np.linspace(min(data5), max(data5), 2000)
    pdf= skewnorm.pdf(x, a=alpha_fit, loc=mu_fit, scale=sigma_fit)    
    #plot
    plt.plot(x, pdf, 'k-',linewidth=2, zorder=2,label=f'Fit: $\\alpha={alpha_fit:.4f}$, $\\mu={mu_fit:.4f}$, $\\sigma={sigma_fit:.4f}$')
    #绘制原始频率密度曲线（虚线）
    plt.plot(bin_centers, hist, linestyle="--", color=colors[14], label='Data density', linewidth=2,zorder=1)
    # 绘制直方圖结果
    plt.hist(data5, bins=50, density=True,alpha=0.6,color=colors[14], label='Data histogram',zorder=0)
    plt.rcParams['mathtext.fontset'] = 'cm'
    plt.title(r'Skew normal distribution fit for $\mathrm{E_k}$ error: IUFNO', fontsize=24) 
    plt.xlabel('Error', fontsize=24)  # x 轴标签
    plt.ylabel('Density', fontsize=24)  # y 轴标签
    plt.xticks(fontsize=24)  # x 轴刻度字体大小
    plt.yticks(fontsize=24)  # y 轴刻度字体大小
    plt.legend(loc='upper right', fontsize=24)  # 添加图例并设置位置
    # 设置边框颜色
    plt.gca().spines['top'].set_color('black')
    plt.gca().spines['right'].set_color('black')
    plt.gca().spines['left'].set_color('black')
    plt.gca().spines['bottom'].set_color('black')
    # 设置 x 轴和 y 轴的间隔
    x_ticks = np.arange(start=0, stop=max(data5), step=0.5)  # 根据需要设置间隔
    y_ticks = np.arange(start=0, stop=1.1, step=0.1)  # 根据需要设置间隔
    # 设置 x,y 轴刻度格式
    plt.gca().xaxis.set_major_formatter(ticker.FormatStrFormatter('%.2f'))
    plt.gca().yaxis.set_major_formatter(ticker.FormatStrFormatter('%.2f'))
    # 显示图例
    plt.legend(fontsize=24)
    # 去除网格线
    plt.grid(False)
    plt.savefig('./GSfit/{}cases/GSfit_IUFNO.png'.format(case_number), dpi=300)  

    plt.close()  # 关闭当前图像，释放内存
    

        



    #6
    plt.figure(figsize=(9.6, 6.5), facecolor='none')  # 设置图形大小
    plt.rcParams['text.color'] = 'black'  # 字体颜色
  
   # 直方图数据
    hist, bin_edges = np.histogram(data6, bins=50, density=True)
    bin_centers = (bin_edges[:-1] + bin_edges[1:]) / 2
    
    # 使用 skewnorm.fit() 进行偏态正态分布的拟合
    alpha_fit, mu_fit, sigma_fit = skewnorm.fit(data6) 
    # 绘制拟合结果的概率密度函数图
    x = np.linspace(min(data6), max(data6), 2000)
    pdf= skewnorm.pdf(x, a=alpha_fit, loc=mu_fit, scale=sigma_fit)    
    #plot
    plt.plot(x, pdf, 'k-',linewidth=2, zorder=2,label=f'Fit: $\\alpha={alpha_fit:.4f}$, $\\mu={mu_fit:.4f}$, $\\sigma={sigma_fit:.4f}$')
    #绘制原始频率密度曲线（虚线）
    plt.plot(bin_centers, hist, linestyle="--", color=colors[28], label='Data density', linewidth=2,zorder=1)
    # 绘制直方圖结果
    plt.hist(data6, bins=50, density=True,alpha=0.6,color=colors[28], label='Data histogram',zorder=0)
    plt.rcParams['mathtext.fontset'] = 'cm'
    plt.title(r'Skew normal distribution fit for $\mathrm{E_k}$ error: IFNO', fontsize=24) 
    plt.xlabel('Error', fontsize=24)  # x 轴标签
    plt.ylabel('Density', fontsize=24)  # y 轴标签
    plt.xticks(fontsize=24)  # x 轴刻度字体大小
    plt.yticks(fontsize=24)  # y 轴刻度字体大小
    plt.legend(loc='upper right', fontsize=24)  # 添加图例并设置位置
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
    plt.gca().yaxis.set_major_formatter(ticker.FormatStrFormatter('%.2f'))
    # 显示图例
    plt.legend(fontsize=24)
    # 去除网格线
    plt.grid(False)
    plt.savefig('./GSfit/{}cases/GSfit_IFNO.png'.format(case_number), dpi=300)  

    plt.close()  # 关闭当前图像，释放内存
    
 
        
####################################################################################################################       
 
    #1
    plt.figure(figsize=(9.6, 6.5), facecolor='none')  # 设置图形大小
    plt.rcParams['text.color'] = 'black'  # 字体颜色
  
   # 直方图数据
    hist, bin_edges = np.histogram(data2, bins=50, density=True)
    bin_centers = (bin_edges[:-1] + bin_edges[1:]) / 2

    # 使用 scipy.stats.norm.fit 来拟合高斯分布
    mu, std = norm.fit(data2)

    #fit
    x = np.linspace(min(data2), max(data2),  2000)
    pdf = norm.pdf(x, mu, std)

    #plot
    plt.plot(x, pdf, 'k-', label=f"Fit: $\mu={mu:.4f}, \sigma={std:.4f}$", linewidth=2,zorder=2)
    #绘制原始频率密度曲线（虚线）
    plt.plot(bin_centers, hist, linestyle="--", color=colors[39], label='Data density', linewidth=2,zorder=1)
    # 绘制直方圖结果
    plt.hist(data2, bins=50, density=True,alpha=0.6,color=colors[39], label='Data histogram',zorder=0)
    plt.rcParams['mathtext.fontset'] = 'cm'
    plt.title(r'Normal distribution fit for $\mathrm{E_k}$ error: F-IUFNO', fontsize=24) 
    plt.xlabel('Error', fontsize=24)  # x 轴标签
    plt.ylabel('Density', fontsize=24)  # y 轴标签
    plt.xticks(fontsize=24)  # x 轴刻度字体大小
    plt.yticks(fontsize=24)  # y 轴刻度字体大小
    plt.legend(loc='upper right', fontsize=24)  # 添加图例并设置位置
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
    plt.gca().yaxis.set_major_formatter(ticker.FormatStrFormatter('%.2f'))
    # 显示图例
    plt.legend(fontsize=24)
    # 去除网格线
    plt.grid(False)
    plt.savefig('./GSfit/{}cases/GSfit_F-IUFNO_gs.png'.format(case_number), dpi=300)  

    plt.close()  # 关闭当前图像，释放内存
 

        
    #2
    plt.figure(figsize=(9.6, 6.5), facecolor='none')  # 设置图形大小
    plt.rcParams['text.color'] = 'black'  # 字体颜色
  
   # 直方图数据
    hist, bin_edges = np.histogram(data3, bins=50, density=True)
    bin_centers = (bin_edges[:-1] + bin_edges[1:]) / 2

    # 使用 scipy.stats.norm.fit 来拟合高斯分布
    mu, std = norm.fit(data3)

    #fit
    x = np.linspace(min(data3), max(data3),  2000)
    pdf = norm.pdf(x, mu, std)

    #plot
    plt.plot(x, pdf, 'k-', label=f"Fit: $\mu={mu:.4f}, \sigma={std:.4f}$", linewidth=2,zorder=2)
    #绘制原始频率密度曲线（虚线）
    plt.plot(bin_centers, hist, linestyle="--", color=colors[2], label='Data density', linewidth=2,zorder=1)
    # 绘制直方圖结果
    plt.hist(data3, bins=50, density=True,alpha=0.6,color=colors[2], label='Data histogram',zorder=0)
    plt.rcParams['mathtext.fontset'] = 'cm'
    plt.title(r'Normal distribution fit for $\mathrm{E_k}$ error: F-IFNO', fontsize=24) 
    plt.xlabel('Error', fontsize=24)  # x 轴标签
    plt.ylabel('Density', fontsize=24)  # y 轴标签
    plt.xticks(fontsize=24)  # x 轴刻度字体大小
    plt.yticks(fontsize=24)  # y 轴刻度字体大小
    plt.legend(loc='upper right', fontsize=24)  # 添加图例并设置位置
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
    plt.gca().yaxis.set_major_formatter(ticker.FormatStrFormatter('%.2f'))
    # 显示图例
    plt.legend(fontsize=24)
    # 去除网格线
    plt.grid(False)
    plt.savefig('./GSfit/{}cases/GSfit_F-IFNO_gs.png'.format(case_number), dpi=300)  

    plt.close()  # 关闭当前图像，释放内存
 

        
 
    #3
    plt.figure(figsize=(9.6, 6.5), facecolor='none')  # 设置图形大小
    plt.rcParams['text.color'] = 'black'  # 字体颜色
  
   # 直方图数据
    hist, bin_edges = np.histogram(data5, bins=50, density=True)
    bin_centers = (bin_edges[:-1] + bin_edges[1:]) / 2

    # 使用 scipy.stats.norm.fit 来拟合高斯分布
    mu, std = norm.fit(data5)

    #fit
    x = np.linspace(min(data5), max(data5),  2000)
    pdf = norm.pdf(x, mu, std)

    #plot
    plt.plot(x, pdf, 'k-', label=f"Fit: $\mu={mu:.4f}, \sigma={std:.4f}$", linewidth=2,zorder=2)
    #绘制原始频率密度曲线（虚线）
    plt.plot(bin_centers, hist, linestyle="--", color=colors[14], label='Data density', linewidth=2,zorder=1)
    # 绘制直方圖结果
    plt.hist(data5, bins=50, density=True,alpha=0.6,color=colors[14], label='Data histogram',zorder=0)
    plt.rcParams['mathtext.fontset'] = 'cm'
    plt.title(r'Normal distribution fit for $\mathrm{E_k}$ error: IUFNO', fontsize=24) 
    plt.xlabel('Error', fontsize=24)  # x 轴标签
    plt.ylabel('Density', fontsize=24)  # y 轴标签
    plt.xticks(fontsize=24)  # x 轴刻度字体大小
    plt.yticks(fontsize=24)  # y 轴刻度字体大小
    plt.legend(loc='upper right', fontsize=24)  # 添加图例并设置位置
    # 设置边框颜色
    plt.gca().spines['top'].set_color('black')
    plt.gca().spines['right'].set_color('black')
    plt.gca().spines['left'].set_color('black')
    plt.gca().spines['bottom'].set_color('black')
    # 设置 x 轴和 y 轴的间隔
    x_ticks = np.arange(start=0, stop=max(data5), step=0.5)  # 根据需要设置间隔
    y_ticks = np.arange(start=0, stop=1.1, step=0.1)  # 根据需要设置间隔
    # 设置 x,y 轴刻度格式
    plt.gca().xaxis.set_major_formatter(ticker.FormatStrFormatter('%.2f'))
    plt.gca().yaxis.set_major_formatter(ticker.FormatStrFormatter('%.2f'))
    # 显示图例
    plt.legend(fontsize=24)
    # 去除网格线
    plt.grid(False)
    plt.savefig('./GSfit/{}cases/GSfit_IUFNO_gs.png'.format(case_number), dpi=300)  

    plt.close()  # 关闭当前图像，释放内存
 

        
    #4
    plt.figure(figsize=(9.6, 6.5), facecolor='none')  # 设置图形大小
    plt.rcParams['text.color'] = 'black'  # 字体颜色
  
   # 直方图数据
    hist, bin_edges = np.histogram(data6, bins=50, density=True)
    bin_centers = (bin_edges[:-1] + bin_edges[1:]) / 2

    # 使用 scipy.stats.norm.fit 来拟合高斯分布
    mu, std = norm.fit(data6)

    #fit
    x = np.linspace(min(data6), max(data6),  2000)
    pdf = norm.pdf(x, mu, std)

    #plot
    plt.plot(x, pdf, 'k-', label=f"Fit: $\mu={mu:.4f}, \sigma={std:.4f}$", linewidth=2,zorder=2)
    #绘制原始频率密度曲线（虚线）
    plt.plot(bin_centers, hist, linestyle="--", color=colors[28], label='Data density', linewidth=2,zorder=1)
    # 绘制直方圖结果
    plt.hist(data6, bins=50, density=True,alpha=0.6,color=colors[28], label='Data histogram',zorder=0)
    plt.rcParams['mathtext.fontset'] = 'cm'
    plt.title(r'Normal distribution fit for $\mathrm{E_k}$ error: IFNO', fontsize=24) 
    plt.xlabel('Error', fontsize=24)  # x 轴标签
    plt.ylabel('Density', fontsize=24)  # y 轴标签
    plt.xticks(fontsize=24)  # x 轴刻度字体大小
    plt.yticks(fontsize=24)  # y 轴刻度字体大小
    plt.legend(loc='upper right', fontsize=24)  # 添加图例并设置位置
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
    plt.gca().yaxis.set_major_formatter(ticker.FormatStrFormatter('%.2f'))
    # 显示图例
    plt.legend(fontsize=24)
    # 去除网格线
    plt.grid(False)
    plt.savefig('./GSfit/{}cases/GSfit_IFNO_gs.png'.format(case_number), dpi=300)  

    plt.close()  # 关闭当前图像，释放内存
           
