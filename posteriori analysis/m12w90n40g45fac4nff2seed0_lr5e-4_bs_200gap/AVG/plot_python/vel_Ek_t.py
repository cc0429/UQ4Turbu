"""
@author: admin
"""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import os
import matplotlib as mpl
#os.chdir(r'C:\Users\Lenovo\Desktop\PINO_3d\post\plot_result')
case_number = 5
period = 251 #确认推进时刻T
################################# 图片保存路径 ################################
figfilePath = os.path.abspath('./plot_results')
figPath = os.path.join(figfilePath, "vel_Ek_t")
if not os.path.exists(figPath):
    os.makedirs(figPath)
print("图片存放路径：", figPath)
################################## 确认文件路径 #################################
#DNS_path = 'p512-200-210/data/d40-T129'

# FNO1_path = 'FNO-p129-d40-T33-646-data10'
# FNO2_path = 'FNO-p256-d40-T65-646-data100'
#FNO3_path = 'FNO-p512-d40-T129-646-data180'

# PINO1_path = 'PINO-p129-d40-T33-646-w19-PDE10'
# PINO2_path = 'PINO-p256-d40-T65-646-w19-PDE100'
#PINO3_path = 'PINO-p512-d40-T129-646-w19-PDE180'

# PINO4_path = 'PINO-p129-d40-T33-646-w181-data10-PDE180'
# # PINO5_path = 'PINO-p256-d40-T65-646-w181-data100-PDE180'
# PINO6_path = 'PINO-p256-d40-T65-646-w181-data180-PDE180'

#-------------------------------------------------------------读入数据，#comment去掉标识符所在行
#fDNS= np.loadtxt("../fDNS/avg_DNS_{}case_Ek_t.dat".format(case_number),dtype=float)

# FNO1= np.loadtxt("./FNO/{}/data/avg/avg_FNO_{}case_Ek_t.dat".format(FNO1_path,case_number),dtype=float)
# FNO2= np.loadtxt("./FNO/{}/data/avg/avg_FNO_{}case_Ek_t.dat".format(FNO2_path,case_number),dtype=float)
#IUFNO= np.loadtxt("./IUFNO/{}/avg_IUFNO_{}case_Ek_t.dat".format(case_number),dtype=float)

# PINO1= np.loadtxt("./PINO/{}/data/avg/avg_PINO_{}case_Ek_t.dat".format(PINO1_path,case_number),dtype=float)
# PINO2= np.loadtxt("./PINO/{}/data/avg/avg_PINO_{}case_Ek_t.dat".format(PINO2_path,case_number),dtype=float)
#fSRIUFNO= np.loadtxt("./fSRIUFNO/{}/avg_fSRIUFNO_{}case_Ek_t.dat".format(PINO3_path,case_number),dtype=float)
# PINO4= np.loadtxt("./PINO/{}/data/avg/avg_PINO_{}case_Ek_t.dat".format(PINO4_path,case_number),dtype=float)
# PINO5= np.loadtxt("./PINO/{}/data/avg/avg_PINO_{}case_Ek_t.dat".format(PINO5_path,case_number),dtype=float)
# PINO6= np.loadtxt("./PINO/{}/data/avg/avg_PINO_{}case_Ek_t.dat".format(PINO6_path,case_number),dtype=float)
fDNS= np.loadtxt("../fDNS/avg_fDNS_{}case_Ek_t.dat".format(case_number),dtype=float)
#DSM= np.loadtxt("../data_source/avg_DSM_gap200/avg_DSM_10case_vel_spec.dat",dtype=float)
#DMM= np.loadtxt("../data_source/avg_DMM_gap200/avg_DMM_10case_vel_spec.dat",dtype=float)
IUFNO_11ep= np.loadtxt("../IUFNO_11ep/avg_IUFNO_{}case_Ek_t.dat".format(case_number),dtype=float)
IUFNO_40ep= np.loadtxt("../IUFNO_40ep/avg_IUFNO_{}case_Ek_t.dat".format(case_number),dtype=float)
F_IUFNO_35ep= np.loadtxt("../F-IUFNO_35ep/avg_FIUFNO_{}case_Ek_t.dat".format(case_number),dtype=float)
SRF_IUFNO_36ep= np.loadtxt("../SRF-IUFNO_36ep/avg_SRFIUFNO_{}case_Ek_t.dat".format(case_number),dtype=float)
F_IUFNO_40ep= np.loadtxt("../F-IUFNO_40ep/avg_FIUFNO_{}case_Ek_t.dat".format(case_number),dtype=float)
SRF_IUFNO_40ep= np.loadtxt("../SRF-IUFNO_40ep/avg_SRFIUFNO_{}case_Ek_t.dat".format(case_number),dtype=float)
F_IFNO_40ep= np.loadtxt("../F-IFNO_40ep/avg_FIFNO_{}case_Ek_t.dat".format(case_number),dtype=float)
#UFNO= np.loadtxt("../data_source/avg_UFNO_gap200/avg_UFNO_10case_vel_spec.dat",dtype=float)
#IFNO= np.loadtxt("../data_source/avg_IFNO_gap200/avg_IFNO_10case_vel_spec.dat",dtype=float)
#IUFNO= np.loadtxt("../data_source/avg_IUFNO_gap200/avg_IUFNO_10case_vel_spec.dat",dtype=float)
#SRF_IFNO_coeff_40ep= np.loadtxt("../SRF-IFNO_coeff_40ep/avg_SRFIUFNO_{}case_Ek_t.dat".format(case_number),dtype=float)
SRF_IFNO_40ep= np.loadtxt("../SRF-IFNO_40ep/avg_SRFIFNO_{}case_Ek_t.dat".format(case_number),dtype=float)
IFNO_40ep= np.loadtxt("../IFNO_40ep/avg_IFNO_{}case_Ek_t.dat".format(case_number),dtype=float)
#################

