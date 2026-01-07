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
case_number =30
time_steps=600
vel_k_list = [1,2,3,4,5,6,7,8,9,10]

mean1=[]
std1=[]
mean2=[]
std2=[]
mean3=[]
std3=[]
mean4=[]
std4=[]
mean5=[]
std5=[]
mean6=[]
std6=[]



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
    data1=fDNS[:,1]
    data2=F_IFNO_40ep[:,1]
    data3=F_IUFNO_40ep[:,1]
    data4=IUFNO_40ep[:,1]
    data5=IFNO[:,1]
    data6=DSM[:,1]




    data1 = np.array(data1)
    data1 = data1.reshape(case_number,time_steps)
    data2 = np.array(data2)
    data2 = data2.reshape(case_number,time_steps)
    data3 = np.array(data3)
    data3 = data3.reshape(case_number,time_steps)
    data4 = np.array(data4)
    data4 = data4.reshape(case_number,time_steps)
    data5 = np.array(data5)
    data5 = data5.reshape(case_number,time_steps)
    data6 = np.array(data6)
    data6 = data6.reshape(case_number,time_steps)

    print("k",k)
    print("data1:",data1.shape)

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

    for i in range(time_steps):
        
        mean1.append(np.mean(data1[:,i]))
        std1.append(np.var(data1[:,i]))

        mean2.append(np.mean(data2[:,i]))
        std2.append(np.var(data2[:,i]))

        mean3.append(np.mean(data3[:,i]))
        std3.append(np.var(data3[:,i]))

        mean4.append(np.mean(data4[:,i]))
        std4.append(np.var(data4[:,i]))
        
        mean5.append(np.mean(data5[:,i]))
        std5.append(np.var(data5[:,i]))

        mean6.append(np.mean(data6[:,i]))
        std6.append(np.var(data6[:,i]))


mean1 = np.array(mean1)
std1 = np.array(std1)
mean2 = np.array(mean2)
std2 = np.array(std2)
mean3 = np.array(mean3)
std3 = np.array(std3)
mean4 = np.array(mean4)
std4 = np.array(std4)
mean5 = np.array(mean5)
std5 = np.array(std5)
mean6 = np.array(mean6)
std6 = np.array(std6)

print("mean1",mean1.shape)
print("std1",std1.shape)
    
    



######################### set figure path1 ################################
figfilePath = os.path.abspath('./Errorbar_with_time_with_k')
figPath = os.path.join(figfilePath, "spectrum_errorbar_with_time_30cases_F-IFNO_k=3-10")

print("图片存放路径：", figPath)


############################## setting of figures #################################
dpi = 600                               #分辨率
width  = 8                              #图宽
height = 6                              #图高
fontSize = 30                          #字体大小
lineWidth = 2.5                         #线宽
boxWidth = 2.5                          #边框线宽
Lmajor = 7                              #主刻度长度
Lminor = 4                              #次刻度长度
xlabPad  = 10                           #x坐标下面显示值距离轴距离
ylabPad  = 10                           #y坐标下面显示值距离轴距离
xlabel = r"$\mathdefault{t/\tau}$"            #坐标标签
ylabel = r"$\mathdefault{Mean \pm Std \ error}$"
xlimit = [1,121]                        #坐标显示范围
#ylimit = [-60,60]
legend2 = ["F-IFNO", "F-IUFNO_ep35", "F-IUFNO_ep40","IUFNO_ep11","IUFNO_ep40","IFNO","DSM","F-IFNO_mag0.1", "F-IUFNO_ep35_mag0.1","F-IUFNO_ep40_mag0.1","IUFNO_ep11_mag0.1","IUFNO_ep40_mag0.1","IFNO_mag0.1","DSM_mag0.1","F-IFNO_mag0.5", "F-IUFNO_ep35_mag0.5","F-IUFNO_ep40_mag0.5","IUFNO_ep11_mag0.5","IUFNO_ep40_mag0.5","IFNO_mag0.5","DSM_mag0.5","F-IFNO_mag1", "F-IUFNO_ep35_mag1","DSM_mag1","F-IFNO_mag2", "F-IUFNO_ep35_mag2","DSM_mag2","F-IFNO_mag5", "F-IUFNO_ep35_mag5","DSM_mag5","F-IFNO_mag10", "F-IUFNO_ep35_mag10","DSM_mag10","fDNS"]
legend = ["k=1", "k=2", "k=3", "k=4", "k=5", "k=6", "k=7", "k=8", "k=9","k=10"]
############################## setting of fonts ####################################
mpl.rc('font', family='STIXGeneral')
mpl.rc('text', usetex=False)
mpl.rcParams['xtick.direction'] = 'in'
mpl.rcParams['ytick.direction'] = 'in'     #xy轴坐标杆标注的方向
plt.rcParams["mathtext.fontset"]  = "cm"   #数学符号的字体
mpl.rcParams["font.family"] = "STIXGeneral"
mpl.mathtext.FontConstantsBase.sup1 = 0.5     #上标相对位置
mpl.mathtext.FontConstantsBase.sub1 = 0.4     #下标相对位置
mpl.mathtext.FontConstantsBase.sub2 = 0.4
# lcolor = ['#FF0000', '#00D200', '#0000FF', '#FF00FF', '#000000', '#000000', '#000000', 'salmon', 'violet', 'yellowgreen']
# lstyle = ["solid", "dashed", "dashdot", ":", ":", "-", "--", "-.", ":", "--", "-."]
# lwidth = [4.0]*np.size(lcolor)
############################## setting of figures #################################

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
    '#DC143C', '#4169E1', '#4682B4', '#008000'                          # 新增颜色至50种
]

markers = ['o', 's', 'D', 'p', '*', '^', 'v', '<', '>', 'x', 'h', '+', 'H', '1', '2', '3', '4', '|', '_', '.']
#-----------------------------------------------------------------------------------------图片大小分辨率
fig = plt.figure(figsize=(width,height), dpi=dpi)     #定义图片宽、高、分辨率
plt.rcParams["font.size"] = fontSize                  #统一字体大小
plt.rcParams["axes.linewidth"] = lineWidth
ax = fig.add_axes([0,0,1,1])                          #用于压缩图片，相当于各边移动距离
# ----------------------------------------------------------------------------------------X坐标轴设置
plt.xscale("linear")                                     #画linear
ax.xaxis.set_major_locator(mpl.ticker.MultipleLocator(20)) #次刻度
ax.xaxis.set_minor_locator(mpl.ticker.MultipleLocator(2))  #次刻度  #主刻度格式
ax.xaxis.set_major_formatter(mpl.ticker.ScalarFormatter())               #应用主刻度格式
ax.xaxis.set_minor_formatter(mpl.ticker.NullFormatter()) #次刻度
# ----------------------------------------------------------------------------------------Y坐标轴设置
plt.yscale("linear")
ax.yaxis.set_major_locator(ticker.MaxNLocator(nbins=6, min_n_ticks=5))  # Automatically set major ticks
ax.yaxis.set_minor_locator(ticker.AutoMinorLocator(5))  # Automatically set minor ticks to be 5 times finer than major ticks
ax.autoscale(enable=True, axis='y', tight=False)
# formatter = mpl.ticker.LogFormatterSciNotation()
ax.yaxis.set_major_formatter(mpl.ticker.ScalarFormatter())
ax.yaxis.set_minor_formatter(mpl.ticker.NullFormatter())
# ----------------------------------------------------------------------------------------坐标边框可见性、及边框宽度
# Hide the top and right spines of the axis
ax.spines['right'].set_visible(True)
ax.spines['top'].set_visible(True)
# Set the axis box line width
ax.spines['bottom'].set_linewidth(boxWidth)
ax.spines['left'].set_linewidth(boxWidth)
ax.spines['top'].set_linewidth(boxWidth)
ax.spines['right'].set_linewidth(boxWidth)
# ----------------------------------------------------------------------------------------坐标刻度设置、标签、显示范围
# Tick Parameters: Edit the major and minor ticks of the x and y axes
ax.xaxis.set_tick_params(which='major', size=Lmajor, width=boxWidth, direction='in',pad=xlabPad, top=False)
ax.xaxis.set_tick_params(which='minor', size=Lminor, width=boxWidth, direction='in',pad=xlabPad, top=False)
ax.yaxis.set_tick_params(which='major', size=Lmajor, width=boxWidth, direction='in',pad=ylabPad, right=False)
ax.yaxis.set_tick_params(which='minor', size=Lminor, width=boxWidth, direction='in',pad=ylabPad, right=False)
plt.xlabel(xlabel)
plt.ylabel(ylabel)
ax.set_xlim(xlimit[0], xlimit[1])
#ax.set_ylim(ylimit[0], ylimit[1])
ncurv = len(legend)  #每个图画4条线

