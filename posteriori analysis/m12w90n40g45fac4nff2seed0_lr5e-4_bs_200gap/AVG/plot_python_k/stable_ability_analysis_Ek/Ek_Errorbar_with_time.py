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


fDNS = np.loadtxt("./result/{}cases/error_with_time_fDNS.dat".format(case_number), dtype=float)
IUFNO = np.loadtxt("./result/{}cases/error_with_time_IUFNO.dat".format(case_number), dtype=float)
F_IUFNO = np.loadtxt("./result/{}cases/error_with_time_F_IUFNO.dat".format(case_number), dtype=float)
F_IFNO = np.loadtxt("./result/{}cases/error_with_time_F_IFNO.dat".format(case_number), dtype=float)
IFNO = np.loadtxt("./result/{}cases/error_with_time_IFNO.dat".format(case_number), dtype=float)
DSM = np.loadtxt("./result/{}cases/error_with_time_DSM.dat".format(case_number), dtype=float)

IUFNO_m01 = np.loadtxt("./result/{}cases/error_with_time_IUFNO_m01.dat".format(case_number), dtype=float)
F_IUFNO_m01 = np.loadtxt("./result/{}cases/error_with_time_F_IUFNO_m01.dat".format(case_number), dtype=float)
F_IFNO_m01 = np.loadtxt("./result/{}cases/error_with_time_F_IFNO_m01.dat".format(case_number), dtype=float)
IFNO_m01 = np.loadtxt("./result/{}cases/error_with_time_IFNO_m01.dat".format(case_number), dtype=float)
DSM_m01 = np.loadtxt("./result/{}cases/error_with_time_DSM_m01.dat".format(case_number), dtype=float)

IUFNO_m05 = np.loadtxt("./result/{}cases/error_with_time_IUFNO_m05.dat".format(case_number), dtype=float)
F_IUFNO_m05 = np.loadtxt("./result/{}cases/error_with_time_F_IUFNO_m05.dat".format(case_number), dtype=float)
F_IFNO_m05 = np.loadtxt("./result/{}cases/error_with_time_F_IFNO_m05.dat".format(case_number), dtype=float)
IFNO_m05 = np.loadtxt("./result/{}cases/error_with_time_IFNO_m05.dat".format(case_number), dtype=float)
DSM_m05 = np.loadtxt("./result/{}cases/error_with_time_DSM_m05.dat".format(case_number), dtype=float)    

IUFNO_m1 = np.loadtxt("./result/{}cases/error_with_time_IUFNO_m1.dat".format(case_number), dtype=float)
F_IUFNO_m1 = np.loadtxt("./result/{}cases/error_with_time_F_IUFNO_m1.dat".format(case_number), dtype=float)
F_IFNO_m1 = np.loadtxt("./result/{}cases/error_with_time_F_IFNO_m1.dat".format(case_number), dtype=float)
IFNO_m1 = np.loadtxt("./result/{}cases/error_with_time_IFNO_m1.dat".format(case_number), dtype=float)
DSM_m1 = np.loadtxt("./result/{}cases/error_with_time_DSM_m1.dat".format(case_number), dtype=float)    

IUFNO_m2 = np.loadtxt("./result/{}cases/error_with_time_IUFNO_m2.dat".format(case_number), dtype=float)
F_IUFNO_m2 = np.loadtxt("./result/{}cases/error_with_time_F_IUFNO_m2.dat".format(case_number), dtype=float)
F_IFNO_m2 = np.loadtxt("./result/{}cases/error_with_time_F_IFNO_m2.dat".format(case_number), dtype=float)
IFNO_m2 = np.loadtxt("./result/{}cases/error_with_time_IFNO_m2.dat".format(case_number), dtype=float)
DSM_m2 = np.loadtxt("./result/{}cases/error_with_time_DSM_m2.dat".format(case_number), dtype=float)    

IUFNO_m5 = np.loadtxt("./result/{}cases/error_with_time_IUFNO_m5.dat".format(case_number), dtype=float)
F_IUFNO_m5 = np.loadtxt("./result/{}cases/error_with_time_F_IUFNO_m5.dat".format(case_number), dtype=float)
F_IFNO_m5 = np.loadtxt("./result/{}cases/error_with_time_F_IFNO_m5.dat".format(case_number), dtype=float)
IFNO_m5 = np.loadtxt("./result/{}cases/error_with_time_IFNO_m5.dat".format(case_number), dtype=float)
DSM_m5 = np.loadtxt("./result/{}cases/error_with_time_DSM_m5.dat".format(case_number), dtype=float)    