y_fDNS=fDNS[:,1]
y_SRF_IUFNO_36ep=SRF_IUFNO_36ep[:,1]
y_F_IUFNO_35ep=F_IUFNO_35ep[:,1]
y_SRF_IUFNO_40ep=SRF_IUFNO_40ep[:,1]
y_F_IUFNO_40ep=F_IUFNO_40ep[:,1]
y_IUFNO_11ep=IUFNO_11ep[:,1]
y_IUFNO_40ep=IUFNO_40ep[:,1]
y_SRF_IFNO_40ep=SRF_IFNO_40ep[:,1]
#y_SRF_IFNO_coeff_40ep=SRF_IFNO_coeff_40ep[:,1]
y_F_IFNO_40ep=F_IFNO_40ep[:,1]
y_IFNO_40ep=IFNO_40ep[:,1]
#y_IFNO_40ep=IFNO_40ep[:,1]
# y_FNO1=FNO1[:,1]
# y_FNO2=FNO2[:,1]
#y_IUFNO=IUFNO[:,1]
#
# y_PINO1 =PINO1[:,1]
# y_PINO2 =PINO2[:,1]
#y_fSRIUFNO =fSRIUFNO[:,1]
# y_PINO4 =PINO4[:,1]
# y_PINO5 =PINO5[:,1]
# y_PINO6 =PINO6[:,1]
#--------------------------


x = fDNS[0:period,0]  #共用的x