# ------------------------------------------------------------------------------------------
x = np.arange(0.2, time_steps*0.2+0.2,0.2)
step1=1

mean=mean2
std=std2
k=3
plt.plot(x, mean[(k-1)*600:k*600], label=legend[2], color='gold', linewidth=lineWidth, linestyle='solid',zorder=5)
plt.fill_between(x, mean[(k-1)*600:k*600] - std[(k-1)*600:k*600], mean[(k-1)*600:k*600] + std[(k-1)*600:k*600], color='gold', alpha=0.3,zorder=5)

k=4
plt.plot(x, mean[(k-1)*600:k*600], label=legend[3], color='green', linewidth=lineWidth, linestyle='solid',zorder=5)
plt.fill_between(x, mean[(k-1)*600:k*600] - std[(k-1)*600:k*600], mean[(k-1)*600:k*600] + std[(k-1)*600:k*600], color='green', alpha=0.3,zorder=5)

k=5
plt.plot(x, mean[(k-1)*600:k*600], label=legend[4], color='#1f77b4', linewidth=lineWidth, linestyle='solid',zorder=5)
plt.fill_between(x, mean[(k-1)*600:k*600] - std[(k-1)*600:k*600], mean[(k-1)*600:k*600] + std[(k-1)*600:k*600], color='#1f77b4', alpha=0.3,zorder=5)

k=6
plt.plot(x, mean[(k-1)*600:k*600], label=legend[5], color='#008080', linewidth=lineWidth, linestyle='solid',zorder=5)
plt.fill_between(x, mean[(k-1)*600:k*600] - std[(k-1)*600:k*600], mean[(k-1)*600:k*600] + std[(k-1)*600:k*600], color='#008080', alpha=0.3,zorder=5)

k=7
plt.plot(x, mean[(k-1)*600:k*600], label=legend[6], color='purple', linewidth=lineWidth, linestyle='solid',zorder=5)
plt.fill_between(x, mean[(k-1)*600:k*600] - std[(k-1)*600:k*600], mean[(k-1)*600:k*600] + std[(k-1)*600:k*600], color='purple', alpha=0.3,zorder=5)

k=8
plt.plot(x, mean[(k-1)*600:k*600], label=legend[7], color='pink', linewidth=lineWidth, linestyle='solid',zorder=5)
plt.fill_between(x, mean[(k-1)*600:k*600] - std[(k-1)*600:k*600], mean[(k-1)*600:k*600] + std[(k-1)*600:k*600], color='pink', alpha=0.3,zorder=5)

k=9
plt.plot(x, mean[(k-1)*600:k*600], label=legend[8], color='#00FFFF', linewidth=lineWidth, linestyle='solid',zorder=5)
plt.fill_between(x, mean[(k-1)*600:k*600] - std[(k-1)*600:k*600], mean[(k-1)*600:k*600] + std[(k-1)*600:k*600], color='#00FFFF', alpha=0.3,zorder=5)

k=10
plt.plot(x, mean[(k-1)*600:k*600], label=legend[9], color='#FF00FF', linewidth=lineWidth, linestyle='solid',zorder=9)
plt.fill_between(x, mean[(k-1)*600:k*600] - std[(k-1)*600:k*600], mean[(k-1)*600:k*600] + std[(k-1)*600:k*600], color='#FF00FF', alpha=0.3,zorder=9)


lgd_loc  = (0.8,0.5)#6 7#6 80 88
lgd_font = {'family':"STIXGeneral", 'size':fontSize*0.6}
lgd = plt.legend(loc=lgd_loc, frameon=False, prop=lgd_font,handlelength=2.5,labelspacing=0.5) #2.5是legend长度,0.5是间距
#plt.title("Mean ± Std error of spectrum: F-IFNO", fontsize=30, color='black', loc='center', pad=15)
plt.savefig(figPath, quality=100, bbox_extra_artists=(lgd,), bbox_inches='tight')
print("Width x Hight: ", fig.get_size_inches())
# plt.cl



######################### set figure path1 ################################
figfilePath = os.path.abspath('./Errorbar_with_time_with_k')
figPath = os.path.join(figfilePath, "spectrum_errorbar_with_time_30cases_F-IUFNO_k=3-10")

print("图片存放路径：", figPath)


############################## setting of figures #################################
dpi = 600                               #分辨率
width  = 8                              #图宽
height = 6                              #图高
fontSize = 30                          #字体大小
lineWidth = 2.5                         #线宽
boxWidth = 2.5                          #边框线宽
Lmajor = 7                              #主刻度长度
Lminor = 4                              #次刻度长度
xlabPad  = 10                           #x坐标下面显示值距离轴距离
ylabPad  = 10                           #y坐标下面显示值距离轴距离
xlabel = r"$\mathdefault{t/\tau}$"            #坐标标签
ylabel = r"$\mathdefault{Mean \pm Std \ error}$"
xlimit = [1,121]                        #坐标显示范围
#ylimit = [-60,60]
legend2 = ["F-IFNO", "F-IUFNO_ep35", "F-IUFNO_ep40","IUFNO_ep11","IUFNO_ep40","IFNO","DSM","F-IFNO_mag0.1", "F-IUFNO_ep35_mag0.1","F-IUFNO_ep40_mag0.1","IUFNO_ep11_mag0.1","IUFNO_ep40_mag0.1","IFNO_mag0.1","DSM_mag0.1","F-IFNO_mag0.5", "F-IUFNO_ep35_mag0.5","F-IUFNO_ep40_mag0.5","IUFNO_ep11_mag0.5","IUFNO_ep40_mag0.5","IFNO_mag0.5","DSM_mag0.5","F-IFNO_mag1", "F-IUFNO_ep35_mag1","DSM_mag1","F-IFNO_mag2", "F-IUFNO_ep35_mag2","DSM_mag2","F-IFNO_mag5", "F-IUFNO_ep35_mag5","DSM_mag5","F-IFNO_mag10", "F-IUFNO_ep35_mag10","DSM_mag10","fDNS"]
legend = ["k=1", "k=2", "k=3", "k=4", "k=5", "k=6", "k=7", "k=8", "k=9","k=10"]
############################## setting of fonts ####################################
mpl.rc('font', family='STIXGeneral')
mpl.rc('text', usetex=False)
mpl.rcParams['xtick.direction'] = 'in'
mpl.rcParams['ytick.direction'] = 'in'     #xy轴坐标杆标注的方向
plt.rcParams["mathtext.fontset"]  = "cm"   #数学符号的字体
mpl.rcParams["font.family"] = "STIXGeneral"
mpl.mathtext.FontConstantsBase.sup1 = 0.5     #上标相对位置
mpl.mathtext.FontConstantsBase.sub1 = 0.4     #下标相对位置
mpl.mathtext.FontConstantsBase.sub2 = 0.4
# lcolor = ['#FF0000', '#00D200', '#0000FF', '#FF00FF', '#000000', '#000000', '#000000', 'salmon', 'violet', 'yellowgreen']
# lstyle = ["solid", "dashed", "dashdot", ":", ":", "-", "--", "-.", ":", "--", "-."]
# lwidth = [4.0]*np.size(lcolor)
############################## setting of figures #################################

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
    '#DC143C', '#4169E1', '#4682B4', '#008000'                          # 新增颜色至50种
]