IUFNO_m10 = np.loadtxt("./result/{}cases/error_with_time_IUFNO_m10.dat".format(case_number), dtype=float)
F_IUFNO_m10 = np.loadtxt("./result/{}cases/error_with_time_F_IUFNO_m10.dat".format(case_number), dtype=float)
F_IFNO_m10 = np.loadtxt("./result/{}cases/error_with_time_F_IFNO_m10.dat".format(case_number), dtype=float)
IFNO_m10 = np.loadtxt("./result/{}cases/error_with_time_IFNO_m10.dat".format(case_number), dtype=float)
DSM_m10 = np.loadtxt("./result/{}cases/error_with_time_DSM_m10.dat".format(case_number), dtype=float)   



#-------------------------输入参数
# time_advance=[20]  #挑推进时间画图
# time_advance=[40]  #挑推进时间画图
#time_advance=[1,2,3,10,15,20,25,30,40,50,60,70,80,90,100,110,120,130,140,150,160,170,180,190,200,210,220,230,240,250]  #挑推进时间画图
data1=fDNS[:,1]

data2=F_IFNO[:,1]
data3=F_IUFNO[:,1]
data4=IUFNO[:,1]
data5=IFNO[:,1]
data6=DSM[:,1]

data7=F_IFNO_m01[:,1]
data8=F_IUFNO_m01[:,1]
data9=IUFNO_m01[:,1]
data10=IFNO_m01[:,1]
data11=DSM_m01[:,1]

data12=F_IFNO_m05[:,1]
data13=F_IUFNO_m05[:,1]
data14=IUFNO_m05[:,1]
data15=IFNO_m05[:,1]
data16=DSM_m05[:,1]

data17=F_IFNO_m1[:,1]
data18=F_IUFNO_m1[:,1]
data19=IUFNO_m1[:,1]
data20=IFNO_m1[:,1]
data21=DSM_m1[:,1]

data22=F_IFNO_m2[:,1]
data23=F_IUFNO_m2[:,1]
data24=IUFNO_m2[:,1]
data25=IFNO_m2[:,1]
data26=DSM_m2[:,1]

data27=F_IFNO_m5[:,1]
data28=F_IUFNO_m5[:,1]
data29=IUFNO_m5[:,1]
data30=IFNO_m5[:,1]
data31=DSM_m5[:,1]

data32=F_IFNO_m10[:,1]
data33=F_IUFNO_m10[:,1]
data34=IUFNO_m10[:,1]
data35=IFNO_m10[:,1]
data36=DSM_m10[:,1]


