"""
@author: admin
"""
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import os


#os.chdir(r'C:\Users\Lenovo\Desktop\PINO_3d\post\plot_result')
case_number = 27
timestep = 600
#==========================================================================DNS
print("fDNS getting dat!")
x_fDNS_dissipation=[]
y_fDNS_dissipation=[]
x_fDNS_Et=[]
y_fDNS_Et=[]
x_fDNS_inc1_PDFs=[]
y_fDNS_inc1_PDFs=[]
x_fDNS_velspectrum=[]
y_fDNS_velspectrum=[]
x_fDNS_structrue2 = []
y_fDNS_structrue2 = []
x_fDNS_structrue4 = []
y_fDNS_structrue4 = []
x_fDNS_urms = []
y_fDNS_urms = []
x_fDNS_wrms = []
y_fDNS_wrms = []
x_fDNS_vort_PDFs = []
y_fDNS_vort_PDFs = []
x_fDNS_vort_statistics = []
y_fDNS_vort_statistics = []
for case_n in range(case_number-1,case_number):
    # print(case_n)
    # 载入后处理文件，包括速度参数，PDFs，能谱，结构函数
    fDNS_vel_parameter= np.loadtxt('./case{}/Result_LES32_fDNS_gap200/post_result/vel_parameter.dat'.format(case_n+1),dtype=float, comments=['step'])
    fDNS_ic1_PDFs = np.loadtxt('./case{}/Result_LES32_fDNS_gap200/post_result/inc1_PDFs.dat'.format(case_n + 1), dtype=float,comments=['step'])
    fDNS_spec = np.loadtxt('./case{}/Result_LES32_fDNS_gap200/post_result/spectrum_vel.dat'.format(case_n + 1), dtype=float,comments=['variables', 'zone'])
    fDNS_structrue2 = np.loadtxt('./case{}/Result_LES32_fDNS_gap200/post_result/structure2.dat'.format(case_n + 1),dtype=float, comments=['step'])
    fDNS_structrue4 = np.loadtxt('./case{}/Result_LES32_fDNS_gap200/post_result/structure4.dat'.format(case_n + 1),dtype=float, comments=['step'])
    fDNS_vort_PDFs = np.loadtxt('./case{}/Result_LES32_fDNS_gap200/post_result/vort_PDFs.dat'.format(case_n + 1), dtype=float,comments=['variables', 'zone'])
    fDNS_vort_statistics = np.loadtxt('./case{}/Result_LES32_fDNS_gap200/post_result/vort_statistics.dat'.format(case_n + 1),dtype=float, comments=['step'])
    # print(VGM.shape)
    # 取出数据
    x_fDNS_urms.append(fDNS_vel_parameter[:,0])  # 只取出第一列数据
    y_fDNS_urms.append(fDNS_vel_parameter[:,3]) #只取出第二列数据
    x_fDNS_wrms.append(fDNS_vel_parameter[:,0])  # 只取出第一列数据
    y_fDNS_wrms.append(fDNS_vel_parameter[:,7]) #只取出第二列数据
    x_fDNS_dissipation.append(fDNS_vel_parameter[:,0])  # 只取出第一列数据
    y_fDNS_dissipation.append(fDNS_vel_parameter[:,8]) #只取出第二列数据
    x_fDNS_Et.append(fDNS_vel_parameter[:,0])  # 只取出第一列数据
    y_fDNS_Et.append(fDNS_vel_parameter[:,6]) #只取出第二列数据
    x_fDNS_inc1_PDFs.append(fDNS_ic1_PDFs[:,0])  # 只取出第一列数据
    y_fDNS_inc1_PDFs.append(fDNS_ic1_PDFs[:,1]) #只取出第二列数据
    x_fDNS_velspectrum.append(fDNS_spec[:,0])  # 只取出第一列数据
    y_fDNS_velspectrum.append(fDNS_spec[:,1]) #只取出第二列数据
    x_fDNS_structrue2.append(fDNS_structrue2[:,0])  # 只取出第一列数据
    y_fDNS_structrue2.append(fDNS_structrue2[:,1]) #只取出第二列数据
    x_fDNS_structrue4.append(fDNS_structrue4[:,0])  # 只取出第一列数据
    y_fDNS_structrue4.append(fDNS_structrue4[:,1]) #只取出第二列数据
    x_fDNS_vort_PDFs.append(fDNS_vort_PDFs[:,0])  # 只取出第一列数据
    y_fDNS_vort_PDFs.append(fDNS_vort_PDFs[:,1]) #只取出第二列数据
    x_fDNS_vort_statistics.append(fDNS_vort_statistics[:,0])  # 只取出第一列数据
    y_fDNS_vort_statistics.append(fDNS_vort_statistics[:,5]) #只取出第二列数据
# 转化为数组
x_fDNS_urms_arr = np.asarray(x_fDNS_urms) #列表转数组
y_fDNS_urms_arr = np.asarray(y_fDNS_urms) #列表转数组
x_fDNS_wrms_arr = np.asarray(x_fDNS_wrms) #列表转数组
y_fDNS_wrms_arr = np.asarray(y_fDNS_wrms) #列表转数组
x_fDNS_dissipation_arr = np.asarray(x_fDNS_dissipation) #列表转数组
y_fDNS_dissipation_arr = np.asarray(y_fDNS_dissipation) #列表转数组
x_fDNS_Et_arr = np.asarray(x_fDNS_Et) #列表转数组
y_fDNS_Et_arr = np.asarray(y_fDNS_Et) #列表转数组
x_fDNS_inc1_PDFs_arr = np.asarray(x_fDNS_inc1_PDFs) #列表转数组
y_fDNS_inc1_PDFs_arr = np.asarray(y_fDNS_inc1_PDFs) #列表转数组
x_fDNS_spe_arr = np.asarray(x_fDNS_velspectrum) #列表转数组
y_fDNS_spe_arr = np.asarray(y_fDNS_velspectrum) #列表转数组
x_fDNS_structrue2 = np.asarray(x_fDNS_structrue2) #列表转数组
y_fDNS_structrue2 = np.asarray(y_fDNS_structrue2) #列表转数组
x_fDNS_structrue4 = np.asarray(x_fDNS_structrue4) #列表转数组
y_fDNS_structrue4 = np.asarray(y_fDNS_structrue4) #列表转数组
x_fDNS_vort_PDFs = np.asarray(x_fDNS_vort_PDFs) #列表转数组
y_fDNS_vort_PDFs = np.asarray(y_fDNS_vort_PDFs) #列表转数组
x_fDNS_vort_statistics = np.asarray(x_fDNS_vort_statistics) #列表转数组
y_fDNS_vort_statistics = np.asarray(y_fDNS_vort_statistics) #列表转数组
# 取均值
x_urms_avg_case = np.mean(x_fDNS_urms_arr,0) #行压缩成一行
y_urms_avg_case = np.mean(y_fDNS_urms_arr,0) #行压缩成一行
x_wrms_avg_case = np.mean(x_fDNS_wrms_arr,0) #行压缩成一行
y_wrms_avg_case = np.mean(y_fDNS_wrms_arr,0) #行压缩成一行
x_dissipation_avg_case = np.mean(x_fDNS_dissipation_arr,0) #行压缩成一行
y_dissipation_avg_case = np.mean(y_fDNS_dissipation_arr,0) #行压缩成一行
x_Et_avg_case = np.mean(x_fDNS_Et_arr,0) #行压缩成一行
y_Et_avg_case = np.mean(y_fDNS_Et_arr,0) #行压缩成一行
x_inc1_PDFs_avg_case = np.mean(x_fDNS_inc1_PDFs_arr,0) #行压缩成一行
y_inc1_PDFs_avg_case = np.mean(y_fDNS_inc1_PDFs_arr,0) #行压缩成一行
x_spe_avg_case = np.mean(x_fDNS_spe_arr,0) #行压缩成一行
y_spe_avg_case = np.mean(y_fDNS_spe_arr,0) #行压缩成一行
x_structrue2_avg_case = np.mean(x_fDNS_structrue2,0) #行压缩成一行
y_structrue2_avg_case = np.mean(y_fDNS_structrue2,0) #行压缩成
x_structrue4_avg_case = np.mean(x_fDNS_structrue4,0) #行压缩成一行
y_structrue4_avg_case = np.mean(y_fDNS_structrue4,0) #行压缩成
x_vort_PDFs_avg_case = np.mean(x_fDNS_vort_PDFs,0) #行压缩成一行
y_vort_PDFs_avg_case = np.mean(y_fDNS_vort_PDFs,0) #行压缩成
x_vort_statistics_avg_case = np.mean(x_fDNS_vort_statistics,0) #行压缩成一行
y_vort_statistics_avg_case = np.mean(y_fDNS_vort_statistics,0) #行压缩成
# 拼接操作
avg_fDNS_urms_10case=np.dstack((x_urms_avg_case,y_urms_avg_case)).squeeze() #拼接
avg_fDNS_wrms_10case=np.dstack((x_wrms_avg_case,y_wrms_avg_case)).squeeze() #拼接
avg_fDNS_dissipation_10case=np.dstack((x_dissipation_avg_case,y_dissipation_avg_case)).squeeze() #拼接
avg_fDNS_Et_10case=np.dstack((x_Et_avg_case,y_Et_avg_case)).squeeze() #拼接
avg_fDNS_inc1_PDFs_10case=np.dstack((x_inc1_PDFs_avg_case,y_inc1_PDFs_avg_case)).squeeze() #拼接
avg_fDNS_spectrum_10case=np.dstack((x_spe_avg_case,y_spe_avg_case)).squeeze() #拼接
avg_fDNS_structrue2_10case=np.dstack((x_structrue2_avg_case,y_structrue2_avg_case)).squeeze() #拼接
avg_fDNS_structrue4_10case=np.dstack((x_structrue4_avg_case,y_structrue4_avg_case)).squeeze() #拼接
avg_fDNS_vort_PDFs_10case=np.dstack((x_vort_PDFs_avg_case,y_vort_PDFs_avg_case)).squeeze() #拼接
avg_fDNS_vort_statistics_10case=np.dstack((x_vort_statistics_avg_case,y_vort_statistics_avg_case)).squeeze() #拼接
#导出均值

np.savetxt('./AVG/fDNS/N{}/avg_fDNS_{}case_urms.dat'.format(case_number,case_number),avg_fDNS_urms_10case, fmt="%16.7f")
np.savetxt('./AVG/fDNS/N{}/avg_fDNS_{}case_wrms.dat'.format(case_number,case_number),avg_fDNS_wrms_10case, fmt="%16.7f")
np.savetxt('./AVG/fDNS/N{}/avg_fDNS_{}case_dissipation.dat'.format(case_number,case_number),avg_fDNS_dissipation_10case, fmt="%16.7f")
np.savetxt('./AVG/fDNS/N{}/avg_fDNS_{}case_Ek_t.dat'.format(case_number,case_number),avg_fDNS_Et_10case, fmt="%16.7f")
np.savetxt('./AVG/fDNS/N{}/avg_fDNS_{}case_inc1_PDFs.dat'.format(case_number,case_number),avg_fDNS_inc1_PDFs_10case, fmt="%16.7f")
np.savetxt('./AVG/fDNS/N{}/avg_fDNS_{}case_vel_spec.dat'.format(case_number,case_number),avg_fDNS_spectrum_10case, fmt="%16.7f")
np.savetxt('./AVG/fDNS/N{}/avg_fDNS_{}case_structrue2.dat'.format(case_number,case_number),avg_fDNS_structrue2_10case, fmt="%16.7f")
np.savetxt('./AVG/fDNS/N{}/avg_fDNS_{}case_structrue4.dat'.format(case_number,case_number),avg_fDNS_structrue4_10case, fmt="%16.7f")
np.savetxt('./AVG/fDNS/N{}/avg_fDNS_{}case_vort_PDFs.dat'.format(case_number,case_number),avg_fDNS_vort_PDFs_10case, fmt="%16.7f")
np.savetxt('./AVG/fDNS/N{}/avg_fDNS_{}case_vort_statistics.dat'.format(case_number,case_number),avg_fDNS_vort_statistics_10case, fmt="%16.7f")
'''
np.savetxt('./AVG/fDNS/{}case/avg_fDNS_{}case_urms.dat'.format(case_number,case_number),avg_fDNS_urms_10case, fmt="%16.7f")
np.savetxt('./AVG/fDNS/{}case/avg_fDNS_{}case_wrms.dat'.format(case_number,case_number),avg_fDNS_wrms_10case, fmt="%16.7f")
np.savetxt('./AVG/fDNS/{}case/avg_fDNS_{}case_dissipation.dat'.format(case_number,case_number),avg_fDNS_dissipation_10case, fmt="%16.7f")
np.savetxt('./AVG/fDNS/{}case/avg_fDNS_{}case_Ek_t.dat'.format(case_number,case_number),avg_fDNS_Et_10case, fmt="%16.7f")
np.savetxt('./AVG/fDNS/{}case/avg_fDNS_{}case_inc1_PDFs.dat'.format(case_number,case_number),avg_fDNS_inc1_PDFs_10case, fmt="%16.7f")
np.savetxt('./AVG/fDNS/{}case/avg_fDNS_{}case_vel_spec.dat'.format(case_number,case_number),avg_fDNS_spectrum_10case, fmt="%16.7f")
np.savetxt('./AVG/fDNS/{}case/avg_fDNS_{}case_structrue2.dat'.format(case_number,case_number),avg_fDNS_structrue2_10case, fmt="%16.7f")
np.savetxt('./AVG/fDNS/{}case/avg_fDNS_{}case_structrue4.dat'.format(case_number,case_number),avg_fDNS_structrue4_10case, fmt="%16.7f")
np.savetxt('./AVG/fDNS/{}case/avg_fDNS_{}case_vort_PDFs.dat'.format(case_number,case_number),avg_fDNS_vort_PDFs_10case, fmt="%16.7f")
np.savetxt('./AVG/fDNS/{}case/avg_fDNS_{}case_vort_statistics.dat'.format(case_number,case_number),avg_fDNS_vort_statistics_10case, fmt="%16.7f")
'''
#==========================================================================FNO
print("IUFNO_11ep getting dat!")
x_IUFNO_dissipation=[]
y_IUFNO_dissipation=[]
x_IUFNO_Et=[]
y_IUFNO_Et=[]
x_IUFNO_inc1_PDFs=[]
y_IUFNO_inc1_PDFs=[]
x_IUFNO_velspectrum=[]
y_IUFNO_velspectrum=[]
x_IUFNO_structrue2 = []
y_IUFNO_structrue2 = []
x_IUFNO_structrue4 = []
y_IUFNO_structrue4 = []
x_IUFNO_urms = []
y_IUFNO_urms = []
x_IUFNO_wrms = []
y_IUFNO_wrms = []
x_IUFNO_vort_PDFs = []
y_IUFNO_vort_PDFs = []
x_IUFNO_vort_statistics = []
y_IUFNO_vort_statistics = []
for case_n in range(case_number-1,case_number):
    # print(case_n)
    # 载入后处理文件，包括速度参数，PDFs，能谱，结构函数
    IUFNO_vel_parameter= np.loadtxt('./case{}/Result_LES32_IUFNO_11ep_gap200/post_result/vel_parameter.dat'.format(case_n+1),dtype=float, comments=['step'])
    IUFNO_ic1_PDFs = np.loadtxt('./case{}/Result_LES32_IUFNO_11ep_gap200/post_result/inc1_PDFs.dat'.format(case_n + 1), dtype=float,comments=['step'])
    IUFNO_spec = np.loadtxt('./case{}/Result_LES32_IUFNO_11ep_gap200/post_result/spectrum_vel.dat'.format(case_n + 1), dtype=float,comments=['variables', 'zone'])
    IUFNO_structrue2 = np.loadtxt('./case{}/Result_LES32_IUFNO_11ep_gap200/post_result/structure2.dat'.format(case_n + 1),dtype=float, comments=['step'])
    IUFNO_structrue4 = np.loadtxt('./case{}/Result_LES32_IUFNO_11ep_gap200/post_result/structure4.dat'.format(case_n + 1),dtype=float, comments=['step'])
    IUFNO_vort_PDFs = np.loadtxt('./case{}/Result_LES32_IUFNO_11ep_gap200/post_result/vort_PDFs.dat'.format(case_n + 1), dtype=float,comments=['variables', 'zone'])
    IUFNO_vort_statistics = np.loadtxt('./case{}/Result_LES32_IUFNO_11ep_gap200/post_result/vort_statistics.dat'.format(case_n + 1),dtype=float, comments=['step'])
    # print(VGM.shape)
    # 取出数据
    x_IUFNO_urms.append(IUFNO_vel_parameter[:,0])  # 只取出第一列数据
    y_IUFNO_urms.append(IUFNO_vel_parameter[:,3]) #只取出第二列数据
    x_IUFNO_wrms.append(IUFNO_vel_parameter[:,0])  # 只取出第一列数据
    y_IUFNO_wrms.append(IUFNO_vel_parameter[:,7]) #只取出第二列数据
    x_IUFNO_dissipation.append(IUFNO_vel_parameter[:,0])  # 只取出第一列数据
    y_IUFNO_dissipation.append(IUFNO_vel_parameter[:,8]) #只取出第二列数据
    x_IUFNO_Et.append(IUFNO_vel_parameter[:,0])  # 只取出第一列数据
    y_IUFNO_Et.append(IUFNO_vel_parameter[:,6]) #只取出第二列数据
    x_IUFNO_inc1_PDFs.append(IUFNO_ic1_PDFs[:,0])  # 只取出第一列数据
    y_IUFNO_inc1_PDFs.append(IUFNO_ic1_PDFs[:,1]) #只取出第二列数据
    x_IUFNO_velspectrum.append(IUFNO_spec[:,0])  # 只取出第一列数据
    y_IUFNO_velspectrum.append(IUFNO_spec[:,1]) #只取出第二列数据
    x_IUFNO_structrue2.append(IUFNO_structrue2[:,0])  # 只取出第一列数据
    y_IUFNO_structrue2.append(IUFNO_structrue2[:,1]) #只取出第二列数据
    x_IUFNO_structrue4.append(IUFNO_structrue4[:,0])  # 只取出第一列数据
    y_IUFNO_structrue4.append(IUFNO_structrue4[:,1]) #只取出第二列数据
    x_IUFNO_vort_PDFs.append(IUFNO_vort_PDFs[:,0])  # 只取出第一列数据
    y_IUFNO_vort_PDFs.append(IUFNO_vort_PDFs[:,1]) #只取出第二列数据
    x_IUFNO_vort_statistics.append(IUFNO_vort_statistics[:,0])  # 只取出第一列数据
    y_IUFNO_vort_statistics.append(IUFNO_vort_statistics[:,5]) #只取出第二列数据
# 转化为数组
x_IUFNO_urms_arr = np.asarray(x_IUFNO_urms) #列表转数组
y_IUFNO_urms_arr = np.asarray(y_IUFNO_urms) #列表转数组
x_IUFNO_wrms_arr = np.asarray(x_IUFNO_wrms) #列表转数组
y_IUFNO_wrms_arr = np.asarray(y_IUFNO_wrms) #列表转数组
x_IUFNO_dissipation_arr = np.asarray(x_IUFNO_dissipation) #列表转数组
y_IUFNO_dissipation_arr = np.asarray(y_IUFNO_dissipation) #列表转数组
x_IUFNO_Et_arr = np.asarray(x_IUFNO_Et) #列表转数组
y_IUFNO_Et_arr = np.asarray(y_IUFNO_Et) #列表转数组
x_IUFNO_inc1_PDFs_arr = np.asarray(x_IUFNO_inc1_PDFs) #列表转数组
y_IUFNO_inc1_PDFs_arr = np.asarray(y_IUFNO_inc1_PDFs) #列表转数组
x_IUFNO_spe_arr = np.asarray(x_IUFNO_velspectrum) #列表转数组
y_IUFNO_spe_arr = np.asarray(y_IUFNO_velspectrum) #列表转数组
x_IUFNO_structrue2 = np.asarray(x_IUFNO_structrue2) #列表转数组
y_IUFNO_structrue2 = np.asarray(y_IUFNO_structrue2) #列表转数组
x_IUFNO_structrue4 = np.asarray(x_IUFNO_structrue4) #列表转数组
y_IUFNO_structrue4 = np.asarray(y_IUFNO_structrue4) #列表转数组
x_IUFNO_vort_PDFs = np.asarray(x_IUFNO_vort_PDFs) #列表转数组
y_IUFNO_vort_PDFs = np.asarray(y_IUFNO_vort_PDFs) #列表转数组
x_IUFNO_vort_statistics = np.asarray(x_IUFNO_vort_statistics) #列表转数组
y_IUFNO_vort_statistics = np.asarray(y_IUFNO_vort_statistics) #列表转数组
# 取均值
x_urms_avg_case = np.mean(x_IUFNO_urms_arr,0) #行压缩成一行
y_urms_avg_case = np.mean(y_IUFNO_urms_arr,0) #行压缩成一行
x_wrms_avg_case = np.mean(x_IUFNO_wrms_arr,0) #行压缩成一行
y_wrms_avg_case = np.mean(y_IUFNO_wrms_arr,0) #行压缩成一行
x_dissipation_avg_case = np.mean(x_IUFNO_dissipation_arr,0) #行压缩成一行
y_dissipation_avg_case = np.mean(y_IUFNO_dissipation_arr,0) #行压缩成一行
x_Et_avg_case = np.mean(x_IUFNO_Et_arr,0) #行压缩成一行
y_Et_avg_case = np.mean(y_IUFNO_Et_arr,0) #行压缩成一行
x_inc1_PDFs_avg_case = np.mean(x_IUFNO_inc1_PDFs_arr,0) #行压缩成一行
y_inc1_PDFs_avg_case = np.mean(y_IUFNO_inc1_PDFs_arr,0) #行压缩成一行
x_spe_avg_case = np.mean(x_IUFNO_spe_arr,0) #行压缩成一行
y_spe_avg_case = np.mean(y_IUFNO_spe_arr,0) #行压缩成一行
x_structrue2_avg_case = np.mean(x_IUFNO_structrue2,0) #行压缩成一行
y_structrue2_avg_case = np.mean(y_IUFNO_structrue2,0) #行压缩成
x_structrue4_avg_case = np.mean(x_IUFNO_structrue4,0) #行压缩成一行
y_structrue4_avg_case = np.mean(y_IUFNO_structrue4,0) #行压缩成
x_vort_PDFs_avg_case = np.mean(x_IUFNO_vort_PDFs,0) #行压缩成一行
y_vort_PDFs_avg_case = np.mean(y_IUFNO_vort_PDFs,0) #行压缩成
x_vort_statistics_avg_case = np.mean(x_IUFNO_vort_statistics,0) #行压缩成一行
y_vort_statistics_avg_case = np.mean(y_IUFNO_vort_statistics,0) #行压缩成
# 拼接操作
avg_IUFNO_urms_10case=np.dstack((x_urms_avg_case,y_urms_avg_case)).squeeze() #拼接
avg_IUFNO_wrms_10case=np.dstack((x_wrms_avg_case,y_wrms_avg_case)).squeeze() #拼接
avg_IUFNO_dissipation_10case=np.dstack((x_dissipation_avg_case,y_dissipation_avg_case)).squeeze() #拼接
avg_IUFNO_Et_10case=np.dstack((x_Et_avg_case,y_Et_avg_case)).squeeze() #拼接
avg_IUFNO_inc1_PDFs_10case=np.dstack((x_inc1_PDFs_avg_case,y_inc1_PDFs_avg_case)).squeeze() #拼接
avg_IUFNO_spectrum_10case=np.dstack((x_spe_avg_case,y_spe_avg_case)).squeeze() #拼接
avg_IUFNO_structrue2_10case=np.dstack((x_structrue2_avg_case,y_structrue2_avg_case)).squeeze() #拼接
avg_IUFNO_structrue4_10case=np.dstack((x_structrue4_avg_case,y_structrue4_avg_case)).squeeze() #拼接
avg_IUFNO_vort_PDFs_10case=np.dstack((x_vort_PDFs_avg_case,y_vort_PDFs_avg_case)).squeeze() #拼接
avg_IUFNO_vort_statistics_10case=np.dstack((x_vort_statistics_avg_case,y_vort_statistics_avg_case)).squeeze() #拼接
#导出均值

np.savetxt('./AVG/IUFNO_11ep/N{}/avg_IUFNO_{}case_urms.dat'.format(case_number,case_number),avg_IUFNO_urms_10case, fmt="%16.7f")
np.savetxt('./AVG/IUFNO_11ep/N{}/avg_IUFNO_{}case_wrms.dat'.format(case_number,case_number),avg_IUFNO_wrms_10case, fmt="%16.7f")
np.savetxt('./AVG/IUFNO_11ep/N{}/avg_IUFNO_{}case_dissipation.dat'.format(case_number,case_number),avg_IUFNO_dissipation_10case, fmt="%16.7f")
np.savetxt('./AVG/IUFNO_11ep/N{}/avg_IUFNO_{}case_Ek_t.dat'.format(case_number,case_number),avg_IUFNO_Et_10case, fmt="%16.7f")
np.savetxt('./AVG/IUFNO_11ep/N{}/avg_IUFNO_{}case_inc1_PDFs.dat'.format(case_number,case_number),avg_IUFNO_inc1_PDFs_10case, fmt="%16.7f")
np.savetxt('./AVG/IUFNO_11ep/N{}/avg_IUFNO_{}case_vel_spec.dat'.format(case_number,case_number),avg_IUFNO_spectrum_10case, fmt="%16.7f")
np.savetxt('./AVG/IUFNO_11ep/N{}/avg_IUFNO_{}case_structrue2.dat'.format(case_number,case_number),avg_IUFNO_structrue2_10case, fmt="%16.7f")
np.savetxt('./AVG/IUFNO_11ep/N{}/avg_IUFNO_{}case_structrue4.dat'.format(case_number,case_number),avg_IUFNO_structrue4_10case, fmt="%16.7f")
np.savetxt('./AVG/IUFNO_11ep/N{}/avg_IUFNO_{}case_vort_PDFs.dat'.format(case_number,case_number),avg_IUFNO_vort_PDFs_10case, fmt="%16.7f")
np.savetxt('./AVG/IUFNO_11ep/N{}/avg_IUFNO_{}case_vort_statistics.dat'.format(case_number,case_number),avg_IUFNO_vort_statistics_10case, fmt="%16.7f")
'''
np.savetxt('./AVG/IUFNO_11ep/{}case/avg_IUFNO_{}case_urms.dat'.format(case_number,case_number),avg_IUFNO_urms_10case, fmt="%16.7f")
np.savetxt('./AVG/IUFNO_11ep/{}case/avg_IUFNO_{}case_wrms.dat'.format(case_number,case_number),avg_IUFNO_wrms_10case, fmt="%16.7f")
np.savetxt('./AVG/IUFNO_11ep/{}case/avg_IUFNO_{}case_dissipation.dat'.format(case_number,case_number),avg_IUFNO_dissipation_10case, fmt="%16.7f")
np.savetxt('./AVG/IUFNO_11ep/{}case/avg_IUFNO_{}case_Ek_t.dat'.format(case_number,case_number),avg_IUFNO_Et_10case, fmt="%16.7f")
np.savetxt('./AVG/IUFNO_11ep/{}case/avg_IUFNO_{}case_inc1_PDFs.dat'.format(case_number,case_number),avg_IUFNO_inc1_PDFs_10case, fmt="%16.7f")
np.savetxt('./AVG/IUFNO_11ep/{}case/avg_IUFNO_{}case_vel_spec.dat'.format(case_number,case_number),avg_IUFNO_spectrum_10case, fmt="%16.7f")
np.savetxt('./AVG/IUFNO_11ep/{}case/avg_IUFNO_{}case_structrue2.dat'.format(case_number,case_number),avg_IUFNO_structrue2_10case, fmt="%16.7f")
np.savetxt('./AVG/IUFNO_11ep/{}case/avg_IUFNO_{}case_structrue4.dat'.format(case_number,case_number),avg_IUFNO_structrue4_10case, fmt="%16.7f")
np.savetxt('./AVG/IUFNO_11ep/{}case/avg_IUFNO_{}case_vort_PDFs.dat'.format(case_number,case_number),avg_IUFNO_vort_PDFs_10case, fmt="%16.7f")
np.savetxt('./AVG/IUFNO_11ep/{}case/avg_IUFNO_{}case_vort_statistics.dat'.format(case_number,case_number),avg_IUFNO_vort_statistics_10case, fmt="%16.7f")
'''
#==========================================================================FNO
print("IUFNO_11ep_mag0.1 getting dat!")
x_IUFNO_dissipation=[]
y_IUFNO_dissipation=[]
x_IUFNO_Et=[]
y_IUFNO_Et=[]
x_IUFNO_inc1_PDFs=[]
y_IUFNO_inc1_PDFs=[]
x_IUFNO_velspectrum=[]
y_IUFNO_velspectrum=[]
x_IUFNO_structrue2 = []
y_IUFNO_structrue2 = []
x_IUFNO_structrue4 = []
y_IUFNO_structrue4 = []
x_IUFNO_urms = []
y_IUFNO_urms = []
x_IUFNO_wrms = []
y_IUFNO_wrms = []
x_IUFNO_vort_PDFs = []
y_IUFNO_vort_PDFs = []
x_IUFNO_vort_statistics = []
y_IUFNO_vort_statistics = []
for case_n in range(case_number-1,case_number):
    # print(case_n)
    # 载入后处理文件，包括速度参数，PDFs，能谱，结构函数
    IUFNO_vel_parameter= np.loadtxt('./case{}/Result_LES32_IUFNO_11ep_gap200_mag0.1/post_result/vel_parameter.dat'.format(case_n+1),dtype=float, comments=['step'])
    IUFNO_ic1_PDFs = np.loadtxt('./case{}/Result_LES32_IUFNO_11ep_gap200_mag0.1/post_result/inc1_PDFs.dat'.format(case_n + 1), dtype=float,comments=['step'])
    IUFNO_spec = np.loadtxt('./case{}/Result_LES32_IUFNO_11ep_gap200_mag0.1/post_result/spectrum_vel.dat'.format(case_n + 1), dtype=float,comments=['variables', 'zone'])
    IUFNO_structrue2 = np.loadtxt('./case{}/Result_LES32_IUFNO_11ep_gap200_mag0.1/post_result/structure2.dat'.format(case_n + 1),dtype=float, comments=['step'])
    IUFNO_structrue4 = np.loadtxt('./case{}/Result_LES32_IUFNO_11ep_gap200_mag0.1/post_result/structure4.dat'.format(case_n + 1),dtype=float, comments=['step'])
    IUFNO_vort_PDFs = np.loadtxt('./case{}/Result_LES32_IUFNO_11ep_gap200_mag0.1/post_result/vort_PDFs.dat'.format(case_n + 1), dtype=float,comments=['variables', 'zone'])
    IUFNO_vort_statistics = np.loadtxt('./case{}/Result_LES32_IUFNO_11ep_gap200_mag0.1/post_result/vort_statistics.dat'.format(case_n + 1),dtype=float, comments=['step'])
    # print(VGM.shape)
    # 取出数据
    x_IUFNO_urms.append(IUFNO_vel_parameter[:,0])  # 只取出第一列数据
    y_IUFNO_urms.append(IUFNO_vel_parameter[:,3]) #只取出第二列数据
    x_IUFNO_wrms.append(IUFNO_vel_parameter[:,0])  # 只取出第一列数据
    y_IUFNO_wrms.append(IUFNO_vel_parameter[:,7]) #只取出第二列数据
    x_IUFNO_dissipation.append(IUFNO_vel_parameter[:,0])  # 只取出第一列数据
    y_IUFNO_dissipation.append(IUFNO_vel_parameter[:,8]) #只取出第二列数据
    x_IUFNO_Et.append(IUFNO_vel_parameter[:,0])  # 只取出第一列数据
    y_IUFNO_Et.append(IUFNO_vel_parameter[:,6]) #只取出第二列数据
    x_IUFNO_inc1_PDFs.append(IUFNO_ic1_PDFs[:,0])  # 只取出第一列数据
    y_IUFNO_inc1_PDFs.append(IUFNO_ic1_PDFs[:,1]) #只取出第二列数据
    x_IUFNO_velspectrum.append(IUFNO_spec[:,0])  # 只取出第一列数据
    y_IUFNO_velspectrum.append(IUFNO_spec[:,1]) #只取出第二列数据
    x_IUFNO_structrue2.append(IUFNO_structrue2[:,0])  # 只取出第一列数据
    y_IUFNO_structrue2.append(IUFNO_structrue2[:,1]) #只取出第二列数据
    x_IUFNO_structrue4.append(IUFNO_structrue4[:,0])  # 只取出第一列数据
    y_IUFNO_structrue4.append(IUFNO_structrue4[:,1]) #只取出第二列数据
    x_IUFNO_vort_PDFs.append(IUFNO_vort_PDFs[:,0])  # 只取出第一列数据
    y_IUFNO_vort_PDFs.append(IUFNO_vort_PDFs[:,1]) #只取出第二列数据
    x_IUFNO_vort_statistics.append(IUFNO_vort_statistics[:,0])  # 只取出第一列数据
    y_IUFNO_vort_statistics.append(IUFNO_vort_statistics[:,5]) #只取出第二列数据
# 转化为数组
x_IUFNO_urms_arr = np.asarray(x_IUFNO_urms) #列表转数组
y_IUFNO_urms_arr = np.asarray(y_IUFNO_urms) #列表转数组
x_IUFNO_wrms_arr = np.asarray(x_IUFNO_wrms) #列表转数组
y_IUFNO_wrms_arr = np.asarray(y_IUFNO_wrms) #列表转数组
x_IUFNO_dissipation_arr = np.asarray(x_IUFNO_dissipation) #列表转数组
y_IUFNO_dissipation_arr = np.asarray(y_IUFNO_dissipation) #列表转数组
x_IUFNO_Et_arr = np.asarray(x_IUFNO_Et) #列表转数组
y_IUFNO_Et_arr = np.asarray(y_IUFNO_Et) #列表转数组
x_IUFNO_inc1_PDFs_arr = np.asarray(x_IUFNO_inc1_PDFs) #列表转数组
y_IUFNO_inc1_PDFs_arr = np.asarray(y_IUFNO_inc1_PDFs) #列表转数组
x_IUFNO_spe_arr = np.asarray(x_IUFNO_velspectrum) #列表转数组
y_IUFNO_spe_arr = np.asarray(y_IUFNO_velspectrum) #列表转数组
x_IUFNO_structrue2 = np.asarray(x_IUFNO_structrue2) #列表转数组
y_IUFNO_structrue2 = np.asarray(y_IUFNO_structrue2) #列表转数组
x_IUFNO_structrue4 = np.asarray(x_IUFNO_structrue4) #列表转数组
y_IUFNO_structrue4 = np.asarray(y_IUFNO_structrue4) #列表转数组
x_IUFNO_vort_PDFs = np.asarray(x_IUFNO_vort_PDFs) #列表转数组
y_IUFNO_vort_PDFs = np.asarray(y_IUFNO_vort_PDFs) #列表转数组
x_IUFNO_vort_statistics = np.asarray(x_IUFNO_vort_statistics) #列表转数组
y_IUFNO_vort_statistics = np.asarray(y_IUFNO_vort_statistics) #列表转数组
# 取均值
x_urms_avg_case = np.mean(x_IUFNO_urms_arr,0) #行压缩成一行
y_urms_avg_case = np.mean(y_IUFNO_urms_arr,0) #行压缩成一行
x_wrms_avg_case = np.mean(x_IUFNO_wrms_arr,0) #行压缩成一行
y_wrms_avg_case = np.mean(y_IUFNO_wrms_arr,0) #行压缩成一行
x_dissipation_avg_case = np.mean(x_IUFNO_dissipation_arr,0) #行压缩成一行
y_dissipation_avg_case = np.mean(y_IUFNO_dissipation_arr,0) #行压缩成一行
x_Et_avg_case = np.mean(x_IUFNO_Et_arr,0) #行压缩成一行
y_Et_avg_case = np.mean(y_IUFNO_Et_arr,0) #行压缩成一行
x_inc1_PDFs_avg_case = np.mean(x_IUFNO_inc1_PDFs_arr,0) #行压缩成一行
y_inc1_PDFs_avg_case = np.mean(y_IUFNO_inc1_PDFs_arr,0) #行压缩成一行
x_spe_avg_case = np.mean(x_IUFNO_spe_arr,0) #行压缩成一行
y_spe_avg_case = np.mean(y_IUFNO_spe_arr,0) #行压缩成一行
x_structrue2_avg_case = np.mean(x_IUFNO_structrue2,0) #行压缩成一行
y_structrue2_avg_case = np.mean(y_IUFNO_structrue2,0) #行压缩成
x_structrue4_avg_case = np.mean(x_IUFNO_structrue4,0) #行压缩成一行
y_structrue4_avg_case = np.mean(y_IUFNO_structrue4,0) #行压缩成
x_vort_PDFs_avg_case = np.mean(x_IUFNO_vort_PDFs,0) #行压缩成一行
y_vort_PDFs_avg_case = np.mean(y_IUFNO_vort_PDFs,0) #行压缩成
x_vort_statistics_avg_case = np.mean(x_IUFNO_vort_statistics,0) #行压缩成一行
y_vort_statistics_avg_case = np.mean(y_IUFNO_vort_statistics,0) #行压缩成
# 拼接操作
avg_IUFNO_urms_10case=np.dstack((x_urms_avg_case,y_urms_avg_case)).squeeze() #拼接
avg_IUFNO_wrms_10case=np.dstack((x_wrms_avg_case,y_wrms_avg_case)).squeeze() #拼接
avg_IUFNO_dissipation_10case=np.dstack((x_dissipation_avg_case,y_dissipation_avg_case)).squeeze() #拼接
avg_IUFNO_Et_10case=np.dstack((x_Et_avg_case,y_Et_avg_case)).squeeze() #拼接
avg_IUFNO_inc1_PDFs_10case=np.dstack((x_inc1_PDFs_avg_case,y_inc1_PDFs_avg_case)).squeeze() #拼接
avg_IUFNO_spectrum_10case=np.dstack((x_spe_avg_case,y_spe_avg_case)).squeeze() #拼接
avg_IUFNO_structrue2_10case=np.dstack((x_structrue2_avg_case,y_structrue2_avg_case)).squeeze() #拼接
avg_IUFNO_structrue4_10case=np.dstack((x_structrue4_avg_case,y_structrue4_avg_case)).squeeze() #拼接
avg_IUFNO_vort_PDFs_10case=np.dstack((x_vort_PDFs_avg_case,y_vort_PDFs_avg_case)).squeeze() #拼接
avg_IUFNO_vort_statistics_10case=np.dstack((x_vort_statistics_avg_case,y_vort_statistics_avg_case)).squeeze() #拼接
#导出均值