markers = ['o', 's', 'D', 'p', '*', '^', 'v', '<', '>', 'x', 'h', '+', 'H', '1', '2', '3', '4', '|', '_', '.']
#-----------------------------------------------------------------------------------------图片大小分辨率
fig = plt.figure(figsize=(width,height), dpi=dpi)     #定义图片宽、高、分辨率
plt.rcParams["font.size"] = fontSize                  #统一字体大小
plt.rcParams["axes.linewidth"] = lineWidth
ax = fig.add_axes([0,0,1,1])                          #用于压缩图片，相当于各边移动距离
# ----------------------------------------------------------------------------------------X坐标轴设置
plt.xscale("linear")                                     #画linear
ax.xaxis.set_major_locator(mpl.ticker.MultipleLocator(20)) #次刻度
ax.xaxis.set_minor_locator(mpl.ticker.MultipleLocator(2))  #次刻度  #主刻度格式
ax.xaxis.set_major_formatter(mpl.ticker.ScalarFormatter())               #应用主刻度格式
ax.xaxis.set_minor_formatter(mpl.ticker.NullFormatter()) #次刻度
# ----------------------------------------------------------------------------------------Y坐标轴设置
plt.yscale("linear")
ax.yaxis.set_major_locator(ticker.MaxNLocator(nbins=6, min_n_ticks=5))  # Automatically set major ticks
ax.yaxis.set_minor_locator(ticker.AutoMinorLocator(5))  # Automatically set minor ticks to be 5 times finer than major ticks
ax.autoscale(enable=True, axis='y', tight=False)
# formatter = mpl.ticker.LogFormatterSciNotation()
ax.yaxis.set_major_formatter(mpl.ticker.ScalarFormatter())
ax.yaxis.set_minor_formatter(mpl.ticker.NullFormatter())
# ----------------------------------------------------------------------------------------坐标边框可见性、及边框宽度
# Hide the top and right spines of the axis
ax.spines['right'].set_visible(True)
ax.spines['top'].set_visible(True)
# Set the axis box line width
ax.spines['bottom'].set_linewidth(boxWidth)
ax.spines['left'].set_linewidth(boxWidth)
ax.spines['top'].set_linewidth(boxWidth)
ax.spines['right'].set_linewidth(boxWidth)
# ----------------------------------------------------------------------------------------坐标刻度设置、标签、显示范围
# Tick Parameters: Edit the major and minor ticks of the x and y axes
ax.xaxis.set_tick_params(which='major', size=Lmajor, width=boxWidth, direction='in',pad=xlabPad, top=False)
ax.xaxis.set_tick_params(which='minor', size=Lminor, width=boxWidth, direction='in',pad=xlabPad, top=False)
ax.yaxis.set_tick_params(which='major', size=Lmajor, width=boxWidth, direction='in',pad=ylabPad, right=False)
ax.yaxis.set_tick_params(which='minor', size=Lminor, width=boxWidth, direction='in',pad=ylabPad, right=False)
plt.xlabel(xlabel)
plt.ylabel(ylabel)
ax.set_xlim(xlimit[0], xlimit[1])
#ax.set_ylim(ylimit[0], ylimit[1])
ncurv = len(legend)  #每个图画4条线

# ------------------------------------------------------------------------------------------
x = np.arange(0.2, time_steps*0.2+0.2,0.2)
step1=1

mean=mean3
std=std3

k=3
plt.plot(x, mean[(k-1)*600:k*600], label=legend[2], color='gold', linewidth=lineWidth, linestyle='solid',zorder=5)
plt.fill_between(x, mean[(k-1)*600:k*600] - std[(k-1)*600:k*600], mean[(k-1)*600:k*600] + std[(k-1)*600:k*600], color='gold', alpha=0.3,zorder=5)

k=4
plt.plot(x, mean[(k-1)*600:k*600], label=legend[3], color='green', linewidth=lineWidth, linestyle='solid',zorder=5)
plt.fill_between(x, mean[(k-1)*600:k*600] - std[(k-1)*600:k*600], mean[(k-1)*600:k*600] + std[(k-1)*600:k*600], color='green', alpha=0.3,zorder=5)

k=5
plt.plot(x, mean[(k-1)*600:k*600], label=legend[4], color='#1f77b4', linewidth=lineWidth, linestyle='solid',zorder=5)
plt.fill_between(x, mean[(k-1)*600:k*600] - std[(k-1)*600:k*600], mean[(k-1)*600:k*600] + std[(k-1)*600:k*600], color='#1f77b4', alpha=0.3,zorder=5)

k=6
plt.plot(x, mean[(k-1)*600:k*600], label=legend[5], color='#008080', linewidth=lineWidth, linestyle='solid',zorder=5)
plt.fill_between(x, mean[(k-1)*600:k*600] - std[(k-1)*600:k*600], mean[(k-1)*600:k*600] + std[(k-1)*600:k*600], color='#008080', alpha=0.3,zorder=5)

k=7
plt.plot(x, mean[(k-1)*600:k*600], label=legend[6], color='purple', linewidth=lineWidth, linestyle='solid',zorder=5)
plt.fill_between(x, mean[(k-1)*600:k*600] - std[(k-1)*600:k*600], mean[(k-1)*600:k*600] + std[(k-1)*600:k*600], color='purple', alpha=0.3,zorder=5)

k=8
plt.plot(x, mean[(k-1)*600:k*600], label=legend[7], color='pink', linewidth=lineWidth, linestyle='solid',zorder=5)
plt.fill_between(x, mean[(k-1)*600:k*600] - std[(k-1)*600:k*600], mean[(k-1)*600:k*600] + std[(k-1)*600:k*600], color='pink', alpha=0.3,zorder=5)

k=9
plt.plot(x, mean[(k-1)*600:k*600], label=legend[8], color='#00FFFF', linewidth=lineWidth, linestyle='solid',zorder=5)
plt.fill_between(x, mean[(k-1)*600:k*600] - std[(k-1)*600:k*600], mean[(k-1)*600:k*600] + std[(k-1)*600:k*600], color='#00FFFF', alpha=0.3,zorder=5)

k=10
plt.plot(x, mean[(k-1)*600:k*600], label=legend[9], color='#FF00FF', linewidth=lineWidth, linestyle='solid',zorder=9)
plt.fill_between(x, mean[(k-1)*600:k*600] - std[(k-1)*600:k*600], mean[(k-1)*600:k*600] + std[(k-1)*600:k*600], color='#FF00FF', alpha=0.3,zorder=9)


lgd_loc  = (0.8,0.5)#6 7#6 80 88
lgd_font = {'family':"STIXGeneral", 'size':fontSize*0.6}
lgd = plt.legend(loc=lgd_loc, frameon=False, prop=lgd_font,handlelength=2.5,labelspacing=0.5) #2.5是legend长度,0.5是间距
#plt.title("Mean ± Std error of spectrum: F-IUFNO", fontsize=30, color='black', loc='center', pad=15)
plt.savefig(figPath, quality=100, bbox_extra_artists=(lgd,), bbox_inches='tight')
print("Width x Hight: ", fig.get_size_inches())
# plt.cl




######################### set figure path1 ################################
figfilePath = os.path.abspath('./Errorbar_with_time_with_k')
figPath = os.path.join(figfilePath, "spectrum_errorbar_with_time_30cases_IUFNO_k=3-10")

print("图片存放路径：", figPath)