print("Size of data1:", len(data1))
print("data1:",data1)


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
data7 = np.array(data7)
data7 = data7.reshape(case_number,time_steps)
data8 = np.array(data8)
data8 = data8.reshape(case_number,time_steps)
data9 = np.array(data9)
data9 = data9.reshape(case_number,time_steps)
data10 = np.array(data10)
data10 = data10.reshape(case_number,time_steps)
data11 = np.array(data11)
data11 = data11.reshape(case_number,time_steps)
data12 = np.array(data12)
data12= data12.reshape(case_number,time_steps)
data13 = np.array(data13)
data13 = data13.reshape(case_number,time_steps)
data14 = np.array(data14)
data14 = data14.reshape(case_number,time_steps)
data15 = np.array(data15)
data15 = data15.reshape(case_number,time_steps)
data16 = np.array(data16)
data16 = data16.reshape(case_number,time_steps)
data17 = np.array(data17)
data17 = data17.reshape(case_number,time_steps)
data18 = np.array(data18)
data18 = data18.reshape(case_number,time_steps)
data19 = np.array(data19)
data19 = data19.reshape(case_number,time_steps)
data20 = np.array(data20)
data20 = data20.reshape(case_number,time_steps)
data21 = np.array(data21)
data21 = data21.reshape(case_number,time_steps)
data22 = np.array(data22)
data22 = data22.reshape(case_number,time_steps)
data23 = np.array(data23)
data23 = data23.reshape(case_number,time_steps)
data24 = np.array(data24)
data24 = data24.reshape(case_number,time_steps)
data25 = np.array(data25)
data25 = data25.reshape(case_number,time_steps)
data26 = np.array(data26)
data26 = data26.reshape(case_number,time_steps)
data27 = np.array(data27)
data27 = data27.reshape(case_number,time_steps)
data28 = np.array(data28)
data28 = data28.reshape(case_number,time_steps)
data29 = np.array(data29)
data29 = data29.reshape(case_number,time_steps)
data30 = np.array(data30)
data30 = data30.reshape(case_number,time_steps)
data31 = np.array(data31)
data31 = data31.reshape(case_number,time_steps)
data32 = np.array(data32)
data32 = data32.reshape(case_number,time_steps)
data33 = np.array(data33)
data33 = data33.reshape(case_number,time_steps)
data34 = np.array(data34)
data34 = data34.reshape(case_number,time_steps)
data35 = np.array(data35)
data35 = data35.reshape(case_number,time_steps)
data36 = np.array(data36)
data36 = data36.reshape(case_number,time_steps)

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
mean7=[]
std7=[]
mean8=[]
std8=[]
mean9=[]
std9=[]
mean10=[]
std10=[]
mean11=[]
std11=[]
mean12=[]
std12=[]
mean13=[]
std13=[]
mean14=[]
std14=[]
mean15=[]
std15=[]
mean16=[]
std16=[]
mean17=[]
std17=[]
mean18=[]
std18=[]
mean19=[]
std19=[]
mean20=[]
std20=[]
mean21=[]
std21=[]
mean22=[]
std22=[]
mean23=[]
std23=[]
mean24=[]
std24=[]
mean25=[]
std25=[]
mean26=[]
std26=[]
mean27=[]
std27=[]
mean28=[]
std28=[]
mean29=[]
std29=[]
mean30=[]
std30=[]
mean31=[]
std31=[]
mean32=[]
std32=[]
mean33=[]
std33=[]
mean34=[]
std34=[]
mean35=[]
std35=[]
mean36=[]
std36=[]
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

    mean7.append(np.mean(data7[:,i]))
    std7.append(np.var(data7[:,i]))

    mean8.append(np.mean(data8[:,i]))
    std8.append(np.var(data8[:,i]))
    
    mean9.append(np.mean(data9[:,i]))
    std9.append(np.var(data9[:,i]))

    mean10.append(np.mean(data10[:,i]))
    std10.append(np.var(data10[:,i]))

    mean11.append(np.mean(data11[:,i]))
    std11.append(np.var(data11[:,i]))

    mean12.append(np.mean(data12[:,i]))
    std12.append(np.var(data12[:,i]))
    
    mean13.append(np.mean(data13[:,i]))
    std13.append(np.var(data13[:,i]))

    mean14.append(np.mean(data14[:,i]))
    std14.append(np.var(data14[:,i]))

    mean15.append(np.mean(data15[:,i]))
    std15.append(np.var(data15[:,i]))

    mean16.append(np.mean(data16[:,i]))
    std16.append(np.var(data16[:,i]))
    
    mean17.append(np.mean(data17[:,i]))
    std17.append(np.var(data17[:,i]))

    mean18.append(np.mean(data18[:,i]))
    std18.append(np.var(data18[:,i]))

    mean19.append(np.mean(data19[:,i]))
    std19.append(np.var(data19[:,i]))

    mean20.append(np.mean(data20[:,i]))
    std20.append(np.var(data20[:,i]))
    
    mean21.append(np.mean(data21[:,i]))
    std21.append(np.var(data21[:,i]))

    mean22.append(np.mean(data22[:,i]))
    std22.append(np.var(data22[:,i]))

    mean23.append(np.mean(data23[:,i]))
    std23.append(np.var(data23[:,i]))

    mean24.append(np.mean(data24[:,i]))
    std24.append(np.var(data24[:,i]))

    mean25.append(np.mean(data25[:,i]))
    std25.append(np.var(data25[:,i]))

    mean26.append(np.mean(data26[:,i]))
    std26.append(np.var(data26[:,i]))

    mean27.append(np.mean(data27[:,i]))
    std27.append(np.var(data27[:,i]))

    mean28.append(np.mean(data28[:,i]))
    std28.append(np.var(data28[:,i]))
    
    mean29.append(np.mean(data29[:,i]))
    std29.append(np.var(data29[:,i]))

    mean30.append(np.mean(data30[:,i]))
    std30.append(np.var(data30[:,i]))

    mean31.append(np.mean(data31[:,i]))
    std31.append(np.var(data31[:,i]))

    mean32.append(np.mean(data32[:,i]))
    std32.append(np.var(data32[:,i]))    
    
    mean33.append(np.mean(data33[:,i]))
    std33.append(np.var(data33[:,i]))

    mean34.append(np.mean(data34[:,i]))
    std34.append(np.var(data34[:,i]))       
    
    mean35.append(np.mean(data35[:,i]))
    std35.append(np.var(data35[:,i]))

    mean36.append(np.mean(data36[:,i]))
    std36.append(np.var(data36[:,i]))    
    
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
mean7 = np.array(mean7)
std7 = np.array(std7)
mean8 = np.array(mean8)
std8 = np.array(std8)
mean9 = np.array(mean9)
std9 = np.array(std9)
mean10 = np.array(mean10)
std10 = np.array(std10)
mean11 = np.array(mean11)
std11 = np.array(std11)
mean12 = np.array(mean12)
std12 = np.array(std12)
mean13 = np.array(mean13)
std13 = np.array(std13)
mean14 = np.array(mean14)
std14 = np.array(std14)
mean15 = np.array(mean15)
std15 = np.array(std15)
mean16 = np.array(mean16)
std16 = np.array(std16)
mean17 = np.array(mean17)
std17 = np.array(std17)
mean18 = np.array(mean18)
std18 = np.array(std18)
mean19 = np.array(mean19)
std19 = np.array(std19)
mean20 = np.array(mean20)
std20 = np.array(std20)
mean21 = np.array(mean21)
std21 = np.array(std21)
mean22 = np.array(mean22)
std22 = np.array(std22)
mean23 = np.array(mean23)
std23 = np.array(std23)
mean24 = np.array(mean24)
std24 = np.array(std24)
mean25 = np.array(mean25)
std25 = np.array(std25)
mean26 = np.array(mean26)
std26 = np.array(std26)
mean27 = np.array(mean27)
std27 = np.array(std27)
mean28 = np.array(mean28)
std28 = np.array(std28)
mean29 = np.array(mean29)
std29 = np.array(std29)
mean30 = np.array(mean30)
std30 = np.array(std30)
mean31 = np.array(mean31)
std31 = np.array(std31)
mean32 = np.array(mean32)
std32 = np.array(std32)
mean33 = np.array(mean33)
std33 = np.array(std33)
mean34 = np.array(mean34)
std34 = np.array(std34)
mean35 = np.array(mean35)
std35 = np.array(std35)
mean36 = np.array(mean36)
std36 = np.array(std36)