############################## setting of figures #################################
dpi = 600                               #分辨率
width  = 8                              #图宽
height = 6                              #图高
fontSize = 30                          #字体大小
lineWidth = 1.5                         #线宽
boxWidth = 2.5                          #边框线宽
Lmajor = 7                              #主刻度长度
Lminor = 4                              #次刻度长度
xlabPad  = 10                           #x坐标下面显示值距离轴距离
ylabPad  = 10                           #y坐标下面显示值距离轴距离
xlabel = r"$\mathdefault{T}$"   #坐标标签
ylabel = r"$\mathdefault{E(t)}$"
xlimit = [0,period+1]                        #坐标显示范围
ylimit = [0.0,10.0]
#legend = ["DNS", "FNO:data10", "FNO:data100", "FNO:data180", "PINO:PDE10", "PINO:PDE100", "PINO:PDE180","PINO:data10+PDE100","PINO:data100+PDE100","PINO:data180+PDE100"]
legend = ["fDNS", "SRF-IUFNO_ep36", "F-IUFNO_ep35","SRF-IUFNO_ep40", "F-IUFNO_ep40","IUFNO_ep11", "SRF-IFNO_ep40", "F-IFNO_ep40", "IFNO_ep40","IUFNO_ep40", "SRF-IFNO_coeff_ep40"]
############################## setting of fonts ####################################
mpl.rc('font', family='Times New Roman')
mpl.rc('text', usetex=False)
mpl.rcParams['xtick.direction'] = 'in'
mpl.rcParams['ytick.direction'] = 'in'     #xy轴坐标杆标注的方向
plt.rcParams["mathtext.fontset"]  = "cm"   #数学符号的字体
mpl.rcParams["font.family"] = "Times New Roman"
# mpl.mathtext.FontConstantsBase.sup1 = 0.5     #上标相对位置
# mpl.mathtext.FontConstantsBase.sub1 = 0.4     #下标相对位置
# mpl.mathtext.FontConstantsBase.sub2 = 0.4
# lcolor = ['#FF0000', '#00D200', '#0000FF', '#FF00FF', '#000000', '#000000', '#000000', 'salmon', 'violet', 'yellowgreen']
# lstyle = ["solid", "dashed", "dashdot", ":", ":", "-", "--", "-.", ":", "--", "-."]
# lwidth = [4.0]*np.size(lcolor)

#设置刻度格式器,确定精度
def minor_tick(x, pos):
    if not x % 1.0:
        return ""
    return "%.1f" % x

############################## setting of figures #################################

                           #输入的[1,5,10,15] #用于文件起名
gfile = "vel_Ek_t.png"              #保存的文件名
gpath = os.path.join(figPath, gfile)
#-----------------------------------------------------------------------------------------图片大小分辨率
fig = plt.figure(figsize=(width,height), dpi=dpi)     #定义图片宽、高、分辨率
plt.rcParams["font.size"] = fontSize                  #统一字体大小
plt.rcParams["axes.linewidth"] = lineWidth
ax = fig.add_axes([0,0,1,1])                          #用于压缩图片，相当于各边移动距离
# ----------------------------------------------------------------------------------------X坐标轴设置
plt.xscale("linear")                                     #画linear
ax.xaxis.set_major_locator(mpl.ticker.MultipleLocator(50)) #次刻度
ax.xaxis.set_minor_locator(mpl.ticker.MultipleLocator(5))  #次刻度  #主刻度格式
ax.xaxis.set_major_formatter(mpl.ticker.ScalarFormatter())               #应用主刻度格式
ax.xaxis.set_minor_formatter(mpl.ticker.NullFormatter()) #次刻度
# ----------------------------------------------------------------------------------------Y坐标轴设置
plt.yscale("linear")
ax.yaxis.set_major_locator(mpl.ticker.MultipleLocator(2))
ax.yaxis.set_minor_locator(mpl.ticker.MultipleLocator(1))
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
ax.set_ylim(ylimit[0], ylimit[1])
ncurv = len(legend)  #每个图画几条线

# ------------------------------------------------------------------------------------------
plt.plot(x, y_fDNS, label=legend[0], color='red', linewidth=lineWidth*2, linestyle='solid',zorder=0)