############################## setting of figures #################################
dpi = 600                               #分辨率
width  = 8                              #图宽
height = 6                              #图高
fontSize = 30                          #字体大小
lineWidth = 2.5                         #线宽
boxWidth = 2.5                          #边框线宽
Lmajor = 7                              #主刻度长度
Lminor = 4                              #次刻度长度
xlabPad  = 10                           #x坐标下面显示值距离轴距离
ylabPad  = 10                           #y坐标下面显示值距离轴距离
xlabel = r"$\mathdefault{t/\tau}$"            #坐标标签
ylabel = r"$\mathdefault{Mean \pm Std \ error}$"
xlimit = [1,121]                        #坐标显示范围
#ylimit = [-60,60]
legend2 = ["F-IFNO", "F-IUFNO_ep35", "F-IUFNO_ep40","IUFNO_ep11","IUFNO_ep40","IFNO","DSM","F-IFNO_mag0.1", "F-IUFNO_ep35_mag0.1","F-IUFNO_ep40_mag0.1","IUFNO_ep11_mag0.1","IUFNO_ep40_mag0.1","IFNO_mag0.1","DSM_mag0.1","F-IFNO_mag0.5", "F-IUFNO_ep35_mag0.5","F-IUFNO_ep40_mag0.5","IUFNO_ep11_mag0.5","IUFNO_ep40_mag0.5","IFNO_mag0.5","DSM_mag0.5","F-IFNO_mag1", "F-IUFNO_ep35_mag1","DSM_mag1","F-IFNO_mag2", "F-IUFNO_ep35_mag2","DSM_mag2","F-IFNO_mag5", "F-IUFNO_ep35_mag5","DSM_mag5","F-IFNO_mag10", "F-IUFNO_ep35_mag10","DSM_mag10","fDNS"]
legend = ["k=1", "k=2", "k=3", "k=4", "k=5", "k=6", "k=7", "k=8", "k=9","k=10"]
############################## setting of fonts ####################################
mpl.rc('font', family='STIXGeneral')
mpl.rc('text', usetex=False)
mpl.rcParams['xtick.direction'] = 'in'
mpl.rcParams['ytick.direction'] = 'in'     #xy轴坐标杆标注的方向
plt.rcParams["mathtext.fontset"]  = "cm"   #数学符号的字体
mpl.rcParams["font.family"] = "STIXGeneral"
mpl.mathtext.FontConstantsBase.sup1 = 0.5     #上标相对位置
mpl.mathtext.FontConstantsBase.sub1 = 0.4     #下标相对位置
mpl.mathtext.FontConstantsBase.sub2 = 0.4
# lcolor = ['#FF0000', '#00D200', '#0000FF', '#FF00FF', '#000000', '#000000', '#000000', 'salmon', 'violet', 'yellowgreen']
# lstyle = ["solid", "dashed", "dashdot", ":", ":", "-", "--", "-.", ":", "--", "-."]
# lwidth = [4.0]*np.size(lcolor)
############################## setting of figures #################################

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
    '#DC143C', '#4169E1', '#4682B4', '#008000'                          # 新增颜色至50种
]

markers = ['o', 's', 'D', 'p', '*', '^', 'v', '<', '>', 'x', 'h', '+', 'H', '1', '2', '3', '4', '|', '_', '.']
#-----------------------------------------------------------------------------------------图片大小分辨率
fig = plt.figure(figsize=(width,height), dpi=dpi)     #定义图片宽、高、分辨率
plt.rcParams["font.size"] = fontSize                  #统一字体大小
plt.rcParams["axes.linewidth"] = lineWidth
ax = fig.add_axes([0,0,1,1])                          #用于压缩图片，相当于各边移动距离
# ----------------------------------------------------------------------------------------X坐标轴设置
plt.xscale("linear")                                     #画linear
ax.xaxis.set_major_locator(mpl.ticker.MultipleLocator(20)) #次刻度
ax.xaxis.set_minor_locator(mpl.ticker.MultipleLocator(2))  #次刻度  #主刻度格式
ax.xaxis.set_major_formatter(mpl.ticker.ScalarFormatter())               #应用主刻度格式
ax.xaxis.set_minor_formatter(mpl.ticker.NullFormatter()) #次刻度
# ----------------------------------------------------------------------------------------Y坐标轴设置
plt.yscale("linear")
ax.yaxis.set_major_locator(ticker.MaxNLocator(nbins=6, min_n_ticks=5))  # Automatically set major ticks
ax.yaxis.set_minor_locator(ticker.AutoMinorLocator(5))  # Automatically set minor ticks to be 5 times finer than major ticks
ax.autoscale(enable=True, axis='y', tight=False)
# formatter = mpl.ticker.LogFormatterSciNotation()
ax.yaxis.set_major_formatter(mpl.ticker.ScalarFormatter())
ax.yaxis.set_minor_formatter(mpl.ticker.NullFormatter())
# ----------------------------------------------------------------------------------------坐标边框可见性、及边框宽度
# Hide the top and right spines of the axis
ax.spines['right'].set_visible(True)
ax.spines['top'].set_visible(True)
# Set the axis box line width
ax.spines['bottom'].set_linewidth(boxWidth)
ax.spines['left'].set_linewidth(boxWidth)
ax.spines['top'].set_linewidth(boxWidth)
ax.spines['right'].set_linewidth(boxWidth)
# ----------------------------------------------------------------------------------------坐标刻度设置、标签、显示范围
# Tick Parameters: Edit the major and minor ticks of the x and y axes
ax.xaxis.set_tick_params(which='major', size=Lmajor, width=boxWidth, direction='in',pad=xlabPad, top=False)
ax.xaxis.set_tick_params(which='minor', size=Lminor, width=boxWidth, direction='in',pad=xlabPad, top=False)
ax.yaxis.set_tick_params(which='major', size=Lmajor, width=boxWidth, direction='in',pad=ylabPad, right=False)
ax.yaxis.set_tick_params(which='minor', size=Lminor, width=boxWidth, direction='in',pad=ylabPad, right=False)
plt.xlabel(xlabel)
plt.ylabel(ylabel)
ax.set_xlim(xlimit[0], xlimit[1])
#ax.set_ylim(ylimit[0], ylimit[1])
ncurv = len(legend)  #每个图画4条线

# ------------------------------------------------------------------------------------------
x = np.arange(0.2, time_steps*0.2+0.2,0.2)
step1=1

mean=mean4
std=std4

k=3
plt.plot(x, mean[(k-1)*600:k*600], label=legend[2], color='gold', linewidth=lineWidth, linestyle='solid',zorder=5)
plt.fill_between(x, mean[(k-1)*600:k*600] - std[(k-1)*600:k*600], mean[(k-1)*600:k*600] + std[(k-1)*600:k*600], color='gold', alpha=0.3,zorder=5)

k=4
plt.plot(x, mean[(k-1)*600:k*600], label=legend[3], color='green', linewidth=lineWidth, linestyle='solid',zorder=5)
plt.fill_between(x, mean[(k-1)*600:k*600] - std[(k-1)*600:k*600], mean[(k-1)*600:k*600] + std[(k-1)*600:k*600], color='green', alpha=0.3,zorder=5)

k=5
plt.plot(x, mean[(k-1)*600:k*600], label=legend[4], color='#1f77b4', linewidth=lineWidth, linestyle='solid',zorder=5)
plt.fill_between(x, mean[(k-1)*600:k*600] - std[(k-1)*600:k*600], mean[(k-1)*600:k*600] + std[(k-1)*600:k*600], color='#1f77b4', alpha=0.3,zorder=5)

k=6
plt.plot(x, mean[(k-1)*600:k*600], label=legend[5], color='#008080', linewidth=lineWidth, linestyle='solid',zorder=5)
plt.fill_between(x, mean[(k-1)*600:k*600] - std[(k-1)*600:k*600], mean[(k-1)*600:k*600] + std[(k-1)*600:k*600], color='#008080', alpha=0.3,zorder=5)

k=7
plt.plot(x, mean[(k-1)*600:k*600], label=legend[6], color='purple', linewidth=lineWidth, linestyle='solid',zorder=5)
plt.fill_between(x, mean[(k-1)*600:k*600] - std[(k-1)*600:k*600], mean[(k-1)*600:k*600] + std[(k-1)*600:k*600], color='purple', alpha=0.3,zorder=5)

k=8
plt.plot(x, mean[(k-1)*600:k*600], label=legend[7], color='pink', linewidth=lineWidth, linestyle='solid',zorder=5)
plt.fill_between(x, mean[(k-1)*600:k*600] - std[(k-1)*600:k*600], mean[(k-1)*600:k*600] + std[(k-1)*600:k*600], color='pink', alpha=0.3,zorder=5)

k=9
plt.plot(x, mean[(k-1)*600:k*600], label=legend[8], color='#00FFFF', linewidth=lineWidth, linestyle='solid',zorder=5)
plt.fill_between(x, mean[(k-1)*600:k*600] - std[(k-1)*600:k*600], mean[(k-1)*600:k*600] + std[(k-1)*600:k*600], color='#00FFFF', alpha=0.3,zorder=5)

