"""
@author: admin
"""
import numpy as np
import matplotlib as mpl
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import os
#os.chdir(r'C:\Users\Lenovo\Desktop\PINO_3d\post\plot_result')
case_number_list =[30]

for idx, case_number in enumerate(case_number_list):
    #-------------------------输入参数
    period = 101 #10个波数
    time_advance=list(range(10, 601, 10))  #挑推进时间画图
    time_advance.insert(1,1)  #挑推进时间画图

    #-------------------------------------------------------------读入数据，#comment去掉标识符所在行

    fDNS= np.loadtxt("../fDNS/{}case/avg_fDNS_{}case_inc1_PDFs.dat".format(case_number,case_number),dtype=float)
    IUFNO = np.loadtxt("../IUFNO_40ep_k=1,2/{}case/avg_{}case_inc1_PDFs.dat".format(case_number, case_number), dtype=float)
    F_IUFNO = np.loadtxt("../F-IUFNO_40ep_k=1,2/{}case/avg_{}case_inc1_PDFs.dat".format(case_number, case_number), dtype=float)
    F_IFNO = np.loadtxt("../F-IFNO_40ep_k=1,2/{}case/avg_{}case_inc1_PDFs.dat".format(case_number, case_number), dtype=float)
    IFNO = np.loadtxt("../IFNO_40ep_k=1,2/{}case/avg_{}case_inc1_PDFs.dat".format(case_number, case_number), dtype=float)
    DSM = np.loadtxt("../DSM/{}case/avg_DSM_{}case_inc1_PDFs.dat".format(case_number, case_number), dtype=float)

    IUFNO_m01 = np.loadtxt("../IUFNO_40ep_k=1,2_mag0.1/{}case/avg_{}case_inc1_PDFs.dat".format(case_number, case_number), dtype=float)
    F_IUFNO_m01 = np.loadtxt("../F-IUFNO_40ep_k=1,2_mag0.1/{}case/avg_{}case_inc1_PDFs.dat".format(case_number, case_number), dtype=float)
    F_IFNO_m01 = np.loadtxt("../F-IFNO_40ep_k=1,2_mag0.1/{}case/avg_{}case_inc1_PDFs.dat".format(case_number, case_number), dtype=float)
    IFNO_m01 = np.loadtxt("../IFNO_40ep_k=1,2_mag0.1/{}case/avg_{}case_inc1_PDFs.dat".format(case_number, case_number), dtype=float)
    DSM_m01 = np.loadtxt("../DSM_mag0.1/{}case/avg_DSM_mag0.1_{}case_inc1_PDFs.dat".format(case_number, case_number), dtype=float)

    IUFNO_m05 = np.loadtxt("../IUFNO_40ep_k=1,2_mag0.5/{}case/avg_{}case_inc1_PDFs.dat".format(case_number, case_number), dtype=float)
    F_IUFNO_m05 = np.loadtxt("../F-IUFNO_40ep_k=1,2_mag0.5/{}case/avg_{}case_inc1_PDFs.dat".format(case_number, case_number), dtype=float)
    F_IFNO_m05 = np.loadtxt("../F-IFNO_40ep_k=1,2_mag0.5/{}case/avg_{}case_inc1_PDFs.dat".format(case_number, case_number), dtype=float)
    IFNO_m05 = np.loadtxt("../IFNO_40ep_k=1,2_mag0.5/{}case/avg_{}case_inc1_PDFs.dat".format(case_number, case_number), dtype=float)
    DSM_m05 = np.loadtxt("../DSM_mag0.5/{}case/avg_DSM_mag0.5_{}case_inc1_PDFs.dat".format(case_number, case_number), dtype=float)

    IUFNO_m1 = np.loadtxt("../IUFNO_40ep_k=1,2_mag1/{}case/avg_{}case_inc1_PDFs.dat".format(case_number, case_number), dtype=float)
    F_IUFNO_m1 = np.loadtxt("../F-IUFNO_40ep_k=1,2_mag1/{}case/avg_{}case_inc1_PDFs.dat".format(case_number, case_number), dtype=float)
    F_IFNO_m1 = np.loadtxt("../F-IFNO_40ep_k=1,2_mag1/{}case/avg_{}case_inc1_PDFs.dat".format(case_number, case_number), dtype=float)
    IFNO_m1 = np.loadtxt("../IFNO_40ep_k=1,2_mag1/{}case/avg_{}case_inc1_PDFs.dat".format(case_number, case_number), dtype=float)
    DSM_m1 = np.loadtxt("../DSM_mag1/{}case/avg_DSM_{}case_inc1_PDFs.dat".format(case_number, case_number), dtype=float)

    IUFNO_m2 = np.loadtxt("../IUFNO_40ep_k=1,2_mag2/{}case/avg_{}case_inc1_PDFs.dat".format(case_number, case_number), dtype=float)
    F_IUFNO_m2 = np.loadtxt("../F-IUFNO_40ep_k=1,2_mag2/{}case/avg_{}case_inc1_PDFs.dat".format(case_number, case_number), dtype=float)
    F_IFNO_m2 = np.loadtxt("../F-IFNO_40ep_k=1,2_mag2/{}case/avg_{}case_inc1_PDFs.dat".format(case_number, case_number), dtype=float)
    IFNO_m2 = np.loadtxt("../IFNO_40ep_k=1,2_mag2/{}case/avg_{}case_inc1_PDFs.dat".format(case_number, case_number), dtype=float)
    DSM_m2 = np.loadtxt("../DSM_mag2/{}case/avg_DSM_{}case_inc1_PDFs.dat".format(case_number, case_number), dtype=float)

    IUFNO_m5 = np.loadtxt("../IUFNO_40ep_k=1,2_mag5/{}case/avg_{}case_inc1_PDFs.dat".format(case_number, case_number), dtype=float)
    F_IUFNO_m5 = np.loadtxt("../F-IUFNO_40ep_k=1,2_mag5/{}case/avg_{}case_inc1_PDFs.dat".format(case_number, case_number), dtype=float)
    F_IFNO_m5 = np.loadtxt("../F-IFNO_40ep_k=1,2_mag5/{}case/avg_{}case_inc1_PDFs.dat".format(case_number, case_number), dtype=float)
    IFNO_m5 = np.loadtxt("../IFNO_40ep_k=1,2_mag5/{}case/avg_{}case_inc1_PDFs.dat".format(case_number, case_number), dtype=float)
    DSM_m5 = np.loadtxt("../DSM_mag5/{}case/avg_DSM_{}case_inc1_PDFs.dat".format(case_number, case_number), dtype=float)
    
    IUFNO_m10 = np.loadtxt("../IUFNO_40ep_k=1,2_mag10/{}case/avg_{}case_inc1_PDFs.dat".format(case_number, case_number), dtype=float)
    F_IUFNO_m10 = np.loadtxt("../F-IUFNO_40ep_k=1,2_mag10/{}case/avg_{}case_inc1_PDFs.dat".format(case_number, case_number), dtype=float)
    F_IFNO_m10 = np.loadtxt("../F-IFNO_40ep_k=1,2_mag10/{}case/avg_{}case_inc1_PDFs.dat".format(case_number, case_number), dtype=float)
    IFNO_m10 = np.loadtxt("../IFNO_40ep_k=1,2_mag10/{}case/avg_{}case_inc1_PDFs.dat".format(case_number, case_number), dtype=float)
    DSM_m10 = np.loadtxt("../DSM_mag10/{}case/avg_DSM_{}case_inc1_PDFs.dat".format(case_number, case_number), dtype=float)    
    #--------------------------
    y_fDNS = []

    y_F_IFNO = []
    y_F_IUFNO = []
    y_IUFNO = []
    y_IFNO = []
    y_DSM = []

    y_F_IFNO_m01 = []
    y_F_IUFNO_m01 = []
    y_IUFNO_m01 = []
    y_IFNO_m01 = []
    y_DSM_m01 = []

    y_F_IFNO_m05 = []
    y_F_IUFNO_m05 = []
    y_IUFNO_m05 = []
    y_IFNO_m05 = []
    y_DSM_m05 = []

    y_F_IFNO_m1 = []
    y_F_IUFNO_m1 = []
    y_IUFNO_m1 = []
    y_IFNO_m1 = []
    y_DSM_m1 = []

    y_F_IFNO_m2 = []
    y_F_IUFNO_m2 = []
    y_IUFNO_m2 = []
    y_IFNO_m2 = []
    y_DSM_m2 = []
    
    y_F_IFNO_m5 = []
    y_F_IUFNO_m5 = []
    y_IUFNO_m5 = []
    y_IFNO_m5 = []
    y_DSM_m5 = []    
    
    y_F_IFNO_m10 = []
    y_F_IUFNO_m10 = []
    y_IUFNO_m10 = []
    y_IFNO_m10 = []
    y_DSM_m10 = []    
    
    x = fDNS[0:period,0]  #共用的x
    for i in range(len(time_advance)):
        j = time_advance[i]
        y_fDNS.append(fDNS[period*(j-1):period*j, 1])
        y_F_IFNO.append(F_IFNO[period * (j - 1): period * j, 1])
        y_F_IUFNO.append(F_IUFNO[period * (j - 1): period * j, 1])       
        y_IUFNO.append(IUFNO[period * (j - 1): period * j, 1])
        y_IFNO.append(IFNO[period*(j-1):period*j, 1])
        y_DSM.append(DSM[period*(j-1):period*j, 1])       
             
        y_F_IFNO_m01.append(F_IFNO_m01[period * (j - 1): period * j, 1])
        y_F_IUFNO_m01.append(F_IUFNO_m01[period * (j - 1): period * j, 1])       
        y_IUFNO_m01.append(IUFNO_m01[period * (j - 1): period * j, 1])
        y_IFNO_m01.append(IFNO_m01[period*(j-1):period*j, 1])
        y_DSM_m01.append(DSM_m01[period*(j-1):period*j, 1])   
        
        y_F_IFNO_m05.append(F_IFNO_m05[period * (j - 1): period * j, 1])
        y_F_IUFNO_m05.append(F_IUFNO_m05[period * (j - 1): period * j, 1])       
        y_IUFNO_m05.append(IUFNO_m05[period * (j - 1): period * j, 1])
        y_IFNO_m05.append(IFNO_m05[period*(j-1):period*j, 1])
        y_DSM_m05.append(DSM_m05[period*(j-1):period*j, 1])           
        
        y_F_IFNO_m1.append(F_IFNO_m1[period * (j - 1): period * j, 1])
        y_F_IUFNO_m1.append(F_IUFNO_m1[period * (j - 1): period * j, 1])       
        y_IUFNO_m1.append(IUFNO_m1[period * (j - 1): period * j, 1])
        y_IFNO_m1.append(IFNO_m1[period*(j-1):period*j, 1])
        y_DSM_m1.append(DSM_m1[period*(j-1):period*j, 1])          
        
        y_F_IFNO_m2.append(F_IFNO_m2[period * (j - 1): period * j, 1])
        y_F_IUFNO_m2.append(F_IUFNO_m2[period * (j - 1): period * j, 1])       
        y_IUFNO_m2.append(IUFNO_m2[period * (j - 1): period * j, 1])
        y_IFNO_m2.append(IFNO_m2[period*(j-1):period*j, 1])
        y_DSM_m2.append(DSM_m2[period*(j-1):period*j, 1])           
        
        y_F_IFNO_m5.append(F_IFNO_m5[period * (j - 1): period * j, 1])
        y_F_IUFNO_m5.append(F_IUFNO_m5[period * (j - 1): period * j, 1])       
        y_IUFNO_m5.append(IUFNO_m5[period * (j - 1): period * j, 1])
        y_IFNO_m5.append(IFNO_m5[period*(j-1):period*j, 1])
        y_DSM_m5.append(DSM_m5[period*(j-1):period*j, 1])           
        
        y_F_IFNO_m10.append(F_IFNO_m10[period * (j - 1): period * j, 1])
        y_F_IUFNO_m10.append(F_IUFNO_m10[period * (j - 1): period * j, 1])       
        y_IUFNO_m10.append(IUFNO_m10[period * (j - 1): period * j, 1])
        y_IFNO_m10.append(IFNO_m10[period*(j-1):period*j, 1])
        y_DSM_m10.append(DSM_m10[period*(j-1):period*j, 1])           
        

    ################################# 图片保存路径 ################################
    figfilePath = os.path.abspath('./plot_results/{}case').format(case_number)
    figPath = os.path.join(figfilePath, "vel_inc1_PDFs/ori")
    if not os.path.exists(figPath):
        os.makedirs(figPath)
    print("图片存放路径：", figPath)

    ############################## setting of figures #################################
    dpi = 600                               #分辨率
    width  = 8                              #图宽
    height = 6                              #图高
    fontSize = 40                          #字体大小
    lineWidth = 2.5                         #线宽
    boxWidth = 2.5                          #边框线宽
    Lmajor = 7                              #主刻度长度
    Lminor = 4                              #次刻度长度
    xlabPad  = 10                           #x坐标下面显示值距离轴距离
    ylabPad  = 10                           #y坐标下面显示值距离轴距离
    xlabel = r"$\mathdefault{\delta_r\bar{u}/\bar{u}^{rms}(r=1\Delta)}$"   #坐标标签
    ylabel = r"$\mathdefault{PDF}$"
    xlimit = [-1.5,1.5]                        #坐标显示范围
    ylimit = [1e-3,1e1]
    legend = ["F-IFNO", "F-IUFNO","IUFNO","IFNO","DSM","fDNS"]
    ############################## setting of fonts ####################################
    mpl.rc('font', family='STIXGeneral')
    mpl.rc('text', usetex=False)
    mpl.rcParams['xtick.direction'] = 'in'
    mpl.rcParams['ytick.direction'] = 'in'     #xy轴坐标杆标注的方向
    plt.rcParams["mathtext.fontset"]  = "cm"   #数学符号的字体
    mpl.rcParams["font.family"] = "STIXGeneral"
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
    colors = ['#A52A2A','#ff7f0e','#ffd700','green','#1f77b4','purple']

    markers = ['o', 's', 'D', 'p', '*', '^', 'v', '<', '>', 'x', 'h', '+', 'H', '1', '2', '3', '4', '|', '_', '.']
    ############################## setting of figures #################################
    for i in range(len(time_advance)):
        j = time_advance[i]                                   #输入的[1,5,10,15] #用于文件起名
        gfile = "vel_inc1_PDFs_t{}_label.png".format(j)               #保存的文件名
        gpath = os.path.join(figPath, gfile)
        #-----------------------------------------------------------------------------------------图片大小分辨率
        fig = plt.figure(figsize=(width,height), dpi=dpi)     #定义图片宽、高、分辨率
        plt.rcParams["font.size"] = fontSize                  #统一字体大小
        plt.rcParams["axes.linewidth"] = lineWidth
        ax = fig.add_axes([0,0,1,1])                          #用于压缩图片，相当于各边移动距离
        # ----------------------------------------------------------------------------------------X坐标轴设置
        plt.xscale("linear")                                     #画linear
        ax.xaxis.set_minor_locator(mpl.ticker.AutoMinorLocator(4)) #次刻度
        # formatter = mpl.ticker.FixedFormatter()                #主刻度格式
        ax.xaxis.set_major_formatter(mpl.ticker.FuncFormatter(minor_tick))               #应用主刻度格式
        ax.xaxis.set_minor_formatter(mpl.ticker.NullFormatter()) #次刻度
        # ----------------------------------------------------------------------------------------Y坐标轴设置
        plt.yscale("log")
        ax.yaxis.set_minor_locator(mpl.ticker.LogLocator(base=10.0, subs=np.arange(0.1,1,0.1)))
        formatter = mpl.ticker.LogFormatterSciNotation()
        ax.yaxis.set_major_formatter(formatter)
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
        plt.plot(x, y_fDNS[i], label=legend[5], color=colors[0], linewidth=lineWidth, linestyle='solid',zorder=0)
        
        plt.scatter(x, y_F_IFNO[i], label=legend[0], facecolor='none', linewidths=lineWidth,edgecolor=colors[1], s=70, alpha=1.0, marker=markers[0],zorder=7)    
        plt.scatter(x, y_F_IUFNO[i], label=legend[1], facecolor='none', linewidths=lineWidth,edgecolor=colors[2], s=70, alpha=1.0,  marker=markers[1],zorder=4)   
        plt.scatter(x, y_IUFNO[i], label=legend[2], facecolor='none', linewidths=lineWidth,edgecolor=colors[3], s=70, alpha=1.0,  marker=markers[4],zorder=2)
        plt.scatter(x, y_IFNO[i], label=legend[3], facecolor='none', linewidths=lineWidth,edgecolor=colors[4], s=70, alpha=1.0, marker=markers[5],zorder=1)
        plt.scatter(x, y_DSM[i], label=legend[4], facecolor='none', linewidths=lineWidth,edgecolor=colors[5], s=70, alpha=1.0, marker=markers[6],zorder=5)

        lgd_loc = (0.75,0.62)#6,7#6,78,82
        lgd_font = {'family': "STIXGeneral", 'size': fontSize * 0.6}
        
                         
        plt.savefig(gpath, bbox_inches='tight')
        print("Width x Hight: ", fig.get_size_inches())
        # plt.cl