######################### set figure path4 ################################
figfilePath = os.path.abspath('./Errorbar_with_time/')
figPath = os.path.join(figfilePath, "Ek_Errorbar_with_time_30cases_m01")

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
xlabel = r"$\mathdefault{t/\tau}$"           #坐标标签
ylabel = r"$\mathdefault{Mean \pm Std \ error \ of \ E_k}$"
xlimit = [1,121]                        #坐标显示范围
ylimit = [-0.2,0.05]
legend = ["F-IFNO", "F-IUFNO", "IUFNO", "IFNO", "DSM", "F-IFNO_mag0.1", "F-IUFNO_mag0.1", "IUFNO_mag0.1", "IFNO_mag0.1", "DSM_mag0.1", "F-IFNO_mag0.5", "F-IUFNO_mag0.5", "IUFNO_mag0.5", "IFNO_mag0.5", "DSM_mag0.5", "F-IFNO_mag1", "F-IUFNO_mag1", "IUFNO_mag1", "IFNO_mag1", "DSM_mag1", "F-IFNO_mag2", "F-IUFNO_mag2", "IUFNO_mag2", "IFNO_mag2", "DSM_mag2", "F-IFNO_mag5", "F-IUFNO_mag5", "IUFNO_mag5", "IFNO_mag5", "DSM_mag5", "F-IFNO_mag10", "F-IUFNO_mag10", "IUFNO_mag10", "IFNO_mag10", "DSM_mag10", "fDNS"]
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
ncurv = len(legend)  #每个图画4条线

# ------------------------------------------------------------------------------------------
x = np.arange(0.2, time_steps*0.2+0.2,0.2)
step1=1
plt.plot(x, mean1, label=legend[35], color='purple', linewidth=lineWidth, linestyle='solid',zorder=1)
plt.fill_between(x, mean1 - std1, mean1 + std1, color='purple', alpha=0.3)

plt.plot(x, mean7, label=legend[5], color='#1f77b4', linewidth=lineWidth, linestyle='solid',zorder=1)
plt.fill_between(x, mean7 - std7, mean7 + std7, color='#1f77b4', alpha=0.3)

plt.plot(x, mean8, label=legend[6], color='#ff7f0e', linewidth=lineWidth, linestyle='solid',zorder=0)
plt.fill_between(x, mean8 - std8, mean8 + std8, color='#ff7f0e', alpha=0.3)

plt.plot(x, mean9, label=legend[7], color='gold', linewidth=lineWidth, linestyle='solid',zorder=0)
plt.fill_between(x, mean9 - std9, mean9 + std9, color='gold', alpha=0.3)

plt.plot(x, mean10, label=legend[8], color='pink', linewidth=lineWidth, linestyle='solid',zorder=0)
plt.fill_between(x, mean10 - std10, mean10 + std10, color='pink', alpha=0.3)

plt.plot(x, mean11, label=legend[9], color='green', linewidth=lineWidth, linestyle='solid',zorder=1)
plt.fill_between(x, mean11 - std11, mean11 + std11, color='green', alpha=0.3)

