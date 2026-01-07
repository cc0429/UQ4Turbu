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
from matplotlib.lines import Line2D
case_number_list =[30]
# 定义高斯函数
def gaussian(x, amplitude, mean, std):
    return amplitude * np.exp(-0.5 * ((x - mean) / std) ** 2)
# 自定义图例元素

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

    colors = ['#A52A2A','#ff7f0e','#ffd700','green','#1f77b4','purple']
    # 绘制 PDF
    #1
    plt.figure(figsize=(14, 10.5), facecolor='none')  # 设置图形大小
    plt.rcParams['text.color'] = 'black'  # 字体颜色
    #plt.rcParams['mathtext.fontset'] = 'cm'
  
   # 直方图数据
    hist, bin_edges = np.histogram(data1, bins=50, density=True)
    bin_centers = (bin_edges[:-1] + bin_edges[1:]) / 2

    # 使用 scipy.stats.norm.fit 来拟合高斯分布
    mu, std = norm.fit(data1)

    #fit
    x = np.linspace(min(data1), max(data1),  2000)
    pdf = norm.pdf(x, mu, std)

    #plot
    plt.plot(x, pdf, 'k-', label=f"Fit: $\mu={mu:.4f}, \sigma={std:.4f}$", linewidth=4,zorder=2)
    #绘制原始频率密度曲线（虚线）
    plt.plot(bin_centers, hist, linestyle="--", color=colors[5], label='Data density', linewidth=4,zorder=1)
    # 绘制直方圖结果
    plt.hist(data1, bins=50, density=True,alpha=0.4,color=colors[5], label='Data histogram',zorder=0)
    plt.rcParams['mathtext.fontset'] = 'cm'
    plt.title(r'Normal distribution fit for $\mathrm{E_k}$ fluctuation: fDNS', fontsize=40, pad=10) 
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
    plt.gca().yaxis.set_major_formatter(ticker.FormatStrFormatter('%.2f'))
    
    handles, labels = plt.gca().get_legend_handles_labels()    
    handles = [handles[1], handles[0], handles[2]]
    labels = [labels[1], labels[0], labels[2]]
   
    # 显示图例
    plt.legend(handles=handles,labels=labels,loc='upper center',bbox_to_anchor=(0.5, -0.18),fontsize=40, ncol=2,columnspacing=-5)
    # 去除网格线
    plt.grid(False)
    #plt.ylim(0, 10) 
    plt.subplots_adjust(bottom=0.31)
    plt.savefig('./GSfit/{}cases/GSfit_fDNS.png'.format(case_number), dpi=300)  

    plt.close()  # 关闭当前图像，释放内存
 
    # 计算数据的均值和标准差
    loc, scale = np.mean(data1), np.std(data1) 
    # Kolmogorov-Smirnov 检验
    ks_stat, p_value = kstest(data1, 'norm', args=(loc, scale))
    # 检验结果解释
    result = "拟合结果较好，数据可以认为符合偏态正态分布" if p_value > 0.05 else "拟合结果不理想，可能需要更复杂的分布模型"
    # 保存到 .dat 文件
    output_file = "./GSfit/{}cases/ks_test_results_fDNS.dat".format(case_number)
    with open(output_file, "w") as file:
        file.write("Kolmogorov-Smirnov 检验结果:\n")
        file.write(f"KS Statistic: {ks_stat:.6f}\n")
        file.write(f"P-Value: {p_value:.6f}\n")
        file.write(f"解释: {result}\n")

    #QQ   
    # 常见分布的定义
    distributions = {
        "Normal": stats.norm,
        "LogNormal": stats.lognorm(s=1),  # 对数正态分布的标准形状参数
        "Exponential": stats.expon,
        "Gamma": stats.gamma(a=2),  # 伽马分布的形状参数
        "Skew normal": stats.skewnorm,  # 偏态正态分布
        "Student's t": stats.t,  # 学生 t 分布
    }

    # 创建一个 2x3 的子图来显示不同分布的 QQ 图（多加了一个分布）
    plt.figure(figsize=(18, 10))

    # 绘制每个分布的 QQ 图
    for i, (dist_name, dist) in enumerate(distributions.items(), 1):
        plt.subplot(2, 3, i)  # 2x3 布局以容纳更多子图
        if dist_name == "Skew normal":
            # 偏态分布需要指定形状参数（例如，偏度参数 a）
            a = 0 # 偏态参数，调整为适合的数据
            stats.probplot(data1, dist=dist, sparams=(a,), plot=plt)
            # 注释偏态分布参数
            plt.text(0.05, 0.95, rf'$\alpha = {a:.4f}$', transform=plt.gca().transAxes, fontsize=21, verticalalignment='top')
        elif dist_name == "Student's t":
            # 学生 t 分布需要指定自由度参数 df
            df = 5  # 这里假设自由度 df=5，调整为适合的数据
            stats.probplot(data1, dist=dist, sparams=(df,), plot=plt)
            # 注释学生 t 分布参数
            plt.text(0.05, 0.95, f'df = {df:.4f}', transform=plt.gca().transAxes, fontsize=21, verticalalignment='top')
        elif dist_name == "LogNormal":
            # 对数正态分布的标准形状参数 s = 1
            stats.probplot(data1, dist=dist, plot=plt)
            # 注释对数正态分布参数
            plt.text(0.05, 0.95, f's = 1.0000', transform=plt.gca().transAxes, fontsize=21, verticalalignment='top')
        elif dist_name == "Gamma":
            # 伽马分布的形状参数 a = 2
            stats.probplot(data1, dist=dist, plot=plt)
            # 注释伽马分布参数
            aa=2.000
            plt.text(0.05, 0.95, rf'$\alpha = {aa:.4f}$', transform=plt.gca().transAxes, fontsize=21, verticalalignment='top')
        else:
            stats.probplot(data1, dist=dist, plot=plt)
            
        plt.rcParams['mathtext.fontset'] = 'cm'    
        plt.title(fr"QQ Plot of {dist_name} for $\mathrm{{E_k}}$ fluctuation: fDNS", fontsize=21)

        # 设置刻度字体大小
        plt.xticks(fontsize=21)
        plt.yticks(fontsize=21)
        plt.gca().get_lines()[1].set_linewidth(4)
        # 设置坐标轴标签字体大小（Q-Q 图自动生成了 "Theoretical Quantiles" 和 "Ordered Values"）
        ax = plt.gca()
        ax.set_xlabel(ax.get_xlabel(), fontsize=21)
        ax.set_ylabel(ax.get_ylabel(), fontsize=21)

    plt.tight_layout()      
    plt.savefig('./GSfit/{}cases/QQPlot_fDNS.png'.format(case_number), dpi=300) 
        


    #2
    plt.figure(figsize=(14, 10.5), facecolor='none')  # 设置图形大小
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
    plt.plot(x, pdf, 'k-',linewidth=4, zorder=2,label=f'Fit: $\\alpha={alpha_fit:.4f}$, $\\mu={mu_fit:.4f}$, $\\sigma={sigma_fit:.4f}$')
    #绘制原始频率密度曲线（虚线）
    plt.plot(bin_centers, hist, linestyle="--", color=colors[1], label='Data density', linewidth=4,zorder=1)
    # 绘制直方圖结果
    plt.hist(data2, bins=50, density=True,alpha=0.4,color=colors[1], label='Data histogram',zorder=0)
    plt.rcParams['mathtext.fontset'] = 'cm'
    plt.title(r'Skew normal distribution fit for $\mathrm{E_k}$ error: F-IUFNO', fontsize=40, pad=10) 
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
    plt.gca().yaxis.set_major_formatter(ticker.FormatStrFormatter('%.2f'))
    handles, labels = plt.gca().get_legend_handles_labels()    
    handles = [handles[1], handles[0], handles[2]]
    labels = [labels[1], labels[0], labels[2]]      
    # 显示图例
    plt.legend(handles=handles,labels=labels,loc='upper center',bbox_to_anchor=(0.5, -0.18),fontsize=40, ncol=2,columnspacing=-5)
    # 去除网格线
    plt.grid(False)
    #plt.ylim(0, 10) 
    plt.subplots_adjust(bottom=0.31)
    plt.savefig('./GSfit/{}cases/GSfit_F-IUFNO.png'.format(case_number), dpi=300)  

    plt.close()  # 关闭当前图像，释放内存
    
    # Kolmogorov-Smirnov 检验
    ks_stat, p_value = ks_2samp(data2, skewnorm.rvs(a=alpha_fit, loc=mu_fit, scale=sigma_fit, size=len(data2)))
    # 检验结果解释
    result = "拟合结果较好，数据可以认为符合偏态正态分布" if p_value > 0.05 else "拟合结果不理想，可能需要更复杂的分布模型"
    # 保存到 .dat 文件
    output_file = "./GSfit/{}cases/ks_test_results_F-IUFNO.dat".format(case_number)
    with open(output_file, "w") as file:
        file.write("Kolmogorov-Smirnov 检验结果:\n")
        file.write(f"KS Statistic: {ks_stat:.6f}\n")
        file.write(f"P-Value: {p_value:.6f}\n")
        file.write(f"解释: {result}\n")
        
    #QQ   
    # 常见分布的定义
    distributions = {
        "Normal": stats.norm,
        "LogNormal": stats.lognorm(s=1),  # 对数正态分布的标准形状参数
        "Exponential": stats.expon,
        "Gamma": stats.gamma(a=2),  # 伽马分布的形状参数
        "Skew normal": stats.skewnorm,  # 偏态正态分布
        "Student's t": stats.t,  # 学生 t 分布
    }

    # 创建一个 2x3 的子图来显示不同分布的 QQ 图（多加了一个分布）
    plt.figure(figsize=(18, 10))

    # 绘制每个分布的 QQ 图
    for i, (dist_name, dist) in enumerate(distributions.items(), 1):
        plt.subplot(2, 3, i)  # 2x3 布局以容纳更多子图
        if dist_name == "Skew normal":
            # 偏态分布需要指定形状参数（例如，偏度参数 a）
            a = alpha_fit # 偏态参数，调整为适合的数据
            stats.probplot(data2, dist=dist, sparams=(a,), plot=plt)
            # 注释偏态分布参数
            plt.text(0.05, 0.95, rf'$\alpha = {a:.4f}$', transform=plt.gca().transAxes, fontsize=21, verticalalignment='top')
        elif dist_name == "Student's t":
            # 学生 t 分布需要指定自由度参数 df
            df = 5  # 这里假设自由度 df=5，调整为适合的数据
            stats.probplot(data2, dist=dist, sparams=(df,), plot=plt)
            # 注释学生 t 分布参数
            plt.text(0.05, 0.95, f'df = {df:.4f}', transform=plt.gca().transAxes, fontsize=21, verticalalignment='top')
        elif dist_name == "LogNormal":
            # 对数正态分布的标准形状参数 s = 1
            stats.probplot(data2, dist=dist, plot=plt)
            # 注释对数正态分布参数
            plt.text(0.05, 0.95, f's = 1.0000', transform=plt.gca().transAxes, fontsize=21, verticalalignment='top')
        elif dist_name == "Gamma":
            # 伽马分布的形状参数 a = 2
            stats.probplot(data2, dist=dist, plot=plt)
            # 注释伽马分布参数
            aa=2.000
            plt.text(0.05, 0.95, rf'$\alpha = {aa:.4f}$', transform=plt.gca().transAxes, fontsize=21, verticalalignment='top')
        else:
            stats.probplot(data2, dist=dist, plot=plt)
            
        plt.rcParams['mathtext.fontset'] = 'cm'    
        plt.title(fr"QQ Plot of {dist_name} for $\mathrm{{E_k}}$ error: F-IUFNO", fontsize=21)
        # 设置刻度字体大小
        plt.xticks(fontsize=21)
        plt.yticks(fontsize=21)
        plt.gca().get_lines()[1].set_linewidth(4)
        # 设置坐标轴标签字体大小（Q-Q 图自动生成了 "Theoretical Quantiles" 和 "Ordered Values"）
        ax = plt.gca()
        ax.set_xlabel(ax.get_xlabel(), fontsize=21)
        ax.set_ylabel(ax.get_ylabel(), fontsize=21)

    plt.tight_layout()  
    plt.savefig('./GSfit/{}cases/QQPlot_F-IUFNO.png'.format(case_number), dpi=300)       
    
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
    plt.title(r'Skew normal distribution fit for $\mathrm{E_k}$ error: F-IFNO', fontsize=40, pad=10) 
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
    plt.gca().yaxis.set_major_formatter(ticker.FormatStrFormatter('%.2f'))
    handles, labels = plt.gca().get_legend_handles_labels()    
    handles = [handles[1], handles[0], handles[2]]
    labels = [labels[1], labels[0], labels[2]]      
    
        
    # 显示图例
    plt.legend(handles=handles,labels=labels,loc='upper center',bbox_to_anchor=(0.5, -0.18),fontsize=40, ncol=2,columnspacing=-5)
    # 去除网格线
    plt.grid(False)
    #plt.ylim(0, 10) 
    plt.subplots_adjust(bottom=0.31)
    plt.savefig('./GSfit/{}cases/GSfit_F-IFNO.png'.format(case_number), dpi=300)  

    plt.close()  # 关闭当前图像，释放内存
    
    # Kolmogorov-Smirnov 检验
    ks_stat, p_value = ks_2samp(data3, skewnorm.rvs(a=alpha_fit, loc=mu_fit, scale=sigma_fit, size=len(data3)))
    # 检验结果解释
    result = "拟合结果较好，数据可以认为符合偏态正态分布" if p_value > 0.05 else "拟合结果不理想，可能需要更复杂的分布模型"
    # 保存到 .dat 文件
    output_file = "./GSfit/{}cases/ks_test_results_F-IFNO.dat".format(case_number)
    with open(output_file, "w") as file:
        file.write("Kolmogorov-Smirnov 检验结果:\n")
        file.write(f"KS Statistic: {ks_stat:.6f}\n")
        file.write(f"P-Value: {p_value:.6f}\n")
        file.write(f"解释: {result}\n")
        
    #QQ   
    # 常见分布的定义
    distributions = {
        "Normal": stats.norm,
        "LogNormal": stats.lognorm(s=1),  # 对数正态分布的标准形状参数
        "Exponential": stats.expon,
        "Gamma": stats.gamma(a=2),  # 伽马分布的形状参数
        "Skew normal": stats.skewnorm,  # 偏态正态分布
        "Student's t": stats.t,  # 学生 t 分布
    }

    # 创建一个 2x3 的子图来显示不同分布的 QQ 图（多加了一个分布）
    plt.figure(figsize=(18, 10))

    # 绘制每个分布的 QQ 图
    for i, (dist_name, dist) in enumerate(distributions.items(), 1):
        plt.subplot(2, 3, i)  # 2x3 布局以容纳更多子图
        if dist_name == "Skew normal":
            # 偏态分布需要指定形状参数（例如，偏度参数 a）
            a = alpha_fit # 偏态参数，调整为适合的数据
            stats.probplot(data3, dist=dist, sparams=(a,), plot=plt)
            # 注释偏态分布参数
            plt.text(0.05, 0.95, rf'$\alpha = {a:.4f}$', transform=plt.gca().transAxes, fontsize=21, verticalalignment='top')
        elif dist_name == "Student's t":
            # 学生 t 分布需要指定自由度参数 df
            df = 5  # 这里假设自由度 df=5，调整为适合的数据
            stats.probplot(data3, dist=dist, sparams=(df,), plot=plt)
            # 注释学生 t 分布参数
            plt.text(0.05, 0.95, f'df = {df:.4f}', transform=plt.gca().transAxes, fontsize=21, verticalalignment='top')
        elif dist_name == "LogNormal":
            # 对数正态分布的标准形状参数 s = 1
            stats.probplot(data3, dist=dist, plot=plt)
            # 注释对数正态分布参数
            plt.text(0.05, 0.95, f's = 1.0000', transform=plt.gca().transAxes, fontsize=21, verticalalignment='top')
        elif dist_name == "Gamma":
            # 伽马分布的形状参数 a = 2
            stats.probplot(data3, dist=dist, plot=plt)
            # 注释伽马分布参数
            aa=2.000
            plt.text(0.05, 0.95, rf'$\alpha = {aa:.4f}$', transform=plt.gca().transAxes, fontsize=21, verticalalignment='top')
        else:
            stats.probplot(data3, dist=dist, plot=plt)
            
        plt.rcParams['mathtext.fontset'] = 'cm'    
        plt.title(fr"QQ Plot of {dist_name} for $\mathrm{{E_k}}$ error: F-IFNO", fontsize=21)
        # 设置刻度字体大小
        plt.xticks(fontsize=21)
        plt.yticks(fontsize=21)
        plt.gca().get_lines()[1].set_linewidth(4)
        # 设置坐标轴标签字体大小（Q-Q 图自动生成了 "Theoretical Quantiles" 和 "Ordered Values"）
        ax = plt.gca()
        ax.set_xlabel(ax.get_xlabel(), fontsize=21)
        ax.set_ylabel(ax.get_ylabel(), fontsize=21)

    plt.tight_layout()  
    plt.savefig('./GSfit/{}cases/QQPlot_F-IFNO.png'.format(case_number), dpi=300)  

    #4
    plt.figure(figsize=(14, 10.5), facecolor='none')  # 设置图形大小
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
    plt.plot(x, pdf, 'k-', label=f"Fit: $\mu={mu:.4f}, \sigma={std:.4f}$", linewidth=4,zorder=2)
    #绘制原始频率密度曲线（虚线）
    plt.plot(bin_centers, hist, linestyle="--", color=colors[4], label='Data density', linewidth=4,zorder=1)
    # 绘制直方圖结果
    plt.hist(data4, bins=50, density=True,alpha=0.4,color=colors[4], label='Data histogram',zorder=0)
    plt.rcParams['mathtext.fontset'] = 'cm'
    plt.title(r'Normal distribution fit for $\mathrm{E_k}$ error: DSM', fontsize=40, pad=10) 
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
    plt.gca().yaxis.set_major_formatter(ticker.FormatStrFormatter('%.2f'))
    handles, labels = plt.gca().get_legend_handles_labels()    
    handles = [handles[1], handles[0], handles[2]]
    labels = [labels[1], labels[0], labels[2]]      
    
        
    # 显示图例
    plt.legend(handles=handles,labels=labels,loc='upper center',bbox_to_anchor=(0.5, -0.18),fontsize=40, ncol=2,columnspacing=-5)
    # 去除网格线
    plt.grid(False)
    #plt.ylim(0, 11) 
    plt.subplots_adjust(bottom=0.31)
    plt.savefig('./GSfit/{}cases/GSfit_DSM.png'.format(case_number), dpi=300)  

    plt.close()  # 关闭当前图像，释放内存
 
    # 计算数据的均值和标准差
    loc, scale = np.mean(data4), np.std(data4) 
    # Kolmogorov-Smirnov 检验
    ks_stat, p_value = kstest(data4, 'norm', args=(loc, scale))
    # 检验结果解释
    result = "拟合结果较好，数据可以认为符合偏态正态分布" if p_value > 0.05 else "拟合结果不理想，可能需要更复杂的分布模型"
    # 保存到 .dat 文件
    output_file = "./GSfit/{}cases/ks_test_results_DSM.dat".format(case_number)
    with open(output_file, "w") as file:
        file.write("Kolmogorov-Smirnov 检验结果:\n")
        file.write(f"KS Statistic: {ks_stat:.6f}\n")
        file.write(f"P-Value: {p_value:.6f}\n")
        file.write(f"解释: {result}\n")
    #QQ   
    # 常见分布的定义
    distributions = {
        "Normal": stats.norm,
        "LogNormal": stats.lognorm(s=1),  # 对数正态分布的标准形状参数
        "Exponential": stats.expon,
        "Gamma": stats.gamma(a=2),  # 伽马分布的形状参数
        "Skew normal": stats.skewnorm,  # 偏态正态分布
        "Student's t": stats.t,  # 学生 t 分布
    }

    # 创建一个 2x3 的子图来显示不同分布的 QQ 图（多加了一个分布）
    plt.figure(figsize=(18, 10))

    # 绘制每个分布的 QQ 图
    for i, (dist_name, dist) in enumerate(distributions.items(), 1):
        plt.subplot(2, 3, i)  # 2x3 布局以容纳更多子图
        if dist_name == "Skew normal":
            # 偏态分布需要指定形状参数（例如，偏度参数 a）
            a = 0 # 偏态参数，调整为适合的数据
            stats.probplot(data4, dist=dist, sparams=(a,), plot=plt)
            # 注释偏态分布参数
            plt.text(0.05, 0.95, rf'$\alpha = {a:.4f}$', transform=plt.gca().transAxes, fontsize=21, verticalalignment='top')
        elif dist_name == "Student's t":
            # 学生 t 分布需要指定自由度参数 df
            df = 5  # 这里假设自由度 df=5，调整为适合的数据
            stats.probplot(data4, dist=dist, sparams=(df,), plot=plt)
            # 注释学生 t 分布参数
            plt.text(0.05, 0.95, f'df = {df:.4f}', transform=plt.gca().transAxes, fontsize=21, verticalalignment='top')
        elif dist_name == "LogNormal":
            # 对数正态分布的标准形状参数 s = 1
            stats.probplot(data4, dist=dist, plot=plt)
            # 注释对数正态分布参数
            plt.text(0.05, 0.95, f's = 1.0000', transform=plt.gca().transAxes, fontsize=21, verticalalignment='top')
        elif dist_name == "Gamma":
            # 伽马分布的形状参数 a = 2
            stats.probplot(data4, dist=dist, plot=plt)
            # 注释伽马分布参数
            aa=2.000
            plt.text(0.05, 0.95, rf'$\alpha = {aa:.4f}$', transform=plt.gca().transAxes, fontsize=21, verticalalignment='top')
        else:
            stats.probplot(data4, dist=dist, plot=plt)
            
        plt.rcParams['mathtext.fontset'] = 'cm'
        plt.title(fr"QQ Plot of {dist_name} for $\mathrm{{E_k}}$ error: DSM", fontsize=21)       
        # 设置刻度字体大小
        plt.xticks(fontsize=21)
        plt.yticks(fontsize=21)
        plt.gca().get_lines()[1].set_linewidth(4)
        # 设置坐标轴标签字体大小（Q-Q 图自动生成了 "Theoretical Quantiles" 和 "Ordered Values"）
        ax = plt.gca()
        ax.set_xlabel(ax.get_xlabel(), fontsize=21)
        ax.set_ylabel(ax.get_ylabel(), fontsize=21)
    plt.tight_layout()      
    plt.savefig('./GSfit/{}cases/QQPlot_DSM.png'.format(case_number), dpi=300)         
        
    #5
    plt.figure(figsize=(14, 10.5), facecolor='none')  # 设置图形大小
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
    plt.plot(x, pdf, 'k-',linewidth=4, zorder=2,label=f'Fit: $\\alpha={alpha_fit:.4f}$, $\\mu={mu_fit:.4f}$, $\\sigma={sigma_fit:.4f}$')
    #绘制原始频率密度曲线（虚线）
    plt.plot(bin_centers, hist, linestyle="--", color=colors[2], label='Data density', linewidth=4,zorder=1)
    # 绘制直方圖结果
    plt.hist(data5, bins=50, density=True,alpha=0.4,color=colors[2], label='Data histogram',zorder=0)
    plt.rcParams['mathtext.fontset'] = 'cm'
    plt.title(r'Skew normal distribution fit for $\mathrm{E_k}$ error: IUFNO', fontsize=40, pad=10) 
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
    x_ticks = np.arange(start=0, stop=max(data5), step=0.5)  # 根据需要设置间隔
    y_ticks = np.arange(start=0, stop=1.1, step=0.1)  # 根据需要设置间隔
    # 设置 x,y 轴刻度格式
    plt.gca().xaxis.set_major_formatter(ticker.FormatStrFormatter('%.2f'))
    plt.gca().yaxis.set_major_formatter(ticker.FormatStrFormatter('%.2f'))
    handles, labels = plt.gca().get_legend_handles_labels()    
    handles = [handles[1], handles[0], handles[2]]
    labels = [labels[1], labels[0], labels[2]]      
    
        
    # 显示图例
    plt.legend(handles=handles,labels=labels,loc='upper center',bbox_to_anchor=(0.5, -0.18),fontsize=40, ncol=2,columnspacing=-5)
    # 去除网格线
    plt.grid(False)
    #plt.ylim(0, 9) 
    plt.subplots_adjust(bottom=0.31)
    plt.savefig('./GSfit/{}cases/GSfit_IUFNO.png'.format(case_number), dpi=300)  

    plt.close()  # 关闭当前图像，释放内存
    
    # Kolmogorov-Smirnov 检验
    ks_stat, p_value = ks_2samp(data5, skewnorm.rvs(a=alpha_fit, loc=mu_fit, scale=sigma_fit, size=len(data5)))
    # 检验结果解释
    result = "拟合结果较好，数据可以认为符合偏态正态分布" if p_value > 0.05 else "拟合结果不理想，可能需要更复杂的分布模型"
    # 保存到 .dat 文件
    output_file = "./GSfit/{}cases/ks_test_results_IUFNO.dat".format(case_number)
    with open(output_file, "w") as file:
        file.write("Kolmogorov-Smirnov 检验结果:\n")
        file.write(f"KS Statistic: {ks_stat:.6f}\n")
        file.write(f"P-Value: {p_value:.6f}\n")
        file.write(f"解释: {result}\n")
        
    #QQ   
    # 常见分布的定义
    distributions = {
        "Normal": stats.norm,
        "LogNormal": stats.lognorm(s=1),  # 对数正态分布的标准形状参数
        "Exponential": stats.expon,
        "Gamma": stats.gamma(a=2),  # 伽马分布的形状参数
        "Skew normal": stats.skewnorm,  # 偏态正态分布
        "Student's t": stats.t,  # 学生 t 分布
    }

    # 创建一个 2x3 的子图来显示不同分布的 QQ 图（多加了一个分布）
    plt.figure(figsize=(18, 10))

    # 绘制每个分布的 QQ 图
    for i, (dist_name, dist) in enumerate(distributions.items(), 1):
        plt.subplot(2, 3, i)  # 2x3 布局以容纳更多子图
        if dist_name == "Skew normal":
            # 偏态分布需要指定形状参数（例如，偏度参数 a）
            a = alpha_fit # 偏态参数，调整为适合的数据
            stats.probplot(data5, dist=dist, sparams=(a,), plot=plt)
            # 注释偏态分布参数
            plt.text(0.05, 0.95, rf'$\alpha = {a:.4f}$', transform=plt.gca().transAxes, fontsize=21, verticalalignment='top')
        elif dist_name == "Student's t":
            # 学生 t 分布需要指定自由度参数 df
            df = 5  # 这里假设自由度 df=5，调整为适合的数据
            stats.probplot(data5, dist=dist, sparams=(df,), plot=plt)
            # 注释学生 t 分布参数
            plt.text(0.05, 0.95, f'df = {df:.4f}', transform=plt.gca().transAxes, fontsize=21, verticalalignment='top')
        elif dist_name == "LogNormal":
            # 对数正态分布的标准形状参数 s = 1
            stats.probplot(data5, dist=dist, plot=plt)
            # 注释对数正态分布参数
            plt.text(0.05, 0.95, f's = 1.0000', transform=plt.gca().transAxes, fontsize=21, verticalalignment='top')
        elif dist_name == "Gamma":
            # 伽马分布的形状参数 a = 2
            stats.probplot(data5, dist=dist, plot=plt)
            # 注释伽马分布参数
            aa=2.000
            plt.text(0.05, 0.95, rf'$\alpha = {aa:.4f}$', transform=plt.gca().transAxes, fontsize=21, verticalalignment='top')
        else:
            stats.probplot(data5, dist=dist, plot=plt)
            
        plt.rcParams['mathtext.fontset'] = 'cm'    
        plt.title(fr"QQ Plot of {dist_name} for $\mathrm{{E_k}}$ error: IUFNO", fontsize=21)
        # 设置刻度字体大小
        plt.xticks(fontsize=21)
        plt.yticks(fontsize=21)
        plt.gca().get_lines()[1].set_linewidth(4)
        # 设置坐标轴标签字体大小（Q-Q 图自动生成了 "Theoretical Quantiles" 和 "Ordered Values"）
        ax = plt.gca()
        ax.set_xlabel(ax.get_xlabel(), fontsize=21)
        ax.set_ylabel(ax.get_ylabel(), fontsize=21)

    plt.tight_layout()  
    plt.savefig('./GSfit/{}cases/QQPlot_IUFNO.png'.format(case_number), dpi=300)  
        



    #6
    plt.figure(figsize=(14, 10.5), facecolor='none')  # 设置图形大小
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
    plt.plot(x, pdf, 'k-',linewidth=4, zorder=2,label=f'Fit: $\\alpha={alpha_fit:.4f}$, $\\mu={mu_fit:.4f}$, $\\sigma={sigma_fit:.4f}$')
    #绘制原始频率密度曲线（虚线）
    plt.plot(bin_centers, hist, linestyle="--", color=colors[3], label='Data density', linewidth=4,zorder=1)
    # 绘制直方圖结果
    plt.hist(data6, bins=50, density=True,alpha=0.4,color=colors[3], label='Data histogram',zorder=0)
    plt.rcParams['mathtext.fontset'] = 'cm'
    plt.title(r'Skew normal distribution fit for $\mathrm{E_k}$ error: IFNO', fontsize=40, pad=10) 
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
    plt.gca().yaxis.set_major_formatter(ticker.FormatStrFormatter('%.2f'))
    handles, labels = plt.gca().get_legend_handles_labels()    
    handles = [handles[1], handles[0], handles[2]]
    labels = [labels[1], labels[0], labels[2]]      
    
        
    # 显示图例
    plt.legend(handles=handles,labels=labels,loc='upper center',bbox_to_anchor=(0.5, -0.18),fontsize=40, ncol=2,columnspacing=-5)
    # 去除网格线
    plt.grid(False)
    #plt.ylim(0, 10) 
    plt.subplots_adjust(bottom=0.31)
    plt.savefig('./GSfit/{}cases/GSfit_IFNO.png'.format(case_number), dpi=300)  

    plt.close()  # 关闭当前图像，释放内存
    
    # Kolmogorov-Smirnov 检验
    ks_stat, p_value = ks_2samp(data6, skewnorm.rvs(a=alpha_fit, loc=mu_fit, scale=sigma_fit, size=len(data6)))
    # 检验结果解释
    result = "拟合结果较好，数据可以认为符合偏态正态分布" if p_value > 0.05 else "拟合结果不理想，可能需要更复杂的分布模型"
    # 保存到 .dat 文件
    output_file = "./GSfit/{}cases/ks_test_results_IFNO.dat".format(case_number)
    with open(output_file, "w") as file:
        file.write("Kolmogorov-Smirnov 检验结果:\n")
        file.write(f"KS Statistic: {ks_stat:.6f}\n")
        file.write(f"P-Value: {p_value:.6f}\n")
        file.write(f"解释: {result}\n")
        
    #QQ   
    # 常见分布的定义
    distributions = {
        "Normal": stats.norm,
        "LogNormal": stats.lognorm(s=1),  # 对数正态分布的标准形状参数
        "Exponential": stats.expon,
        "Gamma": stats.gamma(a=2),  # 伽马分布的形状参数
        "Skew normal": stats.skewnorm,  # 偏态正态分布
        "Student's t": stats.t,  # 学生 t 分布
    }

    # 创建一个 2x3 的子图来显示不同分布的 QQ 图（多加了一个分布）
    plt.figure(figsize=(18, 10))

    # 绘制每个分布的 QQ 图
    for i, (dist_name, dist) in enumerate(distributions.items(), 1):
        plt.subplot(2, 3, i)  # 2x3 布局以容纳更多子图
        if dist_name == "Skew normal":
            # 偏态分布需要指定形状参数（例如，偏度参数 a）
            a = alpha_fit # 偏态参数，调整为适合的数据
            stats.probplot(data6, dist=dist, sparams=(a,), plot=plt)
            # 注释偏态分布参数
            plt.text(0.05, 0.95, rf'$\alpha = {a:.4f}$', transform=plt.gca().transAxes, fontsize=21, verticalalignment='top')
        elif dist_name == "Student's t":
            # 学生 t 分布需要指定自由度参数 df
            df = 5  # 这里假设自由度 df=5，调整为适合的数据
            stats.probplot(data6, dist=dist, sparams=(df,), plot=plt)
            # 注释学生 t 分布参数
            plt.text(0.05, 0.95, f'df = {df:.4f}', transform=plt.gca().transAxes, fontsize=21, verticalalignment='top')
        elif dist_name == "LogNormal":
            # 对数正态分布的标准形状参数 s = 1
            stats.probplot(data6, dist=dist, plot=plt)
            # 注释对数正态分布参数
            plt.text(0.05, 0.95, f's = 1.0000', transform=plt.gca().transAxes, fontsize=21, verticalalignment='top')
        elif dist_name == "Gamma":
            # 伽马分布的形状参数 a = 2
            stats.probplot(data6, dist=dist, plot=plt)
            # 注释伽马分布参数
            aa=2.000
            plt.text(0.05, 0.95, rf'$\alpha = {aa:.4f}$', transform=plt.gca().transAxes, fontsize=21, verticalalignment='top')
        else:
            stats.probplot(data6, dist=dist, plot=plt)
            
        plt.rcParams['mathtext.fontset'] = 'cm'    
        plt.title(fr"QQ Plot of {dist_name} for $\mathrm{{E_k}}$ error: IFNO", fontsize=21)
        # 设置刻度字体大小
        plt.xticks(fontsize=21)
        plt.yticks(fontsize=21)
        plt.gca().get_lines()[1].set_linewidth(4)
        # 设置坐标轴标签字体大小（Q-Q 图自动生成了 "Theoretical Quantiles" 和 "Ordered Values"）
        ax = plt.gca()
        ax.set_xlabel(ax.get_xlabel(), fontsize=21)
        ax.set_ylabel(ax.get_ylabel(), fontsize=21)

    plt.tight_layout()  
    plt.savefig('./GSfit/{}cases/QQPlot_IFNO.png'.format(case_number), dpi=300)  
        