'''
    ################################# 图片保存路径 ################################
    figfilePath = os.path.abspath('./plot_results/{}case').format(case_number)
    figPath = os.path.join(figfilePath, "vel_inc1_PDFs/m01")
    if not os.path.exists(figPath):
        os.makedirs(figPath)
    print("图片存放路径：", figPath)

    ############################## setting of figures #################################
    dpi = 600                               #分辨率
    width  = 8                              #图宽
    height = 6                              #图高
    fontSize = 40                          #字体大小
    lineWidth = 2.5                         #线宽
    boxWidth = 2.5                          #边框线宽
    Lmajor = 7                              #主刻度长度
    Lminor = 4                              #次刻度长度
    xlabPad  = 10                           #x坐标下面显示值距离轴距离
    ylabPad  = 10                           #y坐标下面显示值距离轴距离
    xlabel = r"$\mathdefault{\delta_r\bar{u}/\bar{u}^{rms}(r=1\Delta)}$"   #坐标标签
    ylabel = r"$\mathdefault{PDF}$"
    xlimit = [-1.5,1.5]                        #坐标显示范围
    ylimit = [1e-3,1e1]
    legend = ["F-IFNO_mag0.1", "F-IUFNO_mag0.1","IUFNO_mag0.1","IFNO_mag0.1","DSM_mag0.1","fDNS"]
    ############################## setting of fonts ####################################
    mpl.rc('font', family='STIXGeneral')
    mpl.rc('text', usetex=False)
    mpl.rcParams['xtick.direction'] = 'in'
    mpl.rcParams['ytick.direction'] = 'in'     #xy轴坐标杆标注的方向
    plt.rcParams["mathtext.fontset"]  = "cm"   #数学符号的字体
    mpl.rcParams["font.family"] = "STIXGeneral"
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

    markers = ['o', 's', 'D', 'p', '*', '^', 'v', '<', '>', 'x', 'h', '+', 'H', '1', '2', '3', '4', '|', '_', '.']
    ############################## setting of figures #################################
    for i in range(len(time_advance)):
        j = time_advance[i]                                   #输入的[1,5,10,15] #用于文件起名
        gfile = "vel_inc1_PDFs_t{}.png".format(j)               #保存的文件名
        gpath = os.path.join(figPath, gfile)
        #-----------------------------------------------------------------------------------------图片大小分辨率
        fig = plt.figure(figsize=(width,height), dpi=dpi)     #定义图片宽、高、分辨率
        plt.rcParams["font.size"] = fontSize                  #统一字体大小
        plt.rcParams["axes.linewidth"] = lineWidth
        ax = fig.add_axes([0,0,1,1])                          #用于压缩图片，相当于各边移动距离
        # ----------------------------------------------------------------------------------------X坐标轴设置
        plt.xscale("linear")                                     #画linear
        ax.xaxis.set_minor_locator(mpl.ticker.AutoMinorLocator(4)) #次刻度
        # formatter = mpl.ticker.FixedFormatter()                #主刻度格式
        ax.xaxis.set_major_formatter(mpl.ticker.FuncFormatter(minor_tick))               #应用主刻度格式
        ax.xaxis.set_minor_formatter(mpl.ticker.NullFormatter()) #次刻度
        # ----------------------------------------------------------------------------------------Y坐标轴设置
        plt.yscale("log")
        ax.yaxis.set_minor_locator(mpl.ticker.LogLocator(base=10.0, subs=np.arange(0.1,1,0.1)))
        formatter = mpl.ticker.LogFormatterSciNotation()
        ax.yaxis.set_major_formatter(formatter)
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
        plt.plot(x, y_fDNS[i], label=legend[5], color=colors[0], linewidth=lineWidth, linestyle='solid',zorder=0)
        
        plt.scatter(x, y_F_IFNO_m01[i], label=legend[0], facecolor='none', linewidths=lineWidth,edgecolor=colors[1], s=70, alpha=1.0, marker=markers[0],zorder=7)    
        plt.scatter(x, y_F_IUFNO_m01[i], label=legend[1], facecolor='none', linewidths=lineWidth,edgecolor=colors[2], s=70, alpha=1.0,  marker=markers[1],zorder=4)   
        plt.scatter(x, y_IUFNO_m01[i], label=legend[2], facecolor='none', linewidths=lineWidth,edgecolor=colors[5], s=70, alpha=1.0,  marker=markers[4],zorder=2)
        plt.scatter(x, y_IFNO_m01[i], label=legend[3], facecolor='none', linewidths=lineWidth,edgecolor=colors[6], s=70, alpha=1.0, marker=markers[5],zorder=1)
        plt.scatter(x, y_DSM_m01[i], label=legend[4], facecolor='none', linewidths=lineWidth,edgecolor=colors[7], s=70, alpha=1.0, marker=markers[6],zorder=5)

        lgd_loc = (0.63,0.62)#6,7#6,78,82
        lgd_font = {'family': "STIXGeneral", 'size': fontSize * 0.6}
        
                         
        plt.savefig(gpath, bbox_inches='tight')
        print("Width x Hight: ", fig.get_size_inches())
        # plt.cl        
        
    ################################# 图片保存路径 ################################
    figfilePath = os.path.abspath('./plot_results/{}case').format(case_number)
    figPath = os.path.join(figfilePath, "vel_inc1_PDFs/m05")
    if not os.path.exists(figPath):
        os.makedirs(figPath)
    print("图片存放路径：", figPath)

    ############################## setting of figures #################################
    dpi = 600                               #分辨率
    width  = 8                              #图宽
    height = 6                              #图高
    fontSize = 40                          #字体大小
    lineWidth = 2.5                         #线宽
    boxWidth = 2.5                          #边框线宽
    Lmajor = 7                              #主刻度长度
    Lminor = 4                              #次刻度长度
    xlabPad  = 10                           #x坐标下面显示值距离轴距离
    ylabPad  = 10                           #y坐标下面显示值距离轴距离
    xlabel = r"$\mathdefault{\delta_r\bar{u}/\bar{u}^{rms}(r=1\Delta)}$"   #坐标标签
    ylabel = r"$\mathdefault{PDF}$"
    xlimit = [-1.5,1.5]                        #坐标显示范围
    ylimit = [1e-3,1e1]
    legend = ["F-IFNO_mag0.5", "F-IUFNO_mag0.5","IUFNO_mag0.5","IFNO_mag0.5","DSM_mag0.5","fDNS"]
    ############################## setting of fonts ####################################
    mpl.rc('font', family='STIXGeneral')
    mpl.rc('text', usetex=False)
    mpl.rcParams['xtick.direction'] = 'in'
    mpl.rcParams['ytick.direction'] = 'in'     #xy轴坐标杆标注的方向
    plt.rcParams["mathtext.fontset"]  = "cm"   #数学符号的字体
    mpl.rcParams["font.family"] = "STIXGeneral"
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

    markers = ['o', 's', 'D', 'p', '*', '^', 'v', '<', '>', 'x', 'h', '+', 'H', '1', '2', '3', '4', '|', '_', '.']
    ############################## setting of figures #################################
    for i in range(len(time_advance)):
        j = time_advance[i]                                   #输入的[1,5,10,15] #用于文件起名
        gfile = "vel_inc1_PDFs_t{}.png".format(j)               #保存的文件名
        gpath = os.path.join(figPath, gfile)
        #-----------------------------------------------------------------------------------------图片大小分辨率
        fig = plt.figure(figsize=(width,height), dpi=dpi)     #定义图片宽、高、分辨率
        plt.rcParams["font.size"] = fontSize                  #统一字体大小
        plt.rcParams["axes.linewidth"] = lineWidth
        ax = fig.add_axes([0,0,1,1])                          #用于压缩图片，相当于各边移动距离
        # ----------------------------------------------------------------------------------------X坐标轴设置
        plt.xscale("linear")                                     #画linear
        ax.xaxis.set_minor_locator(mpl.ticker.AutoMinorLocator(4)) #次刻度
        # formatter = mpl.ticker.FixedFormatter()                #主刻度格式
        ax.xaxis.set_major_formatter(mpl.ticker.FuncFormatter(minor_tick))               #应用主刻度格式
        ax.xaxis.set_minor_formatter(mpl.ticker.NullFormatter()) #次刻度
        # ----------------------------------------------------------------------------------------Y坐标轴设置
        plt.yscale("log")
        ax.yaxis.set_minor_locator(mpl.ticker.LogLocator(base=10.0, subs=np.arange(0.1,1,0.1)))
        formatter = mpl.ticker.LogFormatterSciNotation()
        ax.yaxis.set_major_formatter(formatter)
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
        plt.plot(x, y_fDNS[i], label=legend[5], color=colors[0], linewidth=lineWidth, linestyle='solid',zorder=0)
        
        plt.scatter(x, y_F_IFNO_m05[i], label=legend[0], facecolor='none', linewidths=lineWidth,edgecolor=colors[1], s=70, alpha=1.0, marker=markers[0],zorder=7)    
        plt.scatter(x, y_F_IUFNO_m05[i], label=legend[1], facecolor='none', linewidths=lineWidth,edgecolor=colors[2], s=70, alpha=1.0,  marker=markers[1],zorder=4)   
        plt.scatter(x, y_IUFNO_m05[i], label=legend[2], facecolor='none', linewidths=lineWidth,edgecolor=colors[5], s=70, alpha=1.0,  marker=markers[4],zorder=2)
        plt.scatter(x, y_IFNO_m05[i], label=legend[3], facecolor='none', linewidths=lineWidth,edgecolor=colors[6], s=70, alpha=1.0, marker=markers[5],zorder=1)
        plt.scatter(x, y_DSM_m05[i], label=legend[4], facecolor='none', linewidths=lineWidth,edgecolor=colors[7], s=70, alpha=1.0, marker=markers[6],zorder=5)

        lgd_loc = (0.63,0.62)#6,7#6,78,82
        lgd_font = {'family': "STIXGeneral", 'size': fontSize * 0.6}
        
                         
        plt.savefig(gpath, bbox_inches='tight')
        print("Width x Hight: ", fig.get_size_inches())
        # plt.cl  

    ################################# 图片保存路径 ################################
    figfilePath = os.path.abspath('./plot_results/{}case').format(case_number)
    figPath = os.path.join(figfilePath, "vel_inc1_PDFs/m1")
    if not os.path.exists(figPath):
        os.makedirs(figPath)
    print("图片存放路径：", figPath)

    ############################## setting of figures #################################
    dpi = 600                               #分辨率
    width  = 8                              #图宽
    height = 6                              #图高
    fontSize = 40                          #字体大小
    lineWidth = 2.5                         #线宽
    boxWidth = 2.5                          #边框线宽
    Lmajor = 7                              #主刻度长度
    Lminor = 4                              #次刻度长度
    xlabPad  = 10                           #x坐标下面显示值距离轴距离
    ylabPad  = 10                           #y坐标下面显示值距离轴距离
    xlabel = r"$\mathdefault{\delta_r\bar{u}/\bar{u}^{rms}(r=1\Delta)}$"   #坐标标签
    ylabel = r"$\mathdefault{PDF}$"
    xlimit = [-1.5,1.5]                        #坐标显示范围
    ylimit = [1e-3,1e1]
    legend = ["F-IFNO_mag1", "F-IUFNO_mag1","IUFNO_mag1","IFNO_mag1","DSM_mag1","fDNS"]
    ############################## setting of fonts ####################################
    mpl.rc('font', family='STIXGeneral')
    mpl.rc('text', usetex=False)
    mpl.rcParams['xtick.direction'] = 'in'
    mpl.rcParams['ytick.direction'] = 'in'     #xy轴坐标杆标注的方向
    plt.rcParams["mathtext.fontset"]  = "cm"   #数学符号的字体
    mpl.rcParams["font.family"] = "STIXGeneral"
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

    markers = ['o', 's', 'D', 'p', '*', '^', 'v', '<', '>', 'x', 'h', '+', 'H', '1', '2', '3', '4', '|', '_', '.']
    ############################## setting of figures #################################
    for i in range(len(time_advance)):
        j = time_advance[i]                                   #输入的[1,5,10,15] #用于文件起名
        gfile = "vel_inc1_PDFs_t{}.png".format(j)               #保存的文件名
        gpath = os.path.join(figPath, gfile)
        #-----------------------------------------------------------------------------------------图片大小分辨率
        fig = plt.figure(figsize=(width,height), dpi=dpi)     #定义图片宽、高、分辨率
        plt.rcParams["font.size"] = fontSize                  #统一字体大小
        plt.rcParams["axes.linewidth"] = lineWidth
        ax = fig.add_axes([0,0,1,1])                          #用于压缩图片，相当于各边移动距离
        # ----------------------------------------------------------------------------------------X坐标轴设置
        plt.xscale("linear")                                     #画linear
        ax.xaxis.set_minor_locator(mpl.ticker.AutoMinorLocator(4)) #次刻度
        # formatter = mpl.ticker.FixedFormatter()                #主刻度格式
        ax.xaxis.set_major_formatter(mpl.ticker.FuncFormatter(minor_tick))               #应用主刻度格式
        ax.xaxis.set_minor_formatter(mpl.ticker.NullFormatter()) #次刻度
        # ----------------------------------------------------------------------------------------Y坐标轴设置
        plt.yscale("log")
        ax.yaxis.set_minor_locator(mpl.ticker.LogLocator(base=10.0, subs=np.arange(0.1,1,0.1)))
        formatter = mpl.ticker.LogFormatterSciNotation()
        ax.yaxis.set_major_formatter(formatter)
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
        plt.plot(x, y_fDNS[i], label=legend[5], color=colors[0], linewidth=lineWidth, linestyle='solid',zorder=0)
        
        plt.scatter(x, y_F_IFNO_m1[i], label=legend[0], facecolor='none', linewidths=lineWidth,edgecolor=colors[1], s=70, alpha=1.0, marker=markers[0],zorder=7)    
        plt.scatter(x, y_F_IUFNO_m1[i], label=legend[1], facecolor='none', linewidths=lineWidth,edgecolor=colors[2], s=70, alpha=1.0,  marker=markers[1],zorder=4)   
        plt.scatter(x, y_IUFNO_m1[i], label=legend[2], facecolor='none', linewidths=lineWidth,edgecolor=colors[5], s=70, alpha=1.0,  marker=markers[4],zorder=2)
        plt.scatter(x, y_IFNO_m1[i], label=legend[3], facecolor='none', linewidths=lineWidth,edgecolor=colors[6], s=70, alpha=1.0, marker=markers[5],zorder=1)
        plt.scatter(x, y_DSM_m1[i], label=legend[4], facecolor='none', linewidths=lineWidth,edgecolor=colors[7], s=70, alpha=1.0, marker=markers[6],zorder=5)

        lgd_loc = (0.63,0.62)#6,7#6,78,82
        lgd_font = {'family': "STIXGeneral", 'size': fontSize * 0.6}
        
                         
        plt.savefig(gpath, bbox_inches='tight')
        print("Width x Hight: ", fig.get_size_inches())
        # plt.cl  



    ################################# 图片保存路径 ################################
    figfilePath = os.path.abspath('./plot_results/{}case').format(case_number)
    figPath = os.path.join(figfilePath, "vel_inc1_PDFs/m2")
    if not os.path.exists(figPath):
        os.makedirs(figPath)
    print("图片存放路径：", figPath)

    ############################## setting of figures #################################
    dpi = 600                               #分辨率
    width  = 8                              #图宽
    height = 6                              #图高
    fontSize = 40                          #字体大小
    lineWidth = 2.5                         #线宽
    boxWidth = 2.5                          #边框线宽
    Lmajor = 7                              #主刻度长度
    Lminor = 4                              #次刻度长度
    xlabPad  = 10                           #x坐标下面显示值距离轴距离
    ylabPad  = 10                           #y坐标下面显示值距离轴距离
    xlabel = r"$\mathdefault{\delta_r\bar{u}/\bar{u}^{rms}(r=1\Delta)}$"   #坐标标签
    ylabel = r"$\mathdefault{PDF}$"
    xlimit = [-1.5,1.5]                        #坐标显示范围
    ylimit = [1e-3,1e1]
    legend = ["F-IFNO_mag2", "F-IUFNO_mag2","IUFNO_mag2","IFNO_mag2","DSM_mag2","fDNS"]
    ############################## setting of fonts ####################################
    mpl.rc('font', family='STIXGeneral')
    mpl.rc('text', usetex=False)
    mpl.rcParams['xtick.direction'] = 'in'
    mpl.rcParams['ytick.direction'] = 'in'     #xy轴坐标杆标注的方向
    plt.rcParams["mathtext.fontset"]  = "cm"   #数学符号的字体
    mpl.rcParams["font.family"] = "STIXGeneral"
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

    markers = ['o', 's', 'D', 'p', '*', '^', 'v', '<', '>', 'x', 'h', '+', 'H', '1', '2', '3', '4', '|', '_', '.']
    ############################## setting of figures #################################
    for i in range(len(time_advance)):
        j = time_advance[i]                                   #输入的[1,5,10,15] #用于文件起名
        gfile = "vel_inc1_PDFs_t{}.png".format(j)               #保存的文件名
        gpath = os.path.join(figPath, gfile)
        #-----------------------------------------------------------------------------------------图片大小分辨率
        fig = plt.figure(figsize=(width,height), dpi=dpi)     #定义图片宽、高、分辨率
        plt.rcParams["font.size"] = fontSize                  #统一字体大小
        plt.rcParams["axes.linewidth"] = lineWidth
        ax = fig.add_axes([0,0,1,1])                          #用于压缩图片，相当于各边移动距离
        # ----------------------------------------------------------------------------------------X坐标轴设置
        plt.xscale("linear")                                     #画linear
        ax.xaxis.set_minor_locator(mpl.ticker.AutoMinorLocator(4)) #次刻度
        # formatter = mpl.ticker.FixedFormatter()                #主刻度格式
        ax.xaxis.set_major_formatter(mpl.ticker.FuncFormatter(minor_tick))               #应用主刻度格式
        ax.xaxis.set_minor_formatter(mpl.ticker.NullFormatter()) #次刻度
        # ----------------------------------------------------------------------------------------Y坐标轴设置
        plt.yscale("log")
        ax.yaxis.set_minor_locator(mpl.ticker.LogLocator(base=10.0, subs=np.arange(0.1,1,0.1)))
        formatter = mpl.ticker.LogFormatterSciNotation()
        ax.yaxis.set_major_formatter(formatter)
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
        plt.plot(x, y_fDNS[i], label=legend[5], color=colors[0], linewidth=lineWidth, linestyle='solid',zorder=0)
        
        plt.scatter(x, y_F_IFNO_m2[i], label=legend[0], facecolor='none', linewidths=lineWidth,edgecolor=colors[1], s=70, alpha=1.0, marker=markers[0],zorder=7)    
        plt.scatter(x, y_F_IUFNO_m2[i], label=legend[1], facecolor='none', linewidths=lineWidth,edgecolor=colors[2], s=70, alpha=1.0,  marker=markers[1],zorder=4)   
        plt.scatter(x, y_IUFNO_m2[i], label=legend[2], facecolor='none', linewidths=lineWidth,edgecolor=colors[5], s=70, alpha=1.0,  marker=markers[4],zorder=2)
        plt.scatter(x, y_IFNO_m2[i], label=legend[3], facecolor='none', linewidths=lineWidth,edgecolor=colors[6], s=70, alpha=1.0, marker=markers[5],zorder=1)
        plt.scatter(x, y_DSM_m2[i], label=legend[4], facecolor='none', linewidths=lineWidth,edgecolor=colors[7], s=70, alpha=1.0, marker=markers[6],zorder=5)

        lgd_loc = (0.63,0.62)#6,7#6,78,82
        lgd_font = {'family': "STIXGeneral", 'size': fontSize * 0.6}
        
                         
        plt.savefig(gpath, bbox_inches='tight')
        print("Width x Hight: ", fig.get_size_inches())
        # plt.cl  




    ################################# 图片保存路径 ################################
    figfilePath = os.path.abspath('./plot_results/{}case').format(case_number)
    figPath = os.path.join(figfilePath, "vel_inc1_PDFs/m5")
    if not os.path.exists(figPath):
        os.makedirs(figPath)
    print("图片存放路径：", figPath)

    ############################## setting of figures #################################
    dpi = 600                               #分辨率
    width  = 8                              #图宽
    height = 6                              #图高
    fontSize = 40                          #字体大小
    lineWidth = 2.5                         #线宽
    boxWidth = 2.5                          #边框线宽
    Lmajor = 7                              #主刻度长度
    Lminor = 4                              #次刻度长度
    xlabPad  = 10                           #x坐标下面显示值距离轴距离
    ylabPad  = 10                           #y坐标下面显示值距离轴距离
    xlabel = r"$\mathdefault{\delta_r\bar{u}/\bar{u}^{rms}(r=1\Delta)}$"   #坐标标签
    ylabel = r"$\mathdefault{PDF}$"
    xlimit = [-1.5,1.5]                        #坐标显示范围
    ylimit = [1e-3,1e1]
    legend = ["F-IFNO_mag5", "F-IUFNO_mag5","IUFNO_mag5","IFNO_mag5","DSM_mag5","fDNS"]
    ############################## setting of fonts ####################################
    mpl.rc('font', family='STIXGeneral')
    mpl.rc('text', usetex=False)
    mpl.rcParams['xtick.direction'] = 'in'
    mpl.rcParams['ytick.direction'] = 'in'     #xy轴坐标杆标注的方向
    plt.rcParams["mathtext.fontset"]  = "cm"   #数学符号的字体
    mpl.rcParams["font.family"] = "STIXGeneral"
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

    markers = ['o', 's', 'D', 'p', '*', '^', 'v', '<', '>', 'x', 'h', '+', 'H', '1', '2', '3', '4', '|', '_', '.']
    ############################## setting of figures #################################
    for i in range(len(time_advance)):
        j = time_advance[i]                                   #输入的[1,5,10,15] #用于文件起名
        gfile = "vel_inc1_PDFs_t{}.png".format(j)               #保存的文件名
        gpath = os.path.join(figPath, gfile)
        #-----------------------------------------------------------------------------------------图片大小分辨率
        fig = plt.figure(figsize=(width,height), dpi=dpi)     #定义图片宽、高、分辨率
        plt.rcParams["font.size"] = fontSize                  #统一字体大小
        plt.rcParams["axes.linewidth"] = lineWidth
        ax = fig.add_axes([0,0,1,1])                          #用于压缩图片，相当于各边移动距离
        # ----------------------------------------------------------------------------------------X坐标轴设置
        plt.xscale("linear")                                     #画linear
        ax.xaxis.set_minor_locator(mpl.ticker.AutoMinorLocator(4)) #次刻度
        # formatter = mpl.ticker.FixedFormatter()                #主刻度格式
        ax.xaxis.set_major_formatter(mpl.ticker.FuncFormatter(minor_tick))               #应用主刻度格式
        ax.xaxis.set_minor_formatter(mpl.ticker.NullFormatter()) #次刻度
        # ----------------------------------------------------------------------------------------Y坐标轴设置
        plt.yscale("log")
        ax.yaxis.set_minor_locator(mpl.ticker.LogLocator(base=10.0, subs=np.arange(0.1,1,0.1)))
        formatter = mpl.ticker.LogFormatterSciNotation()
        ax.yaxis.set_major_formatter(formatter)
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
        plt.plot(x, y_fDNS[i], label=legend[5], color=colors[0], linewidth=lineWidth, linestyle='solid',zorder=0)
        
        plt.scatter(x, y_F_IFNO_m5[i], label=legend[0], facecolor='none', linewidths=lineWidth,edgecolor=colors[1], s=70, alpha=1.0, marker=markers[0],zorder=7)    
        plt.scatter(x, y_F_IUFNO_m5[i], label=legend[1], facecolor='none', linewidths=lineWidth,edgecolor=colors[2], s=70, alpha=1.0,  marker=markers[1],zorder=4)   
        plt.scatter(x, y_IUFNO_m5[i], label=legend[2], facecolor='none', linewidths=lineWidth,edgecolor=colors[5], s=70, alpha=1.0,  marker=markers[4],zorder=2)
        plt.scatter(x, y_IFNO_m5[i], label=legend[3], facecolor='none', linewidths=lineWidth,edgecolor=colors[6], s=70, alpha=1.0, marker=markers[5],zorder=1)
        #plt.scatter(x, y_DSM_m5[i], label=legend[4], facecolor='none', linewidths=lineWidth,edgecolor=colors[7], s=70, alpha=1.0, marker=markers[6],zorder=5)

        lgd_loc = (0.63,0.68)#6,7#6,78,82
        lgd_font = {'family': "STIXGeneral", 'size': fontSize * 0.6}
        
                         
        plt.savefig(gpath, bbox_inches='tight')
        print("Width x Hight: ", fig.get_size_inches())
        # plt.cl  




    ################################# 图片保存路径 ################################
    figfilePath = os.path.abspath('./plot_results/{}case').format(case_number)
    figPath = os.path.join(figfilePath, "vel_inc1_PDFs/m10")
    if not os.path.exists(figPath):
        os.makedirs(figPath)
    print("图片存放路径：", figPath)

    ############################## setting of figures #################################
    dpi = 600                               #分辨率
    width  = 8                              #图宽
    height = 6                              #图高
    fontSize = 40                          #字体大小
    lineWidth = 2.5                         #线宽
    boxWidth = 2.5                          #边框线宽
    Lmajor = 7                              #主刻度长度
    Lminor = 4                              #次刻度长度
    xlabPad  = 10                           #x坐标下面显示值距离轴距离
    ylabPad  = 10                           #y坐标下面显示值距离轴距离
    xlabel = r"$\mathdefault{\delta_r\bar{u}/\bar{u}^{rms}(r=1\Delta)}$"   #坐标标签
    ylabel = r"$\mathdefault{PDF}$"
    xlimit = [-1.5,1.5]                        #坐标显示范围
    ylimit = [1e-3,1e1]
    legend = ["F-IFNO_mag10", "F-IUFNO_mag10","IUFNO_mag10","IFNO_mag10","DSM_mag10","fDNS"]
    ############################## setting of fonts ####################################
    mpl.rc('font', family='STIXGeneral')
    mpl.rc('text', usetex=False)
    mpl.rcParams['xtick.direction'] = 'in'
    mpl.rcParams['ytick.direction'] = 'in'     #xy轴坐标杆标注的方向
    plt.rcParams["mathtext.fontset"]  = "cm"   #数学符号的字体
    mpl.rcParams["font.family"] = "STIXGeneral"
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

    markers = ['o', 's', 'D', 'p', '*', '^', 'v', '<', '>', 'x', 'h', '+', 'H', '1', '2', '3', '4', '|', '_', '.']
    ############################## setting of figures #################################
    for i in range(len(time_advance)):
        j = time_advance[i]                                   #输入的[1,5,10,15] #用于文件起名
        gfile = "vel_inc1_PDFs_t{}.png".format(j)               #保存的文件名
        gpath = os.path.join(figPath, gfile)
        #-----------------------------------------------------------------------------------------图片大小分辨率
        fig = plt.figure(figsize=(width,height), dpi=dpi)     #定义图片宽、高、分辨率
        plt.rcParams["font.size"] = fontSize                  #统一字体大小
        plt.rcParams["axes.linewidth"] = lineWidth
        ax = fig.add_axes([0,0,1,1])                          #用于压缩图片，相当于各边移动距离
        # ----------------------------------------------------------------------------------------X坐标轴设置
        plt.xscale("linear")                                     #画linear
        ax.xaxis.set_minor_locator(mpl.ticker.AutoMinorLocator(4)) #次刻度
        # formatter = mpl.ticker.FixedFormatter()                #主刻度格式
        ax.xaxis.set_major_formatter(mpl.ticker.FuncFormatter(minor_tick))               #应用主刻度格式
        ax.xaxis.set_minor_formatter(mpl.ticker.NullFormatter()) #次刻度
        # ----------------------------------------------------------------------------------------Y坐标轴设置
        plt.yscale("log")
        ax.yaxis.set_minor_locator(mpl.ticker.LogLocator(base=10.0, subs=np.arange(0.1,1,0.1)))
        formatter = mpl.ticker.LogFormatterSciNotation()
        ax.yaxis.set_major_formatter(formatter)
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
        plt.plot(x, y_fDNS[i], label=legend[5], color=colors[0], linewidth=lineWidth, linestyle='solid',zorder=0)
        
        plt.scatter(x, y_F_IFNO_m10[i], label=legend[0], facecolor='none', linewidths=lineWidth,edgecolor=colors[1], s=70, alpha=1.0, marker=markers[0],zorder=7)    
        plt.scatter(x, y_F_IUFNO_m10[i], label=legend[1], facecolor='none', linewidths=lineWidth,edgecolor=colors[2], s=70, alpha=1.0,  marker=markers[1],zorder=4)   
        plt.scatter(x, y_IUFNO_m10[i], label=legend[2], facecolor='none', linewidths=lineWidth,edgecolor=colors[5], s=70, alpha=1.0,  marker=markers[4],zorder=2)
        plt.scatter(x, y_IFNO_m10[i], label=legend[3], facecolor='none', linewidths=lineWidth,edgecolor=colors[6], s=70, alpha=1.0, marker=markers[5],zorder=1)
        #plt.scatter(x, y_DSM_m10[i], label=legend[4], facecolor='none', linewidths=lineWidth,edgecolor=colors[7], s=70, alpha=1.0, marker=markers[6],zorder=5)

        lgd_loc = (0.63,0.68)#6,7#6,78,82
        lgd_font = {'family': "STIXGeneral", 'size': fontSize * 0.6}
        
                         
        plt.savefig(gpath, bbox_inches='tight')
        print("Width x Hight: ", fig.get_size_inches())
        # plt.cl          
        
'''        
        
        
        
        
        
        
        
        
        
        