lgd_loc  = (0.63,0.25)#6 7#6 80 88
lgd_font = {'family':"STIXGeneral", 'size':fontSize*0.6}
lgd = plt.legend(loc=lgd_loc, frameon=False, prop=lgd_font,handlelength=2.5,labelspacing=0.5) #2.5是legend长度,0.5是间距
#plt.title("Mean ± Std error of Ek", fontsize=30, color='black', loc='center', pad=15)
plt.savefig(figPath, quality=100, bbox_extra_artists=(lgd,), bbox_inches='tight')
print("Width x Hight: ", fig.get_size_inches())
# plt.cl

######################### set figure path4 ################################
figfilePath = os.path.abspath('./Errorbar_with_time/')
figPath = os.path.join(figfilePath, "Ek_Errorbar_with_time_30cases_m05")

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
xlabel = r"$\mathdefault{t/\tau}$"           #坐标标签
ylabel = r"$\mathdefault{Mean \pm Std \ error \ of \ E_k}$"
xlimit = [1,121]                        #坐标显示范围
ylimit = [-0.2,0.05]
legend = ["F-IFNO", "F-IUFNO", "IUFNO", "IFNO", "DSM", "F-IFNO_mag0.1", "F-IUFNO_mag0.1", "IUFNO_mag0.1", "IFNO_mag0.1", "DSM_mag0.1", "F-IFNO_mag0.5", "F-IUFNO_mag0.5", "IUFNO_mag0.5", "IFNO_mag0.5", "DSM_mag0.5", "F-IFNO_mag1", "F-IUFNO_mag1", "IUFNO_mag1", "IFNO_mag1", "DSM_mag1", "F-IFNO_mag2", "F-IUFNO_mag2", "IUFNO_mag2", "IFNO_mag2", "DSM_mag2", "F-IFNO_mag5", "F-IUFNO_mag5", "IUFNO_mag5", "IFNO_mag5", "DSM_mag5", "F-IFNO_mag10", "F-IUFNO_mag10", "IUFNO_mag10", "IFNO_mag10", "DSM_mag10", "fDNS"]
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
ncurv = len(legend)  #每个图画4条线

# ------------------------------------------------------------------------------------------
x = np.arange(0.2, time_steps*0.2+0.2,0.2)
step1=1
plt.plot(x, mean1, label=legend[35], color='purple', linewidth=lineWidth, linestyle='solid',zorder=1)
plt.fill_between(x, mean1 - std1, mean1 + std1, color='purple', alpha=0.3)

plt.plot(x, mean12, label=legend[10], color='#1f77b4', linewidth=lineWidth, linestyle='solid',zorder=1)
plt.fill_between(x, mean12 - std12, mean12 + std12, color='#1f77b4', alpha=0.3)

plt.plot(x, mean13, label=legend[11], color='#ff7f0e', linewidth=lineWidth, linestyle='solid',zorder=0)
plt.fill_between(x, mean13 - std13, mean13 + std13, color='#ff7f0e', alpha=0.3)

plt.plot(x, mean14, label=legend[12], color='gold', linewidth=lineWidth, linestyle='solid',zorder=0)
plt.fill_between(x, mean14 - std14, mean14 + std14, color='gold', alpha=0.3)

plt.plot(x, mean15, label=legend[13], color='pink', linewidth=lineWidth, linestyle='solid',zorder=0)
plt.fill_between(x, mean15 - std15, mean15 + std15, color='pink', alpha=0.3)

plt.plot(x, mean16, label=legend[14], color='green', linewidth=lineWidth, linestyle='solid',zorder=1)
plt.fill_between(x, mean16 - std16, mean16 + std16, color='green', alpha=0.3)

lgd_loc  = (0.63,0.25)#6 7#6 80 88
lgd_font = {'family':"STIXGeneral", 'size':fontSize*0.6}
lgd = plt.legend(loc=lgd_loc, frameon=False, prop=lgd_font,handlelength=2.5,labelspacing=0.5) #2.5是legend长度,0.5是间距
#plt.title("Mean ± Std error of Ek", fontsize=30, color='black', loc='center', pad=15)
plt.savefig(figPath, quality=100, bbox_extra_artists=(lgd,), bbox_inches='tight')
print("Width x Hight: ", fig.get_size_inches())
# plt.cl