k=10
plt.plot(x, mean[(k-1)*600:k*600], label=legend[9], color='#FF00FF', linewidth=lineWidth, linestyle='solid',zorder=9)
plt.fill_between(x, mean[(k-1)*600:k*600] - std[(k-1)*600:k*600], mean[(k-1)*600:k*600] + std[(k-1)*600:k*600], color='#FF00FF', alpha=0.3,zorder=9)


lgd_loc  = (0.8,0.5)#6 7#6 80 88
lgd_font = {'family':"STIXGeneral", 'size':fontSize*0.6}
lgd = plt.legend(loc=lgd_loc, frameon=False, prop=lgd_font,handlelength=2.5,labelspacing=0.5) #2.5是legend长度,0.5是间距
#plt.title("Mean ± Std error of spectrum: IUFNO", fontsize=30, color='black', loc='center', pad=15)
plt.savefig(figPath, quality=100, bbox_extra_artists=(lgd,), bbox_inches='tight')
print("Width x Hight: ", fig.get_size_inches())
# plt.cl






######################### set figure path1 ################################
figfilePath = os.path.abspath('./Errorbar_with_time_with_k')
figPath = os.path.join(figfilePath, "spectrum_errorbar_with_time_30cases_IFNO_k=3-10")

print("图片存放路径：", figPath)


############################## setting of figures #################################
dpi = 600                               #分辨率
width  = 8                              #图宽
height = 6                              #图高
fontSize = 30                          #字体大小
lineWidth = 2.5                         #线宽
boxWidth = 2.5                          #边框线宽
Lmajor = 7                              #主刻度长度
Lminor = 4                              #次刻度长度
xlabPad  = 10                           #x坐标下面显示值距离轴距离
ylabPad  = 10                           #y坐标下面显示值距离轴距离
xlabel = r"$\mathdefault{t/\tau}$"            #坐标标签
ylabel = r"$\mathdefault{Mean \pm Std \ error}$"
xlimit = [1,121]                        #坐标显示范围
#ylimit = [-60,60]
legend2 = ["F-IFNO", "F-IUFNO_ep35", "F-IUFNO_ep40","IUFNO_ep11","IUFNO_ep40","IFNO","DSM","F-IFNO_mag0.1", "F-IUFNO_ep35_mag0.1","F-IUFNO_ep40_mag0.1","IUFNO_ep11_mag0.1","IUFNO_ep40_mag0.1","IFNO_mag0.1","DSM_mag0.1","F-IFNO_mag0.5", "F-IUFNO_ep35_mag0.5","F-IUFNO_ep40_mag0.5","IUFNO_ep11_mag0.5","IUFNO_ep40_mag0.5","IFNO_mag0.5","DSM_mag0.5","F-IFNO_mag1", "F-IUFNO_ep35_mag1","DSM_mag1","F-IFNO_mag2", "F-IUFNO_ep35_mag2","DSM_mag2","F-IFNO_mag5", "F-IUFNO_ep35_mag5","DSM_mag5","F-IFNO_mag10", "F-IUFNO_ep35_mag10","DSM_mag10","fDNS"]
legend = ["k=1", "k=2", "k=3", "k=4", "k=5", "k=6", "k=7", "k=8", "k=9","k=10"]
############################## setting of fonts ####################################
mpl.rc('font', family='STIXGeneral')
mpl.rc('text', usetex=False)
mpl.rcParams['xtick.direction'] = 'in'
mpl.rcParams['ytick.direction'] = 'in'     #xy轴坐标杆标注的方向
plt.rcParams["mathtext.fontset"]  = "cm"   #数学符号的字体
mpl.rcParams["font.family"] = "STIXGeneral"
mpl.mathtext.FontConstantsBase.sup1 = 0.5     #上标相对位置
mpl.mathtext.FontConstantsBase.sub1 = 0.4     #下标相对位置
mpl.mathtext.FontConstantsBase.sub2 = 0.4
# lcolor = ['#FF0000', '#00D200', '#0000FF', '#FF00FF', '#000000', '#000000', '#000000', 'salmon', 'violet', 'yellowgreen']
# lstyle = ["solid", "dashed", "dashdot", ":", ":", "-", "--", "-.", ":", "--", "-."]
# lwidth = [4.0]*np.size(lcolor)
############################## setting of figures #################################

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
    '#DC143C', '#4169E1', '#4682B4', '#008000'                          # 新增颜色至50种
]

markers = ['o', 's', 'D', 'p', '*', '^', 'v', '<', '>', 'x', 'h', '+', 'H', '1', '2', '3', '4', '|', '_', '.']
#-----------------------------------------------------------------------------------------图片大小分辨率
fig = plt.figure(figsize=(width,height), dpi=dpi)     #定义图片宽、高、分辨率
plt.rcParams["font.size"] = fontSize                  #统一字体大小
plt.rcParams["axes.linewidth"] = lineWidth
ax = fig.add_axes([0,0,1,1])                          #用于压缩图片，相当于各边移动距离
# ----------------------------------------------------------------------------------------X坐标轴设置
plt.xscale("linear")                                     #画linear
ax.xaxis.set_major_locator(mpl.ticker.MultipleLocator(20)) #次刻度
ax.xaxis.set_minor_locator(mpl.ticker.MultipleLocator(2))  #次刻度  #主刻度格式
ax.xaxis.set_major_formatter(mpl.ticker.ScalarFormatter())               #应用主刻度格式
ax.xaxis.set_minor_formatter(mpl.ticker.NullFormatter()) #次刻度
# ----------------------------------------------------------------------------------------Y坐标轴设置
plt.yscale("linear")
ax.yaxis.set_major_locator(ticker.MaxNLocator(nbins=6, min_n_ticks=5))  # Automatically set major ticks
ax.yaxis.set_minor_locator(ticker.AutoMinorLocator(5))  # Automatically set minor ticks to be 5 times finer than major ticks
ax.autoscale(enable=True, axis='y', tight=False)
# formatter = mpl.ticker.LogFormatterSciNotation()
ax.yaxis.set_major_formatter(mpl.ticker.ScalarFormatter())
ax.yaxis.set_minor_formatter(mpl.ticker.NullFormatter())
# ----------------------------------------------------------------------------------------坐标边框可见性、及边框宽度
# Hide the top and right spines of the axis
ax.spines['right'].set_visible(True)
ax.spines['top'].set_visible(True)
# Set the axis box line width
ax.spines['bottom'].set_linewidth(boxWidth)
ax.spines['left'].set_linewidth(boxWidth)
ax.spines['top'].set_linewidth(boxWidth)
ax.spines['right'].set_linewidth(boxWidth)
# ----------------------------------------------------------------------------------------坐标刻度设置、标签、显示范围
# Tick Parameters: Edit the major and minor ticks of the x and y axes
ax.xaxis.set_tick_params(which='major', size=Lmajor, width=boxWidth, direction='in',pad=xlabPad, top=False)
ax.xaxis.set_tick_params(which='minor', size=Lminor, width=boxWidth, direction='in',pad=xlabPad, top=False)
ax.yaxis.set_tick_params(which='major', size=Lmajor, width=boxWidth, direction='in',pad=ylabPad, right=False)
ax.yaxis.set_tick_params(which='minor', size=Lminor, width=boxWidth, direction='in',pad=ylabPad, right=False)
plt.xlabel(xlabel)
plt.ylabel(ylabel)
ax.set_xlim(xlimit[0], xlimit[1])
#ax.set_ylim(ylimit[0], ylimit[1])
ncurv = len(legend)  #每个图画4条线

# ------------------------------------------------------------------------------------------
x = np.arange(0.2, time_steps*0.2+0.2,0.2)
step1=1

mean=mean5
std=std5

k=3
plt.plot(x, mean[(k-1)*600:k*600], label=legend[2], color='gold', linewidth=lineWidth, linestyle='solid',zorder=5)
plt.fill_between(x, mean[(k-1)*600:k*600] - std[(k-1)*600:k*600], mean[(k-1)*600:k*600] + std[(k-1)*600:k*600], color='gold', alpha=0.3,zorder=5)