####################################################################################################################       
 
    #1
    plt.figure(figsize=(14, 10.5), facecolor='none')  # 设置图形大小
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
    plt.plot(x, pdf, 'k-', label=f"Fit: $\mu={mu:.4f}, \sigma={std:.4f}$", linewidth=4,zorder=2)
    #绘制原始频率密度曲线（虚线）
    plt.plot(bin_centers, hist, linestyle="--", color=colors[1], label='Data density', linewidth=4,zorder=1)
    # 绘制直方圖结果
    plt.hist(data2, bins=50, density=True,alpha=0.4,color=colors[1], label='Data histogram',zorder=0)
    plt.rcParams['mathtext.fontset'] = 'cm'
    plt.title(r'Normal distribution fit for $\mathrm{E_k}$ error: F-IUFNO', fontsize=40, pad=10) 
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
    plt.gca().yaxis.set_major_formatter(ticker.FormatStrFormatter('%.2f'))
    handles, labels = plt.gca().get_legend_handles_labels()    
    handles = [handles[1], handles[0], handles[2]]
    labels = [labels[1], labels[0], labels[2]]      
    
        
    # 显示图例
    plt.legend(handles=handles,labels=labels,loc='upper center',bbox_to_anchor=(0.5, -0.18),fontsize=40, ncol=2,columnspacing=-5)
    # 去除网格线
    plt.grid(False)
    plt.subplots_adjust(bottom=0.31)
    plt.savefig('./GSfit/{}cases/GSfit_F-IUFNO_gs.png'.format(case_number), dpi=300)  

    plt.close()  # 关闭当前图像，释放内存
 
    # 计算数据的均值和标准差
    loc, scale = np.mean(data2), np.std(data2) 
    # Kolmogorov-Smirnov 检验
    ks_stat, p_value = kstest(data2, 'norm', args=(loc, scale))
    # 检验结果解释
    result = "拟合结果较好，数据可以认为符合偏态正态分布" if p_value > 0.05 else "拟合结果不理想，可能需要更复杂的分布模型"
    # 保存到 .dat 文件
    output_file = "./GSfit/{}cases/ks_test_results_F-IUFNO_gs.dat".format(case_number)
    with open(output_file, "w") as file:
        file.write("Kolmogorov-Smirnov 检验结果:\n")
        file.write(f"KS Statistic: {ks_stat:.6f}\n")
        file.write(f"P-Value: {p_value:.6f}\n")
        file.write(f"解释: {result}\n")
        
    #2
    plt.figure(figsize=(14, 10.5), facecolor='none')  # 设置图形大小
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
    plt.plot(x, pdf, 'k-', label=f"Fit: $\mu={mu:.4f}, \sigma={std:.4f}$", linewidth=4,zorder=2)
    #绘制原始频率密度曲线（虚线）
    plt.plot(bin_centers, hist, linestyle="--", color=colors[0], label='Data density', linewidth=4,zorder=1)
    # 绘制直方圖结果
    plt.hist(data3, bins=50, density=True,alpha=0.4,color=colors[0], label='Data histogram',zorder=0)
    plt.rcParams['mathtext.fontset'] = 'cm'
    plt.title(r'Normal distribution fit for $\mathrm{E_k}$ error: F-IFNO', fontsize=40, pad=10) 
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
    plt.gca().yaxis.set_major_formatter(ticker.FormatStrFormatter('%.2f'))
    handles, labels = plt.gca().get_legend_handles_labels()    
    handles = [handles[1], handles[0], handles[2]]
    labels = [labels[1], labels[0], labels[2]]     
    
        
    # 显示图例
    plt.legend(handles=handles,labels=labels,loc='upper center',bbox_to_anchor=(0.5, -0.18),fontsize=40, ncol=2,columnspacing=-5)
    # 去除网格线
    plt.grid(False)
    plt.subplots_adjust(bottom=0.31)
    plt.savefig('./GSfit/{}cases/GSfit_F-IFNO_gs.png'.format(case_number), dpi=300)  

    plt.close()  # 关闭当前图像，释放内存
 
    # 计算数据的均值和标准差
    loc, scale = np.mean(data3), np.std(data3) 
    # Kolmogorov-Smirnov 检验
    ks_stat, p_value = kstest(data3, 'norm', args=(loc, scale))
    # 检验结果解释
    result = "拟合结果较好，数据可以认为符合偏态正态分布" if p_value > 0.05 else "拟合结果不理想，可能需要更复杂的分布模型"
    # 保存到 .dat 文件
    output_file = "./GSfit/{}cases/ks_test_results_F-IFNO_gs.dat".format(case_number)
    with open(output_file, "w") as file:
        file.write("Kolmogorov-Smirnov 检验结果:\n")
        file.write(f"KS Statistic: {ks_stat:.6f}\n")
        file.write(f"P-Value: {p_value:.6f}\n")
        file.write(f"解释: {result}\n")
        
 
    #3
    plt.figure(figsize=(14, 10.5), facecolor='none')  # 设置图形大小
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
    plt.plot(x, pdf, 'k-', label=f"Fit: $\mu={mu:.4f}, \sigma={std:.4f}$", linewidth=4,zorder=2)
    #绘制原始频率密度曲线（虚线）
    plt.plot(bin_centers, hist, linestyle="--", color=colors[2], label='Data density', linewidth=4,zorder=1)
    # 绘制直方圖结果
    plt.hist(data5, bins=50, density=True,alpha=0.4,color=colors[2], label='Data histogram',zorder=0)
    plt.rcParams['mathtext.fontset'] = 'cm'
    plt.title(r'Normal distribution fit for $\mathrm{E_k}$ error: IUFNO', fontsize=40, pad=10) 
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
    x_ticks = np.arange(start=0, stop=max(data5), step=0.5)  # 根据需要设置间隔
    y_ticks = np.arange(start=0, stop=1.1, step=0.1)  # 根据需要设置间隔
    # 设置 x,y 轴刻度格式
    plt.gca().xaxis.set_major_formatter(ticker.FormatStrFormatter('%.2f'))
    plt.gca().yaxis.set_major_formatter(ticker.FormatStrFormatter('%.2f'))
    handles, labels = plt.gca().get_legend_handles_labels()    
    handles = [handles[1], handles[0], handles[2]]
    labels = [labels[1], labels[0], labels[2]]      
    
        
    # 显示图例
    plt.legend(handles=handles,labels=labels,loc='upper center',bbox_to_anchor=(0.5, -0.18),fontsize=40, ncol=2,columnspacing=-5)
    # 去除网格线
    plt.grid(False)
    plt.subplots_adjust(bottom=0.31)
    plt.savefig('./GSfit/{}cases/GSfit_IUFNO_gs.png'.format(case_number), dpi=300)  

    plt.close()  # 关闭当前图像，释放内存
 
    # 计算数据的均值和标准差
    loc, scale = np.mean(data5), np.std(data5) 
    # Kolmogorov-Smirnov 检验
    ks_stat, p_value = kstest(data5, 'norm', args=(loc, scale))
    # 检验结果解释
    result = "拟合结果较好，数据可以认为符合偏态正态分布" if p_value > 0.05 else "拟合结果不理想，可能需要更复杂的分布模型"
    # 保存到 .dat 文件
    output_file = "./GSfit/{}cases/ks_test_results_IUFNO_gs.dat".format(case_number)
    with open(output_file, "w") as file:
        file.write("Kolmogorov-Smirnov 检验结果:\n")
        file.write(f"KS Statistic: {ks_stat:.6f}\n")
        file.write(f"P-Value: {p_value:.6f}\n")
        file.write(f"解释: {result}\n")
        
    #4
    plt.figure(figsize=(14, 10.5), facecolor='none')  # 设置图形大小
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
    plt.plot(x, pdf, 'k-', label=f"Fit: $\mu={mu:.4f}, \sigma={std:.4f}$", linewidth=4,zorder=2)
    #绘制原始频率密度曲线（虚线）
    plt.plot(bin_centers, hist, linestyle="--", color=colors[3], label='Data density', linewidth=4,zorder=1)
    # 绘制直方圖结果
    plt.hist(data6, bins=50, density=True,alpha=0.4,color=colors[3], label='Data histogram',zorder=0)
    plt.rcParams['mathtext.fontset'] = 'cm'
    plt.title(r'Normal distribution fit for $\mathrm{E_k}$ error: IFNO', fontsize=40, pad=10) 
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
    plt.gca().yaxis.set_major_formatter(ticker.FormatStrFormatter('%.2f'))
    handles, labels = plt.gca().get_legend_handles_labels()    
    handles = [handles[1], handles[0], handles[2]]
    labels = [labels[1], labels[0], labels[2]]      
    
        
    # 显示图例
    plt.legend(handles=handles,labels=labels,loc='upper center',bbox_to_anchor=(0.5, -0.18),fontsize=40, ncol=2,columnspacing=-5)
    # 去除网格线
    plt.grid(False)
    plt.subplots_adjust(bottom=0.31)
    plt.savefig('./GSfit/{}cases/GSfit_IFNO_gs.png'.format(case_number), dpi=300)  

    plt.close()  # 关闭当前图像，释放内存
 
    # 计算数据的均值和标准差
    loc, scale = np.mean(data6), np.std(data6) 
    # Kolmogorov-Smirnov 检验
    ks_stat, p_value = kstest(data6, 'norm', args=(loc, scale))
    # 检验结果解释
    result = "拟合结果较好，数据可以认为符合偏态正态分布" if p_value > 0.05 else "拟合结果不理想，可能需要更复杂的分布模型"
    # 保存到 .dat 文件
    output_file = "./GSfit/{}cases/ks_test_results_IFNO_gs.dat".format(case_number)
    with open(output_file, "w") as file:
        file.write("Kolmogorov-Smirnov 检验结果:\n")
        file.write(f"KS Statistic: {ks_stat:.6f}\n")
        file.write(f"P-Value: {p_value:.6f}\n")
        file.write(f"解释: {result}\n")               