# plt.scatter(x, y_FNO1, label=legend[1], facecolor='none', linewidths=lineWidth,edgecolor='blue', s=80, alpha=1.0, marker='o',zorder=1)
# plt.scatter(x, y_FNO2, label=legend[2], facecolor='none', linewidths=lineWidth,edgecolor='blue', s=80, alpha=1.0, marker='v',zorder=2)
'''plt.scatter(x, y_SRF_IUFNO_36ep, label=legend[1], facecolor='none', linewidths=lineWidth,edgecolor='blue', s=80, alpha=1.0, marker='o',zorder=3)
plt.scatter(x, y_F_IUFNO_35ep, label=legend[2], facecolor='none', linewidths=lineWidth,edgecolor='green', s=80, alpha=1.0, marker='^',zorder=4)
plt.scatter(x, y_SRF_IUFNO_40ep, label=legend[3], facecolor='none', linewidths=lineWidth,edgecolor='purple', s=80, alpha=1.0, marker='*',zorder=5)
plt.scatter(x, y_F_IUFNO_40ep, label=legend[4], facecolor='none', linewidths=lineWidth,edgecolor='orange', s=80, alpha=1.0, marker='v',zorder=3)
plt.scatter(x, y_IUFNO_11ep, label=legend[5], facecolor='none', linewidths=lineWidth,edgecolor='yellow', s=80, alpha=1.0, marker='o',zorder=4)
plt.scatter(x, y_SRF_IFNO_coeff_40ep, label=legend[6], facecolor='none', linewidths=lineWidth,edgecolor='gray', s=80, alpha=1.0, marker='s',zorder=5)
# plt.scatter(x, y_PINO1, label=legend[4], facecolor='none', linewidths=lineWidth, edgecolor='green', s=80, alpha=1.0, marker='o', zorder=4)
# plt.scatter(x, y_PINO2, label=legend[5], facecolor='none', linewidths=lineWidth, edgecolor='green', s=80, alpha=1.0, marker='v', zorder=5)
plt.scatter(x, y_F_IFNO_40ep, label=legend[7], facecolor='none', linewidths=lineWidth, edgecolor='olive', s=80, alpha=1.0, marker='*', zorder=6)'''
# plt.scatter(x, y_PINO4, label=legend[7], facecolor='none', linewidths=lineWidth, edgecolor='darkorange', s=80, alpha=1.0, marker='o', zorder=7)
# plt.scatter(x, y_PINO5, label=legend[8], facecolor='none', linewidths=lineWidth, edgecolor='darkorange', s=80, alpha=1.0, marker='v', zorder=8)
# plt.scatter(x, y_PINO6, label=legend[9], facecolor='none', linewidths=lineWidth, edgecolor='darkorange', s=80, alpha=1.0, marker='*', zorder=9)
plt.plot(x[::1], y_SRF_IUFNO_36ep[::1], label=legend[1], linewidth=lineWidth,color='blue', linestyle='-' ,zorder=0)
plt.plot(x[::1], y_F_IUFNO_35ep[::1], label=legend[2], linewidth=lineWidth,color='green', linestyle='dashed' , zorder=0)
plt.plot(x[::1], y_SRF_IUFNO_40ep[::1], label=legend[3], linewidth=lineWidth,color='purple', linestyle='-.' ,zorder=0)
plt.plot(x[::1], y_F_IUFNO_40ep[::1], label=legend[4], linewidth=lineWidth,color='orange', linestyle='dashdot' ,zorder=0)
plt.plot(x[::1], y_IUFNO_11ep[::1], label=legend[5], linewidth=lineWidth,color='violet', linestyle='dashed' ,zorder=0)
plt.plot(x[::1], y_IUFNO_40ep[::1], label=legend[9], linewidth=lineWidth,color='yellow', linestyle='--',zorder=0)
plt.plot(x[::1], y_SRF_IFNO_40ep[::1], label=legend[6], linewidth=lineWidth,color='cyan', linestyle='solid' ,zorder=0)
#plt.plot(x[::1], y_SRF_IFNO_coeff_40ep[::1], label=legend[10], linewidth=lineWidth,color='gray', linestyle=':' ,zorder=0)
plt.plot(x[::1], y_F_IFNO_40ep[::1], label=legend[7], linewidth=lineWidth, color='olive', linestyle='dashdot' , zorder=0) 
plt.plot(x[::1], y_IFNO_40ep[::1], label=legend[8], linewidth=lineWidth, color='pink', linestyle=':' , zorder=0) 

lgd_loc  = (0.7,0.5)
lgd_font = {'family':"Times New Roman", 'size':fontSize*0.45}
lgd = plt.legend(loc=lgd_loc, frameon=False, prop=lgd_font,handlelength=2.5,labelspacing=0.5) #2.5是legend长度,0.5是间距
plt.savefig(gpath,  bbox_extra_artists=(lgd,), bbox_inches='tight')
print("Width x Hight: ", fig.get_size_inches())
# plt.cl