k=4
plt.plot(x, mean[(k-1)*600:k*600], label=legend[3], color='green', linewidth=lineWidth, linestyle='solid',zorder=5)
plt.fill_between(x, mean[(k-1)*600:k*600] - std[(k-1)*600:k*600], mean[(k-1)*600:k*600] + std[(k-1)*600:k*600], color='green', alpha=0.3,zorder=5)

k=5
plt.plot(x, mean[(k-1)*600:k*600], label=legend[4], color='#1f77b4', linewidth=lineWidth, linestyle='solid',zorder=5)
plt.fill_between(x, mean[(k-1)*600:k*600] - std[(k-1)*600:k*600], mean[(k-1)*600:k*600] + std[(k-1)*600:k*600], color='#1f77b4', alpha=0.3,zorder=5)

k=6
plt.plot(x, mean[(k-1)*600:k*600], label=legend[5], color='#008080', linewidth=lineWidth, linestyle='solid',zorder=5)
plt.fill_between(x, mean[(k-1)*600:k*600] - std[(k-1)*600:k*600], mean[(k-1)*600:k*600] + std[(k-1)*600:k*600], color='#008080', alpha=0.3,zorder=5)

k=7
plt.plot(x, mean[(k-1)*600:k*600], label=legend[6], color='purple', linewidth=lineWidth, linestyle='solid',zorder=5)
plt.fill_between(x, mean[(k-1)*600:k*600] - std[(k-1)*600:k*600], mean[(k-1)*600:k*600] + std[(k-1)*600:k*600], color='purple', alpha=0.3,zorder=5)

k=8
plt.plot(x, mean[(k-1)*600:k*600], label=legend[7], color='pink', linewidth=lineWidth, linestyle='solid',zorder=5)
plt.fill_between(x, mean[(k-1)*600:k*600] - std[(k-1)*600:k*600], mean[(k-1)*600:k*600] + std[(k-1)*600:k*600], color='pink', alpha=0.3,zorder=5)

k=9
plt.plot(x, mean[(k-1)*600:k*600], label=legend[8], color='#00FFFF', linewidth=lineWidth, linestyle='solid',zorder=5)
plt.fill_between(x, mean[(k-1)*600:k*600] - std[(k-1)*600:k*600], mean[(k-1)*600:k*600] + std[(k-1)*600:k*600], color='#00FFFF', alpha=0.3,zorder=5)

k=10
plt.plot(x, mean[(k-1)*600:k*600], label=legend[9], color='#FF00FF', linewidth=lineWidth, linestyle='solid',zorder=9)
plt.fill_between(x, mean[(k-1)*600:k*600] - std[(k-1)*600:k*600], mean[(k-1)*600:k*600] + std[(k-1)*600:k*600], color='#FF00FF', alpha=0.3,zorder=9)


lgd_loc  = (0.8,0.5)#6 7#6 80 88
lgd_font = {'family':"STIXGeneral", 'size':fontSize*0.6}
lgd = plt.legend(loc=lgd_loc, frameon=False, prop=lgd_font,handlelength=2.5,labelspacing=0.5) #2.5是legend长度,0.5是间距
#plt.title("Mean ± Std error of spectrum: IFNO", fontsize=30, color='black', loc='center', pad=15)
plt.savefig(figPath, quality=100, bbox_extra_artists=(lgd,), bbox_inches='tight')
print("Width x Hight: ", fig.get_size_inches())
# plt.cl



######################### set figure path1 ################################
figfilePath = os.path.abspath('./Errorbar_with_time_with_k')
figPath = os.path.join(figfilePath, "spectrum_errorbar_with_time_30cases_DSM_k=3-10")

print("图片存放路径：", figPath)


############################## setting of figures #################################
dpi = 600                               #分辨率
width  = 8                              #图宽
height = 6                              #图高
fontSize = 30                          #字体大小
lineWidth = 2.5                         #线宽
boxWidth = 2.5                          #边框线宽
Lmajor = 7                              #主刻度长度
Lminor = 4                              #次刻度长度
xlabPad  = 10                           #x坐标下面显示值距离轴距离
ylabPad  = 10                           #y坐标下面显示值距离轴距离
xlabel = r"$\mathdefault{t/\tau}$"            #坐标标签
ylabel = r"$\mathdefault{Mean \pm Std \ error}$"
xlimit = [1,121]                        #坐标显示范围
#ylimit = [-60,60]
legend2 = ["F-IFNO", "F-IUFNO_ep35", "F-IUFNO_ep40","IUFNO_ep11","IUFNO_ep40","IFNO","DSM","F-IFNO_mag0.1", "F-IUFNO_ep35_mag0.1","F-IUFNO_ep40_mag0.1","IUFNO_ep11_mag0.1","IUFNO_ep40_mag0.1","IFNO_mag0.1","DSM_mag0.1","F-IFNO_mag0.5", "F-IUFNO_ep35_mag0.5","F-IUFNO_ep40_mag0.5","IUFNO_ep11_mag0.5","IUFNO_ep40_mag0.5","IFNO_mag0.5","DSM_mag0.5","F-IFNO_mag1", "F-IUFNO_ep35_mag1","DSM_mag1","F-IFNO_mag2", "F-IUFNO_ep35_mag2","DSM_mag2","F-IFNO_mag5", "F-IUFNO_ep35_mag5","DSM_mag5","F-IFNO_mag10", "F-IUFNO_ep35_mag10","DSM_mag10","fDNS"]
legend = ["k=1", "k=2", "k=3", "k=4", "k=5", "k=6", "k=7", "k=8", "k=9","k=10"]
############################## setting of fonts ####################################
mpl.rc('font', family='STIXGeneral')
mpl.rc('text', usetex=False)
mpl.rcParams['xtick.direction'] = 'in'
mpl.rcParams['ytick.direction'] = 'in'     #xy轴坐标杆标注的方向
plt.rcParams["mathtext.fontset"]  = "cm"   #数学符号的字体
mpl.rcParams["font.family"] = "STIXGeneral"
mpl.mathtext.FontConstantsBase.sup1 = 0.5     #上标相对位置
mpl.mathtext.FontConstantsBase.sub1 = 0.4     #下标相对位置
mpl.mathtext.FontConstantsBase.sub2 = 0.4
# lcolor = ['#FF0000', '#00D200', '#0000FF', '#FF00FF', '#000000', '#000000', '#000000', 'salmon', 'violet', 'yellowgreen']
# lstyle = ["solid", "dashed", "dashdot", ":", ":", "-", "--", "-.", ":", "--", "-."]
# lwidth = [4.0]*np.size(lcolor)
############################## setting of figures #################################

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
    '#DC143C', '#4169E1', '#4682B4', '#008000'                          # 新增颜色至50种
]

