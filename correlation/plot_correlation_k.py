import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator, FormatStrFormatter
plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.serif'] = ['Times', 'Times', 'STIXGeneral']
#############correlation
step_arrays = {}
correlation_avgs = {}
for spec in range(10):
    # 读取数据1
    data = np.loadtxt("./correlation/correlation_avg_k={}.dat".format(spec+1))

    # 提取 step_array 和 correlation_avg
    step_array = data[:, 0] / 1000  # 直接对 numpy 数组除以 1000
    correlation_avg = data[:, 1]
    step_arrays[spec+1] = step_array
    correlation_avgs[spec+1] = correlation_avg

colors = [
    '#A52A2A', '#ff7f0e', '#ffd700', 'green', '#1f77b4',
    'purple', '#ff007f', '#7f7f7f','#17becf',  '#8c564b','pink','black'
]

markersizes=[7,6.5,6,5.5,5,4.5,4,3.5,3,2.5,2,1.5,1]
linewidths=[4,3.75,3.5,3.25,3,2.75,2.5,2.25,2,1.75,1.5,1.25,1]
###kwitht
plt.figure(figsize=(13,7.5))
for spec in range(10):
    plt.plot(step_arrays[spec+1], correlation_avgs[spec+1], marker='o', linestyle='-',linewidth=3, color=colors[spec],markerfacecolor=colors[spec], markeredgecolor=colors[spec], markersize=6, label="k={}".format(spec+1))

# 添加标题和标签
plt.xlabel(r"$\mathdefault{\Delta T/\tau}$", fontsize=25)
plt.ylabel("Correlation", fontsize=25)
# 设置 x 和 y 轴的主刻度和副刻度
plt.xticks(fontsize=25)
plt.yticks(fontsize=25)

# 设置刻度间隔
plt.gca().xaxis.set_major_locator(MultipleLocator(0.1))  # 主刻度间隔为1
plt.gca().xaxis.set_minor_locator(MultipleLocator(0.02))  # 小刻度为主刻度的五分之一

plt.gca().yaxis.set_major_locator(MultipleLocator(0.1))  # 主刻度间隔为0.1
plt.gca().yaxis.set_minor_locator(MultipleLocator(0.02))  # 小刻度为主刻度的五分之一

# 设置刻度格式，保留4位小数
plt.gca().xaxis.set_major_formatter(FormatStrFormatter('%.2f'))
plt.gca().yaxis.set_major_formatter(FormatStrFormatter('%.2f'))
# 设置 x 和 y 轴的范围
#plt.xlim(0, 1)  # 例如 x 范围从 0 到 1
#plt.ylim(0.4, 1)   # 例如 y 范围从 0 到 1

# 添加网格
#plt.grid(True, linestyle="-", alpha=0.7)

# 添加图例
plt.legend(loc='upper right',fontsize=20, frameon=True, framealpha=0, edgecolor='black', shadow=False)
plt.xlim(-0.05, 1.3)

plt.savefig("./correlation/correlation_plot_kwitht.png", dpi=300, bbox_inches="tight")


###twithk
correlation_avgs_k={}
for ss,step in enumerate(step_array):
    correlation_avgs_k_1 = []
    for spec in range(10):
        correlation_avgs_k_1.append(correlation_avgs[spec+1][ss])
    correlation_avgs_k[ss+1] = correlation_avgs_k_1
    
x = np.arange(1, 11)
plt.figure(figsize=(11,7.5))
for ss,step in enumerate(step_array):
    plt.plot(x, correlation_avgs_k[ss+1], marker='o', linestyle='-',linewidth=3, color=colors[ss],markerfacecolor=colors[ss], markeredgecolor=colors[ss], markersize=6, label=r'$\mathdefault{{\Delta T = {}  \tau}}$'.format(step))

# 添加标题和标签
plt.xlabel("k", fontsize=25)
plt.ylabel("Correlation", fontsize=25)
# 设置 x 和 y 轴的主刻度和副刻度
plt.xticks(fontsize=25)
plt.yticks(fontsize=25)

# 设置刻度间隔
plt.gca().xaxis.set_major_locator(MultipleLocator(1))  # 主刻度间隔为1


plt.gca().yaxis.set_major_locator(MultipleLocator(0.1))  # 主刻度间隔为0.1
plt.gca().yaxis.set_minor_locator(MultipleLocator(0.02))  # 小刻度为主刻度的五分之一

# 设置刻度格式，保留4位小数
plt.gca().xaxis.set_major_formatter(FormatStrFormatter('%.0f'))
plt.gca().yaxis.set_major_formatter(FormatStrFormatter('%.2f'))
# 设置 x 和 y 轴的范围
#plt.xlim(0, 1)  # 例如 x 范围从 0 到 1
#plt.ylim(0.4, 1)   # 例如 y 范围从 0 到 1

# 添加网格


# 添加图例
plt.legend(loc='upper right', fontsize=20, frameon=True, framealpha=0, edgecolor='black', shadow=False)
  

plt.savefig("./correlation/correlation_plot_twithk.png", dpi=300, bbox_inches="tight")