np.savetxt('./AVG/IUFNO_11ep_mag0.1/N{}/avg_IUFNO_{}case_urms.dat'.format(case_number,case_number),avg_IUFNO_urms_10case, fmt="%16.7f")
np.savetxt('./AVG/IUFNO_11ep_mag0.1/N{}/avg_IUFNO_{}case_wrms.dat'.format(case_number,case_number),avg_IUFNO_wrms_10case, fmt="%16.7f")
np.savetxt('./AVG/IUFNO_11ep_mag0.1/N{}/avg_IUFNO_{}case_dissipation.dat'.format(case_number,case_number),avg_IUFNO_dissipation_10case, fmt="%16.7f")
np.savetxt('./AVG/IUFNO_11ep_mag0.1/N{}/avg_IUFNO_{}case_Ek_t.dat'.format(case_number,case_number),avg_IUFNO_Et_10case, fmt="%16.7f")
np.savetxt('./AVG/IUFNO_11ep_mag0.1/N{}/avg_IUFNO_{}case_inc1_PDFs.dat'.format(case_number,case_number),avg_IUFNO_inc1_PDFs_10case, fmt="%16.7f")
np.savetxt('./AVG/IUFNO_11ep_mag0.1/N{}/avg_IUFNO_{}case_vel_spec.dat'.format(case_number,case_number),avg_IUFNO_spectrum_10case, fmt="%16.7f")
np.savetxt('./AVG/IUFNO_11ep_mag0.1/N{}/avg_IUFNO_{}case_structrue2.dat'.format(case_number,case_number),avg_IUFNO_structrue2_10case, fmt="%16.7f")
np.savetxt('./AVG/IUFNO_11ep_mag0.1/N{}/avg_IUFNO_{}case_structrue4.dat'.format(case_number,case_number),avg_IUFNO_structrue4_10case, fmt="%16.7f")
np.savetxt('./AVG/IUFNO_11ep_mag0.1/N{}/avg_IUFNO_{}case_vort_PDFs.dat'.format(case_number,case_number),avg_IUFNO_vort_PDFs_10case, fmt="%16.7f")
np.savetxt('./AVG/IUFNO_11ep_mag0.1/N{}/avg_IUFNO_{}case_vort_statistics.dat'.format(case_number,case_number),avg_IUFNO_vort_statistics_10case, fmt="%16.7f")
'''
np.savetxt('./AVG/IUFNO_11ep_mag0.1/{}case/avg_IUFNO_{}case_urms.dat'.format(case_number,case_number),avg_IUFNO_urms_10case, fmt="%16.7f")
np.savetxt('./AVG/IUFNO_11ep_mag0.1/{}case/avg_IUFNO_{}case_wrms.dat'.format(case_number,case_number),avg_IUFNO_wrms_10case, fmt="%16.7f")
np.savetxt('./AVG/IUFNO_11ep_mag0.1/{}case/avg_IUFNO_{}case_dissipation.dat'.format(case_number,case_number),avg_IUFNO_dissipation_10case, fmt="%16.7f")
np.savetxt('./AVG/IUFNO_11ep_mag0.1/{}case/avg_IUFNO_{}case_Ek_t.dat'.format(case_number,case_number),avg_IUFNO_Et_10case, fmt="%16.7f")
np.savetxt('./AVG/IUFNO_11ep_mag0.1/{}case/avg_IUFNO_{}case_inc1_PDFs.dat'.format(case_number,case_number),avg_IUFNO_inc1_PDFs_10case, fmt="%16.7f")
np.savetxt('./AVG/IUFNO_11ep_mag0.1/{}case/avg_IUFNO_{}case_vel_spec.dat'.format(case_number,case_number),avg_IUFNO_spectrum_10case, fmt="%16.7f")
np.savetxt('./AVG/IUFNO_11ep_mag0.1/{}case/avg_IUFNO_{}case_structrue2.dat'.format(case_number,case_number),avg_IUFNO_structrue2_10case, fmt="%16.7f")
np.savetxt('./AVG/IUFNO_11ep_mag0.1/{}case/avg_IUFNO_{}case_structrue4.dat'.format(case_number,case_number),avg_IUFNO_structrue4_10case, fmt="%16.7f")
np.savetxt('./AVG/IUFNO_11ep_mag0.1/{}case/avg_IUFNO_{}case_vort_PDFs.dat'.format(case_number,case_number),avg_IUFNO_vort_PDFs_10case, fmt="%16.7f")
np.savetxt('./AVG/IUFNO_11ep_mag0.1/{}case/avg_IUFNO_{}case_vort_statistics.dat'.format(case_number,case_number),avg_IUFNO_vort_statistics_10case, fmt="%16.7f")
'''
#======================================================================PINO
print("IUFNO_11ep_mag0.5 getting dat!")
x_IUFNO_dissipation=[]
y_IUFNO_dissipation=[]
x_IUFNO_Et=[]
y_IUFNO_Et=[]
x_IUFNO_inc1_PDFs=[]
y_IUFNO_inc1_PDFs=[]
x_IUFNO_velspectrum=[]
y_IUFNO_velspectrum=[]
x_IUFNO_structrue2 = []
y_IUFNO_structrue2 = []
x_IUFNO_structrue4 = []
y_IUFNO_structrue4 = []
x_IUFNO_urms = []
y_IUFNO_urms = []
x_IUFNO_wrms = []
y_IUFNO_wrms = []
x_IUFNO_vort_PDFs = []
y_IUFNO_vort_PDFs = []
x_IUFNO_vort_statistics = []
y_IUFNO_vort_statistics = []
for case_n in range(case_number-1,case_number):
    # print(case_n)
    # 载入后处理文件，包括速度参数，PDFs，能谱，结构函数
    IUFNO_vel_parameter= np.loadtxt('./case{}/Result_LES32_IUFNO_11ep_gap200_mag0.5/post_result/vel_parameter.dat'.format(case_n+1),dtype=float, comments=['step'])
    IUFNO_ic1_PDFs = np.loadtxt('./case{}/Result_LES32_IUFNO_11ep_gap200_mag0.5/post_result/inc1_PDFs.dat'.format(case_n + 1), dtype=float,comments=['step'])
    IUFNO_spec = np.loadtxt('./case{}/Result_LES32_IUFNO_11ep_gap200_mag0.5/post_result/spectrum_vel.dat'.format(case_n + 1), dtype=float,comments=['variables', 'zone'])
    IUFNO_structrue2 = np.loadtxt('./case{}/Result_LES32_IUFNO_11ep_gap200_mag0.5/post_result/structure2.dat'.format(case_n + 1),dtype=float, comments=['step'])
    IUFNO_structrue4 = np.loadtxt('./case{}/Result_LES32_IUFNO_11ep_gap200_mag0.5/post_result/structure4.dat'.format(case_n + 1),dtype=float, comments=['step'])
    IUFNO_vort_PDFs = np.loadtxt('./case{}/Result_LES32_IUFNO_11ep_gap200_mag0.5/post_result/vort_PDFs.dat'.format(case_n + 1), dtype=float,comments=['variables', 'zone'])
    IUFNO_vort_statistics = np.loadtxt('./case{}/Result_LES32_IUFNO_11ep_gap200_mag0.5/post_result/vort_statistics.dat'.format(case_n + 1),dtype=float, comments=['step'])
    # print(VGM.shape)
    # 取出数据
    x_IUFNO_urms.append(IUFNO_vel_parameter[:,0])  # 只取出第一列数据
    y_IUFNO_urms.append(IUFNO_vel_parameter[:,3]) #只取出第二列数据
    x_IUFNO_wrms.append(IUFNO_vel_parameter[:,0])  # 只取出第一列数据
    y_IUFNO_wrms.append(IUFNO_vel_parameter[:,7]) #只取出第二列数据
    x_IUFNO_dissipation.append(IUFNO_vel_parameter[:,0])  # 只取出第一列数据
    y_IUFNO_dissipation.append(IUFNO_vel_parameter[:,8]) #只取出第二列数据
    x_IUFNO_Et.append(IUFNO_vel_parameter[:,0])  # 只取出第一列数据
    y_IUFNO_Et.append(IUFNO_vel_parameter[:,6]) #只取出第二列数据
    x_IUFNO_inc1_PDFs.append(IUFNO_ic1_PDFs[:,0])  # 只取出第一列数据
    y_IUFNO_inc1_PDFs.append(IUFNO_ic1_PDFs[:,1]) #只取出第二列数据
    x_IUFNO_velspectrum.append(IUFNO_spec[:,0])  # 只取出第一列数据
    y_IUFNO_velspectrum.append(IUFNO_spec[:,1]) #只取出第二列数据
    x_IUFNO_structrue2.append(IUFNO_structrue2[:,0])  # 只取出第一列数据
    y_IUFNO_structrue2.append(IUFNO_structrue2[:,1]) #只取出第二列数据
    x_IUFNO_structrue4.append(IUFNO_structrue4[:,0])  # 只取出第一列数据
    y_IUFNO_structrue4.append(IUFNO_structrue4[:,1]) #只取出第二列数据
    x_IUFNO_vort_PDFs.append(IUFNO_vort_PDFs[:,0])  # 只取出第一列数据
    y_IUFNO_vort_PDFs.append(IUFNO_vort_PDFs[:,1]) #只取出第二列数据
    x_IUFNO_vort_statistics.append(IUFNO_vort_statistics[:,0])  # 只取出第一列数据
    y_IUFNO_vort_statistics.append(IUFNO_vort_statistics[:,5]) #只取出第二列数据
# 转化为数组
x_IUFNO_urms_arr = np.asarray(x_IUFNO_urms) #列表转数组
y_IUFNO_urms_arr = np.asarray(y_IUFNO_urms) #列表转数组
x_IUFNO_wrms_arr = np.asarray(x_IUFNO_wrms) #列表转数组
y_IUFNO_wrms_arr = np.asarray(y_IUFNO_wrms) #列表转数组
x_IUFNO_dissipation_arr = np.asarray(x_IUFNO_dissipation) #列表转数组
y_IUFNO_dissipation_arr = np.asarray(y_IUFNO_dissipation) #列表转数组
x_IUFNO_Et_arr = np.asarray(x_IUFNO_Et) #列表转数组
y_IUFNO_Et_arr = np.asarray(y_IUFNO_Et) #列表转数组
x_IUFNO_inc1_PDFs_arr = np.asarray(x_IUFNO_inc1_PDFs) #列表转数组
y_IUFNO_inc1_PDFs_arr = np.asarray(y_IUFNO_inc1_PDFs) #列表转数组
x_IUFNO_spe_arr = np.asarray(x_IUFNO_velspectrum) #列表转数组
y_IUFNO_spe_arr = np.asarray(y_IUFNO_velspectrum) #列表转数组
x_IUFNO_structrue2 = np.asarray(x_IUFNO_structrue2) #列表转数组
y_IUFNO_structrue2 = np.asarray(y_IUFNO_structrue2) #列表转数组
x_IUFNO_structrue4 = np.asarray(x_IUFNO_structrue4) #列表转数组
y_IUFNO_structrue4 = np.asarray(y_IUFNO_structrue4) #列表转数组
x_IUFNO_vort_PDFs = np.asarray(x_IUFNO_vort_PDFs) #列表转数组
y_IUFNO_vort_PDFs = np.asarray(y_IUFNO_vort_PDFs) #列表转数组
x_IUFNO_vort_statistics = np.asarray(x_IUFNO_vort_statistics) #列表转数组
y_IUFNO_vort_statistics = np.asarray(y_IUFNO_vort_statistics) #列表转数组
# 取均值
x_urms_avg_case = np.mean(x_IUFNO_urms_arr,0) #行压缩成一行
y_urms_avg_case = np.mean(y_IUFNO_urms_arr,0) #行压缩成一行
x_wrms_avg_case = np.mean(x_IUFNO_wrms_arr,0) #行压缩成一行
y_wrms_avg_case = np.mean(y_IUFNO_wrms_arr,0) #行压缩成一行
x_dissipation_avg_case = np.mean(x_IUFNO_dissipation_arr,0) #行压缩成一行
y_dissipation_avg_case = np.mean(y_IUFNO_dissipation_arr,0) #行压缩成一行
x_Et_avg_case = np.mean(x_IUFNO_Et_arr,0) #行压缩成一行
y_Et_avg_case = np.mean(y_IUFNO_Et_arr,0) #行压缩成一行
x_inc1_PDFs_avg_case = np.mean(x_IUFNO_inc1_PDFs_arr,0) #行压缩成一行
y_inc1_PDFs_avg_case = np.mean(y_IUFNO_inc1_PDFs_arr,0) #行压缩成一行
x_spe_avg_case = np.mean(x_IUFNO_spe_arr,0) #行压缩成一行
y_spe_avg_case = np.mean(y_IUFNO_spe_arr,0) #行压缩成一行
x_structrue2_avg_case = np.mean(x_IUFNO_structrue2,0) #行压缩成一行
y_structrue2_avg_case = np.mean(y_IUFNO_structrue2,0) #行压缩成
x_structrue4_avg_case = np.mean(x_IUFNO_structrue4,0) #行压缩成一行
y_structrue4_avg_case = np.mean(y_IUFNO_structrue4,0) #行压缩成
x_vort_PDFs_avg_case = np.mean(x_IUFNO_vort_PDFs,0) #行压缩成一行
y_vort_PDFs_avg_case = np.mean(y_IUFNO_vort_PDFs,0) #行压缩成
x_vort_statistics_avg_case = np.mean(x_IUFNO_vort_statistics,0) #行压缩成一行
y_vort_statistics_avg_case = np.mean(y_IUFNO_vort_statistics,0) #行压缩成
# 拼接操作
avg_IUFNO_urms_10case=np.dstack((x_urms_avg_case,y_urms_avg_case)).squeeze() #拼接
avg_IUFNO_wrms_10case=np.dstack((x_wrms_avg_case,y_wrms_avg_case)).squeeze() #拼接
avg_IUFNO_dissipation_10case=np.dstack((x_dissipation_avg_case,y_dissipation_avg_case)).squeeze() #拼接
avg_IUFNO_Et_10case=np.dstack((x_Et_avg_case,y_Et_avg_case)).squeeze() #拼接
avg_IUFNO_inc1_PDFs_10case=np.dstack((x_inc1_PDFs_avg_case,y_inc1_PDFs_avg_case)).squeeze() #拼接
avg_IUFNO_spectrum_10case=np.dstack((x_spe_avg_case,y_spe_avg_case)).squeeze() #拼接
avg_IUFNO_structrue2_10case=np.dstack((x_structrue2_avg_case,y_structrue2_avg_case)).squeeze() #拼接
avg_IUFNO_structrue4_10case=np.dstack((x_structrue4_avg_case,y_structrue4_avg_case)).squeeze() #拼接
avg_IUFNO_vort_PDFs_10case=np.dstack((x_vort_PDFs_avg_case,y_vort_PDFs_avg_case)).squeeze() #拼接
avg_IUFNO_vort_statistics_10case=np.dstack((x_vort_statistics_avg_case,y_vort_statistics_avg_case)).squeeze() #拼接
#导出均值

np.savetxt('./AVG/IUFNO_11ep_mag0.5/N{}/avg_IUFNO_{}case_urms.dat'.format(case_number,case_number),avg_IUFNO_urms_10case, fmt="%16.7f")
np.savetxt('./AVG/IUFNO_11ep_mag0.5/N{}/avg_IUFNO_{}case_wrms.dat'.format(case_number,case_number),avg_IUFNO_wrms_10case, fmt="%16.7f")
np.savetxt('./AVG/IUFNO_11ep_mag0.5/N{}/avg_IUFNO_{}case_dissipation.dat'.format(case_number,case_number),avg_IUFNO_dissipation_10case, fmt="%16.7f")
np.savetxt('./AVG/IUFNO_11ep_mag0.5/N{}/avg_IUFNO_{}case_Ek_t.dat'.format(case_number,case_number),avg_IUFNO_Et_10case, fmt="%16.7f")
np.savetxt('./AVG/IUFNO_11ep_mag0.5/N{}/avg_IUFNO_{}case_inc1_PDFs.dat'.format(case_number,case_number),avg_IUFNO_inc1_PDFs_10case, fmt="%16.7f")
np.savetxt('./AVG/IUFNO_11ep_mag0.5/N{}/avg_IUFNO_{}case_vel_spec.dat'.format(case_number,case_number),avg_IUFNO_spectrum_10case, fmt="%16.7f")
np.savetxt('./AVG/IUFNO_11ep_mag0.5/N{}/avg_IUFNO_{}case_structrue2.dat'.format(case_number,case_number),avg_IUFNO_structrue2_10case, fmt="%16.7f")
np.savetxt('./AVG/IUFNO_11ep_mag0.5/N{}/avg_IUFNO_{}case_structrue4.dat'.format(case_number,case_number),avg_IUFNO_structrue4_10case, fmt="%16.7f")
np.savetxt('./AVG/IUFNO_11ep_mag0.5/N{}/avg_IUFNO_{}case_vort_PDFs.dat'.format(case_number,case_number),avg_IUFNO_vort_PDFs_10case, fmt="%16.7f")
np.savetxt('./AVG/IUFNO_11ep_mag0.5/N{}/avg_IUFNO_{}case_vort_statistics.dat'.format(case_number,case_number),avg_IUFNO_vort_statistics_10case, fmt="%16.7f")
'''
np.savetxt('./AVG/IUFNO_11ep_mag0.5/{}case/avg_IUFNO_{}case_urms.dat'.format(case_number,case_number),avg_IUFNO_urms_10case, fmt="%16.7f")
np.savetxt('./AVG/IUFNO_11ep_mag0.5/{}case/avg_IUFNO_{}case_wrms.dat'.format(case_number,case_number),avg_IUFNO_wrms_10case, fmt="%16.7f")
np.savetxt('./AVG/IUFNO_11ep_mag0.5/{}case/avg_IUFNO_{}case_dissipation.dat'.format(case_number,case_number),avg_IUFNO_dissipation_10case, fmt="%16.7f")
np.savetxt('./AVG/IUFNO_11ep_mag0.5/{}case/avg_IUFNO_{}case_Ek_t.dat'.format(case_number,case_number),avg_IUFNO_Et_10case, fmt="%16.7f")
np.savetxt('./AVG/IUFNO_11ep_mag0.5/{}case/avg_IUFNO_{}case_inc1_PDFs.dat'.format(case_number,case_number),avg_IUFNO_inc1_PDFs_10case, fmt="%16.7f")
np.savetxt('./AVG/IUFNO_11ep_mag0.5/{}case/avg_IUFNO_{}case_vel_spec.dat'.format(case_number,case_number),avg_IUFNO_spectrum_10case, fmt="%16.7f")
np.savetxt('./AVG/IUFNO_11ep_mag0.5/{}case/avg_IUFNO_{}case_structrue2.dat'.format(case_number,case_number),avg_IUFNO_structrue2_10case, fmt="%16.7f")
np.savetxt('./AVG/IUFNO_11ep_mag0.5/{}case/avg_IUFNO_{}case_structrue4.dat'.format(case_number,case_number),avg_IUFNO_structrue4_10case, fmt="%16.7f")
np.savetxt('./AVG/IUFNO_11ep_mag0.5/{}case/avg_IUFNO_{}case_vort_PDFs.dat'.format(case_number,case_number),avg_IUFNO_vort_PDFs_10case, fmt="%16.7f")
np.savetxt('./AVG/IUFNO_11ep_mag0.5/{}case/avg_IUFNO_{}case_vort_statistics.dat'.format(case_number,case_number),avg_IUFNO_vort_statistics_10case, fmt="%16.7f")
'''

#==========================================================================FNO
print("IUFNO_40ep getting dat!")
x_IUFNO_dissipation=[]
y_IUFNO_dissipation=[]
x_IUFNO_Et=[]
y_IUFNO_Et=[]
x_IUFNO_inc1_PDFs=[]
y_IUFNO_inc1_PDFs=[]
x_IUFNO_velspectrum=[]
y_IUFNO_velspectrum=[]
x_IUFNO_structrue2 = []
y_IUFNO_structrue2 = []
x_IUFNO_structrue4 = []
y_IUFNO_structrue4 = []
x_IUFNO_urms = []
y_IUFNO_urms = []
x_IUFNO_wrms = []
y_IUFNO_wrms = []
x_IUFNO_vort_PDFs = []
y_IUFNO_vort_PDFs = []
x_IUFNO_vort_statistics = []
y_IUFNO_vort_statistics = []
for case_n in range(case_number-1,case_number):
    # print(case_n)
    # 载入后处理文件，包括速度参数，PDFs，能谱，结构函数
    IUFNO_vel_parameter= np.loadtxt('./case{}/Result_LES32_IUFNO_40ep_gap200/post_result/vel_parameter.dat'.format(case_n+1),dtype=float, comments=['step'])
    IUFNO_ic1_PDFs = np.loadtxt('./case{}/Result_LES32_IUFNO_40ep_gap200/post_result/inc1_PDFs.dat'.format(case_n + 1), dtype=float,comments=['step'])
    IUFNO_spec = np.loadtxt('./case{}/Result_LES32_IUFNO_40ep_gap200/post_result/spectrum_vel.dat'.format(case_n + 1), dtype=float,comments=['variables', 'zone'])
    IUFNO_structrue2 = np.loadtxt('./case{}/Result_LES32_IUFNO_40ep_gap200/post_result/structure2.dat'.format(case_n + 1),dtype=float, comments=['step'])
    IUFNO_structrue4 = np.loadtxt('./case{}/Result_LES32_IUFNO_40ep_gap200/post_result/structure4.dat'.format(case_n + 1),dtype=float, comments=['step'])
    IUFNO_vort_PDFs = np.loadtxt('./case{}/Result_LES32_IUFNO_40ep_gap200/post_result/vort_PDFs.dat'.format(case_n + 1), dtype=float,comments=['variables', 'zone'])
    IUFNO_vort_statistics = np.loadtxt('./case{}/Result_LES32_IUFNO_40ep_gap200/post_result/vort_statistics.dat'.format(case_n + 1),dtype=float, comments=['step'])
    # print(VGM.shape)
    # 取出数据
    x_IUFNO_urms.append(IUFNO_vel_parameter[:,0])  # 只取出第一列数据
    y_IUFNO_urms.append(IUFNO_vel_parameter[:,3]) #只取出第二列数据
    x_IUFNO_wrms.append(IUFNO_vel_parameter[:,0])  # 只取出第一列数据
    y_IUFNO_wrms.append(IUFNO_vel_parameter[:,7]) #只取出第二列数据
    x_IUFNO_dissipation.append(IUFNO_vel_parameter[:,0])  # 只取出第一列数据
    y_IUFNO_dissipation.append(IUFNO_vel_parameter[:,8]) #只取出第二列数据
    x_IUFNO_Et.append(IUFNO_vel_parameter[:,0])  # 只取出第一列数据
    y_IUFNO_Et.append(IUFNO_vel_parameter[:,6]) #只取出第二列数据
    x_IUFNO_inc1_PDFs.append(IUFNO_ic1_PDFs[:,0])  # 只取出第一列数据
    y_IUFNO_inc1_PDFs.append(IUFNO_ic1_PDFs[:,1]) #只取出第二列数据
    x_IUFNO_velspectrum.append(IUFNO_spec[:,0])  # 只取出第一列数据
    y_IUFNO_velspectrum.append(IUFNO_spec[:,1]) #只取出第二列数据
    x_IUFNO_structrue2.append(IUFNO_structrue2[:,0])  # 只取出第一列数据
    y_IUFNO_structrue2.append(IUFNO_structrue2[:,1]) #只取出第二列数据
    x_IUFNO_structrue4.append(IUFNO_structrue4[:,0])  # 只取出第一列数据
    y_IUFNO_structrue4.append(IUFNO_structrue4[:,1]) #只取出第二列数据
    x_IUFNO_vort_PDFs.append(IUFNO_vort_PDFs[:,0])  # 只取出第一列数据
    y_IUFNO_vort_PDFs.append(IUFNO_vort_PDFs[:,1]) #只取出第二列数据
    x_IUFNO_vort_statistics.append(IUFNO_vort_statistics[:,0])  # 只取出第一列数据
    y_IUFNO_vort_statistics.append(IUFNO_vort_statistics[:,5]) #只取出第二列数据
# 转化为数组
x_IUFNO_urms_arr = np.asarray(x_IUFNO_urms) #列表转数组
y_IUFNO_urms_arr = np.asarray(y_IUFNO_urms) #列表转数组
x_IUFNO_wrms_arr = np.asarray(x_IUFNO_wrms) #列表转数组
y_IUFNO_wrms_arr = np.asarray(y_IUFNO_wrms) #列表转数组
x_IUFNO_dissipation_arr = np.asarray(x_IUFNO_dissipation) #列表转数组
y_IUFNO_dissipation_arr = np.asarray(y_IUFNO_dissipation) #列表转数组
x_IUFNO_Et_arr = np.asarray(x_IUFNO_Et) #列表转数组
y_IUFNO_Et_arr = np.asarray(y_IUFNO_Et) #列表转数组
x_IUFNO_inc1_PDFs_arr = np.asarray(x_IUFNO_inc1_PDFs) #列表转数组
y_IUFNO_inc1_PDFs_arr = np.asarray(y_IUFNO_inc1_PDFs) #列表转数组
x_IUFNO_spe_arr = np.asarray(x_IUFNO_velspectrum) #列表转数组
y_IUFNO_spe_arr = np.asarray(y_IUFNO_velspectrum) #列表转数组
x_IUFNO_structrue2 = np.asarray(x_IUFNO_structrue2) #列表转数组
y_IUFNO_structrue2 = np.asarray(y_IUFNO_structrue2) #列表转数组
x_IUFNO_structrue4 = np.asarray(x_IUFNO_structrue4) #列表转数组
y_IUFNO_structrue4 = np.asarray(y_IUFNO_structrue4) #列表转数组
x_IUFNO_vort_PDFs = np.asarray(x_IUFNO_vort_PDFs) #列表转数组
y_IUFNO_vort_PDFs = np.asarray(y_IUFNO_vort_PDFs) #列表转数组
x_IUFNO_vort_statistics = np.asarray(x_IUFNO_vort_statistics) #列表转数组
y_IUFNO_vort_statistics = np.asarray(y_IUFNO_vort_statistics) #列表转数组
# 取均值
x_urms_avg_case = np.mean(x_IUFNO_urms_arr,0) #行压缩成一行
y_urms_avg_case = np.mean(y_IUFNO_urms_arr,0) #行压缩成一行
x_wrms_avg_case = np.mean(x_IUFNO_wrms_arr,0) #行压缩成一行
y_wrms_avg_case = np.mean(y_IUFNO_wrms_arr,0) #行压缩成一行
x_dissipation_avg_case = np.mean(x_IUFNO_dissipation_arr,0) #行压缩成一行
y_dissipation_avg_case = np.mean(y_IUFNO_dissipation_arr,0) #行压缩成一行
x_Et_avg_case = np.mean(x_IUFNO_Et_arr,0) #行压缩成一行
y_Et_avg_case = np.mean(y_IUFNO_Et_arr,0) #行压缩成一行
x_inc1_PDFs_avg_case = np.mean(x_IUFNO_inc1_PDFs_arr,0) #行压缩成一行
y_inc1_PDFs_avg_case = np.mean(y_IUFNO_inc1_PDFs_arr,0) #行压缩成一行
x_spe_avg_case = np.mean(x_IUFNO_spe_arr,0) #行压缩成一行
y_spe_avg_case = np.mean(y_IUFNO_spe_arr,0) #行压缩成一行
x_structrue2_avg_case = np.mean(x_IUFNO_structrue2,0) #行压缩成一行
y_structrue2_avg_case = np.mean(y_IUFNO_structrue2,0) #行压缩成
x_structrue4_avg_case = np.mean(x_IUFNO_structrue4,0) #行压缩成一行
y_structrue4_avg_case = np.mean(y_IUFNO_structrue4,0) #行压缩成
x_vort_PDFs_avg_case = np.mean(x_IUFNO_vort_PDFs,0) #行压缩成一行
y_vort_PDFs_avg_case = np.mean(y_IUFNO_vort_PDFs,0) #行压缩成
x_vort_statistics_avg_case = np.mean(x_IUFNO_vort_statistics,0) #行压缩成一行
y_vort_statistics_avg_case = np.mean(y_IUFNO_vort_statistics,0) #行压缩成
# 拼接操作
avg_IUFNO_urms_10case=np.dstack((x_urms_avg_case,y_urms_avg_case)).squeeze() #拼接
avg_IUFNO_wrms_10case=np.dstack((x_wrms_avg_case,y_wrms_avg_case)).squeeze() #拼接
avg_IUFNO_dissipation_10case=np.dstack((x_dissipation_avg_case,y_dissipation_avg_case)).squeeze() #拼接
avg_IUFNO_Et_10case=np.dstack((x_Et_avg_case,y_Et_avg_case)).squeeze() #拼接
avg_IUFNO_inc1_PDFs_10case=np.dstack((x_inc1_PDFs_avg_case,y_inc1_PDFs_avg_case)).squeeze() #拼接
avg_IUFNO_spectrum_10case=np.dstack((x_spe_avg_case,y_spe_avg_case)).squeeze() #拼接
avg_IUFNO_structrue2_10case=np.dstack((x_structrue2_avg_case,y_structrue2_avg_case)).squeeze() #拼接
avg_IUFNO_structrue4_10case=np.dstack((x_structrue4_avg_case,y_structrue4_avg_case)).squeeze() #拼接
avg_IUFNO_vort_PDFs_10case=np.dstack((x_vort_PDFs_avg_case,y_vort_PDFs_avg_case)).squeeze() #拼接
avg_IUFNO_vort_statistics_10case=np.dstack((x_vort_statistics_avg_case,y_vort_statistics_avg_case)).squeeze() #拼接
#导出均值

np.savetxt('./AVG/IUFNO_40ep/N{}/avg_IUFNO_{}case_urms.dat'.format(case_number,case_number),avg_IUFNO_urms_10case, fmt="%16.7f")
np.savetxt('./AVG/IUFNO_40ep/N{}/avg_IUFNO_{}case_wrms.dat'.format(case_number,case_number),avg_IUFNO_wrms_10case, fmt="%16.7f")
np.savetxt('./AVG/IUFNO_40ep/N{}/avg_IUFNO_{}case_dissipation.dat'.format(case_number,case_number),avg_IUFNO_dissipation_10case, fmt="%16.7f")
np.savetxt('./AVG/IUFNO_40ep/N{}/avg_IUFNO_{}case_Ek_t.dat'.format(case_number,case_number),avg_IUFNO_Et_10case, fmt="%16.7f")
np.savetxt('./AVG/IUFNO_40ep/N{}/avg_IUFNO_{}case_inc1_PDFs.dat'.format(case_number,case_number),avg_IUFNO_inc1_PDFs_10case, fmt="%16.7f")
np.savetxt('./AVG/IUFNO_40ep/N{}/avg_IUFNO_{}case_vel_spec.dat'.format(case_number,case_number),avg_IUFNO_spectrum_10case, fmt="%16.7f")
np.savetxt('./AVG/IUFNO_40ep/N{}/avg_IUFNO_{}case_structrue2.dat'.format(case_number,case_number),avg_IUFNO_structrue2_10case, fmt="%16.7f")
np.savetxt('./AVG/IUFNO_40ep/N{}/avg_IUFNO_{}case_structrue4.dat'.format(case_number,case_number),avg_IUFNO_structrue4_10case, fmt="%16.7f")
np.savetxt('./AVG/IUFNO_40ep/N{}/avg_IUFNO_{}case_vort_PDFs.dat'.format(case_number,case_number),avg_IUFNO_vort_PDFs_10case, fmt="%16.7f")
np.savetxt('./AVG/IUFNO_40ep/N{}/avg_IUFNO_{}case_vort_statistics.dat'.format(case_number,case_number),avg_IUFNO_vort_statistics_10case, fmt="%16.7f")
'''
np.savetxt('./AVG/IUFNO_40ep/{}case/avg_IUFNO_{}case_urms.dat'.format(case_number,case_number),avg_IUFNO_urms_10case, fmt="%16.7f")
np.savetxt('./AVG/IUFNO_40ep/{}case/avg_IUFNO_{}case_wrms.dat'.format(case_number,case_number),avg_IUFNO_wrms_10case, fmt="%16.7f")
np.savetxt('./AVG/IUFNO_40ep/{}case/avg_IUFNO_{}case_dissipation.dat'.format(case_number,case_number),avg_IUFNO_dissipation_10case, fmt="%16.7f")
np.savetxt('./AVG/IUFNO_40ep/{}case/avg_IUFNO_{}case_Ek_t.dat'.format(case_number,case_number),avg_IUFNO_Et_10case, fmt="%16.7f")
np.savetxt('./AVG/IUFNO_40ep/{}case/avg_IUFNO_{}case_inc1_PDFs.dat'.format(case_number,case_number),avg_IUFNO_inc1_PDFs_10case, fmt="%16.7f")
np.savetxt('./AVG/IUFNO_40ep/{}case/avg_IUFNO_{}case_vel_spec.dat'.format(case_number,case_number),avg_IUFNO_spectrum_10case, fmt="%16.7f")
np.savetxt('./AVG/IUFNO_40ep/{}case/avg_IUFNO_{}case_structrue2.dat'.format(case_number,case_number),avg_IUFNO_structrue2_10case, fmt="%16.7f")
np.savetxt('./AVG/IUFNO_40ep/{}case/avg_IUFNO_{}case_structrue4.dat'.format(case_number,case_number),avg_IUFNO_structrue4_10case, fmt="%16.7f")
np.savetxt('./AVG/IUFNO_40ep/{}case/avg_IUFNO_{}case_vort_PDFs.dat'.format(case_number,case_number),avg_IUFNO_vort_PDFs_10case, fmt="%16.7f")
np.savetxt('./AVG/IUFNO_40ep/{}case/avg_IUFNO_{}case_vort_statistics.dat'.format(case_number,case_number),avg_IUFNO_vort_statistics_10case, fmt="%16.7f")
'''
#==========================================================================FNO
print("IUFNO_40ep_mag0.1 getting dat!")
x_IUFNO_dissipation=[]
y_IUFNO_dissipation=[]
x_IUFNO_Et=[]
y_IUFNO_Et=[]
x_IUFNO_inc1_PDFs=[]
y_IUFNO_inc1_PDFs=[]
x_IUFNO_velspectrum=[]
y_IUFNO_velspectrum=[]
x_IUFNO_structrue2 = []
y_IUFNO_structrue2 = []
x_IUFNO_structrue4 = []
y_IUFNO_structrue4 = []
x_IUFNO_urms = []
y_IUFNO_urms = []
x_IUFNO_wrms = []
y_IUFNO_wrms = []
x_IUFNO_vort_PDFs = []
y_IUFNO_vort_PDFs = []
x_IUFNO_vort_statistics = []
y_IUFNO_vort_statistics = []
for case_n in range(case_number-1,case_number):
    # print(case_n)
    # 载入后处理文件，包括速度参数，PDFs，能谱，结构函数
    IUFNO_vel_parameter= np.loadtxt('./case{}/Result_LES32_IUFNO_40ep_gap200_mag0.1/post_result/vel_parameter.dat'.format(case_n+1),dtype=float, comments=['step'])
    IUFNO_ic1_PDFs = np.loadtxt('./case{}/Result_LES32_IUFNO_40ep_gap200_mag0.1/post_result/inc1_PDFs.dat'.format(case_n + 1), dtype=float,comments=['step'])
    IUFNO_spec = np.loadtxt('./case{}/Result_LES32_IUFNO_40ep_gap200_mag0.1/post_result/spectrum_vel.dat'.format(case_n + 1), dtype=float,comments=['variables', 'zone'])
    IUFNO_structrue2 = np.loadtxt('./case{}/Result_LES32_IUFNO_40ep_gap200_mag0.1/post_result/structure2.dat'.format(case_n + 1),dtype=float, comments=['step'])
    IUFNO_structrue4 = np.loadtxt('./case{}/Result_LES32_IUFNO_40ep_gap200_mag0.1/post_result/structure4.dat'.format(case_n + 1),dtype=float, comments=['step'])
    IUFNO_vort_PDFs = np.loadtxt('./case{}/Result_LES32_IUFNO_40ep_gap200_mag0.1/post_result/vort_PDFs.dat'.format(case_n + 1), dtype=float,comments=['variables', 'zone'])
    IUFNO_vort_statistics = np.loadtxt('./case{}/Result_LES32_IUFNO_40ep_gap200_mag0.1/post_result/vort_statistics.dat'.format(case_n + 1),dtype=float, comments=['step'])
    # print(VGM.shape)
    # 取出数据
    x_IUFNO_urms.append(IUFNO_vel_parameter[:,0])  # 只取出第一列数据
    y_IUFNO_urms.append(IUFNO_vel_parameter[:,3]) #只取出第二列数据
    x_IUFNO_wrms.append(IUFNO_vel_parameter[:,0])  # 只取出第一列数据
    y_IUFNO_wrms.append(IUFNO_vel_parameter[:,7]) #只取出第二列数据
    x_IUFNO_dissipation.append(IUFNO_vel_parameter[:,0])  # 只取出第一列数据
    y_IUFNO_dissipation.append(IUFNO_vel_parameter[:,8]) #只取出第二列数据
    x_IUFNO_Et.append(IUFNO_vel_parameter[:,0])  # 只取出第一列数据
    y_IUFNO_Et.append(IUFNO_vel_parameter[:,6]) #只取出第二列数据
    x_IUFNO_inc1_PDFs.append(IUFNO_ic1_PDFs[:,0])  # 只取出第一列数据
    y_IUFNO_inc1_PDFs.append(IUFNO_ic1_PDFs[:,1]) #只取出第二列数据
    x_IUFNO_velspectrum.append(IUFNO_spec[:,0])  # 只取出第一列数据
    y_IUFNO_velspectrum.append(IUFNO_spec[:,1]) #只取出第二列数据
    x_IUFNO_structrue2.append(IUFNO_structrue2[:,0])  # 只取出第一列数据
    y_IUFNO_structrue2.append(IUFNO_structrue2[:,1]) #只取出第二列数据
    x_IUFNO_structrue4.append(IUFNO_structrue4[:,0])  # 只取出第一列数据
    y_IUFNO_structrue4.append(IUFNO_structrue4[:,1]) #只取出第二列数据
    x_IUFNO_vort_PDFs.append(IUFNO_vort_PDFs[:,0])  # 只取出第一列数据
    y_IUFNO_vort_PDFs.append(IUFNO_vort_PDFs[:,1]) #只取出第二列数据
    x_IUFNO_vort_statistics.append(IUFNO_vort_statistics[:,0])  # 只取出第一列数据
    y_IUFNO_vort_statistics.append(IUFNO_vort_statistics[:,5]) #只取出第二列数据
