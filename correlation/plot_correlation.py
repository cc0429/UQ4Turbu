import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator, FormatStrFormatter
plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.serif'] = ['Times', 'Times', 'STIXGeneral']
# 读取数据1
data = np.loadtxt("./correlation/correlation_avg.dat")

# 提取 step_array 和 correlation_avg
step_array = data[:, 0] / 1000  # 直接对 numpy 数组除以 1000
correlation_avg = data[:, 1]


plt.figure(figsize=(11, 6))
plt.plot(step_array, correlation_avg, marker='o', linestyle='-',linewidth=3, color='b',markerfacecolor='r', markeredgecolor='r', markersize=9)

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
#plt.legend(fontsize=12)


plt.savefig("./correlation/correlation_plot.png", dpi=300, bbox_inches="tight")


# 读取数据2
data = np.loadtxt("./acf/acf_avg.dat")

# 提取 step_array 和 correlation_avg
step_array = data[:, 0] /1000 # 第一列
acf_avg = data[:, 1] # 第二列


plt.figure(figsize=(11, 6))
plt.plot(step_array, acf_avg, marker='o', linestyle='-',linewidth=3, color='b',markerfacecolor='r', markeredgecolor='r', markersize=9)

# 添加标题和标签
plt.xlabel(r"$\mathdefault{\Delta T/\tau}$", fontsize=25)
plt.ylabel(r"$\mathdefault{f_{ac}}$", fontsize=30)
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
#plt.legend(fontsize=12)
plt.savefig("./acf/acf_plot.png", dpi=300, bbox_inches="tight")