#############acf
step_arrays = {}
correlation_avgs = {}
for spec in range(10):
    # 读取数据1
    data = np.loadtxt("./acf/acf_avg_k={}.dat".format(spec+1))

    # 提取 step_array 和 correlation_avg
    step_array = data[:, 0] / 1000  # 直接对 numpy 数组除以 1000
    correlation_avg = data[:, 1]
    step_arrays[spec+1] = step_array
    correlation_avgs[spec+1] = correlation_avg

colors = [
    '#A52A2A', '#ff7f0e', '#ffd700', 'green', '#1f77b4',
    'purple', '#ff007f', '#7f7f7f','#17becf',  '#8c564b','pink','black'
]


markersizes=[7,6.5,6,5.5,5,4.5,4,3.5,3,2.5,2,1.5,1]
linewidths=[4,3.75,3.5,3.25,3,2.75,2.5,2.25,2,1.75,1.5,1.25,1]

###kwitht
plt.figure(figsize=(11,7.5))
for spec in range(10):
    plt.plot(step_arrays[spec+1], correlation_avgs[spec+1], marker='o', linestyle='-',linewidth=3, color=colors[spec],markerfacecolor=colors[spec], markeredgecolor=colors[spec],markersize= 6, label="k={}".format(spec+1))

# 添加标题和标签
plt.xlabel(r"$\mathdefault{\Delta T/\tau}$", fontsize=25)
plt.ylabel(r"$\mathdefault{f_{ac}(k)}$", fontsize=30)
# 设置 x 和 y 轴的主刻度和副刻度
plt.xticks(fontsize=25)
plt.yticks(fontsize=25)

# 设置刻度间隔
plt.gca().xaxis.set_major_locator(MultipleLocator(0.1))  # 主刻度间隔为1
plt.gca().xaxis.set_minor_locator(MultipleLocator(0.02))  # 小刻度为主刻度的五分之一

plt.gca().yaxis.set_major_locator(MultipleLocator(0.1))  # 主刻度间隔为0.1
plt.gca().yaxis.set_minor_locator(MultipleLocator(0.02))  # 小刻度为主刻度的五分之一

# 设置刻度格式，保留4位小数
plt.gca().xaxis.set_major_formatter(FormatStrFormatter('%.1f'))
plt.gca().yaxis.set_major_formatter(FormatStrFormatter('%.2f'))
# 设置 x 和 y 轴的范围
#plt.xlim(0, 1)  # 例如 x 范围从 0 到 1
#plt.ylim(0.4, 1)   # 例如 y 范围从 0 到 1

# 添加网格
#plt.grid(True, linestyle="-", alpha=0.7)
plt.xlim(-0.05, 1.3)
# 添加图例
plt.legend(loc='upper right', fontsize=20, frameon=True, framealpha=0, edgecolor='black', shadow=False)


plt.savefig("./acf/acf_plot_kwitht.png", dpi=300, bbox_inches="tight")


###twithk
correlation_avgs_k={}
for ss,step in enumerate(step_array):
    correlation_avgs_k_1 = []
    for spec in range(10):
        correlation_avgs_k_1.append(correlation_avgs[spec+1][ss])
    correlation_avgs_k[ss+1] = correlation_avgs_k_1
    
x = np.arange(1, 11)
plt.figure(figsize=(11,7.5))
for ss,step in enumerate(step_array):
    plt.plot(x, correlation_avgs_k[ss+1], marker='o', linestyle='-',linewidth=3, color=colors[ss],markerfacecolor=colors[ss], markeredgecolor=colors[ss], markersize=6, label=r'$\mathdefault{{\Delta T = {}  \tau}}$'.format(step))

# 添加标题和标签
plt.xlabel("k", fontsize=25)
plt.ylabel(r"$\mathdefault{f_{ac}(k)}$", fontsize=30)
# 设置 x 和 y 轴的主刻度和副刻度
plt.xticks(fontsize=25)
plt.yticks(fontsize=25)

# 设置刻度间隔
plt.gca().xaxis.set_major_locator(MultipleLocator(1))  # 主刻度间隔为1


plt.gca().yaxis.set_major_locator(MultipleLocator(0.1))  # 主刻度间隔为0.1
plt.gca().yaxis.set_minor_locator(MultipleLocator(0.02))  # 小刻度为主刻度的五分之一

# 设置刻度格式，保留4位小数
plt.gca().xaxis.set_major_formatter(FormatStrFormatter('%.0f'))
plt.gca().yaxis.set_major_formatter(FormatStrFormatter('%.2f'))
# 设置 x 和 y 轴的范围
#plt.xlim(0, 1)  # 例如 x 范围从 0 到 1
#plt.ylim(0.4, 1)   # 例如 y 范围从 0 到 1

# 添加网格


# 添加图例
plt.legend(loc='upper right', fontsize=20, frameon=True, framealpha=0, edgecolor='black', shadow=False)

plt.savefig("./acf/acf_plot_twithk.png", dpi=300, bbox_inches="tight")