# 转化为数组
x_IUFNO_urms_arr = np.asarray(x_IUFNO_urms) #列表转数组
y_IUFNO_urms_arr = np.asarray(y_IUFNO_urms) #列表转数组
x_IUFNO_wrms_arr = np.asarray(x_IUFNO_wrms) #列表转数组
y_IUFNO_wrms_arr = np.asarray(y_IUFNO_wrms) #列表转数组
x_IUFNO_dissipation_arr = np.asarray(x_IUFNO_dissipation) #列表转数组
y_IUFNO_dissipation_arr = np.asarray(y_IUFNO_dissipation) #列表转数组
x_IUFNO_Et_arr = np.asarray(x_IUFNO_Et) #列表转数组
y_IUFNO_Et_arr = np.asarray(y_IUFNO_Et) #列表转数组
x_IUFNO_inc1_PDFs_arr = np.asarray(x_IUFNO_inc1_PDFs) #列表转数组
y_IUFNO_inc1_PDFs_arr = np.asarray(y_IUFNO_inc1_PDFs) #列表转数组
x_IUFNO_spe_arr = np.asarray(x_IUFNO_velspectrum) #列表转数组
y_IUFNO_spe_arr = np.asarray(y_IUFNO_velspectrum) #列表转数组
x_IUFNO_structrue2 = np.asarray(x_IUFNO_structrue2) #列表转数组
y_IUFNO_structrue2 = np.asarray(y_IUFNO_structrue2) #列表转数组
x_IUFNO_structrue4 = np.asarray(x_IUFNO_structrue4) #列表转数组
y_IUFNO_structrue4 = np.asarray(y_IUFNO_structrue4) #列表转数组
x_IUFNO_vort_PDFs = np.asarray(x_IUFNO_vort_PDFs) #列表转数组
y_IUFNO_vort_PDFs = np.asarray(y_IUFNO_vort_PDFs) #列表转数组
x_IUFNO_vort_statistics = np.asarray(x_IUFNO_vort_statistics) #列表转数组
y_IUFNO_vort_statistics = np.asarray(y_IUFNO_vort_statistics) #列表转数组
# 取均值
x_urms_avg_case = np.mean(x_IUFNO_urms_arr,0) #行压缩成一行
y_urms_avg_case = np.mean(y_IUFNO_urms_arr,0) #行压缩成一行
x_wrms_avg_case = np.mean(x_IUFNO_wrms_arr,0) #行压缩成一行
y_wrms_avg_case = np.mean(y_IUFNO_wrms_arr,0) #行压缩成一行
x_dissipation_avg_case = np.mean(x_IUFNO_dissipation_arr,0) #行压缩成一行
y_dissipation_avg_case = np.mean(y_IUFNO_dissipation_arr,0) #行压缩成一行
x_Et_avg_case = np.mean(x_IUFNO_Et_arr,0) #行压缩成一行
y_Et_avg_case = np.mean(y_IUFNO_Et_arr,0) #行压缩成一行
x_inc1_PDFs_avg_case = np.mean(x_IUFNO_inc1_PDFs_arr,0) #行压缩成一行
y_inc1_PDFs_avg_case = np.mean(y_IUFNO_inc1_PDFs_arr,0) #行压缩成一行
x_spe_avg_case = np.mean(x_IUFNO_spe_arr,0) #行压缩成一行
y_spe_avg_case = np.mean(y_IUFNO_spe_arr,0) #行压缩成一行
x_structrue2_avg_case = np.mean(x_IUFNO_structrue2,0) #行压缩成一行
y_structrue2_avg_case = np.mean(y_IUFNO_structrue2,0) #行压缩成
x_structrue4_avg_case = np.mean(x_IUFNO_structrue4,0) #行压缩成一行
y_structrue4_avg_case = np.mean(y_IUFNO_structrue4,0) #行压缩成
x_vort_PDFs_avg_case = np.mean(x_IUFNO_vort_PDFs,0) #行压缩成一行
y_vort_PDFs_avg_case = np.mean(y_IUFNO_vort_PDFs,0) #行压缩成
x_vort_statistics_avg_case = np.mean(x_IUFNO_vort_statistics,0) #行压缩成一行
y_vort_statistics_avg_case = np.mean(y_IUFNO_vort_statistics,0) #行压缩成
# 拼接操作
avg_IUFNO_urms_10case=np.dstack((x_urms_avg_case,y_urms_avg_case)).squeeze() #拼接
avg_IUFNO_wrms_10case=np.dstack((x_wrms_avg_case,y_wrms_avg_case)).squeeze() #拼接
avg_IUFNO_dissipation_10case=np.dstack((x_dissipation_avg_case,y_dissipation_avg_case)).squeeze() #拼接
avg_IUFNO_Et_10case=np.dstack((x_Et_avg_case,y_Et_avg_case)).squeeze() #拼接
avg_IUFNO_inc1_PDFs_10case=np.dstack((x_inc1_PDFs_avg_case,y_inc1_PDFs_avg_case)).squeeze() #拼接
avg_IUFNO_spectrum_10case=np.dstack((x_spe_avg_case,y_spe_avg_case)).squeeze() #拼接
avg_IUFNO_structrue2_10case=np.dstack((x_structrue2_avg_case,y_structrue2_avg_case)).squeeze() #拼接
avg_IUFNO_structrue4_10case=np.dstack((x_structrue4_avg_case,y_structrue4_avg_case)).squeeze() #拼接
avg_IUFNO_vort_PDFs_10case=np.dstack((x_vort_PDFs_avg_case,y_vort_PDFs_avg_case)).squeeze() #拼接
avg_IUFNO_vort_statistics_10case=np.dstack((x_vort_statistics_avg_case,y_vort_statistics_avg_case)).squeeze() #拼接
#导出均值

np.savetxt('./AVG/IUFNO_40ep_mag0.1/N{}/avg_IUFNO_{}case_urms.dat'.format(case_number,case_number),avg_IUFNO_urms_10case, fmt="%16.7f")
np.savetxt('./AVG/IUFNO_40ep_mag0.1/N{}/avg_IUFNO_{}case_wrms.dat'.format(case_number,case_number),avg_IUFNO_wrms_10case, fmt="%16.7f")
np.savetxt('./AVG/IUFNO_40ep_mag0.1/N{}/avg_IUFNO_{}case_dissipation.dat'.format(case_number,case_number),avg_IUFNO_dissipation_10case, fmt="%16.7f")
np.savetxt('./AVG/IUFNO_40ep_mag0.1/N{}/avg_IUFNO_{}case_Ek_t.dat'.format(case_number,case_number),avg_IUFNO_Et_10case, fmt="%16.7f")
np.savetxt('./AVG/IUFNO_40ep_mag0.1/N{}/avg_IUFNO_{}case_inc1_PDFs.dat'.format(case_number,case_number),avg_IUFNO_inc1_PDFs_10case, fmt="%16.7f")
np.savetxt('./AVG/IUFNO_40ep_mag0.1/N{}/avg_IUFNO_{}case_vel_spec.dat'.format(case_number,case_number),avg_IUFNO_spectrum_10case, fmt="%16.7f")
np.savetxt('./AVG/IUFNO_40ep_mag0.1/N{}/avg_IUFNO_{}case_structrue2.dat'.format(case_number,case_number),avg_IUFNO_structrue2_10case, fmt="%16.7f")
np.savetxt('./AVG/IUFNO_40ep_mag0.1/N{}/avg_IUFNO_{}case_structrue4.dat'.format(case_number,case_number),avg_IUFNO_structrue4_10case, fmt="%16.7f")
np.savetxt('./AVG/IUFNO_40ep_mag0.1/N{}/avg_IUFNO_{}case_vort_PDFs.dat'.format(case_number,case_number),avg_IUFNO_vort_PDFs_10case, fmt="%16.7f")
np.savetxt('./AVG/IUFNO_40ep_mag0.1/N{}/avg_IUFNO_{}case_vort_statistics.dat'.format(case_number,case_number),avg_IUFNO_vort_statistics_10case, fmt="%16.7f")
'''
np.savetxt('./AVG/IUFNO_40ep_mag0.1/{}case/avg_IUFNO_{}case_urms.dat'.format(case_number,case_number),avg_IUFNO_urms_10case, fmt="%16.7f")
np.savetxt('./AVG/IUFNO_40ep_mag0.1/{}case/avg_IUFNO_{}case_wrms.dat'.format(case_number,case_number),avg_IUFNO_wrms_10case, fmt="%16.7f")
np.savetxt('./AVG/IUFNO_40ep_mag0.1/{}case/avg_IUFNO_{}case_dissipation.dat'.format(case_number,case_number),avg_IUFNO_dissipation_10case, fmt="%16.7f")
np.savetxt('./AVG/IUFNO_40ep_mag0.1/{}case/avg_IUFNO_{}case_Ek_t.dat'.format(case_number,case_number),avg_IUFNO_Et_10case, fmt="%16.7f")
np.savetxt('./AVG/IUFNO_40ep_mag0.1/{}case/avg_IUFNO_{}case_inc1_PDFs.dat'.format(case_number,case_number),avg_IUFNO_inc1_PDFs_10case, fmt="%16.7f")
np.savetxt('./AVG/IUFNO_40ep_mag0.1/{}case/avg_IUFNO_{}case_vel_spec.dat'.format(case_number,case_number),avg_IUFNO_spectrum_10case, fmt="%16.7f")
np.savetxt('./AVG/IUFNO_40ep_mag0.1/{}case/avg_IUFNO_{}case_structrue2.dat'.format(case_number,case_number),avg_IUFNO_structrue2_10case, fmt="%16.7f")
np.savetxt('./AVG/IUFNO_40ep_mag0.1/{}case/avg_IUFNO_{}case_structrue4.dat'.format(case_number,case_number),avg_IUFNO_structrue4_10case, fmt="%16.7f")
np.savetxt('./AVG/IUFNO_40ep_mag0.1/{}case/avg_IUFNO_{}case_vort_PDFs.dat'.format(case_number,case_number),avg_IUFNO_vort_PDFs_10case, fmt="%16.7f")
np.savetxt('./AVG/IUFNO_40ep_mag0.1/{}case/avg_IUFNO_{}case_vort_statistics.dat'.format(case_number,case_number),avg_IUFNO_vort_statistics_10case, fmt="%16.7f")
'''
#======================================================================PINO
print("IUFNO_40ep_mag0.5 getting dat!")
x_IUFNO_dissipation=[]
y_IUFNO_dissipation=[]
x_IUFNO_Et=[]
y_IUFNO_Et=[]
x_IUFNO_inc1_PDFs=[]
y_IUFNO_inc1_PDFs=[]
x_IUFNO_velspectrum=[]
y_IUFNO_velspectrum=[]
x_IUFNO_structrue2 = []
y_IUFNO_structrue2 = []
x_IUFNO_structrue4 = []
y_IUFNO_structrue4 = []
x_IUFNO_urms = []
y_IUFNO_urms = []
x_IUFNO_wrms = []
y_IUFNO_wrms = []
x_IUFNO_vort_PDFs = []
y_IUFNO_vort_PDFs = []
x_IUFNO_vort_statistics = []
y_IUFNO_vort_statistics = []
for case_n in range(case_number-1,case_number):
    # print(case_n)
    # 载入后处理文件，包括速度参数，PDFs，能谱，结构函数
    IUFNO_vel_parameter= np.loadtxt('./case{}/Result_LES32_IUFNO_40ep_gap200_mag0.5/post_result/vel_parameter.dat'.format(case_n+1),dtype=float, comments=['step'])
    IUFNO_ic1_PDFs = np.loadtxt('./case{}/Result_LES32_IUFNO_40ep_gap200_mag0.5/post_result/inc1_PDFs.dat'.format(case_n + 1), dtype=float,comments=['step'])
    IUFNO_spec = np.loadtxt('./case{}/Result_LES32_IUFNO_40ep_gap200_mag0.5/post_result/spectrum_vel.dat'.format(case_n + 1), dtype=float,comments=['variables', 'zone'])
    IUFNO_structrue2 = np.loadtxt('./case{}/Result_LES32_IUFNO_40ep_gap200_mag0.5/post_result/structure2.dat'.format(case_n + 1),dtype=float, comments=['step'])
    IUFNO_structrue4 = np.loadtxt('./case{}/Result_LES32_IUFNO_40ep_gap200_mag0.5/post_result/structure4.dat'.format(case_n + 1),dtype=float, comments=['step'])
    IUFNO_vort_PDFs = np.loadtxt('./case{}/Result_LES32_IUFNO_40ep_gap200_mag0.5/post_result/vort_PDFs.dat'.format(case_n + 1), dtype=float,comments=['variables', 'zone'])
    IUFNO_vort_statistics = np.loadtxt('./case{}/Result_LES32_IUFNO_40ep_gap200_mag0.5/post_result/vort_statistics.dat'.format(case_n + 1),dtype=float, comments=['step'])
    # print(VGM.shape)
    # 取出数据
    x_IUFNO_urms.append(IUFNO_vel_parameter[:,0])  # 只取出第一列数据
    y_IUFNO_urms.append(IUFNO_vel_parameter[:,3]) #只取出第二列数据
    x_IUFNO_wrms.append(IUFNO_vel_parameter[:,0])  # 只取出第一列数据
    y_IUFNO_wrms.append(IUFNO_vel_parameter[:,7]) #只取出第二列数据
    x_IUFNO_dissipation.append(IUFNO_vel_parameter[:,0])  # 只取出第一列数据
    y_IUFNO_dissipation.append(IUFNO_vel_parameter[:,8]) #只取出第二列数据
    x_IUFNO_Et.append(IUFNO_vel_parameter[:,0])  # 只取出第一列数据
    y_IUFNO_Et.append(IUFNO_vel_parameter[:,6]) #只取出第二列数据
    x_IUFNO_inc1_PDFs.append(IUFNO_ic1_PDFs[:,0])  # 只取出第一列数据
    y_IUFNO_inc1_PDFs.append(IUFNO_ic1_PDFs[:,1]) #只取出第二列数据
    x_IUFNO_velspectrum.append(IUFNO_spec[:,0])  # 只取出第一列数据
    y_IUFNO_velspectrum.append(IUFNO_spec[:,1]) #只取出第二列数据
    x_IUFNO_structrue2.append(IUFNO_structrue2[:,0])  # 只取出第一列数据
    y_IUFNO_structrue2.append(IUFNO_structrue2[:,1]) #只取出第二列数据
    x_IUFNO_structrue4.append(IUFNO_structrue4[:,0])  # 只取出第一列数据
    y_IUFNO_structrue4.append(IUFNO_structrue4[:,1]) #只取出第二列数据
    x_IUFNO_vort_PDFs.append(IUFNO_vort_PDFs[:,0])  # 只取出第一列数据
    y_IUFNO_vort_PDFs.append(IUFNO_vort_PDFs[:,1]) #只取出第二列数据
    x_IUFNO_vort_statistics.append(IUFNO_vort_statistics[:,0])  # 只取出第一列数据
    y_IUFNO_vort_statistics.append(IUFNO_vort_statistics[:,5]) #只取出第二列数据
# 转化为数组
x_IUFNO_urms_arr = np.asarray(x_IUFNO_urms) #列表转数组
y_IUFNO_urms_arr = np.asarray(y_IUFNO_urms) #列表转数组
x_IUFNO_wrms_arr = np.asarray(x_IUFNO_wrms) #列表转数组
y_IUFNO_wrms_arr = np.asarray(y_IUFNO_wrms) #列表转数组
x_IUFNO_dissipation_arr = np.asarray(x_IUFNO_dissipation) #列表转数组
y_IUFNO_dissipation_arr = np.asarray(y_IUFNO_dissipation) #列表转数组
x_IUFNO_Et_arr = np.asarray(x_IUFNO_Et) #列表转数组
y_IUFNO_Et_arr = np.asarray(y_IUFNO_Et) #列表转数组
x_IUFNO_inc1_PDFs_arr = np.asarray(x_IUFNO_inc1_PDFs) #列表转数组
y_IUFNO_inc1_PDFs_arr = np.asarray(y_IUFNO_inc1_PDFs) #列表转数组
x_IUFNO_spe_arr = np.asarray(x_IUFNO_velspectrum) #列表转数组
y_IUFNO_spe_arr = np.asarray(y_IUFNO_velspectrum) #列表转数组
x_IUFNO_structrue2 = np.asarray(x_IUFNO_structrue2) #列表转数组
y_IUFNO_structrue2 = np.asarray(y_IUFNO_structrue2) #列表转数组
x_IUFNO_structrue4 = np.asarray(x_IUFNO_structrue4) #列表转数组
y_IUFNO_structrue4 = np.asarray(y_IUFNO_structrue4) #列表转数组
x_IUFNO_vort_PDFs = np.asarray(x_IUFNO_vort_PDFs) #列表转数组
y_IUFNO_vort_PDFs = np.asarray(y_IUFNO_vort_PDFs) #列表转数组
x_IUFNO_vort_statistics = np.asarray(x_IUFNO_vort_statistics) #列表转数组
y_IUFNO_vort_statistics = np.asarray(y_IUFNO_vort_statistics) #列表转数组
# 取均值
x_urms_avg_case = np.mean(x_IUFNO_urms_arr,0) #行压缩成一行
y_urms_avg_case = np.mean(y_IUFNO_urms_arr,0) #行压缩成一行
x_wrms_avg_case = np.mean(x_IUFNO_wrms_arr,0) #行压缩成一行
y_wrms_avg_case = np.mean(y_IUFNO_wrms_arr,0) #行压缩成一行
x_dissipation_avg_case = np.mean(x_IUFNO_dissipation_arr,0) #行压缩成一行
y_dissipation_avg_case = np.mean(y_IUFNO_dissipation_arr,0) #行压缩成一行
x_Et_avg_case = np.mean(x_IUFNO_Et_arr,0) #行压缩成一行
y_Et_avg_case = np.mean(y_IUFNO_Et_arr,0) #行压缩成一行
x_inc1_PDFs_avg_case = np.mean(x_IUFNO_inc1_PDFs_arr,0) #行压缩成一行
y_inc1_PDFs_avg_case = np.mean(y_IUFNO_inc1_PDFs_arr,0) #行压缩成一行
x_spe_avg_case = np.mean(x_IUFNO_spe_arr,0) #行压缩成一行
y_spe_avg_case = np.mean(y_IUFNO_spe_arr,0) #行压缩成一行
x_structrue2_avg_case = np.mean(x_IUFNO_structrue2,0) #行压缩成一行
y_structrue2_avg_case = np.mean(y_IUFNO_structrue2,0) #行压缩成
x_structrue4_avg_case = np.mean(x_IUFNO_structrue4,0) #行压缩成一行
y_structrue4_avg_case = np.mean(y_IUFNO_structrue4,0) #行压缩成
x_vort_PDFs_avg_case = np.mean(x_IUFNO_vort_PDFs,0) #行压缩成一行
y_vort_PDFs_avg_case = np.mean(y_IUFNO_vort_PDFs,0) #行压缩成
x_vort_statistics_avg_case = np.mean(x_IUFNO_vort_statistics,0) #行压缩成一行
y_vort_statistics_avg_case = np.mean(y_IUFNO_vort_statistics,0) #行压缩成
# 拼接操作
avg_IUFNO_urms_10case=np.dstack((x_urms_avg_case,y_urms_avg_case)).squeeze() #拼接
avg_IUFNO_wrms_10case=np.dstack((x_wrms_avg_case,y_wrms_avg_case)).squeeze() #拼接
avg_IUFNO_dissipation_10case=np.dstack((x_dissipation_avg_case,y_dissipation_avg_case)).squeeze() #拼接
avg_IUFNO_Et_10case=np.dstack((x_Et_avg_case,y_Et_avg_case)).squeeze() #拼接
avg_IUFNO_inc1_PDFs_10case=np.dstack((x_inc1_PDFs_avg_case,y_inc1_PDFs_avg_case)).squeeze() #拼接
avg_IUFNO_spectrum_10case=np.dstack((x_spe_avg_case,y_spe_avg_case)).squeeze() #拼接
avg_IUFNO_structrue2_10case=np.dstack((x_structrue2_avg_case,y_structrue2_avg_case)).squeeze() #拼接
avg_IUFNO_structrue4_10case=np.dstack((x_structrue4_avg_case,y_structrue4_avg_case)).squeeze() #拼接
avg_IUFNO_vort_PDFs_10case=np.dstack((x_vort_PDFs_avg_case,y_vort_PDFs_avg_case)).squeeze() #拼接
avg_IUFNO_vort_statistics_10case=np.dstack((x_vort_statistics_avg_case,y_vort_statistics_avg_case)).squeeze() #拼接
#导出均值

np.savetxt('./AVG/IUFNO_40ep_mag0.5/N{}/avg_IUFNO_{}case_urms.dat'.format(case_number,case_number),avg_IUFNO_urms_10case, fmt="%16.7f")
np.savetxt('./AVG/IUFNO_40ep_mag0.5/N{}/avg_IUFNO_{}case_wrms.dat'.format(case_number,case_number),avg_IUFNO_wrms_10case, fmt="%16.7f")
np.savetxt('./AVG/IUFNO_40ep_mag0.5/N{}/avg_IUFNO_{}case_dissipation.dat'.format(case_number,case_number),avg_IUFNO_dissipation_10case, fmt="%16.7f")
np.savetxt('./AVG/IUFNO_40ep_mag0.5/N{}/avg_IUFNO_{}case_Ek_t.dat'.format(case_number,case_number),avg_IUFNO_Et_10case, fmt="%16.7f")
np.savetxt('./AVG/IUFNO_40ep_mag0.5/N{}/avg_IUFNO_{}case_inc1_PDFs.dat'.format(case_number,case_number),avg_IUFNO_inc1_PDFs_10case, fmt="%16.7f")
np.savetxt('./AVG/IUFNO_40ep_mag0.5/N{}/avg_IUFNO_{}case_vel_spec.dat'.format(case_number,case_number),avg_IUFNO_spectrum_10case, fmt="%16.7f")
np.savetxt('./AVG/IUFNO_40ep_mag0.5/N{}/avg_IUFNO_{}case_structrue2.dat'.format(case_number,case_number),avg_IUFNO_structrue2_10case, fmt="%16.7f")
np.savetxt('./AVG/IUFNO_40ep_mag0.5/N{}/avg_IUFNO_{}case_structrue4.dat'.format(case_number,case_number),avg_IUFNO_structrue4_10case, fmt="%16.7f")
np.savetxt('./AVG/IUFNO_40ep_mag0.5/N{}/avg_IUFNO_{}case_vort_PDFs.dat'.format(case_number,case_number),avg_IUFNO_vort_PDFs_10case, fmt="%16.7f")
np.savetxt('./AVG/IUFNO_40ep_mag0.5/N{}/avg_IUFNO_{}case_vort_statistics.dat'.format(case_number,case_number),avg_IUFNO_vort_statistics_10case, fmt="%16.7f")
'''
np.savetxt('./AVG/IUFNO_40ep_mag0.5/{}case/avg_IUFNO_{}case_urms.dat'.format(case_number,case_number),avg_IUFNO_urms_10case, fmt="%16.7f")
np.savetxt('./AVG/IUFNO_40ep_mag0.5/{}case/avg_IUFNO_{}case_wrms.dat'.format(case_number,case_number),avg_IUFNO_wrms_10case, fmt="%16.7f")
np.savetxt('./AVG/IUFNO_40ep_mag0.5/{}case/avg_IUFNO_{}case_dissipation.dat'.format(case_number,case_number),avg_IUFNO_dissipation_10case, fmt="%16.7f")
np.savetxt('./AVG/IUFNO_40ep_mag0.5/{}case/avg_IUFNO_{}case_Ek_t.dat'.format(case_number,case_number),avg_IUFNO_Et_10case, fmt="%16.7f")
np.savetxt('./AVG/IUFNO_40ep_mag0.5/{}case/avg_IUFNO_{}case_inc1_PDFs.dat'.format(case_number,case_number),avg_IUFNO_inc1_PDFs_10case, fmt="%16.7f")
np.savetxt('./AVG/IUFNO_40ep_mag0.5/{}case/avg_IUFNO_{}case_vel_spec.dat'.format(case_number,case_number),avg_IUFNO_spectrum_10case, fmt="%16.7f")
np.savetxt('./AVG/IUFNO_40ep_mag0.5/{}case/avg_IUFNO_{}case_structrue2.dat'.format(case_number,case_number),avg_IUFNO_structrue2_10case, fmt="%16.7f")
np.savetxt('./AVG/IUFNO_40ep_mag0.5/{}case/avg_IUFNO_{}case_structrue4.dat'.format(case_number,case_number),avg_IUFNO_structrue4_10case, fmt="%16.7f")
np.savetxt('./AVG/IUFNO_40ep_mag0.5/{}case/avg_IUFNO_{}case_vort_PDFs.dat'.format(case_number,case_number),avg_IUFNO_vort_PDFs_10case, fmt="%16.7f")
np.savetxt('./AVG/IUFNO_40ep_mag0.5/{}case/avg_IUFNO_{}case_vort_statistics.dat'.format(case_number,case_number),avg_IUFNO_vort_statistics_10case, fmt="%16.7f")
'''

#==========================================================================FNO
print("F-IUFNO_40ep getting dat!")
x_IUFNO_dissipation=[]
y_IUFNO_dissipation=[]
x_IUFNO_Et=[]
y_IUFNO_Et=[]
x_IUFNO_inc1_PDFs=[]
y_IUFNO_inc1_PDFs=[]
x_IUFNO_velspectrum=[]
y_IUFNO_velspectrum=[]
x_IUFNO_structrue2 = []
y_IUFNO_structrue2 = []
x_IUFNO_structrue4 = []
y_IUFNO_structrue4 = []
x_IUFNO_urms = []
y_IUFNO_urms = []
x_IUFNO_wrms = []
y_IUFNO_wrms = []
x_IUFNO_vort_PDFs = []
y_IUFNO_vort_PDFs = []
x_IUFNO_vort_statistics = []
y_IUFNO_vort_statistics = []
for case_n in range(case_number-1,case_number):
    # print(case_n)
    # 载入后处理文件，包括速度参数，PDFs，能谱，结构函数
    IUFNO_vel_parameter= np.loadtxt('./case{}/Result_LES32_F-IUFNO_40ep_gap200/post_result/vel_parameter.dat'.format(case_n+1),dtype=float, comments=['step'])
    IUFNO_ic1_PDFs = np.loadtxt('./case{}/Result_LES32_F-IUFNO_40ep_gap200/post_result/inc1_PDFs.dat'.format(case_n + 1), dtype=float,comments=['step'])
    IUFNO_spec = np.loadtxt('./case{}/Result_LES32_F-IUFNO_40ep_gap200/post_result/spectrum_vel.dat'.format(case_n + 1), dtype=float,comments=['variables', 'zone'])
    IUFNO_structrue2 = np.loadtxt('./case{}/Result_LES32_F-IUFNO_40ep_gap200/post_result/structure2.dat'.format(case_n + 1),dtype=float, comments=['step'])
    IUFNO_structrue4 = np.loadtxt('./case{}/Result_LES32_F-IUFNO_40ep_gap200/post_result/structure4.dat'.format(case_n + 1),dtype=float, comments=['step'])
    IUFNO_vort_PDFs = np.loadtxt('./case{}/Result_LES32_F-IUFNO_40ep_gap200/post_result/vort_PDFs.dat'.format(case_n + 1), dtype=float,comments=['variables', 'zone'])
    IUFNO_vort_statistics = np.loadtxt('./case{}/Result_LES32_F-IUFNO_40ep_gap200/post_result/vort_statistics.dat'.format(case_n + 1),dtype=float, comments=['step'])
    # print(VGM.shape)
    # 取出数据
    x_IUFNO_urms.append(IUFNO_vel_parameter[:,0])  # 只取出第一列数据
    y_IUFNO_urms.append(IUFNO_vel_parameter[:,3]) #只取出第二列数据
    x_IUFNO_wrms.append(IUFNO_vel_parameter[:,0])  # 只取出第一列数据
    y_IUFNO_wrms.append(IUFNO_vel_parameter[:,7]) #只取出第二列数据
    x_IUFNO_dissipation.append(IUFNO_vel_parameter[:,0])  # 只取出第一列数据
    y_IUFNO_dissipation.append(IUFNO_vel_parameter[:,8]) #只取出第二列数据
    x_IUFNO_Et.append(IUFNO_vel_parameter[:,0])  # 只取出第一列数据
    y_IUFNO_Et.append(IUFNO_vel_parameter[:,6]) #只取出第二列数据
    x_IUFNO_inc1_PDFs.append(IUFNO_ic1_PDFs[:,0])  # 只取出第一列数据
    y_IUFNO_inc1_PDFs.append(IUFNO_ic1_PDFs[:,1]) #只取出第二列数据
    x_IUFNO_velspectrum.append(IUFNO_spec[:,0])  # 只取出第一列数据
    y_IUFNO_velspectrum.append(IUFNO_spec[:,1]) #只取出第二列数据
    x_IUFNO_structrue2.append(IUFNO_structrue2[:,0])  # 只取出第一列数据
    y_IUFNO_structrue2.append(IUFNO_structrue2[:,1]) #只取出第二列数据
    x_IUFNO_structrue4.append(IUFNO_structrue4[:,0])  # 只取出第一列数据
    y_IUFNO_structrue4.append(IUFNO_structrue4[:,1]) #只取出第二列数据
    x_IUFNO_vort_PDFs.append(IUFNO_vort_PDFs[:,0])  # 只取出第一列数据
    y_IUFNO_vort_PDFs.append(IUFNO_vort_PDFs[:,1]) #只取出第二列数据
    x_IUFNO_vort_statistics.append(IUFNO_vort_statistics[:,0])  # 只取出第一列数据
    y_IUFNO_vort_statistics.append(IUFNO_vort_statistics[:,5]) #只取出第二列数据
# 转化为数组
x_IUFNO_urms_arr = np.asarray(x_IUFNO_urms) #列表转数组
y_IUFNO_urms_arr = np.asarray(y_IUFNO_urms) #列表转数组
x_IUFNO_wrms_arr = np.asarray(x_IUFNO_wrms) #列表转数组
y_IUFNO_wrms_arr = np.asarray(y_IUFNO_wrms) #列表转数组
x_IUFNO_dissipation_arr = np.asarray(x_IUFNO_dissipation) #列表转数组
y_IUFNO_dissipation_arr = np.asarray(y_IUFNO_dissipation) #列表转数组
x_IUFNO_Et_arr = np.asarray(x_IUFNO_Et) #列表转数组
y_IUFNO_Et_arr = np.asarray(y_IUFNO_Et) #列表转数组
x_IUFNO_inc1_PDFs_arr = np.asarray(x_IUFNO_inc1_PDFs) #列表转数组
y_IUFNO_inc1_PDFs_arr = np.asarray(y_IUFNO_inc1_PDFs) #列表转数组
x_IUFNO_spe_arr = np.asarray(x_IUFNO_velspectrum) #列表转数组
y_IUFNO_spe_arr = np.asarray(y_IUFNO_velspectrum) #列表转数组
x_IUFNO_structrue2 = np.asarray(x_IUFNO_structrue2) #列表转数组
y_IUFNO_structrue2 = np.asarray(y_IUFNO_structrue2) #列表转数组
x_IUFNO_structrue4 = np.asarray(x_IUFNO_structrue4) #列表转数组
y_IUFNO_structrue4 = np.asarray(y_IUFNO_structrue4) #列表转数组
x_IUFNO_vort_PDFs = np.asarray(x_IUFNO_vort_PDFs) #列表转数组
y_IUFNO_vort_PDFs = np.asarray(y_IUFNO_vort_PDFs) #列表转数组
x_IUFNO_vort_statistics = np.asarray(x_IUFNO_vort_statistics) #列表转数组
y_IUFNO_vort_statistics = np.asarray(y_IUFNO_vort_statistics) #列表转数组
# 取均值
x_urms_avg_case = np.mean(x_IUFNO_urms_arr,0) #行压缩成一行
y_urms_avg_case = np.mean(y_IUFNO_urms_arr,0) #行压缩成一行
x_wrms_avg_case = np.mean(x_IUFNO_wrms_arr,0) #行压缩成一行
y_wrms_avg_case = np.mean(y_IUFNO_wrms_arr,0) #行压缩成一行
x_dissipation_avg_case = np.mean(x_IUFNO_dissipation_arr,0) #行压缩成一行
y_dissipation_avg_case = np.mean(y_IUFNO_dissipation_arr,0) #行压缩成一行
x_Et_avg_case = np.mean(x_IUFNO_Et_arr,0) #行压缩成一行
y_Et_avg_case = np.mean(y_IUFNO_Et_arr,0) #行压缩成一行
x_inc1_PDFs_avg_case = np.mean(x_IUFNO_inc1_PDFs_arr,0) #行压缩成一行
y_inc1_PDFs_avg_case = np.mean(y_IUFNO_inc1_PDFs_arr,0) #行压缩成一行
x_spe_avg_case = np.mean(x_IUFNO_spe_arr,0) #行压缩成一行
y_spe_avg_case = np.mean(y_IUFNO_spe_arr,0) #行压缩成一行
x_structrue2_avg_case = np.mean(x_IUFNO_structrue2,0) #行压缩成一行
y_structrue2_avg_case = np.mean(y_IUFNO_structrue2,0) #行压缩成
x_structrue4_avg_case = np.mean(x_IUFNO_structrue4,0) #行压缩成一行
y_structrue4_avg_case = np.mean(y_IUFNO_structrue4,0) #行压缩成
x_vort_PDFs_avg_case = np.mean(x_IUFNO_vort_PDFs,0) #行压缩成一行
y_vort_PDFs_avg_case = np.mean(y_IUFNO_vort_PDFs,0) #行压缩成
x_vort_statistics_avg_case = np.mean(x_IUFNO_vort_statistics,0) #行压缩成一行
y_vort_statistics_avg_case = np.mean(y_IUFNO_vort_statistics,0) #行压缩成
# 拼接操作
avg_IUFNO_urms_10case=np.dstack((x_urms_avg_case,y_urms_avg_case)).squeeze() #拼接
avg_IUFNO_wrms_10case=np.dstack((x_wrms_avg_case,y_wrms_avg_case)).squeeze() #拼接
avg_IUFNO_dissipation_10case=np.dstack((x_dissipation_avg_case,y_dissipation_avg_case)).squeeze() #拼接
avg_IUFNO_Et_10case=np.dstack((x_Et_avg_case,y_Et_avg_case)).squeeze() #拼接
avg_IUFNO_inc1_PDFs_10case=np.dstack((x_inc1_PDFs_avg_case,y_inc1_PDFs_avg_case)).squeeze() #拼接
avg_IUFNO_spectrum_10case=np.dstack((x_spe_avg_case,y_spe_avg_case)).squeeze() #拼接
avg_IUFNO_structrue2_10case=np.dstack((x_structrue2_avg_case,y_structrue2_avg_case)).squeeze() #拼接
avg_IUFNO_structrue4_10case=np.dstack((x_structrue4_avg_case,y_structrue4_avg_case)).squeeze() #拼接
avg_IUFNO_vort_PDFs_10case=np.dstack((x_vort_PDFs_avg_case,y_vort_PDFs_avg_case)).squeeze() #拼接
avg_IUFNO_vort_statistics_10case=np.dstack((x_vort_statistics_avg_case,y_vort_statistics_avg_case)).squeeze() #拼接
#导出均值