markers = ['o', 's', 'D', 'p', '*', '^', 'v', '<', '>', 'x', 'h', '+', 'H', '1', '2', '3', '4', '|', '_', '.']
#-----------------------------------------------------------------------------------------图片大小分辨率
fig = plt.figure(figsize=(width,height), dpi=dpi)     #定义图片宽、高、分辨率
plt.rcParams["font.size"] = fontSize                  #统一字体大小
plt.rcParams["axes.linewidth"] = lineWidth
ax = fig.add_axes([0,0,1,1])                          #用于压缩图片，相当于各边移动距离
# ----------------------------------------------------------------------------------------X坐标轴设置
plt.xscale("linear")                                     #画linear
ax.xaxis.set_major_locator(mpl.ticker.MultipleLocator(20)) #次刻度
ax.xaxis.set_minor_locator(mpl.ticker.MultipleLocator(2))  #次刻度  #主刻度格式
ax.xaxis.set_major_formatter(mpl.ticker.ScalarFormatter())               #应用主刻度格式
ax.xaxis.set_minor_formatter(mpl.ticker.NullFormatter()) #次刻度
# ----------------------------------------------------------------------------------------Y坐标轴设置
plt.yscale("linear")
ax.yaxis.set_major_locator(ticker.MaxNLocator(nbins=6, min_n_ticks=5))  # Automatically set major ticks
ax.yaxis.set_minor_locator(ticker.AutoMinorLocator(5))  # Automatically set minor ticks to be 5 times finer than major ticks
ax.autoscale(enable=True, axis='y', tight=False)
# formatter = mpl.ticker.LogFormatterSciNotation()
ax.yaxis.set_major_formatter(mpl.ticker.ScalarFormatter())
ax.yaxis.set_minor_formatter(mpl.ticker.NullFormatter())
# ----------------------------------------------------------------------------------------坐标边框可见性、及边框宽度
# Hide the top and right spines of the axis
ax.spines['right'].set_visible(True)
ax.spines['top'].set_visible(True)
# Set the axis box line width
ax.spines['bottom'].set_linewidth(boxWidth)
ax.spines['left'].set_linewidth(boxWidth)
ax.spines['top'].set_linewidth(boxWidth)
ax.spines['right'].set_linewidth(boxWidth)
# ----------------------------------------------------------------------------------------坐标刻度设置、标签、显示范围
# Tick Parameters: Edit the major and minor ticks of the x and y axes
ax.xaxis.set_tick_params(which='major', size=Lmajor, width=boxWidth, direction='in',pad=xlabPad, top=False)
ax.xaxis.set_tick_params(which='minor', size=Lminor, width=boxWidth, direction='in',pad=xlabPad, top=False)
ax.yaxis.set_tick_params(which='major', size=Lmajor, width=boxWidth, direction='in',pad=ylabPad, right=False)
ax.yaxis.set_tick_params(which='minor', size=Lminor, width=boxWidth, direction='in',pad=ylabPad, right=False)
plt.xlabel(xlabel)
plt.ylabel(ylabel)
ax.set_xlim(xlimit[0], xlimit[1])
#ax.set_ylim(ylimit[0], ylimit[1])
ncurv = len(legend)  #每个图画4条线

# ------------------------------------------------------------------------------------------
x = np.arange(0.2, time_steps*0.2+0.2,0.2)
step1=1

mean=mean6
std=std6
k=3
plt.plot(x, mean[(k-1)*600:k*600], label=legend[2], color='gold', linewidth=lineWidth, linestyle='solid',zorder=5)
plt.fill_between(x, mean[(k-1)*600:k*600] - std[(k-1)*600:k*600], mean[(k-1)*600:k*600] + std[(k-1)*600:k*600], color='gold', alpha=0.3,zorder=5)

k=4
plt.plot(x, mean[(k-1)*600:k*600], label=legend[3], color='green', linewidth=lineWidth, linestyle='solid',zorder=5)
plt.fill_between(x, mean[(k-1)*600:k*600] - std[(k-1)*600:k*600], mean[(k-1)*600:k*600] + std[(k-1)*600:k*600], color='green', alpha=0.3,zorder=5)

k=5
plt.plot(x, mean[(k-1)*600:k*600], label=legend[4], color='#1f77b4', linewidth=lineWidth, linestyle='solid',zorder=5)
plt.fill_between(x, mean[(k-1)*600:k*600] - std[(k-1)*600:k*600], mean[(k-1)*600:k*600] + std[(k-1)*600:k*600], color='#1f77b4', alpha=0.3,zorder=5)

k=6
plt.plot(x, mean[(k-1)*600:k*600], label=legend[5], color='#008080', linewidth=lineWidth, linestyle='solid',zorder=5)
plt.fill_between(x, mean[(k-1)*600:k*600] - std[(k-1)*600:k*600], mean[(k-1)*600:k*600] + std[(k-1)*600:k*600], color='#008080', alpha=0.3,zorder=5)

k=7
plt.plot(x, mean[(k-1)*600:k*600], label=legend[6], color='purple', linewidth=lineWidth, linestyle='solid',zorder=5)
plt.fill_between(x, mean[(k-1)*600:k*600] - std[(k-1)*600:k*600], mean[(k-1)*600:k*600] + std[(k-1)*600:k*600], color='purple', alpha=0.3,zorder=5)

k=8
plt.plot(x, mean[(k-1)*600:k*600], label=legend[7], color='pink', linewidth=lineWidth, linestyle='solid',zorder=5)
plt.fill_between(x, mean[(k-1)*600:k*600] - std[(k-1)*600:k*600], mean[(k-1)*600:k*600] + std[(k-1)*600:k*600], color='pink', alpha=0.3,zorder=5)

k=9
plt.plot(x, mean[(k-1)*600:k*600], label=legend[8], color='#00FFFF', linewidth=lineWidth, linestyle='solid',zorder=5)
plt.fill_between(x, mean[(k-1)*600:k*600] - std[(k-1)*600:k*600], mean[(k-1)*600:k*600] + std[(k-1)*600:k*600], color='#00FFFF', alpha=0.3,zorder=5)

k=10
plt.plot(x, mean[(k-1)*600:k*600], label=legend[9], color='#FF00FF', linewidth=lineWidth, linestyle='solid',zorder=9)
plt.fill_between(x, mean[(k-1)*600:k*600] - std[(k-1)*600:k*600], mean[(k-1)*600:k*600] + std[(k-1)*600:k*600], color='#FF00FF', alpha=0.3,zorder=9)


lgd_loc  = (0.8,0.5)#6 7#6 80 88
lgd_font = {'family':"STIXGeneral", 'size':fontSize*0.6}
lgd = plt.legend(loc=lgd_loc, frameon=False, prop=lgd_font,handlelength=2.5,labelspacing=0.5) #2.5是legend长度,0.5是间距
#plt.title("Mean ± Std error of spectrum: DMS", fontsize=30, color='black', loc='center', pad=15)
plt.savefig(figPath, quality=100, bbox_extra_artists=(lgd,), bbox_inches='tight')
print("Width x Hight: ", fig.get_size_inches())
# plt.cl



######################### set figure path1 ################################
figfilePath = os.path.abspath('./Errorbar_with_time_with_k')
figPath = os.path.join(figfilePath, "spectrum_errorbar_with_time_30cases_fDNS_k=3-10")

print("图片存放路径：", figPath)


############################## setting of figures #################################
dpi = 600                               #分辨率
width  = 8                              #图宽
height = 6                              #图高
fontSize = 30                          #字体大小
lineWidth = 2.5                         #线宽
boxWidth = 2.5                          #边框线宽
Lmajor = 7                              #主刻度长度
Lminor = 4                              #次刻度长度
xlabPad  = 10                           #x坐标下面显示值距离轴距离
ylabPad  = 10                           #y坐标下面显示值距离轴距离
xlabel = r"$\mathdefault{t/\tau}$"            #坐标标签
ylabel = r"$\mathdefault{Mean \pm Std \ error}$"
xlimit = [1,121]                        #坐标显示范围
#ylimit = [-60,60]
legend2 = ["F-IFNO", "F-IUFNO_ep35", "F-IUFNO_ep40","IUFNO_ep11","IUFNO_ep40","IFNO","DSM","F-IFNO_mag0.1", "F-IUFNO_ep35_mag0.1","F-IUFNO_ep40_mag0.1","IUFNO_ep11_mag0.1","IUFNO_ep40_mag0.1","IFNO_mag0.1","DSM_mag0.1","F-IFNO_mag0.5", "F-IUFNO_ep35_mag0.5","F-IUFNO_ep40_mag0.5","IUFNO_ep11_mag0.5","IUFNO_ep40_mag0.5","IFNO_mag0.5","DSM_mag0.5","F-IFNO_mag1", "F-IUFNO_ep35_mag1","DSM_mag1","F-IFNO_mag2", "F-IUFNO_ep35_mag2","DSM_mag2","F-IFNO_mag5", "F-IUFNO_ep35_mag5","DSM_mag5","F-IFNO_mag10", "F-IUFNO_ep35_mag10","DSM_mag10","fDNS"]
legend = ["k=1", "k=2", "k=3", "k=4", "k=5", "k=6", "k=7", "k=8", "k=9","k=10"]
############################## setting of fonts ####################################
mpl.rc('font', family='STIXGeneral')
mpl.rc('text', usetex=False)
mpl.rcParams['xtick.direction'] = 'in'
mpl.rcParams['ytick.direction'] = 'in'     #xy轴坐标杆标注的方向
plt.rcParams["mathtext.fontset"]  = "cm"   #数学符号的字体
mpl.rcParams["font.family"] = "STIXGeneral"
mpl.mathtext.FontConstantsBase.sup1 = 0.5     #上标相对位置
mpl.mathtext.FontConstantsBase.sub1 = 0.4     #下标相对位置
mpl.mathtext.FontConstantsBase.sub2 = 0.4
# lcolor = ['#FF0000', '#00D200', '#0000FF', '#FF00FF', '#000000', '#000000', '#000000', 'salmon', 'violet', 'yellowgreen']
# lstyle = ["solid", "dashed", "dashdot", ":", ":", "-", "--", "-.", ":", "--", "-."]
# lwidth = [4.0]*np.size(lcolor)
############################## setting of figures #################################

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
    '#DC143C', '#4169E1', '#4682B4', '#008000'                          # 新增颜色至50种
]