######################### set figure path4 ################################
figfilePath = os.path.abspath('./Errorbar_with_time/')
figPath = os.path.join(figfilePath, "Ek_Errorbar_with_time_30cases_m1")

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
xlabel = r"$\mathdefault{t/\tau}$"           #坐标标签
ylabel = r"$\mathdefault{Mean \pm Std \ error \ of \ E_k}$"
xlimit = [1,121]                        #坐标显示范围
ylimit = [-0.2,0.05]
legend = ["F-IFNO", "F-IUFNO", "IUFNO", "IFNO", "DSM", "F-IFNO_mag0.1", "F-IUFNO_mag0.1", "IUFNO_mag0.1", "IFNO_mag0.1", "DSM_mag0.1", "F-IFNO_mag0.5", "F-IUFNO_mag0.5", "IUFNO_mag0.5", "IFNO_mag0.5", "DSM_mag0.5", "F-IFNO_mag1", "F-IUFNO_mag1", "IUFNO_mag1", "IFNO_mag1", "DSM_mag1", "F-IFNO_mag2", "F-IUFNO_mag2", "IUFNO_mag2", "IFNO_mag2", "DSM_mag2", "F-IFNO_mag5", "F-IUFNO_mag5", "IUFNO_mag5", "IFNO_mag5", "DSM_mag5", "F-IFNO_mag10", "F-IUFNO_mag10", "IUFNO_mag10", "IFNO_mag10", "DSM_mag10", "fDNS"]
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
ncurv = len(legend)  #每个图画4条线

# ------------------------------------------------------------------------------------------
x = np.arange(0.2, time_steps*0.2+0.2,0.2)
step1=1
plt.plot(x, mean1, label=legend[35], color='purple', linewidth=lineWidth, linestyle='solid',zorder=1)
plt.fill_between(x, mean1 - std1, mean1 + std1, color='purple', alpha=0.3)

plt.plot(x, mean17, label=legend[15], color='#1f77b4', linewidth=lineWidth, linestyle='solid',zorder=1)
plt.fill_between(x, mean17 - std17, mean17 + std17, color='#1f77b4', alpha=0.3)

plt.plot(x, mean18, label=legend[16], color='#ff7f0e', linewidth=lineWidth, linestyle='solid',zorder=0)
plt.fill_between(x, mean18 - std18, mean18 + std18, color='#ff7f0e', alpha=0.3)

plt.plot(x, mean19, label=legend[17], color='gold', linewidth=lineWidth, linestyle='solid',zorder=0)
plt.fill_between(x, mean19 - std19, mean19 + std19, color='gold', alpha=0.3)

plt.plot(x, mean20, label=legend[18], color='pink', linewidth=lineWidth, linestyle='solid',zorder=0)
plt.fill_between(x, mean20 - std20, mean20 + std20, color='pink', alpha=0.3)

plt.plot(x, mean21, label=legend[19], color='green', linewidth=lineWidth, linestyle='solid',zorder=1)
plt.fill_between(x, mean21 - std21, mean21 + std21, color='green', alpha=0.3)

lgd_loc  = (0.63,0.25)#6 7#6 80 88
lgd_font = {'family':"STIXGeneral", 'size':fontSize*0.6}
lgd = plt.legend(loc=lgd_loc, frameon=False, prop=lgd_font,handlelength=2.5,labelspacing=0.5) #2.5是legend长度,0.5是间距
#plt.title("Mean ± Std error of Ek", fontsize=30, color='black', loc='center', pad=15)
plt.savefig(figPath, quality=100, bbox_extra_artists=(lgd,), bbox_inches='tight')
print("Width x Hight: ", fig.get_size_inches())
# plt.cl


######################### set figure path4 ################################
figfilePath = os.path.abspath('./Errorbar_with_time/')
figPath = os.path.join(figfilePath, "Ek_Errorbar_with_time_30cases_m2")

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
xlabel = r"$\mathdefault{t/\tau}$"           #坐标标签
ylabel = r"$\mathdefault{Mean \pm Std \ error \ of \ E_k}$"
xlimit = [1,121]                        #坐标显示范围
ylimit = [-0.2,0.05]
legend = ["F-IFNO", "F-IUFNO", "IUFNO", "IFNO", "DSM", "F-IFNO_mag0.1", "F-IUFNO_mag0.1", "IUFNO_mag0.1", "IFNO_mag0.1", "DSM_mag0.1", "F-IFNO_mag0.5", "F-IUFNO_mag0.5", "IUFNO_mag0.5", "IFNO_mag0.5", "DSM_mag0.5", "F-IFNO_mag1", "F-IUFNO_mag1", "IUFNO_mag1", "IFNO_mag1", "DSM_mag1", "F-IFNO_mag2", "F-IUFNO_mag2", "IUFNO_mag2", "IFNO_mag2", "DSM_mag2", "F-IFNO_mag5", "F-IUFNO_mag5", "IUFNO_mag5", "IFNO_mag5", "DSM_mag5", "F-IFNO_mag10", "F-IUFNO_mag10", "IUFNO_mag10", "IFNO_mag10", "DSM_mag10", "fDNS"]
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
ncurv = len(legend)  #每个图画4条线