np.savetxt('./AVG/F-IUFNO_40ep/N{}/avg_FIUFNO_{}case_urms.dat'.format(case_number,case_number),avg_IUFNO_urms_10case, fmt="%16.7f")
np.savetxt('./AVG/F-IUFNO_40ep/N{}/avg_FIUFNO_{}case_wrms.dat'.format(case_number,case_number),avg_IUFNO_wrms_10case, fmt="%16.7f")
np.savetxt('./AVG/F-IUFNO_40ep/N{}/avg_FIUFNO_{}case_dissipation.dat'.format(case_number,case_number),avg_IUFNO_dissipation_10case, fmt="%16.7f")
np.savetxt('./AVG/F-IUFNO_40ep/N{}/avg_FIUFNO_{}case_Ek_t.dat'.format(case_number,case_number),avg_IUFNO_Et_10case, fmt="%16.7f")
np.savetxt('./AVG/F-IUFNO_40ep/N{}/avg_FIUFNO_{}case_inc1_PDFs.dat'.format(case_number,case_number),avg_IUFNO_inc1_PDFs_10case, fmt="%16.7f")
np.savetxt('./AVG/F-IUFNO_40ep/N{}/avg_FIUFNO_{}case_vel_spec.dat'.format(case_number,case_number),avg_IUFNO_spectrum_10case, fmt="%16.7f")
np.savetxt('./AVG/F-IUFNO_40ep/N{}/avg_FIUFNO_{}case_structrue2.dat'.format(case_number,case_number),avg_IUFNO_structrue2_10case, fmt="%16.7f")
np.savetxt('./AVG/F-IUFNO_40ep/N{}/avg_FIUFNO_{}case_structrue4.dat'.format(case_number,case_number),avg_IUFNO_structrue4_10case, fmt="%16.7f")
np.savetxt('./AVG/F-IUFNO_40ep/N{}/avg_FIUFNO_{}case_vort_PDFs.dat'.format(case_number,case_number),avg_IUFNO_vort_PDFs_10case, fmt="%16.7f")
np.savetxt('./AVG/F-IUFNO_40ep/N{}/avg_FIUFNO_{}case_vort_statistics.dat'.format(case_number,case_number),avg_IUFNO_vort_statistics_10case, fmt="%16.7f")
'''
np.savetxt('./AVG/F-IUFNO_40ep/{}case/avg_FIUFNO_{}case_urms.dat'.format(case_number,case_number),avg_IUFNO_urms_10case, fmt="%16.7f")
np.savetxt('./AVG/F-IUFNO_40ep/{}case/avg_FIUFNO_{}case_wrms.dat'.format(case_number,case_number),avg_IUFNO_wrms_10case, fmt="%16.7f")
np.savetxt('./AVG/F-IUFNO_40ep/{}case/avg_FIUFNO_{}case_dissipation.dat'.format(case_number,case_number),avg_IUFNO_dissipation_10case, fmt="%16.7f")
np.savetxt('./AVG/F-IUFNO_40ep/{}case/avg_FIUFNO_{}case_Ek_t.dat'.format(case_number,case_number),avg_IUFNO_Et_10case, fmt="%16.7f")
np.savetxt('./AVG/F-IUFNO_40ep/{}case/avg_FIUFNO_{}case_inc1_PDFs.dat'.format(case_number,case_number),avg_IUFNO_inc1_PDFs_10case, fmt="%16.7f")
np.savetxt('./AVG/F-IUFNO_40ep/{}case/avg_FIUFNO_{}case_vel_spec.dat'.format(case_number,case_number),avg_IUFNO_spectrum_10case, fmt="%16.7f")
np.savetxt('./AVG/F-IUFNO_40ep/{}case/avg_FIUFNO_{}case_structrue2.dat'.format(case_number,case_number),avg_IUFNO_structrue2_10case, fmt="%16.7f")
np.savetxt('./AVG/F-IUFNO_40ep/{}case/avg_FIUFNO_{}case_structrue4.dat'.format(case_number,case_number),avg_IUFNO_structrue4_10case, fmt="%16.7f")
np.savetxt('./AVG/F-IUFNO_40ep/{}case/avg_FIUFNO_{}case_vort_PDFs.dat'.format(case_number,case_number),avg_IUFNO_vort_PDFs_10case, fmt="%16.7f")
np.savetxt('./AVG/F-IUFNO_40ep/{}case/avg_FIUFNO_{}case_vort_statistics.dat'.format(case_number,case_number),avg_IUFNO_vort_statistics_10case, fmt="%16.7f")
'''
#==========================================================================FNO
print("F-IUFNO_40ep_mag0.1 getting dat!")
x_IUFNO_dissipation=[]
y_IUFNO_dissipation=[]
x_IUFNO_Et=[]
y_IUFNO_Et=[]
x_IUFNO_inc1_PDFs=[]
y_IUFNO_inc1_PDFs=[]
x_IUFNO_velspectrum=[]
y_IUFNO_velspectrum=[]
x_IUFNO_structrue2 = []
y_IUFNO_structrue2 = []
x_IUFNO_structrue4 = []
y_IUFNO_structrue4 = []
x_IUFNO_urms = []
y_IUFNO_urms = []
x_IUFNO_wrms = []
y_IUFNO_wrms = []
x_IUFNO_vort_PDFs = []
y_IUFNO_vort_PDFs = []
x_IUFNO_vort_statistics = []
y_IUFNO_vort_statistics = []
for case_n in range(case_number-1,case_number):
    # print(case_n)
    # 载入后处理文件，包括速度参数，PDFs，能谱，结构函数
    IUFNO_vel_parameter= np.loadtxt('./case{}/Result_LES32_F-IUFNO_40ep_gap200_mag0.1/post_result/vel_parameter.dat'.format(case_n+1),dtype=float, comments=['step'])
    IUFNO_ic1_PDFs = np.loadtxt('./case{}/Result_LES32_F-IUFNO_40ep_gap200_mag0.1/post_result/inc1_PDFs.dat'.format(case_n + 1), dtype=float,comments=['step'])
    IUFNO_spec = np.loadtxt('./case{}/Result_LES32_F-IUFNO_40ep_gap200_mag0.1/post_result/spectrum_vel.dat'.format(case_n + 1), dtype=float,comments=['variables', 'zone'])
    IUFNO_structrue2 = np.loadtxt('./case{}/Result_LES32_F-IUFNO_40ep_gap200_mag0.1/post_result/structure2.dat'.format(case_n + 1),dtype=float, comments=['step'])
    IUFNO_structrue4 = np.loadtxt('./case{}/Result_LES32_F-IUFNO_40ep_gap200_mag0.1/post_result/structure4.dat'.format(case_n + 1),dtype=float, comments=['step'])
    IUFNO_vort_PDFs = np.loadtxt('./case{}/Result_LES32_F-IUFNO_40ep_gap200_mag0.1/post_result/vort_PDFs.dat'.format(case_n + 1), dtype=float,comments=['variables', 'zone'])
    IUFNO_vort_statistics = np.loadtxt('./case{}/Result_LES32_F-IUFNO_40ep_gap200_mag0.1/post_result/vort_statistics.dat'.format(case_n + 1),dtype=float, comments=['step'])
    # print(VGM.shape)
    # 取出数据
    x_IUFNO_urms.append(IUFNO_vel_parameter[:,0])  # 只取出第一列数据
    y_IUFNO_urms.append(IUFNO_vel_parameter[:,3]) #只取出第二列数据
    x_IUFNO_wrms.append(IUFNO_vel_parameter[:,0])  # 只取出第一列数据
    y_IUFNO_wrms.append(IUFNO_vel_parameter[:,7]) #只取出第二列数据
    x_IUFNO_dissipation.append(IUFNO_vel_parameter[:,0])  # 只取出第一列数据
    y_IUFNO_dissipation.append(IUFNO_vel_parameter[:,8]) #只取出第二列数据
    x_IUFNO_Et.append(IUFNO_vel_parameter[:,0])  # 只取出第一列数据
    y_IUFNO_Et.append(IUFNO_vel_parameter[:,6]) #只取出第二列数据
    x_IUFNO_inc1_PDFs.append(IUFNO_ic1_PDFs[:,0])  # 只取出第一列数据
    y_IUFNO_inc1_PDFs.append(IUFNO_ic1_PDFs[:,1]) #只取出第二列数据
    x_IUFNO_velspectrum.append(IUFNO_spec[:,0])  # 只取出第一列数据
    y_IUFNO_velspectrum.append(IUFNO_spec[:,1]) #只取出第二列数据
    x_IUFNO_structrue2.append(IUFNO_structrue2[:,0])  # 只取出第一列数据
    y_IUFNO_structrue2.append(IUFNO_structrue2[:,1]) #只取出第二列数据
    x_IUFNO_structrue4.append(IUFNO_structrue4[:,0])  # 只取出第一列数据
    y_IUFNO_structrue4.append(IUFNO_structrue4[:,1]) #只取出第二列数据
    x_IUFNO_vort_PDFs.append(IUFNO_vort_PDFs[:,0])  # 只取出第一列数据
    y_IUFNO_vort_PDFs.append(IUFNO_vort_PDFs[:,1]) #只取出第二列数据
    x_IUFNO_vort_statistics.append(IUFNO_vort_statistics[:,0])  # 只取出第一列数据
    y_IUFNO_vort_statistics.append(IUFNO_vort_statistics[:,5]) #只取出第二列数据
# 转化为数组
x_IUFNO_urms_arr = np.asarray(x_IUFNO_urms) #列表转数组
y_IUFNO_urms_arr = np.asarray(y_IUFNO_urms) #列表转数组
x_IUFNO_wrms_arr = np.asarray(x_IUFNO_wrms) #列表转数组
y_IUFNO_wrms_arr = np.asarray(y_IUFNO_wrms) #列表转数组
x_IUFNO_dissipation_arr = np.asarray(x_IUFNO_dissipation) #列表转数组
y_IUFNO_dissipation_arr = np.asarray(y_IUFNO_dissipation) #列表转数组
x_IUFNO_Et_arr = np.asarray(x_IUFNO_Et) #列表转数组
y_IUFNO_Et_arr = np.asarray(y_IUFNO_Et) #列表转数组
x_IUFNO_inc1_PDFs_arr = np.asarray(x_IUFNO_inc1_PDFs) #列表转数组
y_IUFNO_inc1_PDFs_arr = np.asarray(y_IUFNO_inc1_PDFs) #列表转数组
x_IUFNO_spe_arr = np.asarray(x_IUFNO_velspectrum) #列表转数组
y_IUFNO_spe_arr = np.asarray(y_IUFNO_velspectrum) #列表转数组
x_IUFNO_structrue2 = np.asarray(x_IUFNO_structrue2) #列表转数组
y_IUFNO_structrue2 = np.asarray(y_IUFNO_structrue2) #列表转数组
x_IUFNO_structrue4 = np.asarray(x_IUFNO_structrue4) #列表转数组
y_IUFNO_structrue4 = np.asarray(y_IUFNO_structrue4) #列表转数组
x_IUFNO_vort_PDFs = np.asarray(x_IUFNO_vort_PDFs) #列表转数组
y_IUFNO_vort_PDFs = np.asarray(y_IUFNO_vort_PDFs) #列表转数组
x_IUFNO_vort_statistics = np.asarray(x_IUFNO_vort_statistics) #列表转数组
y_IUFNO_vort_statistics = np.asarray(y_IUFNO_vort_statistics) #列表转数组
# 取均值
x_urms_avg_case = np.mean(x_IUFNO_urms_arr,0) #行压缩成一行
y_urms_avg_case = np.mean(y_IUFNO_urms_arr,0) #行压缩成一行
x_wrms_avg_case = np.mean(x_IUFNO_wrms_arr,0) #行压缩成一行
y_wrms_avg_case = np.mean(y_IUFNO_wrms_arr,0) #行压缩成一行
x_dissipation_avg_case = np.mean(x_IUFNO_dissipation_arr,0) #行压缩成一行
y_dissipation_avg_case = np.mean(y_IUFNO_dissipation_arr,0) #行压缩成一行
x_Et_avg_case = np.mean(x_IUFNO_Et_arr,0) #行压缩成一行
y_Et_avg_case = np.mean(y_IUFNO_Et_arr,0) #行压缩成一行
x_inc1_PDFs_avg_case = np.mean(x_IUFNO_inc1_PDFs_arr,0) #行压缩成一行
y_inc1_PDFs_avg_case = np.mean(y_IUFNO_inc1_PDFs_arr,0) #行压缩成一行
x_spe_avg_case = np.mean(x_IUFNO_spe_arr,0) #行压缩成一行
y_spe_avg_case = np.mean(y_IUFNO_spe_arr,0) #行压缩成一行
x_structrue2_avg_case = np.mean(x_IUFNO_structrue2,0) #行压缩成一行
y_structrue2_avg_case = np.mean(y_IUFNO_structrue2,0) #行压缩成
x_structrue4_avg_case = np.mean(x_IUFNO_structrue4,0) #行压缩成一行
y_structrue4_avg_case = np.mean(y_IUFNO_structrue4,0) #行压缩成
x_vort_PDFs_avg_case = np.mean(x_IUFNO_vort_PDFs,0) #行压缩成一行
y_vort_PDFs_avg_case = np.mean(y_IUFNO_vort_PDFs,0) #行压缩成
x_vort_statistics_avg_case = np.mean(x_IUFNO_vort_statistics,0) #行压缩成一行
y_vort_statistics_avg_case = np.mean(y_IUFNO_vort_statistics,0) #行压缩成
# 拼接操作
avg_IUFNO_urms_10case=np.dstack((x_urms_avg_case,y_urms_avg_case)).squeeze() #拼接
avg_IUFNO_wrms_10case=np.dstack((x_wrms_avg_case,y_wrms_avg_case)).squeeze() #拼接
avg_IUFNO_dissipation_10case=np.dstack((x_dissipation_avg_case,y_dissipation_avg_case)).squeeze() #拼接
avg_IUFNO_Et_10case=np.dstack((x_Et_avg_case,y_Et_avg_case)).squeeze() #拼接
avg_IUFNO_inc1_PDFs_10case=np.dstack((x_inc1_PDFs_avg_case,y_inc1_PDFs_avg_case)).squeeze() #拼接
avg_IUFNO_spectrum_10case=np.dstack((x_spe_avg_case,y_spe_avg_case)).squeeze() #拼接
avg_IUFNO_structrue2_10case=np.dstack((x_structrue2_avg_case,y_structrue2_avg_case)).squeeze() #拼接
avg_IUFNO_structrue4_10case=np.dstack((x_structrue4_avg_case,y_structrue4_avg_case)).squeeze() #拼接
avg_IUFNO_vort_PDFs_10case=np.dstack((x_vort_PDFs_avg_case,y_vort_PDFs_avg_case)).squeeze() #拼接
avg_IUFNO_vort_statistics_10case=np.dstack((x_vort_statistics_avg_case,y_vort_statistics_avg_case)).squeeze() #拼接
#导出均值

np.savetxt('./AVG/F-IUFNO_40ep_mag0.1/N{}/avg_FIUFNO_{}case_urms.dat'.format(case_number,case_number),avg_IUFNO_urms_10case, fmt="%16.7f")
np.savetxt('./AVG/F-IUFNO_40ep_mag0.1/N{}/avg_FIUFNO_{}case_wrms.dat'.format(case_number,case_number),avg_IUFNO_wrms_10case, fmt="%16.7f")
np.savetxt('./AVG/F-IUFNO_40ep_mag0.1/N{}/avg_FIUFNO_{}case_dissipation.dat'.format(case_number,case_number),avg_IUFNO_dissipation_10case, fmt="%16.7f")
np.savetxt('./AVG/F-IUFNO_40ep_mag0.1/N{}/avg_FIUFNO_{}case_Ek_t.dat'.format(case_number,case_number),avg_IUFNO_Et_10case, fmt="%16.7f")
np.savetxt('./AVG/F-IUFNO_40ep_mag0.1/N{}/avg_FIUFNO_{}case_inc1_PDFs.dat'.format(case_number,case_number),avg_IUFNO_inc1_PDFs_10case, fmt="%16.7f")
np.savetxt('./AVG/F-IUFNO_40ep_mag0.1/N{}/avg_FIUFNO_{}case_vel_spec.dat'.format(case_number,case_number),avg_IUFNO_spectrum_10case, fmt="%16.7f")
np.savetxt('./AVG/F-IUFNO_40ep_mag0.1/N{}/avg_FIUFNO_{}case_structrue2.dat'.format(case_number,case_number),avg_IUFNO_structrue2_10case, fmt="%16.7f")
np.savetxt('./AVG/F-IUFNO_40ep_mag0.1/N{}/avg_FIUFNO_{}case_structrue4.dat'.format(case_number,case_number),avg_IUFNO_structrue4_10case, fmt="%16.7f")
np.savetxt('./AVG/F-IUFNO_40ep_mag0.1/N{}/avg_FIUFNO_{}case_vort_PDFs.dat'.format(case_number,case_number),avg_IUFNO_vort_PDFs_10case, fmt="%16.7f")
np.savetxt('./AVG/F-IUFNO_40ep_mag0.1/N{}/avg_FIUFNO_{}case_vort_statistics.dat'.format(case_number,case_number),avg_IUFNO_vort_statistics_10case, fmt="%16.7f")
'''
np.savetxt('./AVG/F-IUFNO_40ep_mag0.1/{}case/avg_FIUFNO_{}case_urms.dat'.format(case_number,case_number),avg_IUFNO_urms_10case, fmt="%16.7f")
np.savetxt('./AVG/F-IUFNO_40ep_mag0.1/{}case/avg_FIUFNO_{}case_wrms.dat'.format(case_number,case_number),avg_IUFNO_wrms_10case, fmt="%16.7f")
np.savetxt('./AVG/F-IUFNO_40ep_mag0.1/{}case/avg_FIUFNO_{}case_dissipation.dat'.format(case_number,case_number),avg_IUFNO_dissipation_10case, fmt="%16.7f")
np.savetxt('./AVG/F-IUFNO_40ep_mag0.1/{}case/avg_FIUFNO_{}case_Ek_t.dat'.format(case_number,case_number),avg_IUFNO_Et_10case, fmt="%16.7f")
np.savetxt('./AVG/F-IUFNO_40ep_mag0.1/{}case/avg_FIUFNO_{}case_inc1_PDFs.dat'.format(case_number,case_number),avg_IUFNO_inc1_PDFs_10case, fmt="%16.7f")
np.savetxt('./AVG/F-IUFNO_40ep_mag0.1/{}case/avg_FIUFNO_{}case_vel_spec.dat'.format(case_number,case_number),avg_IUFNO_spectrum_10case, fmt="%16.7f")
np.savetxt('./AVG/F-IUFNO_40ep_mag0.1/{}case/avg_FIUFNO_{}case_structrue2.dat'.format(case_number,case_number),avg_IUFNO_structrue2_10case, fmt="%16.7f")
np.savetxt('./AVG/F-IUFNO_40ep_mag0.1/{}case/avg_FIUFNO_{}case_structrue4.dat'.format(case_number,case_number),avg_IUFNO_structrue4_10case, fmt="%16.7f")
np.savetxt('./AVG/F-IUFNO_40ep_mag0.1/{}case/avg_FIUFNO_{}case_vort_PDFs.dat'.format(case_number,case_number),avg_IUFNO_vort_PDFs_10case, fmt="%16.7f")
np.savetxt('./AVG/F-IUFNO_40ep_mag0.1/{}case/avg_FIUFNO_{}case_vort_statistics.dat'.format(case_number,case_number),avg_IUFNO_vort_statistics_10case, fmt="%16.7f")
'''

#==========================================================================FNO
print("F-IUFNO_40ep_mag0.5 getting dat!")
x_IUFNO_dissipation=[]
y_IUFNO_dissipation=[]
x_IUFNO_Et=[]
y_IUFNO_Et=[]
x_IUFNO_inc1_PDFs=[]
y_IUFNO_inc1_PDFs=[]
x_IUFNO_velspectrum=[]
y_IUFNO_velspectrum=[]
x_IUFNO_structrue2 = []
y_IUFNO_structrue2 = []
x_IUFNO_structrue4 = []
y_IUFNO_structrue4 = []
x_IUFNO_urms = []
y_IUFNO_urms = []
x_IUFNO_wrms = []
y_IUFNO_wrms = []
x_IUFNO_vort_PDFs = []
y_IUFNO_vort_PDFs = []
x_IUFNO_vort_statistics = []
y_IUFNO_vort_statistics = []
for case_n in range(case_number-1,case_number):
    # print(case_n)
    # 载入后处理文件，包括速度参数，PDFs，能谱，结构函数
    IUFNO_vel_parameter= np.loadtxt('./case{}/Result_LES32_F-IUFNO_40ep_gap200_mag0.5/post_result/vel_parameter.dat'.format(case_n+1),dtype=float, comments=['step'])
    IUFNO_ic1_PDFs = np.loadtxt('./case{}/Result_LES32_F-IUFNO_40ep_gap200_mag0.5/post_result/inc1_PDFs.dat'.format(case_n + 1), dtype=float,comments=['step'])
    IUFNO_spec = np.loadtxt('./case{}/Result_LES32_F-IUFNO_40ep_gap200_mag0.5/post_result/spectrum_vel.dat'.format(case_n + 1), dtype=float,comments=['variables', 'zone'])
    IUFNO_structrue2 = np.loadtxt('./case{}/Result_LES32_F-IUFNO_40ep_gap200_mag0.5/post_result/structure2.dat'.format(case_n + 1),dtype=float, comments=['step'])
    IUFNO_structrue4 = np.loadtxt('./case{}/Result_LES32_F-IUFNO_40ep_gap200_mag0.5/post_result/structure4.dat'.format(case_n + 1),dtype=float, comments=['step'])
    IUFNO_vort_PDFs = np.loadtxt('./case{}/Result_LES32_F-IUFNO_40ep_gap200_mag0.5/post_result/vort_PDFs.dat'.format(case_n + 1), dtype=float,comments=['variables', 'zone'])
    IUFNO_vort_statistics = np.loadtxt('./case{}/Result_LES32_F-IUFNO_40ep_gap200_mag0.5/post_result/vort_statistics.dat'.format(case_n + 1),dtype=float, comments=['step'])
    # print(VGM.shape)
    # 取出数据
    x_IUFNO_urms.append(IUFNO_vel_parameter[:,0])  # 只取出第一列数据
    y_IUFNO_urms.append(IUFNO_vel_parameter[:,3]) #只取出第二列数据
    x_IUFNO_wrms.append(IUFNO_vel_parameter[:,0])  # 只取出第一列数据
    y_IUFNO_wrms.append(IUFNO_vel_parameter[:,7]) #只取出第二列数据
    x_IUFNO_dissipation.append(IUFNO_vel_parameter[:,0])  # 只取出第一列数据
    y_IUFNO_dissipation.append(IUFNO_vel_parameter[:,8]) #只取出第二列数据
    x_IUFNO_Et.append(IUFNO_vel_parameter[:,0])  # 只取出第一列数据
    y_IUFNO_Et.append(IUFNO_vel_parameter[:,6]) #只取出第二列数据
    x_IUFNO_inc1_PDFs.append(IUFNO_ic1_PDFs[:,0])  # 只取出第一列数据
    y_IUFNO_inc1_PDFs.append(IUFNO_ic1_PDFs[:,1]) #只取出第二列数据
    x_IUFNO_velspectrum.append(IUFNO_spec[:,0])  # 只取出第一列数据
    y_IUFNO_velspectrum.append(IUFNO_spec[:,1]) #只取出第二列数据
    x_IUFNO_structrue2.append(IUFNO_structrue2[:,0])  # 只取出第一列数据
    y_IUFNO_structrue2.append(IUFNO_structrue2[:,1]) #只取出第二列数据
    x_IUFNO_structrue4.append(IUFNO_structrue4[:,0])  # 只取出第一列数据
    y_IUFNO_structrue4.append(IUFNO_structrue4[:,1]) #只取出第二列数据
    x_IUFNO_vort_PDFs.append(IUFNO_vort_PDFs[:,0])  # 只取出第一列数据
    y_IUFNO_vort_PDFs.append(IUFNO_vort_PDFs[:,1]) #只取出第二列数据
    x_IUFNO_vort_statistics.append(IUFNO_vort_statistics[:,0])  # 只取出第一列数据
    y_IUFNO_vort_statistics.append(IUFNO_vort_statistics[:,5]) #只取出第二列数据
# 转化为数组
x_IUFNO_urms_arr = np.asarray(x_IUFNO_urms) #列表转数组
y_IUFNO_urms_arr = np.asarray(y_IUFNO_urms) #列表转数组
x_IUFNO_wrms_arr = np.asarray(x_IUFNO_wrms) #列表转数组
y_IUFNO_wrms_arr = np.asarray(y_IUFNO_wrms) #列表转数组
x_IUFNO_dissipation_arr = np.asarray(x_IUFNO_dissipation) #列表转数组
y_IUFNO_dissipation_arr = np.asarray(y_IUFNO_dissipation) #列表转数组
x_IUFNO_Et_arr = np.asarray(x_IUFNO_Et) #列表转数组
y_IUFNO_Et_arr = np.asarray(y_IUFNO_Et) #列表转数组
x_IUFNO_inc1_PDFs_arr = np.asarray(x_IUFNO_inc1_PDFs) #列表转数组
y_IUFNO_inc1_PDFs_arr = np.asarray(y_IUFNO_inc1_PDFs) #列表转数组
x_IUFNO_spe_arr = np.asarray(x_IUFNO_velspectrum) #列表转数组
y_IUFNO_spe_arr = np.asarray(y_IUFNO_velspectrum) #列表转数组
x_IUFNO_structrue2 = np.asarray(x_IUFNO_structrue2) #列表转数组
y_IUFNO_structrue2 = np.asarray(y_IUFNO_structrue2) #列表转数组
x_IUFNO_structrue4 = np.asarray(x_IUFNO_structrue4) #列表转数组
y_IUFNO_structrue4 = np.asarray(y_IUFNO_structrue4) #列表转数组
x_IUFNO_vort_PDFs = np.asarray(x_IUFNO_vort_PDFs) #列表转数组
y_IUFNO_vort_PDFs = np.asarray(y_IUFNO_vort_PDFs) #列表转数组
x_IUFNO_vort_statistics = np.asarray(x_IUFNO_vort_statistics) #列表转数组
y_IUFNO_vort_statistics = np.asarray(y_IUFNO_vort_statistics) #列表转数组
# 取均值
x_urms_avg_case = np.mean(x_IUFNO_urms_arr,0) #行压缩成一行
y_urms_avg_case = np.mean(y_IUFNO_urms_arr,0) #行压缩成一行
x_wrms_avg_case = np.mean(x_IUFNO_wrms_arr,0) #行压缩成一行
y_wrms_avg_case = np.mean(y_IUFNO_wrms_arr,0) #行压缩成一行
x_dissipation_avg_case = np.mean(x_IUFNO_dissipation_arr,0) #行压缩成一行
y_dissipation_avg_case = np.mean(y_IUFNO_dissipation_arr,0) #行压缩成一行
x_Et_avg_case = np.mean(x_IUFNO_Et_arr,0) #行压缩成一行
y_Et_avg_case = np.mean(y_IUFNO_Et_arr,0) #行压缩成一行
x_inc1_PDFs_avg_case = np.mean(x_IUFNO_inc1_PDFs_arr,0) #行压缩成一行
y_inc1_PDFs_avg_case = np.mean(y_IUFNO_inc1_PDFs_arr,0) #行压缩成一行
x_spe_avg_case = np.mean(x_IUFNO_spe_arr,0) #行压缩成一行
y_spe_avg_case = np.mean(y_IUFNO_spe_arr,0) #行压缩成一行
x_structrue2_avg_case = np.mean(x_IUFNO_structrue2,0) #行压缩成一行
y_structrue2_avg_case = np.mean(y_IUFNO_structrue2,0) #行压缩成
x_structrue4_avg_case = np.mean(x_IUFNO_structrue4,0) #行压缩成一行
y_structrue4_avg_case = np.mean(y_IUFNO_structrue4,0) #行压缩成
x_vort_PDFs_avg_case = np.mean(x_IUFNO_vort_PDFs,0) #行压缩成一行
y_vort_PDFs_avg_case = np.mean(y_IUFNO_vort_PDFs,0) #行压缩成
x_vort_statistics_avg_case = np.mean(x_IUFNO_vort_statistics,0) #行压缩成一行
y_vort_statistics_avg_case = np.mean(y_IUFNO_vort_statistics,0) #行压缩成
# 拼接操作
avg_IUFNO_urms_10case=np.dstack((x_urms_avg_case,y_urms_avg_case)).squeeze() #拼接
avg_IUFNO_wrms_10case=np.dstack((x_wrms_avg_case,y_wrms_avg_case)).squeeze() #拼接
avg_IUFNO_dissipation_10case=np.dstack((x_dissipation_avg_case,y_dissipation_avg_case)).squeeze() #拼接
avg_IUFNO_Et_10case=np.dstack((x_Et_avg_case,y_Et_avg_case)).squeeze() #拼接
avg_IUFNO_inc1_PDFs_10case=np.dstack((x_inc1_PDFs_avg_case,y_inc1_PDFs_avg_case)).squeeze() #拼接
avg_IUFNO_spectrum_10case=np.dstack((x_spe_avg_case,y_spe_avg_case)).squeeze() #拼接
avg_IUFNO_structrue2_10case=np.dstack((x_structrue2_avg_case,y_structrue2_avg_case)).squeeze() #拼接
avg_IUFNO_structrue4_10case=np.dstack((x_structrue4_avg_case,y_structrue4_avg_case)).squeeze() #拼接
avg_IUFNO_vort_PDFs_10case=np.dstack((x_vort_PDFs_avg_case,y_vort_PDFs_avg_case)).squeeze() #拼接
avg_IUFNO_vort_statistics_10case=np.dstack((x_vort_statistics_avg_case,y_vort_statistics_avg_case)).squeeze() #拼接
#导出均值

np.savetxt('./AVG/F-IUFNO_40ep_mag0.5/N{}/avg_FIUFNO_{}case_urms.dat'.format(case_number,case_number),avg_IUFNO_urms_10case, fmt="%16.7f")
np.savetxt('./AVG/F-IUFNO_40ep_mag0.5/N{}/avg_FIUFNO_{}case_wrms.dat'.format(case_number,case_number),avg_IUFNO_wrms_10case, fmt="%16.7f")
np.savetxt('./AVG/F-IUFNO_40ep_mag0.5/N{}/avg_FIUFNO_{}case_dissipation.dat'.format(case_number,case_number),avg_IUFNO_dissipation_10case, fmt="%16.7f")
np.savetxt('./AVG/F-IUFNO_40ep_mag0.5/N{}/avg_FIUFNO_{}case_Ek_t.dat'.format(case_number,case_number),avg_IUFNO_Et_10case, fmt="%16.7f")
np.savetxt('./AVG/F-IUFNO_40ep_mag0.5/N{}/avg_FIUFNO_{}case_inc1_PDFs.dat'.format(case_number,case_number),avg_IUFNO_inc1_PDFs_10case, fmt="%16.7f")
np.savetxt('./AVG/F-IUFNO_40ep_mag0.5/N{}/avg_FIUFNO_{}case_vel_spec.dat'.format(case_number,case_number),avg_IUFNO_spectrum_10case, fmt="%16.7f")
np.savetxt('./AVG/F-IUFNO_40ep_mag0.5/N{}/avg_FIUFNO_{}case_structrue2.dat'.format(case_number,case_number),avg_IUFNO_structrue2_10case, fmt="%16.7f")
np.savetxt('./AVG/F-IUFNO_40ep_mag0.5/N{}/avg_FIUFNO_{}case_structrue4.dat'.format(case_number,case_number),avg_IUFNO_structrue4_10case, fmt="%16.7f")
np.savetxt('./AVG/F-IUFNO_40ep_mag0.5/N{}/avg_FIUFNO_{}case_vort_PDFs.dat'.format(case_number,case_number),avg_IUFNO_vort_PDFs_10case, fmt="%16.7f")
np.savetxt('./AVG/F-IUFNO_40ep_mag0.5/N{}/avg_FIUFNO_{}case_vort_statistics.dat'.format(case_number,case_number),avg_IUFNO_vort_statistics_10case, fmt="%16.7f")
'''
np.savetxt('./AVG/F-IUFNO_40ep_mag0.5/{}case/avg_FIUFNO_{}case_urms.dat'.format(case_number,case_number),avg_IUFNO_urms_10case, fmt="%16.7f")
np.savetxt('./AVG/F-IUFNO_40ep_mag0.5/{}case/avg_FIUFNO_{}case_wrms.dat'.format(case_number,case_number),avg_IUFNO_wrms_10case, fmt="%16.7f")
np.savetxt('./AVG/F-IUFNO_40ep_mag0.5/{}case/avg_FIUFNO_{}case_dissipation.dat'.format(case_number,case_number),avg_IUFNO_dissipation_10case, fmt="%16.7f")
np.savetxt('./AVG/F-IUFNO_40ep_mag0.5/{}case/avg_FIUFNO_{}case_Ek_t.dat'.format(case_number,case_number),avg_IUFNO_Et_10case, fmt="%16.7f")
np.savetxt('./AVG/F-IUFNO_40ep_mag0.5/{}case/avg_FIUFNO_{}case_inc1_PDFs.dat'.format(case_number,case_number),avg_IUFNO_inc1_PDFs_10case, fmt="%16.7f")
np.savetxt('./AVG/F-IUFNO_40ep_mag0.5/{}case/avg_FIUFNO_{}case_vel_spec.dat'.format(case_number,case_number),avg_IUFNO_spectrum_10case, fmt="%16.7f")
np.savetxt('./AVG/F-IUFNO_40ep_mag0.5/{}case/avg_FIUFNO_{}case_structrue2.dat'.format(case_number,case_number),avg_IUFNO_structrue2_10case, fmt="%16.7f")
np.savetxt('./AVG/F-IUFNO_40ep_mag0.5/{}case/avg_FIUFNO_{}case_structrue4.dat'.format(case_number,case_number),avg_IUFNO_structrue4_10case, fmt="%16.7f")
np.savetxt('./AVG/F-IUFNO_40ep_mag0.5/{}case/avg_FIUFNO_{}case_vort_PDFs.dat'.format(case_number,case_number),avg_IUFNO_vort_PDFs_10case, fmt="%16.7f")
np.savetxt('./AVG/F-IUFNO_40ep_mag0.5/{}case/avg_FIUFNO_{}case_vort_statistics.dat'.format(case_number,case_number),avg_IUFNO_vort_statistics_10case, fmt="%16.7f")
'''