markers = ['o', 's', 'D', 'p', '*', '^', 'v', '<', '>', 'x', 'h', '+', 'H', '1', '2', '3', '4', '|', '_', '.']
#-----------------------------------------------------------------------------------------图片大小分辨率
fig = plt.figure(figsize=(width,height), dpi=dpi)     #定义图片宽、高、分辨率
plt.rcParams["font.size"] = fontSize                  #统一字体大小
plt.rcParams["axes.linewidth"] = lineWidth
ax = fig.add_axes([0,0,1,1])                          #用于压缩图片，相当于各边移动距离
# ----------------------------------------------------------------------------------------X坐标轴设置
plt.xscale("linear")                                     #画linear
ax.xaxis.set_major_locator(mpl.ticker.MultipleLocator(20)) #次刻度
ax.xaxis.set_minor_locator(mpl.ticker.MultipleLocator(2))  #次刻度  #主刻度格式
ax.xaxis.set_major_formatter(mpl.ticker.ScalarFormatter())               #应用主刻度格式
ax.xaxis.set_minor_formatter(mpl.ticker.NullFormatter()) #次刻度
# ----------------------------------------------------------------------------------------Y坐标轴设置
plt.yscale("linear")
ax.yaxis.set_major_locator(ticker.MaxNLocator(nbins=6, min_n_ticks=5))  # Automatically set major ticks
ax.yaxis.set_minor_locator(ticker.AutoMinorLocator(5))  # Automatically set minor ticks to be 5 times finer than major ticks
ax.autoscale(enable=True, axis='y', tight=False)
# formatter = mpl.ticker.LogFormatterSciNotation()
ax.yaxis.set_major_formatter(mpl.ticker.ScalarFormatter())
ax.yaxis.set_minor_formatter(mpl.ticker.NullFormatter())
# ----------------------------------------------------------------------------------------坐标边框可见性、及边框宽度
# Hide the top and right spines of the axis
ax.spines['right'].set_visible(True)
ax.spines['top'].set_visible(True)
# Set the axis box line width
ax.spines['bottom'].set_linewidth(boxWidth)
ax.spines['left'].set_linewidth(boxWidth)
ax.spines['top'].set_linewidth(boxWidth)
ax.spines['right'].set_linewidth(boxWidth)
# ----------------------------------------------------------------------------------------坐标刻度设置、标签、显示范围
# Tick Parameters: Edit the major and minor ticks of the x and y axes
ax.xaxis.set_tick_params(which='major', size=Lmajor, width=boxWidth, direction='in',pad=xlabPad, top=False)
ax.xaxis.set_tick_params(which='minor', size=Lminor, width=boxWidth, direction='in',pad=xlabPad, top=False)
ax.yaxis.set_tick_params(which='major', size=Lmajor, width=boxWidth, direction='in',pad=ylabPad, right=False)
ax.yaxis.set_tick_params(which='minor', size=Lminor, width=boxWidth, direction='in',pad=ylabPad, right=False)
plt.xlabel(xlabel)
plt.ylabel(ylabel)
ax.set_xlim(xlimit[0], xlimit[1])
#ax.set_ylim(ylimit[0], ylimit[1])
ncurv = len(legend)  #每个图画4条线

# ------------------------------------------------------------------------------------------
x = np.arange(0.2, time_steps*0.2+0.2,0.2)
step1=1

mean=mean1
std=std1

k=3
plt.plot(x, mean[(k-1)*600:k*600], label=legend[2], color='gold', linewidth=lineWidth, linestyle='solid',zorder=5)
plt.fill_between(x, mean[(k-1)*600:k*600] - std[(k-1)*600:k*600], mean[(k-1)*600:k*600] + std[(k-1)*600:k*600], color='gold', alpha=0.3,zorder=5)

k=4
plt.plot(x, mean[(k-1)*600:k*600], label=legend[3], color='green', linewidth=lineWidth, linestyle='solid',zorder=5)
plt.fill_between(x, mean[(k-1)*600:k*600] - std[(k-1)*600:k*600], mean[(k-1)*600:k*600] + std[(k-1)*600:k*600], color='green', alpha=0.3,zorder=5)

k=5
plt.plot(x, mean[(k-1)*600:k*600], label=legend[4], color='#1f77b4', linewidth=lineWidth, linestyle='solid',zorder=5)
plt.fill_between(x, mean[(k-1)*600:k*600] - std[(k-1)*600:k*600], mean[(k-1)*600:k*600] + std[(k-1)*600:k*600], color='#1f77b4', alpha=0.3,zorder=5)

k=6
plt.plot(x, mean[(k-1)*600:k*600], label=legend[5], color='#008080', linewidth=lineWidth, linestyle='solid',zorder=5)
plt.fill_between(x, mean[(k-1)*600:k*600] - std[(k-1)*600:k*600], mean[(k-1)*600:k*600] + std[(k-1)*600:k*600], color='#008080', alpha=0.3,zorder=5)

k=7
plt.plot(x, mean[(k-1)*600:k*600], label=legend[6], color='purple', linewidth=lineWidth, linestyle='solid',zorder=5)
plt.fill_between(x, mean[(k-1)*600:k*600] - std[(k-1)*600:k*600], mean[(k-1)*600:k*600] + std[(k-1)*600:k*600], color='purple', alpha=0.3,zorder=5)

k=8
plt.plot(x, mean[(k-1)*600:k*600], label=legend[7], color='pink', linewidth=lineWidth, linestyle='solid',zorder=5)
plt.fill_between(x, mean[(k-1)*600:k*600] - std[(k-1)*600:k*600], mean[(k-1)*600:k*600] + std[(k-1)*600:k*600], color='pink', alpha=0.3,zorder=5)

k=9
plt.plot(x, mean[(k-1)*600:k*600], label=legend[8], color='#00FFFF', linewidth=lineWidth, linestyle='solid',zorder=5)
plt.fill_between(x, mean[(k-1)*600:k*600] - std[(k-1)*600:k*600], mean[(k-1)*600:k*600] + std[(k-1)*600:k*600], color='#00FFFF', alpha=0.3,zorder=5)

k=10
plt.plot(x, mean[(k-1)*600:k*600], label=legend[9], color='#FF00FF', linewidth=lineWidth, linestyle='solid',zorder=9)
plt.fill_between(x, mean[(k-1)*600:k*600] - std[(k-1)*600:k*600], mean[(k-1)*600:k*600] + std[(k-1)*600:k*600], color='#FF00FF', alpha=0.3,zorder=9)


lgd_loc  = (0.8,0.5)#6 7#6 80 88
lgd_font = {'family':"STIXGeneral", 'size':fontSize*0.6}
lgd = plt.legend(loc=lgd_loc, frameon=False, prop=lgd_font,handlelength=2.5,labelspacing=0.5) #2.5是legend长度,0.5是间距
#plt.title("Mean ± Std error of spectrum: fDNS", fontsize=30, color='black', loc='center', pad=15)
plt.savefig(figPath, quality=100, bbox_extra_artists=(lgd,), bbox_inches='tight')
print("Width x Hight: ", fig.get_size_inches())
# plt.cl