# ------------------------------------------------------------------------------------------
x = np.arange(0.2, time_steps*0.2+0.2,0.2)
step1=1
plt.plot(x, mean1, label=legend[35], color='purple', linewidth=lineWidth, linestyle='solid',zorder=1)
plt.fill_between(x, mean1 - std1, mean1 + std1, color='purple', alpha=0.3)

plt.plot(x, mean22, label=legend[20], color='#1f77b4', linewidth=lineWidth, linestyle='solid',zorder=1)
plt.fill_between(x, mean22 - std22, mean22 + std22, color='#1f77b4', alpha=0.3)

plt.plot(x, mean23, label=legend[21], color='#ff7f0e', linewidth=lineWidth, linestyle='solid',zorder=0)
plt.fill_between(x, mean23 - std23, mean23 + std23, color='#ff7f0e', alpha=0.3)

plt.plot(x, mean24, label=legend[22], color='gold', linewidth=lineWidth, linestyle='solid',zorder=0)
plt.fill_between(x, mean24 - std24, mean24 + std24, color='gold', alpha=0.3)

plt.plot(x, mean25, label=legend[23], color='pink', linewidth=lineWidth, linestyle='solid',zorder=0)
plt.fill_between(x, mean25 - std25, mean25 + std25, color='pink', alpha=0.3)

plt.plot(x, mean26, label=legend[24], color='green', linewidth=lineWidth, linestyle='solid',zorder=1)
plt.fill_between(x, mean26 - std26, mean26 + std26, color='green', alpha=0.3)

lgd_loc  = (0.63,0.25)#6 7#6 80 88
lgd_font = {'family':"STIXGeneral", 'size':fontSize*0.6}
lgd = plt.legend(loc=lgd_loc, frameon=False, prop=lgd_font,handlelength=2.5,labelspacing=0.5) #2.5是legend长度,0.5是间距
#plt.title("Mean ± Std error of Ek", fontsize=30, color='black', loc='center', pad=15)
plt.savefig(figPath, quality=100, bbox_extra_artists=(lgd,), bbox_inches='tight')
print("Width x Hight: ", fig.get_size_inches())
# plt.cl


######################### set figure path4 ################################
figfilePath = os.path.abspath('./Errorbar_with_time/')
figPath = os.path.join(figfilePath, "Ek_Errorbar_with_time_30cases_m5")

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
xlabel = r"$\mathdefault{t/\tau}$"           #坐标标签
ylabel = r"$\mathdefault{Mean \pm Std \ error \ of \ E_k}$"
xlimit = [1,121]                        #坐标显示范围
ylimit = [-0.06,0.06]
legend = ["F-IFNO", "F-IUFNO", "IUFNO", "IFNO", "DSM", "F-IFNO_mag0.1", "F-IUFNO_mag0.1", "IUFNO_mag0.1", "IFNO_mag0.1", "DSM_mag0.1", "F-IFNO_mag0.5", "F-IUFNO_mag0.5", "IUFNO_mag0.5", "IFNO_mag0.5", "DSM_mag0.5", "F-IFNO_mag1", "F-IUFNO_mag1", "IUFNO_mag1", "IFNO_mag1", "DSM_mag1", "F-IFNO_mag2", "F-IUFNO_mag2", "IUFNO_mag2", "IFNO_mag2", "DSM_mag2", "F-IFNO_mag5", "F-IUFNO_mag5", "IUFNO_mag5", "IFNO_mag5", "DSM_mag5", "F-IFNO_mag10", "F-IUFNO_mag10", "IUFNO_mag10", "IFNO_mag10", "DSM_mag10", "fDNS"]
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
ncurv = len(legend)  #每个图画4条线

# ------------------------------------------------------------------------------------------
x = np.arange(0.2, time_steps*0.2+0.2,0.2)
step1=1
plt.plot(x, mean1, label=legend[35], color='purple', linewidth=lineWidth, linestyle='solid',zorder=1)
plt.fill_between(x, mean1 - std1, mean1 + std1, color='purple', alpha=0.3)

plt.plot(x, mean27, label=legend[25], color='#1f77b4', linewidth=lineWidth, linestyle='solid',zorder=1)
plt.fill_between(x, mean27 - std27, mean27 + std27, color='#1f77b4', alpha=0.3)

plt.plot(x, mean28, label=legend[26], color='#ff7f0e', linewidth=lineWidth, linestyle='solid',zorder=0)
plt.fill_between(x, mean28 - std28, mean28 + std28, color='#ff7f0e', alpha=0.3)

plt.plot(x, mean29, label=legend[27], color='gold', linewidth=lineWidth, linestyle='solid',zorder=0)
plt.fill_between(x, mean29 - std29, mean29 + std29, color='gold', alpha=0.3)