#==========================================================================FNO
print("F-IUFNO_35ep getting dat!")
x_IUFNO_dissipation=[]
y_IUFNO_dissipation=[]
x_IUFNO_Et=[]
y_IUFNO_Et=[]
x_IUFNO_inc1_PDFs=[]
y_IUFNO_inc1_PDFs=[]
x_IUFNO_velspectrum=[]
y_IUFNO_velspectrum=[]
x_IUFNO_structrue2 = []
y_IUFNO_structrue2 = []
x_IUFNO_structrue4 = []
y_IUFNO_structrue4 = []
x_IUFNO_urms = []
y_IUFNO_urms = []
x_IUFNO_wrms = []
y_IUFNO_wrms = []
x_IUFNO_vort_PDFs = []
y_IUFNO_vort_PDFs = []
x_IUFNO_vort_statistics = []
y_IUFNO_vort_statistics = []
for case_n in range(case_number-1,case_number):
    # print(case_n)
    # 载入后处理文件，包括速度参数，PDFs，能谱，结构函数
    IUFNO_vel_parameter= np.loadtxt('./case{}/Result_LES32_F-IUFNO_35ep_gap200/post_result/vel_parameter.dat'.format(case_n+1),dtype=float, comments=['step'])
    IUFNO_ic1_PDFs = np.loadtxt('./case{}/Result_LES32_F-IUFNO_35ep_gap200/post_result/inc1_PDFs.dat'.format(case_n + 1), dtype=float,comments=['step'])
    IUFNO_spec = np.loadtxt('./case{}/Result_LES32_F-IUFNO_35ep_gap200/post_result/spectrum_vel.dat'.format(case_n + 1), dtype=float,comments=['variables', 'zone'])
    IUFNO_structrue2 = np.loadtxt('./case{}/Result_LES32_F-IUFNO_35ep_gap200/post_result/structure2.dat'.format(case_n + 1),dtype=float, comments=['step'])
    IUFNO_structrue4 = np.loadtxt('./case{}/Result_LES32_F-IUFNO_35ep_gap200/post_result/structure4.dat'.format(case_n + 1),dtype=float, comments=['step'])
    IUFNO_vort_PDFs = np.loadtxt('./case{}/Result_LES32_F-IUFNO_35ep_gap200/post_result/vort_PDFs.dat'.format(case_n + 1), dtype=float,comments=['variables', 'zone'])
    IUFNO_vort_statistics = np.loadtxt('./case{}/Result_LES32_F-IUFNO_35ep_gap200/post_result/vort_statistics.dat'.format(case_n + 1),dtype=float, comments=['step'])
    # print(VGM.shape)
    # 取出数据
    x_IUFNO_urms.append(IUFNO_vel_parameter[:,0])  # 只取出第一列数据
    y_IUFNO_urms.append(IUFNO_vel_parameter[:,3]) #只取出第二列数据
    x_IUFNO_wrms.append(IUFNO_vel_parameter[:,0])  # 只取出第一列数据
    y_IUFNO_wrms.append(IUFNO_vel_parameter[:,7]) #只取出第二列数据
    x_IUFNO_dissipation.append(IUFNO_vel_parameter[:,0])  # 只取出第一列数据
    y_IUFNO_dissipation.append(IUFNO_vel_parameter[:,8]) #只取出第二列数据
    x_IUFNO_Et.append(IUFNO_vel_parameter[:,0])  # 只取出第一列数据
    y_IUFNO_Et.append(IUFNO_vel_parameter[:,6]) #只取出第二列数据
    x_IUFNO_inc1_PDFs.append(IUFNO_ic1_PDFs[:,0])  # 只取出第一列数据
    y_IUFNO_inc1_PDFs.append(IUFNO_ic1_PDFs[:,1]) #只取出第二列数据
    x_IUFNO_velspectrum.append(IUFNO_spec[:,0])  # 只取出第一列数据
    y_IUFNO_velspectrum.append(IUFNO_spec[:,1]) #只取出第二列数据
    x_IUFNO_structrue2.append(IUFNO_structrue2[:,0])  # 只取出第一列数据
    y_IUFNO_structrue2.append(IUFNO_structrue2[:,1]) #只取出第二列数据
    x_IUFNO_structrue4.append(IUFNO_structrue4[:,0])  # 只取出第一列数据
    y_IUFNO_structrue4.append(IUFNO_structrue4[:,1]) #只取出第二列数据
    x_IUFNO_vort_PDFs.append(IUFNO_vort_PDFs[:,0])  # 只取出第一列数据
    y_IUFNO_vort_PDFs.append(IUFNO_vort_PDFs[:,1]) #只取出第二列数据
    x_IUFNO_vort_statistics.append(IUFNO_vort_statistics[:,0])  # 只取出第一列数据
    y_IUFNO_vort_statistics.append(IUFNO_vort_statistics[:,5]) #只取出第二列数据
# 转化为数组
x_IUFNO_urms_arr = np.asarray(x_IUFNO_urms) #列表转数组
y_IUFNO_urms_arr = np.asarray(y_IUFNO_urms) #列表转数组
x_IUFNO_wrms_arr = np.asarray(x_IUFNO_wrms) #列表转数组
y_IUFNO_wrms_arr = np.asarray(y_IUFNO_wrms) #列表转数组
x_IUFNO_dissipation_arr = np.asarray(x_IUFNO_dissipation) #列表转数组
y_IUFNO_dissipation_arr = np.asarray(y_IUFNO_dissipation) #列表转数组
x_IUFNO_Et_arr = np.asarray(x_IUFNO_Et) #列表转数组
y_IUFNO_Et_arr = np.asarray(y_IUFNO_Et) #列表转数组
x_IUFNO_inc1_PDFs_arr = np.asarray(x_IUFNO_inc1_PDFs) #列表转数组
y_IUFNO_inc1_PDFs_arr = np.asarray(y_IUFNO_inc1_PDFs) #列表转数组
x_IUFNO_spe_arr = np.asarray(x_IUFNO_velspectrum) #列表转数组
y_IUFNO_spe_arr = np.asarray(y_IUFNO_velspectrum) #列表转数组
x_IUFNO_structrue2 = np.asarray(x_IUFNO_structrue2) #列表转数组
y_IUFNO_structrue2 = np.asarray(y_IUFNO_structrue2) #列表转数组
x_IUFNO_structrue4 = np.asarray(x_IUFNO_structrue4) #列表转数组
y_IUFNO_structrue4 = np.asarray(y_IUFNO_structrue4) #列表转数组
x_IUFNO_vort_PDFs = np.asarray(x_IUFNO_vort_PDFs) #列表转数组
y_IUFNO_vort_PDFs = np.asarray(y_IUFNO_vort_PDFs) #列表转数组
x_IUFNO_vort_statistics = np.asarray(x_IUFNO_vort_statistics) #列表转数组
y_IUFNO_vort_statistics = np.asarray(y_IUFNO_vort_statistics) #列表转数组
# 取均值
x_urms_avg_case = np.mean(x_IUFNO_urms_arr,0) #行压缩成一行
y_urms_avg_case = np.mean(y_IUFNO_urms_arr,0) #行压缩成一行
x_wrms_avg_case = np.mean(x_IUFNO_wrms_arr,0) #行压缩成一行
y_wrms_avg_case = np.mean(y_IUFNO_wrms_arr,0) #行压缩成一行
x_dissipation_avg_case = np.mean(x_IUFNO_dissipation_arr,0) #行压缩成一行
y_dissipation_avg_case = np.mean(y_IUFNO_dissipation_arr,0) #行压缩成一行
x_Et_avg_case = np.mean(x_IUFNO_Et_arr,0) #行压缩成一行
y_Et_avg_case = np.mean(y_IUFNO_Et_arr,0) #行压缩成一行
x_inc1_PDFs_avg_case = np.mean(x_IUFNO_inc1_PDFs_arr,0) #行压缩成一行
y_inc1_PDFs_avg_case = np.mean(y_IUFNO_inc1_PDFs_arr,0) #行压缩成一行
x_spe_avg_case = np.mean(x_IUFNO_spe_arr,0) #行压缩成一行
y_spe_avg_case = np.mean(y_IUFNO_spe_arr,0) #行压缩成一行
x_structrue2_avg_case = np.mean(x_IUFNO_structrue2,0) #行压缩成一行
y_structrue2_avg_case = np.mean(y_IUFNO_structrue2,0) #行压缩成
x_structrue4_avg_case = np.mean(x_IUFNO_structrue4,0) #行压缩成一行
y_structrue4_avg_case = np.mean(y_IUFNO_structrue4,0) #行压缩成
x_vort_PDFs_avg_case = np.mean(x_IUFNO_vort_PDFs,0) #行压缩成一行
y_vort_PDFs_avg_case = np.mean(y_IUFNO_vort_PDFs,0) #行压缩成
x_vort_statistics_avg_case = np.mean(x_IUFNO_vort_statistics,0) #行压缩成一行
y_vort_statistics_avg_case = np.mean(y_IUFNO_vort_statistics,0) #行压缩成
# 拼接操作
avg_IUFNO_urms_10case=np.dstack((x_urms_avg_case,y_urms_avg_case)).squeeze() #拼接
avg_IUFNO_wrms_10case=np.dstack((x_wrms_avg_case,y_wrms_avg_case)).squeeze() #拼接
avg_IUFNO_dissipation_10case=np.dstack((x_dissipation_avg_case,y_dissipation_avg_case)).squeeze() #拼接
avg_IUFNO_Et_10case=np.dstack((x_Et_avg_case,y_Et_avg_case)).squeeze() #拼接
avg_IUFNO_inc1_PDFs_10case=np.dstack((x_inc1_PDFs_avg_case,y_inc1_PDFs_avg_case)).squeeze() #拼接
avg_IUFNO_spectrum_10case=np.dstack((x_spe_avg_case,y_spe_avg_case)).squeeze() #拼接
avg_IUFNO_structrue2_10case=np.dstack((x_structrue2_avg_case,y_structrue2_avg_case)).squeeze() #拼接
avg_IUFNO_structrue4_10case=np.dstack((x_structrue4_avg_case,y_structrue4_avg_case)).squeeze() #拼接
avg_IUFNO_vort_PDFs_10case=np.dstack((x_vort_PDFs_avg_case,y_vort_PDFs_avg_case)).squeeze() #拼接
avg_IUFNO_vort_statistics_10case=np.dstack((x_vort_statistics_avg_case,y_vort_statistics_avg_case)).squeeze() #拼接
#导出均值

np.savetxt('./AVG/F-IUFNO_35ep/N{}/avg_FIUFNO_{}case_urms.dat'.format(case_number,case_number),avg_IUFNO_urms_10case, fmt="%16.7f")
np.savetxt('./AVG/F-IUFNO_35ep/N{}/avg_FIUFNO_{}case_wrms.dat'.format(case_number,case_number),avg_IUFNO_wrms_10case, fmt="%16.7f")
np.savetxt('./AVG/F-IUFNO_35ep/N{}/avg_FIUFNO_{}case_dissipation.dat'.format(case_number,case_number),avg_IUFNO_dissipation_10case, fmt="%16.7f")
np.savetxt('./AVG/F-IUFNO_35ep/N{}/avg_FIUFNO_{}case_Ek_t.dat'.format(case_number,case_number),avg_IUFNO_Et_10case, fmt="%16.7f")
np.savetxt('./AVG/F-IUFNO_35ep/N{}/avg_FIUFNO_{}case_inc1_PDFs.dat'.format(case_number,case_number),avg_IUFNO_inc1_PDFs_10case, fmt="%16.7f")
np.savetxt('./AVG/F-IUFNO_35ep/N{}/avg_FIUFNO_{}case_vel_spec.dat'.format(case_number,case_number),avg_IUFNO_spectrum_10case, fmt="%16.7f")
np.savetxt('./AVG/F-IUFNO_35ep/N{}/avg_FIUFNO_{}case_structrue2.dat'.format(case_number,case_number),avg_IUFNO_structrue2_10case, fmt="%16.7f")
np.savetxt('./AVG/F-IUFNO_35ep/N{}/avg_FIUFNO_{}case_structrue4.dat'.format(case_number,case_number),avg_IUFNO_structrue4_10case, fmt="%16.7f")
np.savetxt('./AVG/F-IUFNO_35ep/N{}/avg_FIUFNO_{}case_vort_PDFs.dat'.format(case_number,case_number),avg_IUFNO_vort_PDFs_10case, fmt="%16.7f")
np.savetxt('./AVG/F-IUFNO_35ep/N{}/avg_FIUFNO_{}case_vort_statistics.dat'.format(case_number,case_number),avg_IUFNO_vort_statistics_10case, fmt="%16.7f")

'''
np.savetxt('./AVG/F-IUFNO_35ep/{}case/avg_FIUFNO_{}case_urms.dat'.format(case_number,case_number),avg_IUFNO_urms_10case, fmt="%16.7f")
np.savetxt('./AVG/F-IUFNO_35ep/{}case/avg_FIUFNO_{}case_wrms.dat'.format(case_number,case_number),avg_IUFNO_wrms_10case, fmt="%16.7f")
np.savetxt('./AVG/F-IUFNO_35ep/{}case/avg_FIUFNO_{}case_dissipation.dat'.format(case_number,case_number),avg_IUFNO_dissipation_10case, fmt="%16.7f")
np.savetxt('./AVG/F-IUFNO_35ep/{}case/avg_FIUFNO_{}case_Ek_t.dat'.format(case_number,case_number),avg_IUFNO_Et_10case, fmt="%16.7f")
np.savetxt('./AVG/F-IUFNO_35ep/{}case/avg_FIUFNO_{}case_inc1_PDFs.dat'.format(case_number,case_number),avg_IUFNO_inc1_PDFs_10case, fmt="%16.7f")
np.savetxt('./AVG/F-IUFNO_35ep/{}case/avg_FIUFNO_{}case_vel_spec.dat'.format(case_number,case_number),avg_IUFNO_spectrum_10case, fmt="%16.7f")
np.savetxt('./AVG/F-IUFNO_35ep/{}case/avg_FIUFNO_{}case_structrue2.dat'.format(case_number,case_number),avg_IUFNO_structrue2_10case, fmt="%16.7f")
np.savetxt('./AVG/F-IUFNO_35ep/{}case/avg_FIUFNO_{}case_structrue4.dat'.format(case_number,case_number),avg_IUFNO_structrue4_10case, fmt="%16.7f")
np.savetxt('./AVG/F-IUFNO_35ep/{}case/avg_FIUFNO_{}case_vort_PDFs.dat'.format(case_number,case_number),avg_IUFNO_vort_PDFs_10case, fmt="%16.7f")
np.savetxt('./AVG/F-IUFNO_35ep/{}case/avg_FIUFNO_{}case_vort_statistics.dat'.format(case_number,case_number),avg_IUFNO_vort_statistics_10case, fmt="%16.7f")
'''
#==========================================================================FNO
print("F-IUFNO_35ep_mag0.1 getting dat!")
x_IUFNO_dissipation=[]
y_IUFNO_dissipation=[]
x_IUFNO_Et=[]
y_IUFNO_Et=[]
x_IUFNO_inc1_PDFs=[]
y_IUFNO_inc1_PDFs=[]
x_IUFNO_velspectrum=[]
y_IUFNO_velspectrum=[]
x_IUFNO_structrue2 = []
y_IUFNO_structrue2 = []
x_IUFNO_structrue4 = []
y_IUFNO_structrue4 = []
x_IUFNO_urms = []
y_IUFNO_urms = []
x_IUFNO_wrms = []
y_IUFNO_wrms = []
x_IUFNO_vort_PDFs = []
y_IUFNO_vort_PDFs = []
x_IUFNO_vort_statistics = []
y_IUFNO_vort_statistics = []
for case_n in range(case_number-1,case_number):
    # print(case_n)
    # 载入后处理文件，包括速度参数，PDFs，能谱，结构函数
    IUFNO_vel_parameter= np.loadtxt('./case{}/Result_LES32_F-IUFNO_35ep_gap200_mag0.1/post_result/vel_parameter.dat'.format(case_n+1),dtype=float, comments=['step'])
    IUFNO_ic1_PDFs = np.loadtxt('./case{}/Result_LES32_F-IUFNO_35ep_gap200_mag0.1/post_result/inc1_PDFs.dat'.format(case_n + 1), dtype=float,comments=['step'])
    IUFNO_spec = np.loadtxt('./case{}/Result_LES32_F-IUFNO_35ep_gap200_mag0.1/post_result/spectrum_vel.dat'.format(case_n + 1), dtype=float,comments=['variables', 'zone'])
    IUFNO_structrue2 = np.loadtxt('./case{}/Result_LES32_F-IUFNO_35ep_gap200_mag0.1/post_result/structure2.dat'.format(case_n + 1),dtype=float, comments=['step'])
    IUFNO_structrue4 = np.loadtxt('./case{}/Result_LES32_F-IUFNO_35ep_gap200_mag0.1/post_result/structure4.dat'.format(case_n + 1),dtype=float, comments=['step'])
    IUFNO_vort_PDFs = np.loadtxt('./case{}/Result_LES32_F-IUFNO_35ep_gap200_mag0.1/post_result/vort_PDFs.dat'.format(case_n + 1), dtype=float,comments=['variables', 'zone'])
    IUFNO_vort_statistics = np.loadtxt('./case{}/Result_LES32_F-IUFNO_35ep_gap200_mag0.1/post_result/vort_statistics.dat'.format(case_n + 1),dtype=float, comments=['step'])
    # print(VGM.shape)
    # 取出数据
    x_IUFNO_urms.append(IUFNO_vel_parameter[:,0])  # 只取出第一列数据
    y_IUFNO_urms.append(IUFNO_vel_parameter[:,3]) #只取出第二列数据
    x_IUFNO_wrms.append(IUFNO_vel_parameter[:,0])  # 只取出第一列数据
    y_IUFNO_wrms.append(IUFNO_vel_parameter[:,7]) #只取出第二列数据
    x_IUFNO_dissipation.append(IUFNO_vel_parameter[:,0])  # 只取出第一列数据
    y_IUFNO_dissipation.append(IUFNO_vel_parameter[:,8]) #只取出第二列数据
    x_IUFNO_Et.append(IUFNO_vel_parameter[:,0])  # 只取出第一列数据
    y_IUFNO_Et.append(IUFNO_vel_parameter[:,6]) #只取出第二列数据
    x_IUFNO_inc1_PDFs.append(IUFNO_ic1_PDFs[:,0])  # 只取出第一列数据
    y_IUFNO_inc1_PDFs.append(IUFNO_ic1_PDFs[:,1]) #只取出第二列数据
    x_IUFNO_velspectrum.append(IUFNO_spec[:,0])  # 只取出第一列数据
    y_IUFNO_velspectrum.append(IUFNO_spec[:,1]) #只取出第二列数据
    x_IUFNO_structrue2.append(IUFNO_structrue2[:,0])  # 只取出第一列数据
    y_IUFNO_structrue2.append(IUFNO_structrue2[:,1]) #只取出第二列数据
    x_IUFNO_structrue4.append(IUFNO_structrue4[:,0])  # 只取出第一列数据
    y_IUFNO_structrue4.append(IUFNO_structrue4[:,1]) #只取出第二列数据
    x_IUFNO_vort_PDFs.append(IUFNO_vort_PDFs[:,0])  # 只取出第一列数据
    y_IUFNO_vort_PDFs.append(IUFNO_vort_PDFs[:,1]) #只取出第二列数据
    x_IUFNO_vort_statistics.append(IUFNO_vort_statistics[:,0])  # 只取出第一列数据
    y_IUFNO_vort_statistics.append(IUFNO_vort_statistics[:,5]) #只取出第二列数据
# 转化为数组
x_IUFNO_urms_arr = np.asarray(x_IUFNO_urms) #列表转数组
y_IUFNO_urms_arr = np.asarray(y_IUFNO_urms) #列表转数组
x_IUFNO_wrms_arr = np.asarray(x_IUFNO_wrms) #列表转数组
y_IUFNO_wrms_arr = np.asarray(y_IUFNO_wrms) #列表转数组
x_IUFNO_dissipation_arr = np.asarray(x_IUFNO_dissipation) #列表转数组
y_IUFNO_dissipation_arr = np.asarray(y_IUFNO_dissipation) #列表转数组
x_IUFNO_Et_arr = np.asarray(x_IUFNO_Et) #列表转数组
y_IUFNO_Et_arr = np.asarray(y_IUFNO_Et) #列表转数组
x_IUFNO_inc1_PDFs_arr = np.asarray(x_IUFNO_inc1_PDFs) #列表转数组
y_IUFNO_inc1_PDFs_arr = np.asarray(y_IUFNO_inc1_PDFs) #列表转数组
x_IUFNO_spe_arr = np.asarray(x_IUFNO_velspectrum) #列表转数组
y_IUFNO_spe_arr = np.asarray(y_IUFNO_velspectrum) #列表转数组
x_IUFNO_structrue2 = np.asarray(x_IUFNO_structrue2) #列表转数组
y_IUFNO_structrue2 = np.asarray(y_IUFNO_structrue2) #列表转数组
x_IUFNO_structrue4 = np.asarray(x_IUFNO_structrue4) #列表转数组
y_IUFNO_structrue4 = np.asarray(y_IUFNO_structrue4) #列表转数组
x_IUFNO_vort_PDFs = np.asarray(x_IUFNO_vort_PDFs) #列表转数组
y_IUFNO_vort_PDFs = np.asarray(y_IUFNO_vort_PDFs) #列表转数组
x_IUFNO_vort_statistics = np.asarray(x_IUFNO_vort_statistics) #列表转数组
y_IUFNO_vort_statistics = np.asarray(y_IUFNO_vort_statistics) #列表转数组
# 取均值
x_urms_avg_case = np.mean(x_IUFNO_urms_arr,0) #行压缩成一行
y_urms_avg_case = np.mean(y_IUFNO_urms_arr,0) #行压缩成一行
x_wrms_avg_case = np.mean(x_IUFNO_wrms_arr,0) #行压缩成一行
y_wrms_avg_case = np.mean(y_IUFNO_wrms_arr,0) #行压缩成一行
x_dissipation_avg_case = np.mean(x_IUFNO_dissipation_arr,0) #行压缩成一行
y_dissipation_avg_case = np.mean(y_IUFNO_dissipation_arr,0) #行压缩成一行
x_Et_avg_case = np.mean(x_IUFNO_Et_arr,0) #行压缩成一行
y_Et_avg_case = np.mean(y_IUFNO_Et_arr,0) #行压缩成一行
x_inc1_PDFs_avg_case = np.mean(x_IUFNO_inc1_PDFs_arr,0) #行压缩成一行
y_inc1_PDFs_avg_case = np.mean(y_IUFNO_inc1_PDFs_arr,0) #行压缩成一行
x_spe_avg_case = np.mean(x_IUFNO_spe_arr,0) #行压缩成一行
y_spe_avg_case = np.mean(y_IUFNO_spe_arr,0) #行压缩成一行
x_structrue2_avg_case = np.mean(x_IUFNO_structrue2,0) #行压缩成一行
y_structrue2_avg_case = np.mean(y_IUFNO_structrue2,0) #行压缩成
x_structrue4_avg_case = np.mean(x_IUFNO_structrue4,0) #行压缩成一行
y_structrue4_avg_case = np.mean(y_IUFNO_structrue4,0) #行压缩成
x_vort_PDFs_avg_case = np.mean(x_IUFNO_vort_PDFs,0) #行压缩成一行
y_vort_PDFs_avg_case = np.mean(y_IUFNO_vort_PDFs,0) #行压缩成
x_vort_statistics_avg_case = np.mean(x_IUFNO_vort_statistics,0) #行压缩成一行
y_vort_statistics_avg_case = np.mean(y_IUFNO_vort_statistics,0) #行压缩成
# 拼接操作
avg_IUFNO_urms_10case=np.dstack((x_urms_avg_case,y_urms_avg_case)).squeeze() #拼接
avg_IUFNO_wrms_10case=np.dstack((x_wrms_avg_case,y_wrms_avg_case)).squeeze() #拼接
avg_IUFNO_dissipation_10case=np.dstack((x_dissipation_avg_case,y_dissipation_avg_case)).squeeze() #拼接
avg_IUFNO_Et_10case=np.dstack((x_Et_avg_case,y_Et_avg_case)).squeeze() #拼接
avg_IUFNO_inc1_PDFs_10case=np.dstack((x_inc1_PDFs_avg_case,y_inc1_PDFs_avg_case)).squeeze() #拼接
avg_IUFNO_spectrum_10case=np.dstack((x_spe_avg_case,y_spe_avg_case)).squeeze() #拼接
avg_IUFNO_structrue2_10case=np.dstack((x_structrue2_avg_case,y_structrue2_avg_case)).squeeze() #拼接
avg_IUFNO_structrue4_10case=np.dstack((x_structrue4_avg_case,y_structrue4_avg_case)).squeeze() #拼接
avg_IUFNO_vort_PDFs_10case=np.dstack((x_vort_PDFs_avg_case,y_vort_PDFs_avg_case)).squeeze() #拼接
avg_IUFNO_vort_statistics_10case=np.dstack((x_vort_statistics_avg_case,y_vort_statistics_avg_case)).squeeze() #拼接
#导出均值

np.savetxt('./AVG/F-IUFNO_35ep_mag0.1/N{}/avg_FIUFNO_{}case_urms.dat'.format(case_number,case_number),avg_IUFNO_urms_10case, fmt="%16.7f")
np.savetxt('./AVG/F-IUFNO_35ep_mag0.1/N{}/avg_FIUFNO_{}case_wrms.dat'.format(case_number,case_number),avg_IUFNO_wrms_10case, fmt="%16.7f")
np.savetxt('./AVG/F-IUFNO_35ep_mag0.1/N{}/avg_FIUFNO_{}case_dissipation.dat'.format(case_number,case_number),avg_IUFNO_dissipation_10case, fmt="%16.7f")
np.savetxt('./AVG/F-IUFNO_35ep_mag0.1/N{}/avg_FIUFNO_{}case_Ek_t.dat'.format(case_number,case_number),avg_IUFNO_Et_10case, fmt="%16.7f")
np.savetxt('./AVG/F-IUFNO_35ep_mag0.1/N{}/avg_FIUFNO_{}case_inc1_PDFs.dat'.format(case_number,case_number),avg_IUFNO_inc1_PDFs_10case, fmt="%16.7f")
np.savetxt('./AVG/F-IUFNO_35ep_mag0.1/N{}/avg_FIUFNO_{}case_vel_spec.dat'.format(case_number,case_number),avg_IUFNO_spectrum_10case, fmt="%16.7f")
np.savetxt('./AVG/F-IUFNO_35ep_mag0.1/N{}/avg_FIUFNO_{}case_structrue2.dat'.format(case_number,case_number),avg_IUFNO_structrue2_10case, fmt="%16.7f")
np.savetxt('./AVG/F-IUFNO_35ep_mag0.1/N{}/avg_FIUFNO_{}case_structrue4.dat'.format(case_number,case_number),avg_IUFNO_structrue4_10case, fmt="%16.7f")
np.savetxt('./AVG/F-IUFNO_35ep_mag0.1/N{}/avg_FIUFNO_{}case_vort_PDFs.dat'.format(case_number,case_number),avg_IUFNO_vort_PDFs_10case, fmt="%16.7f")
np.savetxt('./AVG/F-IUFNO_35ep_mag0.1/N{}/avg_FIUFNO_{}case_vort_statistics.dat'.format(case_number,case_number),avg_IUFNO_vort_statistics_10case, fmt="%16.7f")
'''
np.savetxt('./AVG/F-IUFNO_35ep_mag0.1/{}case/avg_FIUFNO_{}case_urms.dat'.format(case_number,case_number),avg_IUFNO_urms_10case, fmt="%16.7f")
np.savetxt('./AVG/F-IUFNO_35ep_mag0.1/{}case/avg_FIUFNO_{}case_wrms.dat'.format(case_number,case_number),avg_IUFNO_wrms_10case, fmt="%16.7f")
np.savetxt('./AVG/F-IUFNO_35ep_mag0.1/{}case/avg_FIUFNO_{}case_dissipation.dat'.format(case_number,case_number),avg_IUFNO_dissipation_10case, fmt="%16.7f")
np.savetxt('./AVG/F-IUFNO_35ep_mag0.1/{}case/avg_FIUFNO_{}case_Ek_t.dat'.format(case_number,case_number),avg_IUFNO_Et_10case, fmt="%16.7f")
np.savetxt('./AVG/F-IUFNO_35ep_mag0.1/{}case/avg_FIUFNO_{}case_inc1_PDFs.dat'.format(case_number,case_number),avg_IUFNO_inc1_PDFs_10case, fmt="%16.7f")
np.savetxt('./AVG/F-IUFNO_35ep_mag0.1/{}case/avg_FIUFNO_{}case_vel_spec.dat'.format(case_number,case_number),avg_IUFNO_spectrum_10case, fmt="%16.7f")
np.savetxt('./AVG/F-IUFNO_35ep_mag0.1/{}case/avg_FIUFNO_{}case_structrue2.dat'.format(case_number,case_number),avg_IUFNO_structrue2_10case, fmt="%16.7f")
np.savetxt('./AVG/F-IUFNO_35ep_mag0.1/{}case/avg_FIUFNO_{}case_structrue4.dat'.format(case_number,case_number),avg_IUFNO_structrue4_10case, fmt="%16.7f")
np.savetxt('./AVG/F-IUFNO_35ep_mag0.1/{}case/avg_FIUFNO_{}case_vort_PDFs.dat'.format(case_number,case_number),avg_IUFNO_vort_PDFs_10case, fmt="%16.7f")
np.savetxt('./AVG/F-IUFNO_35ep_mag0.1/{}case/avg_FIUFNO_{}case_vort_statistics.dat'.format(case_number,case_number),avg_IUFNO_vort_statistics_10case, fmt="%16.7f")
'''

#==========================================================================FNO
print("F-IUFNO_35ep_mag0.5 getting dat!")
x_IUFNO_dissipation=[]
y_IUFNO_dissipation=[]
x_IUFNO_Et=[]
y_IUFNO_Et=[]
x_IUFNO_inc1_PDFs=[]
y_IUFNO_inc1_PDFs=[]
x_IUFNO_velspectrum=[]
y_IUFNO_velspectrum=[]
x_IUFNO_structrue2 = []
y_IUFNO_structrue2 = []
x_IUFNO_structrue4 = []
y_IUFNO_structrue4 = []
x_IUFNO_urms = []
y_IUFNO_urms = []
x_IUFNO_wrms = []
y_IUFNO_wrms = []
x_IUFNO_vort_PDFs = []
y_IUFNO_vort_PDFs = []
x_IUFNO_vort_statistics = []
y_IUFNO_vort_statistics = []
for case_n in range(case_number-1,case_number):
    # print(case_n)
    # 载入后处理文件，包括速度参数，PDFs，能谱，结构函数
    IUFNO_vel_parameter= np.loadtxt('./case{}/Result_LES32_F-IUFNO_35ep_gap200_mag0.5/post_result/vel_parameter.dat'.format(case_n+1),dtype=float, comments=['step'])
    IUFNO_ic1_PDFs = np.loadtxt('./case{}/Result_LES32_F-IUFNO_35ep_gap200_mag0.5/post_result/inc1_PDFs.dat'.format(case_n + 1), dtype=float,comments=['step'])
    IUFNO_spec = np.loadtxt('./case{}/Result_LES32_F-IUFNO_35ep_gap200_mag0.5/post_result/spectrum_vel.dat'.format(case_n + 1), dtype=float,comments=['variables', 'zone'])
    IUFNO_structrue2 = np.loadtxt('./case{}/Result_LES32_F-IUFNO_35ep_gap200_mag0.5/post_result/structure2.dat'.format(case_n + 1),dtype=float, comments=['step'])
    IUFNO_structrue4 = np.loadtxt('./case{}/Result_LES32_F-IUFNO_35ep_gap200_mag0.5/post_result/structure4.dat'.format(case_n + 1),dtype=float, comments=['step'])
    IUFNO_vort_PDFs = np.loadtxt('./case{}/Result_LES32_F-IUFNO_35ep_gap200_mag0.5/post_result/vort_PDFs.dat'.format(case_n + 1), dtype=float,comments=['variables', 'zone'])
    IUFNO_vort_statistics = np.loadtxt('./case{}/Result_LES32_F-IUFNO_35ep_gap200_mag0.5/post_result/vort_statistics.dat'.format(case_n + 1),dtype=float, comments=['step'])
    # print(VGM.shape)
    # 取出数据
    x_IUFNO_urms.append(IUFNO_vel_parameter[:,0])  # 只取出第一列数据
    y_IUFNO_urms.append(IUFNO_vel_parameter[:,3]) #只取出第二列数据
    x_IUFNO_wrms.append(IUFNO_vel_parameter[:,0])  # 只取出第一列数据
    y_IUFNO_wrms.append(IUFNO_vel_parameter[:,7]) #只取出第二列数据
    x_IUFNO_dissipation.append(IUFNO_vel_parameter[:,0])  # 只取出第一列数据
    y_IUFNO_dissipation.append(IUFNO_vel_parameter[:,8]) #只取出第二列数据
    x_IUFNO_Et.append(IUFNO_vel_parameter[:,0])  # 只取出第一列数据
    y_IUFNO_Et.append(IUFNO_vel_parameter[:,6]) #只取出第二列数据
    x_IUFNO_inc1_PDFs.append(IUFNO_ic1_PDFs[:,0])  # 只取出第一列数据
    y_IUFNO_inc1_PDFs.append(IUFNO_ic1_PDFs[:,1]) #只取出第二列数据
    x_IUFNO_velspectrum.append(IUFNO_spec[:,0])  # 只取出第一列数据
    y_IUFNO_velspectrum.append(IUFNO_spec[:,1]) #只取出第二列数据
    x_IUFNO_structrue2.append(IUFNO_structrue2[:,0])  # 只取出第一列数据
    y_IUFNO_structrue2.append(IUFNO_structrue2[:,1]) #只取出第二列数据
    x_IUFNO_structrue4.append(IUFNO_structrue4[:,0])  # 只取出第一列数据
    y_IUFNO_structrue4.append(IUFNO_structrue4[:,1]) #只取出第二列数据
    x_IUFNO_vort_PDFs.append(IUFNO_vort_PDFs[:,0])  # 只取出第一列数据
    y_IUFNO_vort_PDFs.append(IUFNO_vort_PDFs[:,1]) #只取出第二列数据
    x_IUFNO_vort_statistics.append(IUFNO_vort_statistics[:,0])  # 只取出第一列数据
    y_IUFNO_vort_statistics.append(IUFNO_vort_statistics[:,5]) #只取出第二列数据
# 转化为数组
x_IUFNO_urms_arr = np.asarray(x_IUFNO_urms) #列表转数组
y_IUFNO_urms_arr = np.asarray(y_IUFNO_urms) #列表转数组
x_IUFNO_wrms_arr = np.asarray(x_IUFNO_wrms) #列表转数组
y_IUFNO_wrms_arr = np.asarray(y_IUFNO_wrms) #列表转数组
x_IUFNO_dissipation_arr = np.asarray(x_IUFNO_dissipation) #列表转数组
y_IUFNO_dissipation_arr = np.asarray(y_IUFNO_dissipation) #列表转数组
x_IUFNO_Et_arr = np.asarray(x_IUFNO_Et) #列表转数组
y_IUFNO_Et_arr = np.asarray(y_IUFNO_Et) #列表转数组
x_IUFNO_inc1_PDFs_arr = np.asarray(x_IUFNO_inc1_PDFs) #列表转数组
y_IUFNO_inc1_PDFs_arr = np.asarray(y_IUFNO_inc1_PDFs) #列表转数组
x_IUFNO_spe_arr = np.asarray(x_IUFNO_velspectrum) #列表转数组
y_IUFNO_spe_arr = np.asarray(y_IUFNO_velspectrum) #列表转数组
x_IUFNO_structrue2 = np.asarray(x_IUFNO_structrue2) #列表转数组
y_IUFNO_structrue2 = np.asarray(y_IUFNO_structrue2) #列表转数组
x_IUFNO_structrue4 = np.asarray(x_IUFNO_structrue4) #列表转数组
y_IUFNO_structrue4 = np.asarray(y_IUFNO_structrue4) #列表转数组
x_IUFNO_vort_PDFs = np.asarray(x_IUFNO_vort_PDFs) #列表转数组
y_IUFNO_vort_PDFs = np.asarray(y_IUFNO_vort_PDFs) #列表转数组
x_IUFNO_vort_statistics = np.asarray(x_IUFNO_vort_statistics) #列表转数组
y_IUFNO_vort_statistics = np.asarray(y_IUFNO_vort_statistics) #列表转数组
# 取均值
x_urms_avg_case = np.mean(x_IUFNO_urms_arr,0) #行压缩成一行
y_urms_avg_case = np.mean(y_IUFNO_urms_arr,0) #行压缩成一行
x_wrms_avg_case = np.mean(x_IUFNO_wrms_arr,0) #行压缩成一行
y_wrms_avg_case = np.mean(y_IUFNO_wrms_arr,0) #行压缩成一行
x_dissipation_avg_case = np.mean(x_IUFNO_dissipation_arr,0) #行压缩成一行
y_dissipation_avg_case = np.mean(y_IUFNO_dissipation_arr,0) #行压缩成一行
x_Et_avg_case = np.mean(x_IUFNO_Et_arr,0) #行压缩成一行
y_Et_avg_case = np.mean(y_IUFNO_Et_arr,0) #行压缩成一行
x_inc1_PDFs_avg_case = np.mean(x_IUFNO_inc1_PDFs_arr,0) #行压缩成一行
y_inc1_PDFs_avg_case = np.mean(y_IUFNO_inc1_PDFs_arr,0) #行压缩成一行
x_spe_avg_case = np.mean(x_IUFNO_spe_arr,0) #行压缩成一行
y_spe_avg_case = np.mean(y_IUFNO_spe_arr,0) #行压缩成一行
x_structrue2_avg_case = np.mean(x_IUFNO_structrue2,0) #行压缩成一行
y_structrue2_avg_case = np.mean(y_IUFNO_structrue2,0) #行压缩成
x_structrue4_avg_case = np.mean(x_IUFNO_structrue4,0) #行压缩成一行
y_structrue4_avg_case = np.mean(y_IUFNO_structrue4,0) #行压缩成
x_vort_PDFs_avg_case = np.mean(x_IUFNO_vort_PDFs,0) #行压缩成一行
y_vort_PDFs_avg_case = np.mean(y_IUFNO_vort_PDFs,0) #行压缩成
x_vort_statistics_avg_case = np.mean(x_IUFNO_vort_statistics,0) #行压缩成一行
y_vort_statistics_avg_case = np.mean(y_IUFNO_vort_statistics,0) #行压缩成
# 拼接操作
avg_IUFNO_urms_10case=np.dstack((x_urms_avg_case,y_urms_avg_case)).squeeze() #拼接
avg_IUFNO_wrms_10case=np.dstack((x_wrms_avg_case,y_wrms_avg_case)).squeeze() #拼接
avg_IUFNO_dissipation_10case=np.dstack((x_dissipation_avg_case,y_dissipation_avg_case)).squeeze() #拼接
avg_IUFNO_Et_10case=np.dstack((x_Et_avg_case,y_Et_avg_case)).squeeze() #拼接
avg_IUFNO_inc1_PDFs_10case=np.dstack((x_inc1_PDFs_avg_case,y_inc1_PDFs_avg_case)).squeeze() #拼接
avg_IUFNO_spectrum_10case=np.dstack((x_spe_avg_case,y_spe_avg_case)).squeeze() #拼接
avg_IUFNO_structrue2_10case=np.dstack((x_structrue2_avg_case,y_structrue2_avg_case)).squeeze() #拼接
avg_IUFNO_structrue4_10case=np.dstack((x_structrue4_avg_case,y_structrue4_avg_case)).squeeze() #拼接
avg_IUFNO_vort_PDFs_10case=np.dstack((x_vort_PDFs_avg_case,y_vort_PDFs_avg_case)).squeeze() #拼接
avg_IUFNO_vort_statistics_10case=np.dstack((x_vort_statistics_avg_case,y_vort_statistics_avg_case)).squeeze() #拼接
#导出均值

np.savetxt('./AVG/F-IUFNO_35ep_mag0.5/N{}/avg_FIUFNO_{}case_urms.dat'.format(case_number,case_number),avg_IUFNO_urms_10case, fmt="%16.7f")
np.savetxt('./AVG/F-IUFNO_35ep_mag0.5/N{}/avg_FIUFNO_{}case_wrms.dat'.format(case_number,case_number),avg_IUFNO_wrms_10case, fmt="%16.7f")
np.savetxt('./AVG/F-IUFNO_35ep_mag0.5/N{}/avg_FIUFNO_{}case_dissipation.dat'.format(case_number,case_number),avg_IUFNO_dissipation_10case, fmt="%16.7f")
np.savetxt('./AVG/F-IUFNO_35ep_mag0.5/N{}/avg_FIUFNO_{}case_Ek_t.dat'.format(case_number,case_number),avg_IUFNO_Et_10case, fmt="%16.7f")
np.savetxt('./AVG/F-IUFNO_35ep_mag0.5/N{}/avg_FIUFNO_{}case_inc1_PDFs.dat'.format(case_number,case_number),avg_IUFNO_inc1_PDFs_10case, fmt="%16.7f")
np.savetxt('./AVG/F-IUFNO_35ep_mag0.5/N{}/avg_FIUFNO_{}case_vel_spec.dat'.format(case_number,case_number),avg_IUFNO_spectrum_10case, fmt="%16.7f")
np.savetxt('./AVG/F-IUFNO_35ep_mag0.5/N{}/avg_FIUFNO_{}case_structrue2.dat'.format(case_number,case_number),avg_IUFNO_structrue2_10case, fmt="%16.7f")
np.savetxt('./AVG/F-IUFNO_35ep_mag0.5/N{}/avg_FIUFNO_{}case_structrue4.dat'.format(case_number,case_number),avg_IUFNO_structrue4_10case, fmt="%16.7f")
np.savetxt('./AVG/F-IUFNO_35ep_mag0.5/N{}/avg_FIUFNO_{}case_vort_PDFs.dat'.format(case_number,case_number),avg_IUFNO_vort_PDFs_10case, fmt="%16.7f")
np.savetxt('./AVG/F-IUFNO_35ep_mag0.5/N{}/avg_FIUFNO_{}case_vort_statistics.dat'.format(case_number,case_number),avg_IUFNO_vort_statistics_10case, fmt="%16.7f")
'''
np.savetxt('./AVG/F-IUFNO_35ep_mag0.5/{}case/avg_FIUFNO_{}case_urms.dat'.format(case_number,case_number),avg_IUFNO_urms_10case, fmt="%16.7f")
np.savetxt('./AVG/F-IUFNO_35ep_mag0.5/{}case/avg_FIUFNO_{}case_wrms.dat'.format(case_number,case_number),avg_IUFNO_wrms_10case, fmt="%16.7f")
np.savetxt('./AVG/F-IUFNO_35ep_mag0.5/{}case/avg_FIUFNO_{}case_dissipation.dat'.format(case_number,case_number),avg_IUFNO_dissipation_10case, fmt="%16.7f")
np.savetxt('./AVG/F-IUFNO_35ep_mag0.5/{}case/avg_FIUFNO_{}case_Ek_t.dat'.format(case_number,case_number),avg_IUFNO_Et_10case, fmt="%16.7f")
np.savetxt('./AVG/F-IUFNO_35ep_mag0.5/{}case/avg_FIUFNO_{}case_inc1_PDFs.dat'.format(case_number,case_number),avg_IUFNO_inc1_PDFs_10case, fmt="%16.7f")
np.savetxt('./AVG/F-IUFNO_35ep_mag0.5/{}case/avg_FIUFNO_{}case_vel_spec.dat'.format(case_number,case_number),avg_IUFNO_spectrum_10case, fmt="%16.7f")
np.savetxt('./AVG/F-IUFNO_35ep_mag0.5/{}case/avg_FIUFNO_{}case_structrue2.dat'.format(case_number,case_number),avg_IUFNO_structrue2_10case, fmt="%16.7f")
np.savetxt('./AVG/F-IUFNO_35ep_mag0.5/{}case/avg_FIUFNO_{}case_structrue4.dat'.format(case_number,case_number),avg_IUFNO_structrue4_10case, fmt="%16.7f")
np.savetxt('./AVG/F-IUFNO_35ep_mag0.5/{}case/avg_FIUFNO_{}case_vort_PDFs.dat'.format(case_number,case_number),avg_IUFNO_vort_PDFs_10case, fmt="%16.7f")
np.savetxt('./AVG/F-IUFNO_35ep_mag0.5/{}case/avg_FIUFNO_{}case_vort_statistics.dat'.format(case_number,case_number),avg_IUFNO_vort_statistics_10case, fmt="%16.7f")

'''
#==========================================================================FNO
print("F-IFNO_40ep getting dat!")
x_IUFNO_dissipation=[]
y_IUFNO_dissipation=[]
x_IUFNO_Et=[]
y_IUFNO_Et=[]
x_IUFNO_inc1_PDFs=[]
y_IUFNO_inc1_PDFs=[]
x_IUFNO_velspectrum=[]
y_IUFNO_velspectrum=[]
x_IUFNO_structrue2 = []
y_IUFNO_structrue2 = []
x_IUFNO_structrue4 = []
y_IUFNO_structrue4 = []
x_IUFNO_urms = []
y_IUFNO_urms = []
x_IUFNO_wrms = []
y_IUFNO_wrms = []
x_IUFNO_vort_PDFs = []
y_IUFNO_vort_PDFs = []
x_IUFNO_vort_statistics = []
y_IUFNO_vort_statistics = []
for case_n in range(case_number-1,case_number):
    # print(case_n)
    # 载入后处理文件，包括速度参数，PDFs，能谱，结构函数
    IUFNO_vel_parameter= np.loadtxt('./case{}/Result_LES32_F-IFNO_40ep_gap200/post_result/vel_parameter.dat'.format(case_n+1),dtype=float, comments=['step'])
    IUFNO_ic1_PDFs = np.loadtxt('./case{}/Result_LES32_F-IFNO_40ep_gap200/post_result/inc1_PDFs.dat'.format(case_n + 1), dtype=float,comments=['step'])
    IUFNO_spec = np.loadtxt('./case{}/Result_LES32_F-IFNO_40ep_gap200/post_result/spectrum_vel.dat'.format(case_n + 1), dtype=float,comments=['variables', 'zone'])
    IUFNO_structrue2 = np.loadtxt('./case{}/Result_LES32_F-IFNO_40ep_gap200/post_result/structure2.dat'.format(case_n + 1),dtype=float, comments=['step'])
    IUFNO_structrue4 = np.loadtxt('./case{}/Result_LES32_F-IFNO_40ep_gap200/post_result/structure4.dat'.format(case_n + 1),dtype=float, comments=['step'])
    IUFNO_vort_PDFs = np.loadtxt('./case{}/Result_LES32_F-IFNO_40ep_gap200/post_result/vort_PDFs.dat'.format(case_n + 1), dtype=float,comments=['variables', 'zone'])
    IUFNO_vort_statistics = np.loadtxt('./case{}/Result_LES32_F-IFNO_40ep_gap200/post_result/vort_statistics.dat'.format(case_n + 1),dtype=float, comments=['step'])
    # print(VGM.shape)
    # 取出数据
    x_IUFNO_urms.append(IUFNO_vel_parameter[:,0])  # 只取出第一列数据
    y_IUFNO_urms.append(IUFNO_vel_parameter[:,3]) #只取出第二列数据
    x_IUFNO_wrms.append(IUFNO_vel_parameter[:,0])  # 只取出第一列数据
    y_IUFNO_wrms.append(IUFNO_vel_parameter[:,7]) #只取出第二列数据
    x_IUFNO_dissipation.append(IUFNO_vel_parameter[:,0])  # 只取出第一列数据
    y_IUFNO_dissipation.append(IUFNO_vel_parameter[:,8]) #只取出第二列数据
    x_IUFNO_Et.append(IUFNO_vel_parameter[:,0])  # 只取出第一列数据
    y_IUFNO_Et.append(IUFNO_vel_parameter[:,6]) #只取出第二列数据
    x_IUFNO_inc1_PDFs.append(IUFNO_ic1_PDFs[:,0])  # 只取出第一列数据
    y_IUFNO_inc1_PDFs.append(IUFNO_ic1_PDFs[:,1]) #只取出第二列数据
    x_IUFNO_velspectrum.append(IUFNO_spec[:,0])  # 只取出第一列数据
    y_IUFNO_velspectrum.append(IUFNO_spec[:,1]) #只取出第二列数据
    x_IUFNO_structrue2.append(IUFNO_structrue2[:,0])  # 只取出第一列数据
    y_IUFNO_structrue2.append(IUFNO_structrue2[:,1]) #只取出第二列数据
    x_IUFNO_structrue4.append(IUFNO_structrue4[:,0])  # 只取出第一列数据
    y_IUFNO_structrue4.append(IUFNO_structrue4[:,1]) #只取出第二列数据
    x_IUFNO_vort_PDFs.append(IUFNO_vort_PDFs[:,0])  # 只取出第一列数据
    y_IUFNO_vort_PDFs.append(IUFNO_vort_PDFs[:,1]) #只取出第二列数据
    x_IUFNO_vort_statistics.append(IUFNO_vort_statistics[:,0])  # 只取出第一列数据
    y_IUFNO_vort_statistics.append(IUFNO_vort_statistics[:,5]) #只取出第二列数据
# 转化为数组
x_IUFNO_urms_arr = np.asarray(x_IUFNO_urms) #列表转数组
y_IUFNO_urms_arr = np.asarray(y_IUFNO_urms) #列表转数组
x_IUFNO_wrms_arr = np.asarray(x_IUFNO_wrms) #列表转数组
y_IUFNO_wrms_arr = np.asarray(y_IUFNO_wrms) #列表转数组
x_IUFNO_dissipation_arr = np.asarray(x_IUFNO_dissipation) #列表转数组
y_IUFNO_dissipation_arr = np.asarray(y_IUFNO_dissipation) #列表转数组
x_IUFNO_Et_arr = np.asarray(x_IUFNO_Et) #列表转数组
y_IUFNO_Et_arr = np.asarray(y_IUFNO_Et) #列表转数组
x_IUFNO_inc1_PDFs_arr = np.asarray(x_IUFNO_inc1_PDFs) #列表转数组
y_IUFNO_inc1_PDFs_arr = np.asarray(y_IUFNO_inc1_PDFs) #列表转数组
x_IUFNO_spe_arr = np.asarray(x_IUFNO_velspectrum) #列表转数组
y_IUFNO_spe_arr = np.asarray(y_IUFNO_velspectrum) #列表转数组
x_IUFNO_structrue2 = np.asarray(x_IUFNO_structrue2) #列表转数组
y_IUFNO_structrue2 = np.asarray(y_IUFNO_structrue2) #列表转数组
x_IUFNO_structrue4 = np.asarray(x_IUFNO_structrue4) #列表转数组
y_IUFNO_structrue4 = np.asarray(y_IUFNO_structrue4) #列表转数组
x_IUFNO_vort_PDFs = np.asarray(x_IUFNO_vort_PDFs) #列表转数组
y_IUFNO_vort_PDFs = np.asarray(y_IUFNO_vort_PDFs) #列表转数组
x_IUFNO_vort_statistics = np.asarray(x_IUFNO_vort_statistics) #列表转数组
y_IUFNO_vort_statistics = np.asarray(y_IUFNO_vort_statistics) #列表转数组
# 取均值
x_urms_avg_case = np.mean(x_IUFNO_urms_arr,0) #行压缩成一行
y_urms_avg_case = np.mean(y_IUFNO_urms_arr,0) #行压缩成一行
x_wrms_avg_case = np.mean(x_IUFNO_wrms_arr,0) #行压缩成一行
y_wrms_avg_case = np.mean(y_IUFNO_wrms_arr,0) #行压缩成一行
x_dissipation_avg_case = np.mean(x_IUFNO_dissipation_arr,0) #行压缩成一行
y_dissipation_avg_case = np.mean(y_IUFNO_dissipation_arr,0) #行压缩成一行
x_Et_avg_case = np.mean(x_IUFNO_Et_arr,0) #行压缩成一行
y_Et_avg_case = np.mean(y_IUFNO_Et_arr,0) #行压缩成一行
x_inc1_PDFs_avg_case = np.mean(x_IUFNO_inc1_PDFs_arr,0) #行压缩成一行
y_inc1_PDFs_avg_case = np.mean(y_IUFNO_inc1_PDFs_arr,0) #行压缩成一行
x_spe_avg_case = np.mean(x_IUFNO_spe_arr,0) #行压缩成一行
y_spe_avg_case = np.mean(y_IUFNO_spe_arr,0) #行压缩成一行
x_structrue2_avg_case = np.mean(x_IUFNO_structrue2,0) #行压缩成一行
y_structrue2_avg_case = np.mean(y_IUFNO_structrue2,0) #行压缩成
x_structrue4_avg_case = np.mean(x_IUFNO_structrue4,0) #行压缩成一行
y_structrue4_avg_case = np.mean(y_IUFNO_structrue4,0) #行压缩成
x_vort_PDFs_avg_case = np.mean(x_IUFNO_vort_PDFs,0) #行压缩成一行
y_vort_PDFs_avg_case = np.mean(y_IUFNO_vort_PDFs,0) #行压缩成
x_vort_statistics_avg_case = np.mean(x_IUFNO_vort_statistics,0) #行压缩成一行
y_vort_statistics_avg_case = np.mean(y_IUFNO_vort_statistics,0) #行压缩成
# 拼接操作
avg_IUFNO_urms_10case=np.dstack((x_urms_avg_case,y_urms_avg_case)).squeeze() #拼接
avg_IUFNO_wrms_10case=np.dstack((x_wrms_avg_case,y_wrms_avg_case)).squeeze() #拼接
avg_IUFNO_dissipation_10case=np.dstack((x_dissipation_avg_case,y_dissipation_avg_case)).squeeze() #拼接
avg_IUFNO_Et_10case=np.dstack((x_Et_avg_case,y_Et_avg_case)).squeeze() #拼接
avg_IUFNO_inc1_PDFs_10case=np.dstack((x_inc1_PDFs_avg_case,y_inc1_PDFs_avg_case)).squeeze() #拼接
avg_IUFNO_spectrum_10case=np.dstack((x_spe_avg_case,y_spe_avg_case)).squeeze() #拼接
avg_IUFNO_structrue2_10case=np.dstack((x_structrue2_avg_case,y_structrue2_avg_case)).squeeze() #拼接
avg_IUFNO_structrue4_10case=np.dstack((x_structrue4_avg_case,y_structrue4_avg_case)).squeeze() #拼接
avg_IUFNO_vort_PDFs_10case=np.dstack((x_vort_PDFs_avg_case,y_vort_PDFs_avg_case)).squeeze() #拼接
avg_IUFNO_vort_statistics_10case=np.dstack((x_vort_statistics_avg_case,y_vort_statistics_avg_case)).squeeze() #拼接
#导出均值

np.savetxt('./AVG/F-IFNO_40ep/N{}/avg_FIFNO_{}case_urms.dat'.format(case_number,case_number),avg_IUFNO_urms_10case, fmt="%16.7f")
np.savetxt('./AVG/F-IFNO_40ep/N{}/avg_FIFNO_{}case_wrms.dat'.format(case_number,case_number),avg_IUFNO_wrms_10case, fmt="%16.7f")
np.savetxt('./AVG/F-IFNO_40ep/N{}/avg_FIFNO_{}case_dissipation.dat'.format(case_number,case_number),avg_IUFNO_dissipation_10case, fmt="%16.7f")
np.savetxt('./AVG/F-IFNO_40ep/N{}/avg_FIFNO_{}case_Ek_t.dat'.format(case_number,case_number),avg_IUFNO_Et_10case, fmt="%16.7f")
np.savetxt('./AVG/F-IFNO_40ep/N{}/avg_FIFNO_{}case_inc1_PDFs.dat'.format(case_number,case_number),avg_IUFNO_inc1_PDFs_10case, fmt="%16.7f")
np.savetxt('./AVG/F-IFNO_40ep/N{}/avg_FIFNO_{}case_vel_spec.dat'.format(case_number,case_number),avg_IUFNO_spectrum_10case, fmt="%16.7f")
np.savetxt('./AVG/F-IFNO_40ep/N{}/avg_FIFNO_{}case_structrue2.dat'.format(case_number,case_number),avg_IUFNO_structrue2_10case, fmt="%16.7f")
np.savetxt('./AVG/F-IFNO_40ep/N{}/avg_FIFNO_{}case_structrue4.dat'.format(case_number,case_number),avg_IUFNO_structrue4_10case, fmt="%16.7f")
np.savetxt('./AVG/F-IFNO_40ep/N{}/avg_FIFNO_{}case_vort_PDFs.dat'.format(case_number,case_number),avg_IUFNO_vort_PDFs_10case, fmt="%16.7f")
np.savetxt('./AVG/F-IFNO_40ep/N{}/avg_FIFNO_{}case_vort_statistics.dat'.format(case_number,case_number),avg_IUFNO_vort_statistics_10case, fmt="%16.7f")
'''
np.savetxt('./AVG/F-IFNO_40ep/{}case/avg_FIFNO_{}case_urms.dat'.format(case_number,case_number),avg_IUFNO_urms_10case, fmt="%16.7f")
np.savetxt('./AVG/F-IFNO_40ep/{}case/avg_FIFNO_{}case_wrms.dat'.format(case_number,case_number),avg_IUFNO_wrms_10case, fmt="%16.7f")
np.savetxt('./AVG/F-IFNO_40ep/{}case/avg_FIFNO_{}case_dissipation.dat'.format(case_number,case_number),avg_IUFNO_dissipation_10case, fmt="%16.7f")
np.savetxt('./AVG/F-IFNO_40ep/{}case/avg_FIFNO_{}case_Ek_t.dat'.format(case_number,case_number),avg_IUFNO_Et_10case, fmt="%16.7f")
np.savetxt('./AVG/F-IFNO_40ep/{}case/avg_FIFNO_{}case_inc1_PDFs.dat'.format(case_number,case_number),avg_IUFNO_inc1_PDFs_10case, fmt="%16.7f")
np.savetxt('./AVG/F-IFNO_40ep/{}case/avg_FIFNO_{}case_vel_spec.dat'.format(case_number,case_number),avg_IUFNO_spectrum_10case, fmt="%16.7f")
np.savetxt('./AVG/F-IFNO_40ep/{}case/avg_FIFNO_{}case_structrue2.dat'.format(case_number,case_number),avg_IUFNO_structrue2_10case, fmt="%16.7f")
np.savetxt('./AVG/F-IFNO_40ep/{}case/avg_FIFNO_{}case_structrue4.dat'.format(case_number,case_number),avg_IUFNO_structrue4_10case, fmt="%16.7f")
np.savetxt('./AVG/F-IFNO_40ep/{}case/avg_FIFNO_{}case_vort_PDFs.dat'.format(case_number,case_number),avg_IUFNO_vort_PDFs_10case, fmt="%16.7f")
np.savetxt('./AVG/F-IFNO_40ep/{}case/avg_FIFNO_{}case_vort_statistics.dat'.format(case_number,case_number),avg_IUFNO_vort_statistics_10case, fmt="%16.7f")
'''
#==========================================================================FNO
print("F-IFNO_40ep_mag0.1 getting dat!")
x_IUFNO_dissipation=[]
y_IUFNO_dissipation=[]
x_IUFNO_Et=[]
y_IUFNO_Et=[]
x_IUFNO_inc1_PDFs=[]
y_IUFNO_inc1_PDFs=[]
x_IUFNO_velspectrum=[]
y_IUFNO_velspectrum=[]
x_IUFNO_structrue2 = []
y_IUFNO_structrue2 = []
x_IUFNO_structrue4 = []
y_IUFNO_structrue4 = []
x_IUFNO_urms = []
y_IUFNO_urms = []
x_IUFNO_wrms = []
y_IUFNO_wrms = []
x_IUFNO_vort_PDFs = []
y_IUFNO_vort_PDFs = []
x_IUFNO_vort_statistics = []
y_IUFNO_vort_statistics = []
for case_n in range(case_number-1,case_number):
    # print(case_n)
    # 载入后处理文件，包括速度参数，PDFs，能谱，结构函数
    IUFNO_vel_parameter= np.loadtxt('./case{}/Result_LES32_F-IFNO_40ep_gap200_mag0.1/post_result/vel_parameter.dat'.format(case_n+1),dtype=float, comments=['step'])
    IUFNO_ic1_PDFs = np.loadtxt('./case{}/Result_LES32_F-IFNO_40ep_gap200_mag0.1/post_result/inc1_PDFs.dat'.format(case_n + 1), dtype=float,comments=['step'])
    IUFNO_spec = np.loadtxt('./case{}/Result_LES32_F-IFNO_40ep_gap200_mag0.1/post_result/spectrum_vel.dat'.format(case_n + 1), dtype=float,comments=['variables', 'zone'])
    IUFNO_structrue2 = np.loadtxt('./case{}/Result_LES32_F-IFNO_40ep_gap200_mag0.1/post_result/structure2.dat'.format(case_n + 1),dtype=float, comments=['step'])
    IUFNO_structrue4 = np.loadtxt('./case{}/Result_LES32_F-IFNO_40ep_gap200_mag0.1/post_result/structure4.dat'.format(case_n + 1),dtype=float, comments=['step'])
    IUFNO_vort_PDFs = np.loadtxt('./case{}/Result_LES32_F-IFNO_40ep_gap200_mag0.1/post_result/vort_PDFs.dat'.format(case_n + 1), dtype=float,comments=['variables', 'zone'])
    IUFNO_vort_statistics = np.loadtxt('./case{}/Result_LES32_F-IFNO_40ep_gap200_mag0.1/post_result/vort_statistics.dat'.format(case_n + 1),dtype=float, comments=['step'])
    # print(VGM.shape)
    # 取出数据
    x_IUFNO_urms.append(IUFNO_vel_parameter[:,0])  # 只取出第一列数据
    y_IUFNO_urms.append(IUFNO_vel_parameter[:,3]) #只取出第二列数据
    x_IUFNO_wrms.append(IUFNO_vel_parameter[:,0])  # 只取出第一列数据
    y_IUFNO_wrms.append(IUFNO_vel_parameter[:,7]) #只取出第二列数据
    x_IUFNO_dissipation.append(IUFNO_vel_parameter[:,0])  # 只取出第一列数据
    y_IUFNO_dissipation.append(IUFNO_vel_parameter[:,8]) #只取出第二列数据
    x_IUFNO_Et.append(IUFNO_vel_parameter[:,0])  # 只取出第一列数据
    y_IUFNO_Et.append(IUFNO_vel_parameter[:,6]) #只取出第二列数据
    x_IUFNO_inc1_PDFs.append(IUFNO_ic1_PDFs[:,0])  # 只取出第一列数据
    y_IUFNO_inc1_PDFs.append(IUFNO_ic1_PDFs[:,1]) #只取出第二列数据
    x_IUFNO_velspectrum.append(IUFNO_spec[:,0])  # 只取出第一列数据
    y_IUFNO_velspectrum.append(IUFNO_spec[:,1]) #只取出第二列数据
    x_IUFNO_structrue2.append(IUFNO_structrue2[:,0])  # 只取出第一列数据
    y_IUFNO_structrue2.append(IUFNO_structrue2[:,1]) #只取出第二列数据
    x_IUFNO_structrue4.append(IUFNO_structrue4[:,0])  # 只取出第一列数据
    y_IUFNO_structrue4.append(IUFNO_structrue4[:,1]) #只取出第二列数据
    x_IUFNO_vort_PDFs.append(IUFNO_vort_PDFs[:,0])  # 只取出第一列数据
    y_IUFNO_vort_PDFs.append(IUFNO_vort_PDFs[:,1]) #只取出第二列数据
    x_IUFNO_vort_statistics.append(IUFNO_vort_statistics[:,0])  # 只取出第一列数据
    y_IUFNO_vort_statistics.append(IUFNO_vort_statistics[:,5]) #只取出第二列数据
# 转化为数组
x_IUFNO_urms_arr = np.asarray(x_IUFNO_urms) #列表转数组
y_IUFNO_urms_arr = np.asarray(y_IUFNO_urms) #列表转数组
x_IUFNO_wrms_arr = np.asarray(x_IUFNO_wrms) #列表转数组
y_IUFNO_wrms_arr = np.asarray(y_IUFNO_wrms) #列表转数组
x_IUFNO_dissipation_arr = np.asarray(x_IUFNO_dissipation) #列表转数组
y_IUFNO_dissipation_arr = np.asarray(y_IUFNO_dissipation) #列表转数组
x_IUFNO_Et_arr = np.asarray(x_IUFNO_Et) #列表转数组
y_IUFNO_Et_arr = np.asarray(y_IUFNO_Et) #列表转数组
x_IUFNO_inc1_PDFs_arr = np.asarray(x_IUFNO_inc1_PDFs) #列表转数组
y_IUFNO_inc1_PDFs_arr = np.asarray(y_IUFNO_inc1_PDFs) #列表转数组
x_IUFNO_spe_arr = np.asarray(x_IUFNO_velspectrum) #列表转数组
y_IUFNO_spe_arr = np.asarray(y_IUFNO_velspectrum) #列表转数组
x_IUFNO_structrue2 = np.asarray(x_IUFNO_structrue2) #列表转数组
y_IUFNO_structrue2 = np.asarray(y_IUFNO_structrue2) #列表转数组
x_IUFNO_structrue4 = np.asarray(x_IUFNO_structrue4) #列表转数组
y_IUFNO_structrue4 = np.asarray(y_IUFNO_structrue4) #列表转数组
x_IUFNO_vort_PDFs = np.asarray(x_IUFNO_vort_PDFs) #列表转数组
y_IUFNO_vort_PDFs = np.asarray(y_IUFNO_vort_PDFs) #列表转数组
x_IUFNO_vort_statistics = np.asarray(x_IUFNO_vort_statistics) #列表转数组
y_IUFNO_vort_statistics = np.asarray(y_IUFNO_vort_statistics) #列表转数组
# 取均值
x_urms_avg_case = np.mean(x_IUFNO_urms_arr,0) #行压缩成一行
y_urms_avg_case = np.mean(y_IUFNO_urms_arr,0) #行压缩成一行
x_wrms_avg_case = np.mean(x_IUFNO_wrms_arr,0) #行压缩成一行
y_wrms_avg_case = np.mean(y_IUFNO_wrms_arr,0) #行压缩成一行
x_dissipation_avg_case = np.mean(x_IUFNO_dissipation_arr,0) #行压缩成一行
y_dissipation_avg_case = np.mean(y_IUFNO_dissipation_arr,0) #行压缩成一行
x_Et_avg_case = np.mean(x_IUFNO_Et_arr,0) #行压缩成一行
y_Et_avg_case = np.mean(y_IUFNO_Et_arr,0) #行压缩成一行
x_inc1_PDFs_avg_case = np.mean(x_IUFNO_inc1_PDFs_arr,0) #行压缩成一行
y_inc1_PDFs_avg_case = np.mean(y_IUFNO_inc1_PDFs_arr,0) #行压缩成一行
x_spe_avg_case = np.mean(x_IUFNO_spe_arr,0) #行压缩成一行
y_spe_avg_case = np.mean(y_IUFNO_spe_arr,0) #行压缩成一行
x_structrue2_avg_case = np.mean(x_IUFNO_structrue2,0) #行压缩成一行
y_structrue2_avg_case = np.mean(y_IUFNO_structrue2,0) #行压缩成
x_structrue4_avg_case = np.mean(x_IUFNO_structrue4,0) #行压缩成一行
y_structrue4_avg_case = np.mean(y_IUFNO_structrue4,0) #行压缩成
x_vort_PDFs_avg_case = np.mean(x_IUFNO_vort_PDFs,0) #行压缩成一行
y_vort_PDFs_avg_case = np.mean(y_IUFNO_vort_PDFs,0) #行压缩成
x_vort_statistics_avg_case = np.mean(x_IUFNO_vort_statistics,0) #行压缩成一行
y_vort_statistics_avg_case = np.mean(y_IUFNO_vort_statistics,0) #行压缩成
# 拼接操作
avg_IUFNO_urms_10case=np.dstack((x_urms_avg_case,y_urms_avg_case)).squeeze() #拼接
avg_IUFNO_wrms_10case=np.dstack((x_wrms_avg_case,y_wrms_avg_case)).squeeze() #拼接
avg_IUFNO_dissipation_10case=np.dstack((x_dissipation_avg_case,y_dissipation_avg_case)).squeeze() #拼接
avg_IUFNO_Et_10case=np.dstack((x_Et_avg_case,y_Et_avg_case)).squeeze() #拼接
avg_IUFNO_inc1_PDFs_10case=np.dstack((x_inc1_PDFs_avg_case,y_inc1_PDFs_avg_case)).squeeze() #拼接
avg_IUFNO_spectrum_10case=np.dstack((x_spe_avg_case,y_spe_avg_case)).squeeze() #拼接
avg_IUFNO_structrue2_10case=np.dstack((x_structrue2_avg_case,y_structrue2_avg_case)).squeeze() #拼接
avg_IUFNO_structrue4_10case=np.dstack((x_structrue4_avg_case,y_structrue4_avg_case)).squeeze() #拼接
avg_IUFNO_vort_PDFs_10case=np.dstack((x_vort_PDFs_avg_case,y_vort_PDFs_avg_case)).squeeze() #拼接
avg_IUFNO_vort_statistics_10case=np.dstack((x_vort_statistics_avg_case,y_vort_statistics_avg_case)).squeeze() #拼接
#导出均值

np.savetxt('./AVG/F-IFNO_40ep_mag0.1/N{}/avg_FIFNO_{}case_urms.dat'.format(case_number,case_number),avg_IUFNO_urms_10case, fmt="%16.7f")
np.savetxt('./AVG/F-IFNO_40ep_mag0.1/N{}/avg_FIFNO_{}case_wrms.dat'.format(case_number,case_number),avg_IUFNO_wrms_10case, fmt="%16.7f")
np.savetxt('./AVG/F-IFNO_40ep_mag0.1/N{}/avg_FIFNO_{}case_dissipation.dat'.format(case_number,case_number),avg_IUFNO_dissipation_10case, fmt="%16.7f")
np.savetxt('./AVG/F-IFNO_40ep_mag0.1/N{}/avg_FIFNO_{}case_Ek_t.dat'.format(case_number,case_number),avg_IUFNO_Et_10case, fmt="%16.7f")
np.savetxt('./AVG/F-IFNO_40ep_mag0.1/N{}/avg_FIFNO_{}case_inc1_PDFs.dat'.format(case_number,case_number),avg_IUFNO_inc1_PDFs_10case, fmt="%16.7f")
np.savetxt('./AVG/F-IFNO_40ep_mag0.1/N{}/avg_FIFNO_{}case_vel_spec.dat'.format(case_number,case_number),avg_IUFNO_spectrum_10case, fmt="%16.7f")
np.savetxt('./AVG/F-IFNO_40ep_mag0.1/N{}/avg_FIFNO_{}case_structrue2.dat'.format(case_number,case_number),avg_IUFNO_structrue2_10case, fmt="%16.7f")
np.savetxt('./AVG/F-IFNO_40ep_mag0.1/N{}/avg_FIFNO_{}case_structrue4.dat'.format(case_number,case_number),avg_IUFNO_structrue4_10case, fmt="%16.7f")
np.savetxt('./AVG/F-IFNO_40ep_mag0.1/N{}/avg_FIFNO_{}case_vort_PDFs.dat'.format(case_number,case_number),avg_IUFNO_vort_PDFs_10case, fmt="%16.7f")
np.savetxt('./AVG/F-IFNO_40ep_mag0.1/N{}/avg_FIFNO_{}case_vort_statistics.dat'.format(case_number,case_number),avg_IUFNO_vort_statistics_10case, fmt="%16.7f")
'''
np.savetxt('./AVG/F-IFNO_40ep_mag0.1/{}case/avg_FIFNO_{}case_urms.dat'.format(case_number,case_number),avg_IUFNO_urms_10case, fmt="%16.7f")
np.savetxt('./AVG/F-IFNO_40ep_mag0.1/{}case/avg_FIFNO_{}case_wrms.dat'.format(case_number,case_number),avg_IUFNO_wrms_10case, fmt="%16.7f")
np.savetxt('./AVG/F-IFNO_40ep_mag0.1/{}case/avg_FIFNO_{}case_dissipation.dat'.format(case_number,case_number),avg_IUFNO_dissipation_10case, fmt="%16.7f")
np.savetxt('./AVG/F-IFNO_40ep_mag0.1/{}case/avg_FIFNO_{}case_Ek_t.dat'.format(case_number,case_number),avg_IUFNO_Et_10case, fmt="%16.7f")
np.savetxt('./AVG/F-IFNO_40ep_mag0.1/{}case/avg_FIFNO_{}case_inc1_PDFs.dat'.format(case_number,case_number),avg_IUFNO_inc1_PDFs_10case, fmt="%16.7f")
np.savetxt('./AVG/F-IFNO_40ep_mag0.1/{}case/avg_FIFNO_{}case_vel_spec.dat'.format(case_number,case_number),avg_IUFNO_spectrum_10case, fmt="%16.7f")
np.savetxt('./AVG/F-IFNO_40ep_mag0.1/{}case/avg_FIFNO_{}case_structrue2.dat'.format(case_number,case_number),avg_IUFNO_structrue2_10case, fmt="%16.7f")
np.savetxt('./AVG/F-IFNO_40ep_mag0.1/{}case/avg_FIFNO_{}case_structrue4.dat'.format(case_number,case_number),avg_IUFNO_structrue4_10case, fmt="%16.7f")
np.savetxt('./AVG/F-IFNO_40ep_mag0.1/{}case/avg_FIFNO_{}case_vort_PDFs.dat'.format(case_number,case_number),avg_IUFNO_vort_PDFs_10case, fmt="%16.7f")
np.savetxt('./AVG/F-IFNO_40ep_mag0.1/{}case/avg_FIFNO_{}case_vort_statistics.dat'.format(case_number,case_number),avg_IUFNO_vort_statistics_10case, fmt="%16.7f")
'''