plt.plot(x, mean30, label=legend[28], color='pink', linewidth=lineWidth, linestyle='solid',zorder=0)
plt.fill_between(x, mean30 - std30, mean30 + std30, color='pink', alpha=0.3)
'''
plt.plot(x, mean31, label=legend[29], color='green', linewidth=lineWidth, linestyle='solid',zorder=1)
plt.fill_between(x, mean31 - std31, mean31 + std31, color='green', alpha=0.3)
'''
lgd_loc  = (0.63,0.68)#6 7#6 80 88
lgd_font = {'family':"STIXGeneral", 'size':fontSize*0.6}
lgd = plt.legend(loc=lgd_loc, frameon=False, prop=lgd_font,handlelength=2.5,labelspacing=0.5) #2.5是legend长度,0.5是间距
#plt.title("Mean ± Std error of Ek", fontsize=30, color='black', loc='center', pad=15)
plt.savefig(figPath, quality=100, bbox_extra_artists=(lgd,), bbox_inches='tight')
print("Width x Hight: ", fig.get_size_inches())
# plt.cl


######################### set figure path4 ################################
figfilePath = os.path.abspath('./Errorbar_with_time/')
figPath = os.path.join(figfilePath, "Ek_Errorbar_with_time_30cases_m10")

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
xlabel = r"$\mathdefault{t/\tau}$"           #坐标标签
ylabel = r"$\mathdefault{Mean \pm Std \ error \ of \ E_k}$"
xlimit = [1,121]                        #坐标显示范围
ylimit = [-0.06,0.06]
legend = ["F-IFNO", "F-IUFNO", "IUFNO", "IFNO", "DSM", "F-IFNO_mag0.1", "F-IUFNO_mag0.1", "IUFNO_mag0.1", "IFNO_mag0.1", "DSM_mag0.1", "F-IFNO_mag0.5", "F-IUFNO_mag0.5", "IUFNO_mag0.5", "IFNO_mag0.5", "DSM_mag0.5", "F-IFNO_mag1", "F-IUFNO_mag1", "IUFNO_mag1", "IFNO_mag1", "DSM_mag1", "F-IFNO_mag2", "F-IUFNO_mag2", "IUFNO_mag2", "IFNO_mag2", "DSM_mag2", "F-IFNO_mag5", "F-IUFNO_mag5", "IUFNO_mag5", "IFNO_mag5", "DSM_mag5", "F-IFNO_mag10", "F-IUFNO_mag10", "IUFNO_mag10", "IFNO_mag10", "DSM_mag10", "fDNS"]
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
ncurv = len(legend)  #每个图画4条线

# ------------------------------------------------------------------------------------------
x = np.arange(0.2, time_steps*0.2+0.2,0.2)
step1=1
plt.plot(x, mean1, label=legend[35], color='purple', linewidth=lineWidth, linestyle='solid',zorder=1)
plt.fill_between(x, mean1 - std1, mean1 + std1, color='purple', alpha=0.3)

plt.plot(x, mean32, label=legend[30], color='#1f77b4', linewidth=lineWidth, linestyle='solid',zorder=1)
plt.fill_between(x, mean32 - std32, mean32 + std32, color='#1f77b4', alpha=0.3)

plt.plot(x, mean33, label=legend[31], color='#ff7f0e', linewidth=lineWidth, linestyle='solid',zorder=0)
plt.fill_between(x, mean33 - std33, mean33 + std33, color='#ff7f0e', alpha=0.3)

plt.plot(x, mean34, label=legend[32], color='gold', linewidth=lineWidth, linestyle='solid',zorder=0)
plt.fill_between(x, mean34 - std34, mean34 + std34, color='gold', alpha=0.3)

plt.plot(x, mean35, label=legend[33], color='pink', linewidth=lineWidth, linestyle='solid',zorder=0)
plt.fill_between(x, mean35 - std35, mean35 + std35, color='pink', alpha=0.3)
'''
plt.plot(x, mean36, label=legend[34], color='green', linewidth=lineWidth, linestyle='solid',zorder=1)
plt.fill_between(x, mean36 - std36, mean36 + std36, color='green', alpha=0.3)
'''
lgd_loc  = (0.63,0.68)#6 7#6 80 88
lgd_font = {'family':"STIXGeneral", 'size':fontSize*0.6}
lgd = plt.legend(loc=lgd_loc, frameon=False, prop=lgd_font,handlelength=2.5,labelspacing=0.5) #2.5是legend长度,0.5是间距
#plt.title("Mean ± Std error of Ek", fontsize=30, color='black', loc='center', pad=15)
plt.savefig(figPath, quality=100, bbox_extra_artists=(lgd,), bbox_inches='tight')
print("Width x Hight: ", fig.get_size_inches())
# plt.cl