#==========================================================================FNO
print("F-IFNO_40ep_mag0.5 getting dat!")
x_IUFNO_dissipation=[]
y_IUFNO_dissipation=[]
x_IUFNO_Et=[]
y_IUFNO_Et=[]
x_IUFNO_inc1_PDFs=[]
y_IUFNO_inc1_PDFs=[]
x_IUFNO_velspectrum=[]
y_IUFNO_velspectrum=[]
x_IUFNO_structrue2 = []
y_IUFNO_structrue2 = []
x_IUFNO_structrue4 = []
y_IUFNO_structrue4 = []
x_IUFNO_urms = []
y_IUFNO_urms = []
x_IUFNO_wrms = []
y_IUFNO_wrms = []
x_IUFNO_vort_PDFs = []
y_IUFNO_vort_PDFs = []
x_IUFNO_vort_statistics = []
y_IUFNO_vort_statistics = []
for case_n in range(case_number-1,case_number):
    # print(case_n)
    # 载入后处理文件，包括速度参数，PDFs，能谱，结构函数
    IUFNO_vel_parameter= np.loadtxt('./case{}/Result_LES32_F-IFNO_40ep_gap200_mag0.5/post_result/vel_parameter.dat'.format(case_n+1),dtype=float, comments=['step'])
    IUFNO_ic1_PDFs = np.loadtxt('./case{}/Result_LES32_F-IFNO_40ep_gap200_mag0.5/post_result/inc1_PDFs.dat'.format(case_n + 1), dtype=float,comments=['step'])
    IUFNO_spec = np.loadtxt('./case{}/Result_LES32_F-IFNO_40ep_gap200_mag0.5/post_result/spectrum_vel.dat'.format(case_n + 1), dtype=float,comments=['variables', 'zone'])
    IUFNO_structrue2 = np.loadtxt('./case{}/Result_LES32_F-IFNO_40ep_gap200_mag0.5/post_result/structure2.dat'.format(case_n + 1),dtype=float, comments=['step'])
    IUFNO_structrue4 = np.loadtxt('./case{}/Result_LES32_F-IFNO_40ep_gap200_mag0.5/post_result/structure4.dat'.format(case_n + 1),dtype=float, comments=['step'])
    IUFNO_vort_PDFs = np.loadtxt('./case{}/Result_LES32_F-IFNO_40ep_gap200_mag0.5/post_result/vort_PDFs.dat'.format(case_n + 1), dtype=float,comments=['variables', 'zone'])
    IUFNO_vort_statistics = np.loadtxt('./case{}/Result_LES32_F-IFNO_40ep_gap200_mag0.5/post_result/vort_statistics.dat'.format(case_n + 1),dtype=float, comments=['step'])
    # print(VGM.shape)
    # 取出数据
    x_IUFNO_urms.append(IUFNO_vel_parameter[:,0])  # 只取出第一列数据
    y_IUFNO_urms.append(IUFNO_vel_parameter[:,3]) #只取出第二列数据
    x_IUFNO_wrms.append(IUFNO_vel_parameter[:,0])  # 只取出第一列数据
    y_IUFNO_wrms.append(IUFNO_vel_parameter[:,7]) #只取出第二列数据
    x_IUFNO_dissipation.append(IUFNO_vel_parameter[:,0])  # 只取出第一列数据
    y_IUFNO_dissipation.append(IUFNO_vel_parameter[:,8]) #只取出第二列数据
    x_IUFNO_Et.append(IUFNO_vel_parameter[:,0])  # 只取出第一列数据
    y_IUFNO_Et.append(IUFNO_vel_parameter[:,6]) #只取出第二列数据
    x_IUFNO_inc1_PDFs.append(IUFNO_ic1_PDFs[:,0])  # 只取出第一列数据
    y_IUFNO_inc1_PDFs.append(IUFNO_ic1_PDFs[:,1]) #只取出第二列数据
    x_IUFNO_velspectrum.append(IUFNO_spec[:,0])  # 只取出第一列数据
    y_IUFNO_velspectrum.append(IUFNO_spec[:,1]) #只取出第二列数据
    x_IUFNO_structrue2.append(IUFNO_structrue2[:,0])  # 只取出第一列数据
    y_IUFNO_structrue2.append(IUFNO_structrue2[:,1]) #只取出第二列数据
    x_IUFNO_structrue4.append(IUFNO_structrue4[:,0])  # 只取出第一列数据
    y_IUFNO_structrue4.append(IUFNO_structrue4[:,1]) #只取出第二列数据
    x_IUFNO_vort_PDFs.append(IUFNO_vort_PDFs[:,0])  # 只取出第一列数据
    y_IUFNO_vort_PDFs.append(IUFNO_vort_PDFs[:,1]) #只取出第二列数据
    x_IUFNO_vort_statistics.append(IUFNO_vort_statistics[:,0])  # 只取出第一列数据
    y_IUFNO_vort_statistics.append(IUFNO_vort_statistics[:,5]) #只取出第二列数据
# 转化为数组
x_IUFNO_urms_arr = np.asarray(x_IUFNO_urms) #列表转数组
y_IUFNO_urms_arr = np.asarray(y_IUFNO_urms) #列表转数组
x_IUFNO_wrms_arr = np.asarray(x_IUFNO_wrms) #列表转数组
y_IUFNO_wrms_arr = np.asarray(y_IUFNO_wrms) #列表转数组
x_IUFNO_dissipation_arr = np.asarray(x_IUFNO_dissipation) #列表转数组
y_IUFNO_dissipation_arr = np.asarray(y_IUFNO_dissipation) #列表转数组
x_IUFNO_Et_arr = np.asarray(x_IUFNO_Et) #列表转数组
y_IUFNO_Et_arr = np.asarray(y_IUFNO_Et) #列表转数组
x_IUFNO_inc1_PDFs_arr = np.asarray(x_IUFNO_inc1_PDFs) #列表转数组
y_IUFNO_inc1_PDFs_arr = np.asarray(y_IUFNO_inc1_PDFs) #列表转数组
x_IUFNO_spe_arr = np.asarray(x_IUFNO_velspectrum) #列表转数组
y_IUFNO_spe_arr = np.asarray(y_IUFNO_velspectrum) #列表转数组
x_IUFNO_structrue2 = np.asarray(x_IUFNO_structrue2) #列表转数组
y_IUFNO_structrue2 = np.asarray(y_IUFNO_structrue2) #列表转数组
x_IUFNO_structrue4 = np.asarray(x_IUFNO_structrue4) #列表转数组
y_IUFNO_structrue4 = np.asarray(y_IUFNO_structrue4) #列表转数组
x_IUFNO_vort_PDFs = np.asarray(x_IUFNO_vort_PDFs) #列表转数组
y_IUFNO_vort_PDFs = np.asarray(y_IUFNO_vort_PDFs) #列表转数组
x_IUFNO_vort_statistics = np.asarray(x_IUFNO_vort_statistics) #列表转数组
y_IUFNO_vort_statistics = np.asarray(y_IUFNO_vort_statistics) #列表转数组
# 取均值
x_urms_avg_case = np.mean(x_IUFNO_urms_arr,0) #行压缩成一行
y_urms_avg_case = np.mean(y_IUFNO_urms_arr,0) #行压缩成一行
x_wrms_avg_case = np.mean(x_IUFNO_wrms_arr,0) #行压缩成一行
y_wrms_avg_case = np.mean(y_IUFNO_wrms_arr,0) #行压缩成一行
x_dissipation_avg_case = np.mean(x_IUFNO_dissipation_arr,0) #行压缩成一行
y_dissipation_avg_case = np.mean(y_IUFNO_dissipation_arr,0) #行压缩成一行
x_Et_avg_case = np.mean(x_IUFNO_Et_arr,0) #行压缩成一行
y_Et_avg_case = np.mean(y_IUFNO_Et_arr,0) #行压缩成一行
x_inc1_PDFs_avg_case = np.mean(x_IUFNO_inc1_PDFs_arr,0) #行压缩成一行
y_inc1_PDFs_avg_case = np.mean(y_IUFNO_inc1_PDFs_arr,0) #行压缩成一行
x_spe_avg_case = np.mean(x_IUFNO_spe_arr,0) #行压缩成一行
y_spe_avg_case = np.mean(y_IUFNO_spe_arr,0) #行压缩成一行
x_structrue2_avg_case = np.mean(x_IUFNO_structrue2,0) #行压缩成一行
y_structrue2_avg_case = np.mean(y_IUFNO_structrue2,0) #行压缩成
x_structrue4_avg_case = np.mean(x_IUFNO_structrue4,0) #行压缩成一行
y_structrue4_avg_case = np.mean(y_IUFNO_structrue4,0) #行压缩成
x_vort_PDFs_avg_case = np.mean(x_IUFNO_vort_PDFs,0) #行压缩成一行
y_vort_PDFs_avg_case = np.mean(y_IUFNO_vort_PDFs,0) #行压缩成
x_vort_statistics_avg_case = np.mean(x_IUFNO_vort_statistics,0) #行压缩成一行
y_vort_statistics_avg_case = np.mean(y_IUFNO_vort_statistics,0) #行压缩成
# 拼接操作
avg_IUFNO_urms_10case=np.dstack((x_urms_avg_case,y_urms_avg_case)).squeeze() #拼接
avg_IUFNO_wrms_10case=np.dstack((x_wrms_avg_case,y_wrms_avg_case)).squeeze() #拼接
avg_IUFNO_dissipation_10case=np.dstack((x_dissipation_avg_case,y_dissipation_avg_case)).squeeze() #拼接
avg_IUFNO_Et_10case=np.dstack((x_Et_avg_case,y_Et_avg_case)).squeeze() #拼接
avg_IUFNO_inc1_PDFs_10case=np.dstack((x_inc1_PDFs_avg_case,y_inc1_PDFs_avg_case)).squeeze() #拼接
avg_IUFNO_spectrum_10case=np.dstack((x_spe_avg_case,y_spe_avg_case)).squeeze() #拼接
avg_IUFNO_structrue2_10case=np.dstack((x_structrue2_avg_case,y_structrue2_avg_case)).squeeze() #拼接
avg_IUFNO_structrue4_10case=np.dstack((x_structrue4_avg_case,y_structrue4_avg_case)).squeeze() #拼接
avg_IUFNO_vort_PDFs_10case=np.dstack((x_vort_PDFs_avg_case,y_vort_PDFs_avg_case)).squeeze() #拼接
avg_IUFNO_vort_statistics_10case=np.dstack((x_vort_statistics_avg_case,y_vort_statistics_avg_case)).squeeze() #拼接
#导出均值

np.savetxt('./AVG/F-IFNO_40ep_mag0.5/N{}/avg_FIFNO_{}case_urms.dat'.format(case_number,case_number),avg_IUFNO_urms_10case, fmt="%16.7f")
np.savetxt('./AVG/F-IFNO_40ep_mag0.5/N{}/avg_FIFNO_{}case_wrms.dat'.format(case_number,case_number),avg_IUFNO_wrms_10case, fmt="%16.7f")
np.savetxt('./AVG/F-IFNO_40ep_mag0.5/N{}/avg_FIFNO_{}case_dissipation.dat'.format(case_number,case_number),avg_IUFNO_dissipation_10case, fmt="%16.7f")
np.savetxt('./AVG/F-IFNO_40ep_mag0.5/N{}/avg_FIFNO_{}case_Ek_t.dat'.format(case_number,case_number),avg_IUFNO_Et_10case, fmt="%16.7f")
np.savetxt('./AVG/F-IFNO_40ep_mag0.5/N{}/avg_FIFNO_{}case_inc1_PDFs.dat'.format(case_number,case_number),avg_IUFNO_inc1_PDFs_10case, fmt="%16.7f")
np.savetxt('./AVG/F-IFNO_40ep_mag0.5/N{}/avg_FIFNO_{}case_vel_spec.dat'.format(case_number,case_number),avg_IUFNO_spectrum_10case, fmt="%16.7f")
np.savetxt('./AVG/F-IFNO_40ep_mag0.5/N{}/avg_FIFNO_{}case_structrue2.dat'.format(case_number,case_number),avg_IUFNO_structrue2_10case, fmt="%16.7f")
np.savetxt('./AVG/F-IFNO_40ep_mag0.5/N{}/avg_FIFNO_{}case_structrue4.dat'.format(case_number,case_number),avg_IUFNO_structrue4_10case, fmt="%16.7f")
np.savetxt('./AVG/F-IFNO_40ep_mag0.5/N{}/avg_FIFNO_{}case_vort_PDFs.dat'.format(case_number,case_number),avg_IUFNO_vort_PDFs_10case, fmt="%16.7f")
np.savetxt('./AVG/F-IFNO_40ep_mag0.5/N{}/avg_FIFNO_{}case_vort_statistics.dat'.format(case_number,case_number),avg_IUFNO_vort_statistics_10case, fmt="%16.7f")
'''
np.savetxt('./AVG/F-IFNO_40ep_mag0.5/{}case/avg_FIFNO_{}case_urms.dat'.format(case_number,case_number),avg_IUFNO_urms_10case, fmt="%16.7f")
np.savetxt('./AVG/F-IFNO_40ep_mag0.5/{}case/avg_FIFNO_{}case_wrms.dat'.format(case_number,case_number),avg_IUFNO_wrms_10case, fmt="%16.7f")
np.savetxt('./AVG/F-IFNO_40ep_mag0.5/{}case/avg_FIFNO_{}case_dissipation.dat'.format(case_number,case_number),avg_IUFNO_dissipation_10case, fmt="%16.7f")
np.savetxt('./AVG/F-IFNO_40ep_mag0.5/{}case/avg_FIFNO_{}case_Ek_t.dat'.format(case_number,case_number),avg_IUFNO_Et_10case, fmt="%16.7f")
np.savetxt('./AVG/F-IFNO_40ep_mag0.5/{}case/avg_FIFNO_{}case_inc1_PDFs.dat'.format(case_number,case_number),avg_IUFNO_inc1_PDFs_10case, fmt="%16.7f")
np.savetxt('./AVG/F-IFNO_40ep_mag0.5/{}case/avg_FIFNO_{}case_vel_spec.dat'.format(case_number,case_number),avg_IUFNO_spectrum_10case, fmt="%16.7f")
np.savetxt('./AVG/F-IFNO_40ep_mag0.5/{}case/avg_FIFNO_{}case_structrue2.dat'.format(case_number,case_number),avg_IUFNO_structrue2_10case, fmt="%16.7f")
np.savetxt('./AVG/F-IFNO_40ep_mag0.5/{}case/avg_FIFNO_{}case_structrue4.dat'.format(case_number,case_number),avg_IUFNO_structrue4_10case, fmt="%16.7f")
np.savetxt('./AVG/F-IFNO_40ep_mag0.5/{}case/avg_FIFNO_{}case_vort_PDFs.dat'.format(case_number,case_number),avg_IUFNO_vort_PDFs_10case, fmt="%16.7f")
np.savetxt('./AVG/F-IFNO_40ep_mag0.5/{}case/avg_FIFNO_{}case_vort_statistics.dat'.format(case_number,case_number),avg_IUFNO_vort_statistics_10case, fmt="%16.7f")
'''

#==========================================================================FNO
print("IFNO_40ep getting dat!")
x_IUFNO_dissipation=[]
y_IUFNO_dissipation=[]
x_IUFNO_Et=[]
y_IUFNO_Et=[]
x_IUFNO_inc1_PDFs=[]
y_IUFNO_inc1_PDFs=[]
x_IUFNO_velspectrum=[]
y_IUFNO_velspectrum=[]
x_IUFNO_structrue2 = []
y_IUFNO_structrue2 = []
x_IUFNO_structrue4 = []
y_IUFNO_structrue4 = []
x_IUFNO_urms = []
y_IUFNO_urms = []
x_IUFNO_wrms = []
y_IUFNO_wrms = []
x_IUFNO_vort_PDFs = []
y_IUFNO_vort_PDFs = []
x_IUFNO_vort_statistics = []
y_IUFNO_vort_statistics = []
for case_n in range(case_number-1,case_number):
    # print(case_n)
    # 载入后处理文件，包括速度参数，PDFs，能谱，结构函数
    IUFNO_vel_parameter= np.loadtxt('./case{}/Result_LES32_IFNO_gap200/post_result/vel_parameter.dat'.format(case_n+1),dtype=float, comments=['step'])
    IUFNO_ic1_PDFs = np.loadtxt('./case{}/Result_LES32_IFNO_gap200/post_result/inc1_PDFs.dat'.format(case_n + 1), dtype=float,comments=['step'])
    IUFNO_spec = np.loadtxt('./case{}/Result_LES32_IFNO_gap200/post_result/spectrum_vel.dat'.format(case_n + 1), dtype=float,comments=['variables', 'zone'])
    IUFNO_structrue2 = np.loadtxt('./case{}/Result_LES32_IFNO_gap200/post_result/structure2.dat'.format(case_n + 1),dtype=float, comments=['step'])
    IUFNO_structrue4 = np.loadtxt('./case{}/Result_LES32_IFNO_gap200/post_result/structure4.dat'.format(case_n + 1),dtype=float, comments=['step'])
    IUFNO_vort_PDFs = np.loadtxt('./case{}/Result_LES32_IFNO_gap200/post_result/vort_PDFs.dat'.format(case_n + 1), dtype=float,comments=['variables', 'zone'])
    IUFNO_vort_statistics = np.loadtxt('./case{}/Result_LES32_IFNO_gap200/post_result/vort_statistics.dat'.format(case_n + 1),dtype=float, comments=['step'])
    # print(VGM.shape)
    # 取出数据
    x_IUFNO_urms.append(IUFNO_vel_parameter[:,0])  # 只取出第一列数据
    y_IUFNO_urms.append(IUFNO_vel_parameter[:,3]) #只取出第二列数据
    x_IUFNO_wrms.append(IUFNO_vel_parameter[:,0])  # 只取出第一列数据
    y_IUFNO_wrms.append(IUFNO_vel_parameter[:,7]) #只取出第二列数据
    x_IUFNO_dissipation.append(IUFNO_vel_parameter[:,0])  # 只取出第一列数据
    y_IUFNO_dissipation.append(IUFNO_vel_parameter[:,8]) #只取出第二列数据
    x_IUFNO_Et.append(IUFNO_vel_parameter[:,0])  # 只取出第一列数据
    y_IUFNO_Et.append(IUFNO_vel_parameter[:,6]) #只取出第二列数据
    x_IUFNO_inc1_PDFs.append(IUFNO_ic1_PDFs[:,0])  # 只取出第一列数据
    y_IUFNO_inc1_PDFs.append(IUFNO_ic1_PDFs[:,1]) #只取出第二列数据
    x_IUFNO_velspectrum.append(IUFNO_spec[:,0])  # 只取出第一列数据
    y_IUFNO_velspectrum.append(IUFNO_spec[:,1]) #只取出第二列数据
    x_IUFNO_structrue2.append(IUFNO_structrue2[:,0])  # 只取出第一列数据
    y_IUFNO_structrue2.append(IUFNO_structrue2[:,1]) #只取出第二列数据
    x_IUFNO_structrue4.append(IUFNO_structrue4[:,0])  # 只取出第一列数据
    y_IUFNO_structrue4.append(IUFNO_structrue4[:,1]) #只取出第二列数据
    x_IUFNO_vort_PDFs.append(IUFNO_vort_PDFs[:,0])  # 只取出第一列数据
    y_IUFNO_vort_PDFs.append(IUFNO_vort_PDFs[:,1]) #只取出第二列数据
    x_IUFNO_vort_statistics.append(IUFNO_vort_statistics[:,0])  # 只取出第一列数据
    y_IUFNO_vort_statistics.append(IUFNO_vort_statistics[:,5]) #只取出第二列数据
# 转化为数组
x_IUFNO_urms_arr = np.asarray(x_IUFNO_urms) #列表转数组
y_IUFNO_urms_arr = np.asarray(y_IUFNO_urms) #列表转数组
x_IUFNO_wrms_arr = np.asarray(x_IUFNO_wrms) #列表转数组
y_IUFNO_wrms_arr = np.asarray(y_IUFNO_wrms) #列表转数组
x_IUFNO_dissipation_arr = np.asarray(x_IUFNO_dissipation) #列表转数组
y_IUFNO_dissipation_arr = np.asarray(y_IUFNO_dissipation) #列表转数组
x_IUFNO_Et_arr = np.asarray(x_IUFNO_Et) #列表转数组
y_IUFNO_Et_arr = np.asarray(y_IUFNO_Et) #列表转数组
x_IUFNO_inc1_PDFs_arr = np.asarray(x_IUFNO_inc1_PDFs) #列表转数组
y_IUFNO_inc1_PDFs_arr = np.asarray(y_IUFNO_inc1_PDFs) #列表转数组
x_IUFNO_spe_arr = np.asarray(x_IUFNO_velspectrum) #列表转数组
y_IUFNO_spe_arr = np.asarray(y_IUFNO_velspectrum) #列表转数组
x_IUFNO_structrue2 = np.asarray(x_IUFNO_structrue2) #列表转数组
y_IUFNO_structrue2 = np.asarray(y_IUFNO_structrue2) #列表转数组
x_IUFNO_structrue4 = np.asarray(x_IUFNO_structrue4) #列表转数组
y_IUFNO_structrue4 = np.asarray(y_IUFNO_structrue4) #列表转数组
x_IUFNO_vort_PDFs = np.asarray(x_IUFNO_vort_PDFs) #列表转数组
y_IUFNO_vort_PDFs = np.asarray(y_IUFNO_vort_PDFs) #列表转数组
x_IUFNO_vort_statistics = np.asarray(x_IUFNO_vort_statistics) #列表转数组
y_IUFNO_vort_statistics = np.asarray(y_IUFNO_vort_statistics) #列表转数组
# 取均值
x_urms_avg_case = np.mean(x_IUFNO_urms_arr,0) #行压缩成一行
y_urms_avg_case = np.mean(y_IUFNO_urms_arr,0) #行压缩成一行
x_wrms_avg_case = np.mean(x_IUFNO_wrms_arr,0) #行压缩成一行
y_wrms_avg_case = np.mean(y_IUFNO_wrms_arr,0) #行压缩成一行
x_dissipation_avg_case = np.mean(x_IUFNO_dissipation_arr,0) #行压缩成一行
y_dissipation_avg_case = np.mean(y_IUFNO_dissipation_arr,0) #行压缩成一行
x_Et_avg_case = np.mean(x_IUFNO_Et_arr,0) #行压缩成一行
y_Et_avg_case = np.mean(y_IUFNO_Et_arr,0) #行压缩成一行
x_inc1_PDFs_avg_case = np.mean(x_IUFNO_inc1_PDFs_arr,0) #行压缩成一行
y_inc1_PDFs_avg_case = np.mean(y_IUFNO_inc1_PDFs_arr,0) #行压缩成一行
x_spe_avg_case = np.mean(x_IUFNO_spe_arr,0) #行压缩成一行
y_spe_avg_case = np.mean(y_IUFNO_spe_arr,0) #行压缩成一行
x_structrue2_avg_case = np.mean(x_IUFNO_structrue2,0) #行压缩成一行
y_structrue2_avg_case = np.mean(y_IUFNO_structrue2,0) #行压缩成
x_structrue4_avg_case = np.mean(x_IUFNO_structrue4,0) #行压缩成一行
y_structrue4_avg_case = np.mean(y_IUFNO_structrue4,0) #行压缩成
x_vort_PDFs_avg_case = np.mean(x_IUFNO_vort_PDFs,0) #行压缩成一行
y_vort_PDFs_avg_case = np.mean(y_IUFNO_vort_PDFs,0) #行压缩成
x_vort_statistics_avg_case = np.mean(x_IUFNO_vort_statistics,0) #行压缩成一行
y_vort_statistics_avg_case = np.mean(y_IUFNO_vort_statistics,0) #行压缩成
# 拼接操作
avg_IUFNO_urms_10case=np.dstack((x_urms_avg_case,y_urms_avg_case)).squeeze() #拼接
avg_IUFNO_wrms_10case=np.dstack((x_wrms_avg_case,y_wrms_avg_case)).squeeze() #拼接
avg_IUFNO_dissipation_10case=np.dstack((x_dissipation_avg_case,y_dissipation_avg_case)).squeeze() #拼接
avg_IUFNO_Et_10case=np.dstack((x_Et_avg_case,y_Et_avg_case)).squeeze() #拼接
avg_IUFNO_inc1_PDFs_10case=np.dstack((x_inc1_PDFs_avg_case,y_inc1_PDFs_avg_case)).squeeze() #拼接
avg_IUFNO_spectrum_10case=np.dstack((x_spe_avg_case,y_spe_avg_case)).squeeze() #拼接
avg_IUFNO_structrue2_10case=np.dstack((x_structrue2_avg_case,y_structrue2_avg_case)).squeeze() #拼接
avg_IUFNO_structrue4_10case=np.dstack((x_structrue4_avg_case,y_structrue4_avg_case)).squeeze() #拼接
avg_IUFNO_vort_PDFs_10case=np.dstack((x_vort_PDFs_avg_case,y_vort_PDFs_avg_case)).squeeze() #拼接
avg_IUFNO_vort_statistics_10case=np.dstack((x_vort_statistics_avg_case,y_vort_statistics_avg_case)).squeeze() #拼接
#导出均值

np.savetxt('./AVG/IFNO/N{}/avg_IFNO_{}case_urms.dat'.format(case_number,case_number),avg_IUFNO_urms_10case, fmt="%16.7f")
np.savetxt('./AVG/IFNO/N{}/avg_IFNO_{}case_wrms.dat'.format(case_number,case_number),avg_IUFNO_wrms_10case, fmt="%16.7f")
np.savetxt('./AVG/IFNO/N{}/avg_IFNO_{}case_dissipation.dat'.format(case_number,case_number),avg_IUFNO_dissipation_10case, fmt="%16.7f")
np.savetxt('./AVG/IFNO/N{}/avg_IFNO_{}case_Ek_t.dat'.format(case_number,case_number),avg_IUFNO_Et_10case, fmt="%16.7f")
np.savetxt('./AVG/IFNO/N{}/avg_IFNO_{}case_inc1_PDFs.dat'.format(case_number,case_number),avg_IUFNO_inc1_PDFs_10case, fmt="%16.7f")
np.savetxt('./AVG/IFNO/N{}/avg_IFNO_{}case_vel_spec.dat'.format(case_number,case_number),avg_IUFNO_spectrum_10case, fmt="%16.7f")
np.savetxt('./AVG/IFNO/N{}/avg_IFNO_{}case_structrue2.dat'.format(case_number,case_number),avg_IUFNO_structrue2_10case, fmt="%16.7f")
np.savetxt('./AVG/IFNO/N{}/avg_IFNO_{}case_structrue4.dat'.format(case_number,case_number),avg_IUFNO_structrue4_10case, fmt="%16.7f")
np.savetxt('./AVG/IFNO/N{}/avg_IFNO_{}case_vort_PDFs.dat'.format(case_number,case_number),avg_IUFNO_vort_PDFs_10case, fmt="%16.7f")
np.savetxt('./AVG/IFNO/N{}/avg_IFNO_{}case_vort_statistics.dat'.format(case_number,case_number),avg_IUFNO_vort_statistics_10case, fmt="%16.7f")
'''
np.savetxt('./AVG/IFNO/{}case/avg_IFNO_{}case_urms.dat'.format(case_number,case_number),avg_IUFNO_urms_10case, fmt="%16.7f")
np.savetxt('./AVG/IFNO/{}case/avg_IFNO_{}case_wrms.dat'.format(case_number,case_number),avg_IUFNO_wrms_10case, fmt="%16.7f")
np.savetxt('./AVG/IFNO/{}case/avg_IFNO_{}case_dissipation.dat'.format(case_number,case_number),avg_IUFNO_dissipation_10case, fmt="%16.7f")
np.savetxt('./AVG/IFNO/{}case/avg_IFNO_{}case_Ek_t.dat'.format(case_number,case_number),avg_IUFNO_Et_10case, fmt="%16.7f")
np.savetxt('./AVG/IFNO/{}case/avg_IFNO_{}case_inc1_PDFs.dat'.format(case_number,case_number),avg_IUFNO_inc1_PDFs_10case, fmt="%16.7f")
np.savetxt('./AVG/IFNO/{}case/avg_IFNO_{}case_vel_spec.dat'.format(case_number,case_number),avg_IUFNO_spectrum_10case, fmt="%16.7f")
np.savetxt('./AVG/IFNO/{}case/avg_IFNO_{}case_structrue2.dat'.format(case_number,case_number),avg_IUFNO_structrue2_10case, fmt="%16.7f")
np.savetxt('./AVG/IFNO/{}case/avg_IFNO_{}case_structrue4.dat'.format(case_number,case_number),avg_IUFNO_structrue4_10case, fmt="%16.7f")
np.savetxt('./AVG/IFNO/{}case/avg_IFNO_{}case_vort_PDFs.dat'.format(case_number,case_number),avg_IUFNO_vort_PDFs_10case, fmt="%16.7f")
np.savetxt('./AVG/IFNO/{}case/avg_IFNO_{}case_vort_statistics.dat'.format(case_number,case_number),avg_IUFNO_vort_statistics_10case, fmt="%16.7f")
'''

#==========================================================================FNO
print("DSM getting dat!")
x_IUFNO_dissipation=[]
y_IUFNO_dissipation=[]
x_IUFNO_Et=[]
y_IUFNO_Et=[]
x_IUFNO_inc1_PDFs=[]
y_IUFNO_inc1_PDFs=[]
x_IUFNO_velspectrum=[]
y_IUFNO_velspectrum=[]
x_IUFNO_structrue2 = []
y_IUFNO_structrue2 = []
x_IUFNO_structrue4 = []
y_IUFNO_structrue4 = []
x_IUFNO_urms = []
y_IUFNO_urms = []
x_IUFNO_wrms = []
y_IUFNO_wrms = []
x_IUFNO_vort_PDFs = []
y_IUFNO_vort_PDFs = []
x_IUFNO_vort_statistics = []
y_IUFNO_vort_statistics = []
for case_n in range(case_number-1,case_number):
    # print(case_n)
    # 载入后处理文件，包括速度参数，PDFs，能谱，结构函数
    IUFNO_vel_parameter= np.loadtxt('./case{}/Result_LES32_DSM_gap200/post_result/vel_parameter.dat'.format(case_n+1),dtype=float, comments=['step'])
    IUFNO_ic1_PDFs = np.loadtxt('./case{}/Result_LES32_DSM_gap200/post_result/inc1_PDFs.dat'.format(case_n + 1), dtype=float,comments=['step'])
    IUFNO_spec = np.loadtxt('./case{}/Result_LES32_DSM_gap200/post_result/spectrum_vel.dat'.format(case_n + 1), dtype=float,comments=['variables', 'zone'])
    IUFNO_structrue2 = np.loadtxt('./case{}/Result_LES32_DSM_gap200/post_result/structure2.dat'.format(case_n + 1),dtype=float, comments=['step'])
    IUFNO_structrue4 = np.loadtxt('./case{}/Result_LES32_DSM_gap200/post_result/structure4.dat'.format(case_n + 1),dtype=float, comments=['step'])
    IUFNO_vort_PDFs = np.loadtxt('./case{}/Result_LES32_DSM_gap200/post_result/vort_PDFs.dat'.format(case_n + 1), dtype=float,comments=['variables', 'zone'])
    IUFNO_vort_statistics = np.loadtxt('./case{}/Result_LES32_DSM_gap200/post_result/vort_statistics.dat'.format(case_n + 1),dtype=float, comments=['step'])
    # print(VGM.shape)
    # 取出数据
    x_IUFNO_urms.append(IUFNO_vel_parameter[:,0])  # 只取出第一列数据
    y_IUFNO_urms.append(IUFNO_vel_parameter[:,3]) #只取出第二列数据
    x_IUFNO_wrms.append(IUFNO_vel_parameter[:,0])  # 只取出第一列数据
    y_IUFNO_wrms.append(IUFNO_vel_parameter[:,7]) #只取出第二列数据
    x_IUFNO_dissipation.append(IUFNO_vel_parameter[:,0])  # 只取出第一列数据
    y_IUFNO_dissipation.append(IUFNO_vel_parameter[:,8]) #只取出第二列数据
    x_IUFNO_Et.append(IUFNO_vel_parameter[:,0])  # 只取出第一列数据
    y_IUFNO_Et.append(IUFNO_vel_parameter[:,6]) #只取出第二列数据
    x_IUFNO_inc1_PDFs.append(IUFNO_ic1_PDFs[:,0])  # 只取出第一列数据
    y_IUFNO_inc1_PDFs.append(IUFNO_ic1_PDFs[:,1]) #只取出第二列数据
    x_IUFNO_velspectrum.append(IUFNO_spec[:,0])  # 只取出第一列数据
    y_IUFNO_velspectrum.append(IUFNO_spec[:,1]) #只取出第二列数据
    x_IUFNO_structrue2.append(IUFNO_structrue2[:,0])  # 只取出第一列数据
    y_IUFNO_structrue2.append(IUFNO_structrue2[:,1]) #只取出第二列数据
    x_IUFNO_structrue4.append(IUFNO_structrue4[:,0])  # 只取出第一列数据
    y_IUFNO_structrue4.append(IUFNO_structrue4[:,1]) #只取出第二列数据
    x_IUFNO_vort_PDFs.append(IUFNO_vort_PDFs[:,0])  # 只取出第一列数据
    y_IUFNO_vort_PDFs.append(IUFNO_vort_PDFs[:,1]) #只取出第二列数据
    x_IUFNO_vort_statistics.append(IUFNO_vort_statistics[:,0])  # 只取出第一列数据
    y_IUFNO_vort_statistics.append(IUFNO_vort_statistics[:,5]) #只取出第二列数据
# 转化为数组
x_IUFNO_urms_arr = np.asarray(x_IUFNO_urms) #列表转数组
y_IUFNO_urms_arr = np.asarray(y_IUFNO_urms) #列表转数组
x_IUFNO_wrms_arr = np.asarray(x_IUFNO_wrms) #列表转数组
y_IUFNO_wrms_arr = np.asarray(y_IUFNO_wrms) #列表转数组
x_IUFNO_dissipation_arr = np.asarray(x_IUFNO_dissipation) #列表转数组
y_IUFNO_dissipation_arr = np.asarray(y_IUFNO_dissipation) #列表转数组
x_IUFNO_Et_arr = np.asarray(x_IUFNO_Et) #列表转数组
y_IUFNO_Et_arr = np.asarray(y_IUFNO_Et) #列表转数组
x_IUFNO_inc1_PDFs_arr = np.asarray(x_IUFNO_inc1_PDFs) #列表转数组
y_IUFNO_inc1_PDFs_arr = np.asarray(y_IUFNO_inc1_PDFs) #列表转数组
x_IUFNO_spe_arr = np.asarray(x_IUFNO_velspectrum) #列表转数组
y_IUFNO_spe_arr = np.asarray(y_IUFNO_velspectrum) #列表转数组
x_IUFNO_structrue2 = np.asarray(x_IUFNO_structrue2) #列表转数组
y_IUFNO_structrue2 = np.asarray(y_IUFNO_structrue2) #列表转数组
x_IUFNO_structrue4 = np.asarray(x_IUFNO_structrue4) #列表转数组
y_IUFNO_structrue4 = np.asarray(y_IUFNO_structrue4) #列表转数组
x_IUFNO_vort_PDFs = np.asarray(x_IUFNO_vort_PDFs) #列表转数组
y_IUFNO_vort_PDFs = np.asarray(y_IUFNO_vort_PDFs) #列表转数组
x_IUFNO_vort_statistics = np.asarray(x_IUFNO_vort_statistics) #列表转数组
y_IUFNO_vort_statistics = np.asarray(y_IUFNO_vort_statistics) #列表转数组
# 取均值
x_urms_avg_case = np.mean(x_IUFNO_urms_arr,0) #行压缩成一行
y_urms_avg_case = np.mean(y_IUFNO_urms_arr,0) #行压缩成一行
x_wrms_avg_case = np.mean(x_IUFNO_wrms_arr,0) #行压缩成一行
y_wrms_avg_case = np.mean(y_IUFNO_wrms_arr,0) #行压缩成一行
x_dissipation_avg_case = np.mean(x_IUFNO_dissipation_arr,0) #行压缩成一行
y_dissipation_avg_case = np.mean(y_IUFNO_dissipation_arr,0) #行压缩成一行
x_Et_avg_case = np.mean(x_IUFNO_Et_arr,0) #行压缩成一行
y_Et_avg_case = np.mean(y_IUFNO_Et_arr,0) #行压缩成一行
x_inc1_PDFs_avg_case = np.mean(x_IUFNO_inc1_PDFs_arr,0) #行压缩成一行
y_inc1_PDFs_avg_case = np.mean(y_IUFNO_inc1_PDFs_arr,0) #行压缩成一行
x_spe_avg_case = np.mean(x_IUFNO_spe_arr,0) #行压缩成一行
y_spe_avg_case = np.mean(y_IUFNO_spe_arr,0) #行压缩成一行
x_structrue2_avg_case = np.mean(x_IUFNO_structrue2,0) #行压缩成一行
y_structrue2_avg_case = np.mean(y_IUFNO_structrue2,0) #行压缩成
x_structrue4_avg_case = np.mean(x_IUFNO_structrue4,0) #行压缩成一行
y_structrue4_avg_case = np.mean(y_IUFNO_structrue4,0) #行压缩成
x_vort_PDFs_avg_case = np.mean(x_IUFNO_vort_PDFs,0) #行压缩成一行
y_vort_PDFs_avg_case = np.mean(y_IUFNO_vort_PDFs,0) #行压缩成
x_vort_statistics_avg_case = np.mean(x_IUFNO_vort_statistics,0) #行压缩成一行
y_vort_statistics_avg_case = np.mean(y_IUFNO_vort_statistics,0) #行压缩成
# 拼接操作
avg_IUFNO_urms_10case=np.dstack((x_urms_avg_case,y_urms_avg_case)).squeeze() #拼接
avg_IUFNO_wrms_10case=np.dstack((x_wrms_avg_case,y_wrms_avg_case)).squeeze() #拼接
avg_IUFNO_dissipation_10case=np.dstack((x_dissipation_avg_case,y_dissipation_avg_case)).squeeze() #拼接
avg_IUFNO_Et_10case=np.dstack((x_Et_avg_case,y_Et_avg_case)).squeeze() #拼接
avg_IUFNO_inc1_PDFs_10case=np.dstack((x_inc1_PDFs_avg_case,y_inc1_PDFs_avg_case)).squeeze() #拼接
avg_IUFNO_spectrum_10case=np.dstack((x_spe_avg_case,y_spe_avg_case)).squeeze() #拼接
avg_IUFNO_structrue2_10case=np.dstack((x_structrue2_avg_case,y_structrue2_avg_case)).squeeze() #拼接
avg_IUFNO_structrue4_10case=np.dstack((x_structrue4_avg_case,y_structrue4_avg_case)).squeeze() #拼接
avg_IUFNO_vort_PDFs_10case=np.dstack((x_vort_PDFs_avg_case,y_vort_PDFs_avg_case)).squeeze() #拼接
avg_IUFNO_vort_statistics_10case=np.dstack((x_vort_statistics_avg_case,y_vort_statistics_avg_case)).squeeze() #拼接
#导出均值

np.savetxt('./AVG/DSM/N{}/avg_DSM_{}case_urms.dat'.format(case_number,case_number),avg_IUFNO_urms_10case, fmt="%16.7f")
np.savetxt('./AVG/DSM/N{}/avg_DSM_{}case_wrms.dat'.format(case_number,case_number),avg_IUFNO_wrms_10case, fmt="%16.7f")
np.savetxt('./AVG/DSM/N{}/avg_DSM_{}case_dissipation.dat'.format(case_number,case_number),avg_IUFNO_dissipation_10case, fmt="%16.7f")
np.savetxt('./AVG/DSM/N{}/avg_DSM_{}case_Ek_t.dat'.format(case_number,case_number),avg_IUFNO_Et_10case, fmt="%16.7f")
np.savetxt('./AVG/DSM/N{}/avg_DSM_{}case_inc1_PDFs.dat'.format(case_number,case_number),avg_IUFNO_inc1_PDFs_10case, fmt="%16.7f")
np.savetxt('./AVG/DSM/N{}/avg_DSM_{}case_vel_spec.dat'.format(case_number,case_number),avg_IUFNO_spectrum_10case, fmt="%16.7f")
np.savetxt('./AVG/DSM/N{}/avg_DSM_{}case_structrue2.dat'.format(case_number,case_number),avg_IUFNO_structrue2_10case, fmt="%16.7f")
np.savetxt('./AVG/DSM/N{}/avg_DSM_{}case_structrue4.dat'.format(case_number,case_number),avg_IUFNO_structrue4_10case, fmt="%16.7f")
np.savetxt('./AVG/DSM/N{}/avg_DSM_{}case_vort_PDFs.dat'.format(case_number,case_number),avg_IUFNO_vort_PDFs_10case, fmt="%16.7f")
np.savetxt('./AVG/DSM/N{}/avg_DSM_{}case_vort_statistics.dat'.format(case_number,case_number),avg_IUFNO_vort_statistics_10case, fmt="%16.7f")
'''
np.savetxt('./AVG/DSM/{}case/avg_DSM_{}case_urms.dat'.format(case_number,case_number),avg_IUFNO_urms_10case, fmt="%16.7f")
np.savetxt('./AVG/DSM/{}case/avg_DSM_{}case_wrms.dat'.format(case_number,case_number),avg_IUFNO_wrms_10case, fmt="%16.7f")
np.savetxt('./AVG/DSM/{}case/avg_DSM_{}case_dissipation.dat'.format(case_number,case_number),avg_IUFNO_dissipation_10case, fmt="%16.7f")
np.savetxt('./AVG/DSM/{}case/avg_DSM_{}case_Ek_t.dat'.format(case_number,case_number),avg_IUFNO_Et_10case, fmt="%16.7f")
np.savetxt('./AVG/DSM/{}case/avg_DSM_{}case_inc1_PDFs.dat'.format(case_number,case_number),avg_IUFNO_inc1_PDFs_10case, fmt="%16.7f")
np.savetxt('./AVG/DSM/{}case/avg_DSM_{}case_vel_spec.dat'.format(case_number,case_number),avg_IUFNO_spectrum_10case, fmt="%16.7f")
np.savetxt('./AVG/DSM/{}case/avg_DSM_{}case_structrue2.dat'.format(case_number,case_number),avg_IUFNO_structrue2_10case, fmt="%16.7f")
np.savetxt('./AVG/DSM/{}case/avg_DSM_{}case_structrue4.dat'.format(case_number,case_number),avg_IUFNO_structrue4_10case, fmt="%16.7f")
np.savetxt('./AVG/DSM/{}case/avg_DSM_{}case_vort_PDFs.dat'.format(case_number,case_number),avg_IUFNO_vort_PDFs_10case, fmt="%16.7f")
np.savetxt('./AVG/DSM/{}case/avg_DSM_{}case_vort_statistics.dat'.format(case_number,case_number),avg_IUFNO_vort_statistics_10case, fmt="%16.7f")
'''

#==========================================================================FNO
print("DSM mag0.1 getting dat!")
x_IUFNO_dissipation=[]
y_IUFNO_dissipation=[]
x_IUFNO_Et=[]
y_IUFNO_Et=[]
x_IUFNO_inc1_PDFs=[]
y_IUFNO_inc1_PDFs=[]
x_IUFNO_velspectrum=[]
y_IUFNO_velspectrum=[]
x_IUFNO_structrue2 = []
y_IUFNO_structrue2 = []
x_IUFNO_structrue4 = []
y_IUFNO_structrue4 = []
x_IUFNO_urms = []
y_IUFNO_urms = []
x_IUFNO_wrms = []
y_IUFNO_wrms = []
x_IUFNO_vort_PDFs = []
y_IUFNO_vort_PDFs = []
x_IUFNO_vort_statistics = []
y_IUFNO_vort_statistics = []
for case_n in range(case_number-1,case_number):
    # print(case_n)
    # 载入后处理文件，包括速度参数，PDFs，能谱，结构函数
    IUFNO_vel_parameter= np.loadtxt('./case{}/Result_LES32_DSM_mag0.1_gap200/post_result/vel_parameter.dat'.format(case_n+1),dtype=float, comments=['step'])
    IUFNO_ic1_PDFs = np.loadtxt('./case{}/Result_LES32_DSM_mag0.1_gap200/post_result/inc1_PDFs.dat'.format(case_n + 1), dtype=float,comments=['step'])
    IUFNO_spec = np.loadtxt('./case{}/Result_LES32_DSM_mag0.1_gap200/post_result/spectrum_vel.dat'.format(case_n + 1), dtype=float,comments=['variables', 'zone'])
    IUFNO_structrue2 = np.loadtxt('./case{}/Result_LES32_DSM_mag0.1_gap200/post_result/structure2.dat'.format(case_n + 1),dtype=float, comments=['step'])
    IUFNO_structrue4 = np.loadtxt('./case{}/Result_LES32_DSM_mag0.1_gap200/post_result/structure4.dat'.format(case_n + 1),dtype=float, comments=['step'])
    IUFNO_vort_PDFs = np.loadtxt('./case{}/Result_LES32_DSM_mag0.1_gap200/post_result/vort_PDFs.dat'.format(case_n + 1), dtype=float,comments=['variables', 'zone'])
    IUFNO_vort_statistics = np.loadtxt('./case{}/Result_LES32_DSM_mag0.1_gap200/post_result/vort_statistics.dat'.format(case_n + 1),dtype=float, comments=['step'])
    # print(VGM.shape)
    # 取出数据
    x_IUFNO_urms.append(IUFNO_vel_parameter[:,0])  # 只取出第一列数据
    y_IUFNO_urms.append(IUFNO_vel_parameter[:,3]) #只取出第二列数据
    x_IUFNO_wrms.append(IUFNO_vel_parameter[:,0])  # 只取出第一列数据
    y_IUFNO_wrms.append(IUFNO_vel_parameter[:,7]) #只取出第二列数据
    x_IUFNO_dissipation.append(IUFNO_vel_parameter[:,0])  # 只取出第一列数据
    y_IUFNO_dissipation.append(IUFNO_vel_parameter[:,8]) #只取出第二列数据
    x_IUFNO_Et.append(IUFNO_vel_parameter[:,0])  # 只取出第一列数据
    y_IUFNO_Et.append(IUFNO_vel_parameter[:,6]) #只取出第二列数据
    x_IUFNO_inc1_PDFs.append(IUFNO_ic1_PDFs[:,0])  # 只取出第一列数据
    y_IUFNO_inc1_PDFs.append(IUFNO_ic1_PDFs[:,1]) #只取出第二列数据
    x_IUFNO_velspectrum.append(IUFNO_spec[:,0])  # 只取出第一列数据
    y_IUFNO_velspectrum.append(IUFNO_spec[:,1]) #只取出第二列数据
    x_IUFNO_structrue2.append(IUFNO_structrue2[:,0])  # 只取出第一列数据
    y_IUFNO_structrue2.append(IUFNO_structrue2[:,1]) #只取出第二列数据
    x_IUFNO_structrue4.append(IUFNO_structrue4[:,0])  # 只取出第一列数据
    y_IUFNO_structrue4.append(IUFNO_structrue4[:,1]) #只取出第二列数据
    x_IUFNO_vort_PDFs.append(IUFNO_vort_PDFs[:,0])  # 只取出第一列数据
    y_IUFNO_vort_PDFs.append(IUFNO_vort_PDFs[:,1]) #只取出第二列数据
    x_IUFNO_vort_statistics.append(IUFNO_vort_statistics[:,0])  # 只取出第一列数据
    y_IUFNO_vort_statistics.append(IUFNO_vort_statistics[:,5]) #只取出第二列数据
# 转化为数组
x_IUFNO_urms_arr = np.asarray(x_IUFNO_urms) #列表转数组
y_IUFNO_urms_arr = np.asarray(y_IUFNO_urms) #列表转数组
x_IUFNO_wrms_arr = np.asarray(x_IUFNO_wrms) #列表转数组
y_IUFNO_wrms_arr = np.asarray(y_IUFNO_wrms) #列表转数组
x_IUFNO_dissipation_arr = np.asarray(x_IUFNO_dissipation) #列表转数组
y_IUFNO_dissipation_arr = np.asarray(y_IUFNO_dissipation) #列表转数组
x_IUFNO_Et_arr = np.asarray(x_IUFNO_Et) #列表转数组
y_IUFNO_Et_arr = np.asarray(y_IUFNO_Et) #列表转数组
x_IUFNO_inc1_PDFs_arr = np.asarray(x_IUFNO_inc1_PDFs) #列表转数组
y_IUFNO_inc1_PDFs_arr = np.asarray(y_IUFNO_inc1_PDFs) #列表转数组
x_IUFNO_spe_arr = np.asarray(x_IUFNO_velspectrum) #列表转数组
y_IUFNO_spe_arr = np.asarray(y_IUFNO_velspectrum) #列表转数组
x_IUFNO_structrue2 = np.asarray(x_IUFNO_structrue2) #列表转数组
y_IUFNO_structrue2 = np.asarray(y_IUFNO_structrue2) #列表转数组
x_IUFNO_structrue4 = np.asarray(x_IUFNO_structrue4) #列表转数组
y_IUFNO_structrue4 = np.asarray(y_IUFNO_structrue4) #列表转数组
x_IUFNO_vort_PDFs = np.asarray(x_IUFNO_vort_PDFs) #列表转数组
y_IUFNO_vort_PDFs = np.asarray(y_IUFNO_vort_PDFs) #列表转数组
x_IUFNO_vort_statistics = np.asarray(x_IUFNO_vort_statistics) #列表转数组
y_IUFNO_vort_statistics = np.asarray(y_IUFNO_vort_statistics) #列表转数组
# 取均值
x_urms_avg_case = np.mean(x_IUFNO_urms_arr,0) #行压缩成一行
y_urms_avg_case = np.mean(y_IUFNO_urms_arr,0) #行压缩成一行
x_wrms_avg_case = np.mean(x_IUFNO_wrms_arr,0) #行压缩成一行
y_wrms_avg_case = np.mean(y_IUFNO_wrms_arr,0) #行压缩成一行
x_dissipation_avg_case = np.mean(x_IUFNO_dissipation_arr,0) #行压缩成一行
y_dissipation_avg_case = np.mean(y_IUFNO_dissipation_arr,0) #行压缩成一行
x_Et_avg_case = np.mean(x_IUFNO_Et_arr,0) #行压缩成一行
y_Et_avg_case = np.mean(y_IUFNO_Et_arr,0) #行压缩成一行
x_inc1_PDFs_avg_case = np.mean(x_IUFNO_inc1_PDFs_arr,0) #行压缩成一行
y_inc1_PDFs_avg_case = np.mean(y_IUFNO_inc1_PDFs_arr,0) #行压缩成一行
x_spe_avg_case = np.mean(x_IUFNO_spe_arr,0) #行压缩成一行
y_spe_avg_case = np.mean(y_IUFNO_spe_arr,0) #行压缩成一行
x_structrue2_avg_case = np.mean(x_IUFNO_structrue2,0) #行压缩成一行
y_structrue2_avg_case = np.mean(y_IUFNO_structrue2,0) #行压缩成
x_structrue4_avg_case = np.mean(x_IUFNO_structrue4,0) #行压缩成一行
y_structrue4_avg_case = np.mean(y_IUFNO_structrue4,0) #行压缩成
x_vort_PDFs_avg_case = np.mean(x_IUFNO_vort_PDFs,0) #行压缩成一行
y_vort_PDFs_avg_case = np.mean(y_IUFNO_vort_PDFs,0) #行压缩成
x_vort_statistics_avg_case = np.mean(x_IUFNO_vort_statistics,0) #行压缩成一行
y_vort_statistics_avg_case = np.mean(y_IUFNO_vort_statistics,0) #行压缩成
# 拼接操作
avg_IUFNO_urms_10case=np.dstack((x_urms_avg_case,y_urms_avg_case)).squeeze() #拼接
avg_IUFNO_wrms_10case=np.dstack((x_wrms_avg_case,y_wrms_avg_case)).squeeze() #拼接
avg_IUFNO_dissipation_10case=np.dstack((x_dissipation_avg_case,y_dissipation_avg_case)).squeeze() #拼接
avg_IUFNO_Et_10case=np.dstack((x_Et_avg_case,y_Et_avg_case)).squeeze() #拼接
avg_IUFNO_inc1_PDFs_10case=np.dstack((x_inc1_PDFs_avg_case,y_inc1_PDFs_avg_case)).squeeze() #拼接
avg_IUFNO_spectrum_10case=np.dstack((x_spe_avg_case,y_spe_avg_case)).squeeze() #拼接
avg_IUFNO_structrue2_10case=np.dstack((x_structrue2_avg_case,y_structrue2_avg_case)).squeeze() #拼接
avg_IUFNO_structrue4_10case=np.dstack((x_structrue4_avg_case,y_structrue4_avg_case)).squeeze() #拼接
avg_IUFNO_vort_PDFs_10case=np.dstack((x_vort_PDFs_avg_case,y_vort_PDFs_avg_case)).squeeze() #拼接
avg_IUFNO_vort_statistics_10case=np.dstack((x_vort_statistics_avg_case,y_vort_statistics_avg_case)).squeeze() #拼接
#导出均值

np.savetxt('./AVG/DSM_mag0.1/N{}/avg_DSM_mag0.1_{}case_urms.dat'.format(case_number,case_number),avg_IUFNO_urms_10case, fmt="%16.7f")
np.savetxt('./AVG/DSM_mag0.1/N{}/avg_DSM_mag0.1_{}case_wrms.dat'.format(case_number,case_number),avg_IUFNO_wrms_10case, fmt="%16.7f")
np.savetxt('./AVG/DSM_mag0.1/N{}/avg_DSM_mag0.1_{}case_dissipation.dat'.format(case_number,case_number),avg_IUFNO_dissipation_10case, fmt="%16.7f")
np.savetxt('./AVG/DSM_mag0.1/N{}/avg_DSM_mag0.1_{}case_Ek_t.dat'.format(case_number,case_number),avg_IUFNO_Et_10case, fmt="%16.7f")
np.savetxt('./AVG/DSM_mag0.1/N{}/avg_DSM_mag0.1_{}case_inc1_PDFs.dat'.format(case_number,case_number),avg_IUFNO_inc1_PDFs_10case, fmt="%16.7f")
np.savetxt('./AVG/DSM_mag0.1/N{}/avg_DSM_mag0.1_{}case_vel_spec.dat'.format(case_number,case_number),avg_IUFNO_spectrum_10case, fmt="%16.7f")
np.savetxt('./AVG/DSM_mag0.1/N{}/avg_DSM_mag0.1_{}case_structrue2.dat'.format(case_number,case_number),avg_IUFNO_structrue2_10case, fmt="%16.7f")
np.savetxt('./AVG/DSM_mag0.1/N{}/avg_DSM_mag0.1_{}case_structrue4.dat'.format(case_number,case_number),avg_IUFNO_structrue4_10case, fmt="%16.7f")
np.savetxt('./AVG/DSM_mag0.1/N{}/avg_DSM_mag0.1_{}case_vort_PDFs.dat'.format(case_number,case_number),avg_IUFNO_vort_PDFs_10case, fmt="%16.7f")
np.savetxt('./AVG/DSM_mag0.1/N{}/avg_DSM_mag0.1_{}case_vort_statistics.dat'.format(case_number,case_number),avg_IUFNO_vort_statistics_10case, fmt="%16.7f")
'''
np.savetxt('./AVG/DSM_mag0.1/{}case/avg_DSM_mag0.1_{}case_urms.dat'.format(case_number,case_number),avg_IUFNO_urms_10case, fmt="%16.7f")
np.savetxt('./AVG/DSM_mag0.1/{}case/avg_DSM_mag0.1_{}case_wrms.dat'.format(case_number,case_number),avg_IUFNO_wrms_10case, fmt="%16.7f")
np.savetxt('./AVG/DSM_mag0.1/{}case/avg_DSM_mag0.1_{}case_dissipation.dat'.format(case_number,case_number),avg_IUFNO_dissipation_10case, fmt="%16.7f")
np.savetxt('./AVG/DSM_mag0.1/{}case/avg_DSM_mag0.1_{}case_Ek_t.dat'.format(case_number,case_number),avg_IUFNO_Et_10case, fmt="%16.7f")
np.savetxt('./AVG/DSM_mag0.1/{}case/avg_DSM_mag0.1_{}case_inc1_PDFs.dat'.format(case_number,case_number),avg_IUFNO_inc1_PDFs_10case, fmt="%16.7f")
np.savetxt('./AVG/DSM_mag0.1/{}case/avg_DSM_mag0.1_{}case_vel_spec.dat'.format(case_number,case_number),avg_IUFNO_spectrum_10case, fmt="%16.7f")
np.savetxt('./AVG/DSM_mag0.1/{}case/avg_DSM_mag0.1_{}case_structrue2.dat'.format(case_number,case_number),avg_IUFNO_structrue2_10case, fmt="%16.7f")
np.savetxt('./AVG/DSM_mag0.1/{}case/avg_DSM_mag0.1_{}case_structrue4.dat'.format(case_number,case_number),avg_IUFNO_structrue4_10case, fmt="%16.7f")
np.savetxt('./AVG/DSM_mag0.1/{}case/avg_DSM_mag0.1_{}case_vort_PDFs.dat'.format(case_number,case_number),avg_IUFNO_vort_PDFs_10case, fmt="%16.7f")
np.savetxt('./AVG/DSM_mag0.1/{}case/avg_DSM_mag0.1_{}case_vort_statistics.dat'.format(case_number,case_number),avg_IUFNO_vort_statistics_10case, fmt="%16.7f")
'''

#==========================================================================FNO
print("DSM mag0.5 getting dat!")
x_IUFNO_dissipation=[]
y_IUFNO_dissipation=[]
x_IUFNO_Et=[]
y_IUFNO_Et=[]
x_IUFNO_inc1_PDFs=[]
y_IUFNO_inc1_PDFs=[]
x_IUFNO_velspectrum=[]
y_IUFNO_velspectrum=[]
x_IUFNO_structrue2 = []
y_IUFNO_structrue2 = []
x_IUFNO_structrue4 = []
y_IUFNO_structrue4 = []
x_IUFNO_urms = []
y_IUFNO_urms = []
x_IUFNO_wrms = []
y_IUFNO_wrms = []
x_IUFNO_vort_PDFs = []
y_IUFNO_vort_PDFs = []
x_IUFNO_vort_statistics = []
y_IUFNO_vort_statistics = []
for case_n in range(case_number-1,case_number):
    # print(case_n)
    # 载入后处理文件，包括速度参数，PDFs，能谱，结构函数
    IUFNO_vel_parameter= np.loadtxt('./case{}/Result_LES32_DSM_mag0.5_gap200/post_result/vel_parameter.dat'.format(case_n+1),dtype=float, comments=['step'])
    IUFNO_ic1_PDFs = np.loadtxt('./case{}/Result_LES32_DSM_mag0.5_gap200/post_result/inc1_PDFs.dat'.format(case_n + 1), dtype=float,comments=['step'])
    IUFNO_spec = np.loadtxt('./case{}/Result_LES32_DSM_mag0.5_gap200/post_result/spectrum_vel.dat'.format(case_n + 1), dtype=float,comments=['variables', 'zone'])
    IUFNO_structrue2 = np.loadtxt('./case{}/Result_LES32_DSM_mag0.5_gap200/post_result/structure2.dat'.format(case_n + 1),dtype=float, comments=['step'])
    IUFNO_structrue4 = np.loadtxt('./case{}/Result_LES32_DSM_mag0.5_gap200/post_result/structure4.dat'.format(case_n + 1),dtype=float, comments=['step'])
    IUFNO_vort_PDFs = np.loadtxt('./case{}/Result_LES32_DSM_mag0.5_gap200/post_result/vort_PDFs.dat'.format(case_n + 1), dtype=float,comments=['variables', 'zone'])
    IUFNO_vort_statistics = np.loadtxt('./case{}/Result_LES32_DSM_mag0.5_gap200/post_result/vort_statistics.dat'.format(case_n + 1),dtype=float, comments=['step'])
    # print(VGM.shape)
    # 取出数据
    x_IUFNO_urms.append(IUFNO_vel_parameter[:,0])  # 只取出第一列数据
    y_IUFNO_urms.append(IUFNO_vel_parameter[:,3]) #只取出第二列数据
    x_IUFNO_wrms.append(IUFNO_vel_parameter[:,0])  # 只取出第一列数据
    y_IUFNO_wrms.append(IUFNO_vel_parameter[:,7]) #只取出第二列数据
    x_IUFNO_dissipation.append(IUFNO_vel_parameter[:,0])  # 只取出第一列数据
    y_IUFNO_dissipation.append(IUFNO_vel_parameter[:,8]) #只取出第二列数据
    x_IUFNO_Et.append(IUFNO_vel_parameter[:,0])  # 只取出第一列数据
    y_IUFNO_Et.append(IUFNO_vel_parameter[:,6]) #只取出第二列数据
    x_IUFNO_inc1_PDFs.append(IUFNO_ic1_PDFs[:,0])  # 只取出第一列数据
    y_IUFNO_inc1_PDFs.append(IUFNO_ic1_PDFs[:,1]) #只取出第二列数据
    x_IUFNO_velspectrum.append(IUFNO_spec[:,0])  # 只取出第一列数据
    y_IUFNO_velspectrum.append(IUFNO_spec[:,1]) #只取出第二列数据
    x_IUFNO_structrue2.append(IUFNO_structrue2[:,0])  # 只取出第一列数据
    y_IUFNO_structrue2.append(IUFNO_structrue2[:,1]) #只取出第二列数据
    x_IUFNO_structrue4.append(IUFNO_structrue4[:,0])  # 只取出第一列数据
    y_IUFNO_structrue4.append(IUFNO_structrue4[:,1]) #只取出第二列数据
    x_IUFNO_vort_PDFs.append(IUFNO_vort_PDFs[:,0])  # 只取出第一列数据
    y_IUFNO_vort_PDFs.append(IUFNO_vort_PDFs[:,1]) #只取出第二列数据
    x_IUFNO_vort_statistics.append(IUFNO_vort_statistics[:,0])  # 只取出第一列数据
    y_IUFNO_vort_statistics.append(IUFNO_vort_statistics[:,5]) #只取出第二列数据
# 转化为数组
x_IUFNO_urms_arr = np.asarray(x_IUFNO_urms) #列表转数组
y_IUFNO_urms_arr = np.asarray(y_IUFNO_urms) #列表转数组
x_IUFNO_wrms_arr = np.asarray(x_IUFNO_wrms) #列表转数组
y_IUFNO_wrms_arr = np.asarray(y_IUFNO_wrms) #列表转数组
x_IUFNO_dissipation_arr = np.asarray(x_IUFNO_dissipation) #列表转数组
y_IUFNO_dissipation_arr = np.asarray(y_IUFNO_dissipation) #列表转数组
x_IUFNO_Et_arr = np.asarray(x_IUFNO_Et) #列表转数组
y_IUFNO_Et_arr = np.asarray(y_IUFNO_Et) #列表转数组
x_IUFNO_inc1_PDFs_arr = np.asarray(x_IUFNO_inc1_PDFs) #列表转数组
y_IUFNO_inc1_PDFs_arr = np.asarray(y_IUFNO_inc1_PDFs) #列表转数组
x_IUFNO_spe_arr = np.asarray(x_IUFNO_velspectrum) #列表转数组
y_IUFNO_spe_arr = np.asarray(y_IUFNO_velspectrum) #列表转数组
x_IUFNO_structrue2 = np.asarray(x_IUFNO_structrue2) #列表转数组
y_IUFNO_structrue2 = np.asarray(y_IUFNO_structrue2) #列表转数组
x_IUFNO_structrue4 = np.asarray(x_IUFNO_structrue4) #列表转数组
y_IUFNO_structrue4 = np.asarray(y_IUFNO_structrue4) #列表转数组
x_IUFNO_vort_PDFs = np.asarray(x_IUFNO_vort_PDFs) #列表转数组
y_IUFNO_vort_PDFs = np.asarray(y_IUFNO_vort_PDFs) #列表转数组
x_IUFNO_vort_statistics = np.asarray(x_IUFNO_vort_statistics) #列表转数组
y_IUFNO_vort_statistics = np.asarray(y_IUFNO_vort_statistics) #列表转数组
# 取均值
x_urms_avg_case = np.mean(x_IUFNO_urms_arr,0) #行压缩成一行
y_urms_avg_case = np.mean(y_IUFNO_urms_arr,0) #行压缩成一行
x_wrms_avg_case = np.mean(x_IUFNO_wrms_arr,0) #行压缩成一行
y_wrms_avg_case = np.mean(y_IUFNO_wrms_arr,0) #行压缩成一行
x_dissipation_avg_case = np.mean(x_IUFNO_dissipation_arr,0) #行压缩成一行
y_dissipation_avg_case = np.mean(y_IUFNO_dissipation_arr,0) #行压缩成一行
x_Et_avg_case = np.mean(x_IUFNO_Et_arr,0) #行压缩成一行
y_Et_avg_case = np.mean(y_IUFNO_Et_arr,0) #行压缩成一行
x_inc1_PDFs_avg_case = np.mean(x_IUFNO_inc1_PDFs_arr,0) #行压缩成一行
y_inc1_PDFs_avg_case = np.mean(y_IUFNO_inc1_PDFs_arr,0) #行压缩成一行
x_spe_avg_case = np.mean(x_IUFNO_spe_arr,0) #行压缩成一行
y_spe_avg_case = np.mean(y_IUFNO_spe_arr,0) #行压缩成一行
x_structrue2_avg_case = np.mean(x_IUFNO_structrue2,0) #行压缩成一行
y_structrue2_avg_case = np.mean(y_IUFNO_structrue2,0) #行压缩成
x_structrue4_avg_case = np.mean(x_IUFNO_structrue4,0) #行压缩成一行
y_structrue4_avg_case = np.mean(y_IUFNO_structrue4,0) #行压缩成
x_vort_PDFs_avg_case = np.mean(x_IUFNO_vort_PDFs,0) #行压缩成一行
y_vort_PDFs_avg_case = np.mean(y_IUFNO_vort_PDFs,0) #行压缩成
x_vort_statistics_avg_case = np.mean(x_IUFNO_vort_statistics,0) #行压缩成一行
y_vort_statistics_avg_case = np.mean(y_IUFNO_vort_statistics,0) #行压缩成
# 拼接操作
avg_IUFNO_urms_10case=np.dstack((x_urms_avg_case,y_urms_avg_case)).squeeze() #拼接
avg_IUFNO_wrms_10case=np.dstack((x_wrms_avg_case,y_wrms_avg_case)).squeeze() #拼接
avg_IUFNO_dissipation_10case=np.dstack((x_dissipation_avg_case,y_dissipation_avg_case)).squeeze() #拼接
avg_IUFNO_Et_10case=np.dstack((x_Et_avg_case,y_Et_avg_case)).squeeze() #拼接
avg_IUFNO_inc1_PDFs_10case=np.dstack((x_inc1_PDFs_avg_case,y_inc1_PDFs_avg_case)).squeeze() #拼接
avg_IUFNO_spectrum_10case=np.dstack((x_spe_avg_case,y_spe_avg_case)).squeeze() #拼接
avg_IUFNO_structrue2_10case=np.dstack((x_structrue2_avg_case,y_structrue2_avg_case)).squeeze() #拼接
avg_IUFNO_structrue4_10case=np.dstack((x_structrue4_avg_case,y_structrue4_avg_case)).squeeze() #拼接
avg_IUFNO_vort_PDFs_10case=np.dstack((x_vort_PDFs_avg_case,y_vort_PDFs_avg_case)).squeeze() #拼接
avg_IUFNO_vort_statistics_10case=np.dstack((x_vort_statistics_avg_case,y_vort_statistics_avg_case)).squeeze() #拼接
#导出均值

np.savetxt('./AVG/DSM_mag0.5/N{}/avg_DSM_mag0.5_{}case_urms.dat'.format(case_number,case_number),avg_IUFNO_urms_10case, fmt="%16.7f")
np.savetxt('./AVG/DSM_mag0.5/N{}/avg_DSM_mag0.5_{}case_wrms.dat'.format(case_number,case_number),avg_IUFNO_wrms_10case, fmt="%16.7f")
np.savetxt('./AVG/DSM_mag0.5/N{}/avg_DSM_mag0.5_{}case_dissipation.dat'.format(case_number,case_number),avg_IUFNO_dissipation_10case, fmt="%16.7f")
np.savetxt('./AVG/DSM_mag0.5/N{}/avg_DSM_mag0.5_{}case_Ek_t.dat'.format(case_number,case_number),avg_IUFNO_Et_10case, fmt="%16.7f")
np.savetxt('./AVG/DSM_mag0.5/N{}/avg_DSM_mag0.5_{}case_inc1_PDFs.dat'.format(case_number,case_number),avg_IUFNO_inc1_PDFs_10case, fmt="%16.7f")
np.savetxt('./AVG/DSM_mag0.5/N{}/avg_DSM_mag0.5_{}case_vel_spec.dat'.format(case_number,case_number),avg_IUFNO_spectrum_10case, fmt="%16.7f")
np.savetxt('./AVG/DSM_mag0.5/N{}/avg_DSM_mag0.5_{}case_structrue2.dat'.format(case_number,case_number),avg_IUFNO_structrue2_10case, fmt="%16.7f")
np.savetxt('./AVG/DSM_mag0.5/N{}/avg_DSM_mag0.5_{}case_structrue4.dat'.format(case_number,case_number),avg_IUFNO_structrue4_10case, fmt="%16.7f")
np.savetxt('./AVG/DSM_mag0.5/N{}/avg_DSM_mag0.5_{}case_vort_PDFs.dat'.format(case_number,case_number),avg_IUFNO_vort_PDFs_10case, fmt="%16.7f")
np.savetxt('./AVG/DSM_mag0.5/N{}/avg_DSM_mag0.5_{}case_vort_statistics.dat'.format(case_number,case_number),avg_IUFNO_vort_statistics_10case, fmt="%16.7f")
'''
np.savetxt('./AVG/DSM_mag0.5/{}case/avg_DSM_mag0.5_{}case_urms.dat'.format(case_number,case_number),avg_IUFNO_urms_10case, fmt="%16.7f")
np.savetxt('./AVG/DSM_mag0.5/{}case/avg_DSM_mag0.5_{}case_wrms.dat'.format(case_number,case_number),avg_IUFNO_wrms_10case, fmt="%16.7f")
np.savetxt('./AVG/DSM_mag0.5/{}case/avg_DSM_mag0.5_{}case_dissipation.dat'.format(case_number,case_number),avg_IUFNO_dissipation_10case, fmt="%16.7f")
np.savetxt('./AVG/DSM_mag0.5/{}case/avg_DSM_mag0.5_{}case_Ek_t.dat'.format(case_number,case_number),avg_IUFNO_Et_10case, fmt="%16.7f")
np.savetxt('./AVG/DSM_mag0.5/{}case/avg_DSM_mag0.5_{}case_inc1_PDFs.dat'.format(case_number,case_number),avg_IUFNO_inc1_PDFs_10case, fmt="%16.7f")
np.savetxt('./AVG/DSM_mag0.5/{}case/avg_DSM_mag0.5_{}case_vel_spec.dat'.format(case_number,case_number),avg_IUFNO_spectrum_10case, fmt="%16.7f")
np.savetxt('./AVG/DSM_mag0.5/{}case/avg_DSM_mag0.5_{}case_structrue2.dat'.format(case_number,case_number),avg_IUFNO_structrue2_10case, fmt="%16.7f")
np.savetxt('./AVG/DSM_mag0.5/{}case/avg_DSM_mag0.5_{}case_structrue4.dat'.format(case_number,case_number),avg_IUFNO_structrue4_10case, fmt="%16.7f")
np.savetxt('./AVG/DSM_mag0.5/{}case/avg_DSM_mag0.5_{}case_vort_PDFs.dat'.format(case_number,case_number),avg_IUFNO_vort_PDFs_10case, fmt="%16.7f")
np.savetxt('./AVG/DSM_mag0.5/{}case/avg_DSM_mag0.5_{}case_vort_statistics.dat'.format(case_number,case_number),avg_IUFNO_vort_statistics_10case, fmt="%16.7f")
'''


print("Done!")