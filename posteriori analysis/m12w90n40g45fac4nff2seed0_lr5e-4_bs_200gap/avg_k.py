"""
@author: admin
"""
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import os

mag_list=[0.1,0.5,1,2,5,10]
mag_list=[1,2,5,10]
#os.chdir(r'C:\Users\Lenovo\Desktop\PINO_3d\post\plot_result')
case_number_list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
#case_number_list = [30,1,10,20]
timestep = 600

for im, mag in enumerate(mag_list):

    for idx, case_number in enumerate(case_number_list):
      
       
        #==========================================================================FNO
        print("IFNO getting dat!")
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
        x_IUFNO_Strms = []
        y_IUFNO_Strms = []
        x_IUFNO_St_PDFs = []
        y_IUFNO_St_PDFs = []
        x_IUFNO_St_statistics = []
        y_IUFNO_St_statistics = []    
        for case_n in range(case_number-1,case_number):
            # print(case_n)
            # 载入后处理文件，包括速度参数，PDFs，能谱，结构函数
            IUFNO_vel_parameter= np.loadtxt('./case{}/Result_LES32_IFNO_gap200_mag{}/post_result/vel_parameter.dat'.format(case_n+1,mag),dtype=float, comments=['step'])
            IUFNO_ic1_PDFs = np.loadtxt('./case{}/Result_LES32_IFNO_gap200_mag{}/post_result/inc1_PDFs.dat'.format(case_n+1,mag), dtype=float,comments=['step'])
            IUFNO_spec = np.loadtxt('./case{}/Result_LES32_IFNO_gap200_mag{}/post_result/spectrum_vel.dat'.format(case_n+1,mag), dtype=float,comments=['variables', 'zone'])
            IUFNO_structrue2 = np.loadtxt('./case{}/Result_LES32_IFNO_gap200_mag{}/post_result/structure2.dat'.format(case_n+1,mag),dtype=float, comments=['step'])
            IUFNO_structrue4 = np.loadtxt('./case{}/Result_LES32_IFNO_gap200_mag{}/post_result/structure4.dat'.format(case_n+1,mag),dtype=float, comments=['step'])
            IUFNO_vort_PDFs = np.loadtxt('./case{}/Result_LES32_IFNO_gap200_mag{}/post_result/vort_PDFs.dat'.format(case_n+1,mag), dtype=float,comments=['variables', 'zone'])
            IUFNO_vort_statistics = np.loadtxt('./case{}/Result_LES32_IFNO_gap200_mag{}/post_result/vort_statistics.dat'.format(case_n+1,mag),dtype=float, comments=['step'])
            IUFNO_St_PDFs = np.loadtxt('./case{}/Result_LES32_IFNO_gap200_mag{}/post_result/St_PDFs.dat'.format(case_n+1,mag), dtype=float,comments=['variables', 'zone'])
            IUFNO_St_statistics = np.loadtxt('./case{}/Result_LES32_IFNO_gap200_mag{}/post_result/St_statistics.dat'.format(case_n+1,mag),dtype=float, comments=['step'])        
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
            x_IUFNO_Strms.append(IUFNO_St_statistics[:,0])  # 只取出第一列数据
            y_IUFNO_Strms.append(IUFNO_St_statistics[:,5]) #只取出第二列数据
            x_IUFNO_St_PDFs.append(IUFNO_St_PDFs[:,0])  # 只取出第一列数据
            y_IUFNO_St_PDFs.append(IUFNO_St_PDFs[:,1]) #只取出第二列数据
            x_IUFNO_St_statistics.append(IUFNO_St_statistics[:,0])  # 只取出第一列数据
            y_IUFNO_St_statistics.append(IUFNO_St_statistics[:,5]) #只取出第二列数据        
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
        x_IUFNO_Strms = np.asarray(x_IUFNO_Strms) #列表转数组
        y_IUFNO_Strms = np.asarray(y_IUFNO_Strms) #列表转数组    
        x_IUFNO_St_PDFs = np.asarray(x_IUFNO_St_PDFs) #列表转数组
        y_IUFNO_St_PDFs = np.asarray(y_IUFNO_St_PDFs) #列表转数组
        x_IUFNO_St_statistics = np.asarray(x_IUFNO_St_statistics) #列表转数组
        y_IUFNO_St_statistics = np.asarray(y_IUFNO_St_statistics) #列表转数组    
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
        x_Strms_avg_case = np.mean(x_IUFNO_Strms,0) #行压缩成一行
        y_Strms_avg_case = np.mean(y_IUFNO_Strms,0) #行压缩成  
        x_St_PDFs_avg_case = np.mean(x_IUFNO_St_PDFs,0) #行压缩成一行
        y_St_PDFs_avg_case = np.mean(y_IUFNO_St_PDFs,0) #行压缩成
        x_St_statistics_avg_case = np.mean(x_IUFNO_St_statistics,0) #行压缩成一行
        y_St_statistics_avg_case = np.mean(y_IUFNO_St_statistics,0) #行压缩成    
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
        avg_IUFNO_Strms_10case=np.dstack((x_Strms_avg_case,y_Strms_avg_case)).squeeze() #拼接
        avg_IUFNO_St_PDFs_10case=np.dstack((x_St_PDFs_avg_case,y_St_PDFs_avg_case)).squeeze() #拼接
        avg_IUFNO_St_statistics_10case=np.dstack((x_St_statistics_avg_case,y_St_statistics_avg_case)).squeeze() #拼接   
        #导出均值
      
        np.savetxt('./AVG/IFNO_40ep_mag{}/N{}/avg_{}case_urms.dat'.format(mag,case_number,case_number),avg_IUFNO_urms_10case, fmt="%16.7f")
        np.savetxt('./AVG/IFNO_40ep_mag{}/N{}/avg_{}case_wrms.dat'.format(mag,case_number,case_number),avg_IUFNO_wrms_10case, fmt="%16.7f")
        np.savetxt('./AVG/IFNO_40ep_mag{}/N{}/avg_{}case_dissipation.dat'.format(mag,case_number,case_number),avg_IUFNO_dissipation_10case, fmt="%16.7f")
        np.savetxt('./AVG/IFNO_40ep_mag{}/N{}/avg_{}case_Ek_t.dat'.format(mag,case_number,case_number),avg_IUFNO_Et_10case, fmt="%16.7f")
        np.savetxt('./AVG/IFNO_40ep_mag{}/N{}/avg_{}case_inc1_PDFs.dat'.format(mag,case_number,case_number),avg_IUFNO_inc1_PDFs_10case, fmt="%16.7f")
        np.savetxt('./AVG/IFNO_40ep_mag{}/N{}/avg_{}case_vel_spec.dat'.format(mag,case_number,case_number),avg_IUFNO_spectrum_10case, fmt="%16.7f")
        np.savetxt('./AVG/IFNO_40ep_mag{}/N{}/avg_{}case_structrue2.dat'.format(mag,case_number,case_number),avg_IUFNO_structrue2_10case, fmt="%16.7f")
        np.savetxt('./AVG/IFNO_40ep_mag{}/N{}/avg_{}case_structrue4.dat'.format(mag,case_number,case_number),avg_IUFNO_structrue4_10case, fmt="%16.7f")
        np.savetxt('./AVG/IFNO_40ep_mag{}/N{}/avg_{}case_vort_PDFs.dat'.format(mag,case_number,case_number),avg_IUFNO_vort_PDFs_10case, fmt="%16.7f")
        np.savetxt('./AVG/IFNO_40ep_mag{}/N{}/avg_{}case_vort_statistics.dat'.format(mag,case_number,case_number),avg_IUFNO_vort_statistics_10case, fmt="%16.7f")
        np.savetxt('./AVG/IFNO_40ep_mag{}/N{}/avg_{}case_Strms.dat'.format(mag,case_number,case_number),avg_IUFNO_Strms_10case, fmt="%16.7f")
        np.savetxt('./AVG/IFNO_40ep_mag{}/N{}/avg_{}case_St_PDFs.dat'.format(mag,case_number,case_number),avg_IUFNO_St_PDFs_10case, fmt="%16.7f")
        np.savetxt('./AVG/IFNO_40ep_mag{}/N{}/avg_{}case_St_statistics.dat'.format(mag,case_number,case_number),avg_IUFNO_St_statistics_10case, fmt="%16.7f")    
        '''
        np.savetxt('./AVG/IFNO_40ep_mag{}/{}case/avg_{}case_urms.dat'.format(mag,case_number,case_number),avg_IUFNO_urms_10case, fmt="%16.7f")
        np.savetxt('./AVG/IFNO_40ep_mag{}/{}case/avg_{}case_wrms.dat'.format(mag,case_number,case_number),avg_IUFNO_wrms_10case, fmt="%16.7f")
        np.savetxt('./AVG/IFNO_40ep_mag{}/{}case/avg_{}case_dissipation.dat'.format(mag,case_number,case_number),avg_IUFNO_dissipation_10case, fmt="%16.7f")
        np.savetxt('./AVG/IFNO_40ep_mag{}/{}case/avg_{}case_Ek_t.dat'.format(mag,case_number,case_number),avg_IUFNO_Et_10case, fmt="%16.7f")
        np.savetxt('./AVG/IFNO_40ep_mag{}/{}case/avg_{}case_inc1_PDFs.dat'.format(mag,case_number,case_number),avg_IUFNO_inc1_PDFs_10case, fmt="%16.7f")
        np.savetxt('./AVG/IFNO_40ep_mag{}/{}case/avg_{}case_vel_spec.dat'.format(mag,case_number,case_number),avg_IUFNO_spectrum_10case, fmt="%16.7f")
        np.savetxt('./AVG/IFNO_40ep_mag{}/{}case/avg_{}case_structrue2.dat'.format(mag,case_number,case_number),avg_IUFNO_structrue2_10case, fmt="%16.7f")
        np.savetxt('./AVG/IFNO_40ep_mag{}/{}case/avg_{}case_structrue4.dat'.format(mag,case_number,case_number),avg_IUFNO_structrue4_10case, fmt="%16.7f")
        np.savetxt('./AVG/IFNO_40ep_mag{}/{}case/avg_{}case_vort_PDFs.dat'.format(mag,case_number,case_number),avg_IUFNO_vort_PDFs_10case, fmt="%16.7f")
        np.savetxt('./AVG/IFNO_40ep_mag{}/{}case/avg_{}case_vort_statistics.dat'.format(mag,case_number,case_number),avg_IUFNO_vort_statistics_10case, fmt="%16.7f")
        np.savetxt('./AVG/IFNO_40ep_mag{}/{}case/avg_{}case_Strms.dat'.format(mag,case_number,case_number),avg_IUFNO_Strms_10case, fmt="%16.7f")
        np.savetxt('./AVG/IFNO_40ep_mag{}/{}case/avg_{}case_St_PDFs.dat'.format(mag,case_number,case_number),avg_IUFNO_St_PDFs_10case, fmt="%16.7f")
        np.savetxt('./AVG/IFNO_40ep_mag{}/{}case/avg_{}case_St_statistics.dat'.format(mag,case_number,case_number),avg_IUFNO_St_statistics_10case, fmt="%16.7f")   
        

        '''
        #==========================================================================FNO
        print("IUFNO getting dat!")
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
        x_IUFNO_Strms = []
        y_IUFNO_Strms = []
        x_IUFNO_St_PDFs = []
        y_IUFNO_St_PDFs = []
        x_IUFNO_St_statistics = []
        y_IUFNO_St_statistics = []    
        for case_n in range(case_number-1,case_number):
            # print(case_n)
            # 载入后处理文件，包括速度参数，PDFs，能谱，结构函数
            IUFNO_vel_parameter= np.loadtxt('./case{}/Result_LES32_IUFNO_40ep_gap200_mag{}/post_result/vel_parameter.dat'.format(case_n+1,mag),dtype=float, comments=['step'])
            IUFNO_ic1_PDFs = np.loadtxt('./case{}/Result_LES32_IUFNO_40ep_gap200_mag{}/post_result/inc1_PDFs.dat'.format(case_n+1,mag), dtype=float,comments=['step'])
            IUFNO_spec = np.loadtxt('./case{}/Result_LES32_IUFNO_40ep_gap200_mag{}/post_result/spectrum_vel.dat'.format(case_n+1,mag), dtype=float,comments=['variables', 'zone'])
            IUFNO_structrue2 = np.loadtxt('./case{}/Result_LES32_IUFNO_40ep_gap200_mag{}/post_result/structure2.dat'.format(case_n+1,mag),dtype=float, comments=['step'])
            IUFNO_structrue4 = np.loadtxt('./case{}/Result_LES32_IUFNO_40ep_gap200_mag{}/post_result/structure4.dat'.format(case_n+1,mag),dtype=float, comments=['step'])
            IUFNO_vort_PDFs = np.loadtxt('./case{}/Result_LES32_IUFNO_40ep_gap200_mag{}/post_result/vort_PDFs.dat'.format(case_n+1,mag), dtype=float,comments=['variables', 'zone'])
            IUFNO_vort_statistics = np.loadtxt('./case{}/Result_LES32_IUFNO_40ep_gap200_mag{}/post_result/vort_statistics.dat'.format(case_n+1,mag),dtype=float, comments=['step'])
            IUFNO_St_PDFs = np.loadtxt('./case{}/Result_LES32_IUFNO_40ep_gap200_mag{}/post_result/St_PDFs.dat'.format(case_n+1,mag), dtype=float,comments=['variables', 'zone'])
            IUFNO_St_statistics = np.loadtxt('./case{}/Result_LES32_IUFNO_40ep_gap200_mag{}/post_result/St_statistics.dat'.format(case_n+1,mag),dtype=float, comments=['step'])        
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
            x_IUFNO_Strms.append(IUFNO_St_statistics[:,0])  # 只取出第一列数据
            y_IUFNO_Strms.append(IUFNO_St_statistics[:,5]) #只取出第二列数据
            x_IUFNO_St_PDFs.append(IUFNO_St_PDFs[:,0])  # 只取出第一列数据
            y_IUFNO_St_PDFs.append(IUFNO_St_PDFs[:,1]) #只取出第二列数据
            x_IUFNO_St_statistics.append(IUFNO_St_statistics[:,0])  # 只取出第一列数据
            y_IUFNO_St_statistics.append(IUFNO_St_statistics[:,5]) #只取出第二列数据        
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
        x_IUFNO_Strms = np.asarray(x_IUFNO_Strms) #列表转数组
        y_IUFNO_Strms = np.asarray(y_IUFNO_Strms) #列表转数组    
        x_IUFNO_St_PDFs = np.asarray(x_IUFNO_St_PDFs) #列表转数组
        y_IUFNO_St_PDFs = np.asarray(y_IUFNO_St_PDFs) #列表转数组
        x_IUFNO_St_statistics = np.asarray(x_IUFNO_St_statistics) #列表转数组
        y_IUFNO_St_statistics = np.asarray(y_IUFNO_St_statistics) #列表转数组    
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
        x_Strms_avg_case = np.mean(x_IUFNO_Strms,0) #行压缩成一行
        y_Strms_avg_case = np.mean(y_IUFNO_Strms,0) #行压缩成  
        x_St_PDFs_avg_case = np.mean(x_IUFNO_St_PDFs,0) #行压缩成一行
        y_St_PDFs_avg_case = np.mean(y_IUFNO_St_PDFs,0) #行压缩成
        x_St_statistics_avg_case = np.mean(x_IUFNO_St_statistics,0) #行压缩成一行
        y_St_statistics_avg_case = np.mean(y_IUFNO_St_statistics,0) #行压缩成    
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
        avg_IUFNO_Strms_10case=np.dstack((x_Strms_avg_case,y_Strms_avg_case)).squeeze() #拼接
        avg_IUFNO_St_PDFs_10case=np.dstack((x_St_PDFs_avg_case,y_St_PDFs_avg_case)).squeeze() #拼接
        avg_IUFNO_St_statistics_10case=np.dstack((x_St_statistics_avg_case,y_St_statistics_avg_case)).squeeze() #拼接   
        #导出均值
    
        np.savetxt('./AVG/IUFNO_40ep_mag{}/N{}/avg_{}case_urms.dat'.format(mag,case_number,case_number),avg_IUFNO_urms_10case, fmt="%16.7f")
        np.savetxt('./AVG/IUFNO_40ep_mag{}/N{}/avg_{}case_wrms.dat'.format(mag,case_number,case_number),avg_IUFNO_wrms_10case, fmt="%16.7f")
        np.savetxt('./AVG/IUFNO_40ep_mag{}/N{}/avg_{}case_dissipation.dat'.format(mag,case_number,case_number),avg_IUFNO_dissipation_10case, fmt="%16.7f")
        np.savetxt('./AVG/IUFNO_40ep_mag{}/N{}/avg_{}case_Ek_t.dat'.format(mag,case_number,case_number),avg_IUFNO_Et_10case, fmt="%16.7f")
        np.savetxt('./AVG/IUFNO_40ep_mag{}/N{}/avg_{}case_inc1_PDFs.dat'.format(mag,case_number,case_number),avg_IUFNO_inc1_PDFs_10case, fmt="%16.7f")
        np.savetxt('./AVG/IUFNO_40ep_mag{}/N{}/avg_{}case_vel_spec.dat'.format(mag,case_number,case_number),avg_IUFNO_spectrum_10case, fmt="%16.7f")
        np.savetxt('./AVG/IUFNO_40ep_mag{}/N{}/avg_{}case_structrue2.dat'.format(mag,case_number,case_number),avg_IUFNO_structrue2_10case, fmt="%16.7f")
        np.savetxt('./AVG/IUFNO_40ep_mag{}/N{}/avg_{}case_structrue4.dat'.format(mag,case_number,case_number),avg_IUFNO_structrue4_10case, fmt="%16.7f")
        np.savetxt('./AVG/IUFNO_40ep_mag{}/N{}/avg_{}case_vort_PDFs.dat'.format(mag,case_number,case_number),avg_IUFNO_vort_PDFs_10case, fmt="%16.7f")
        np.savetxt('./AVG/IUFNO_40ep_mag{}/N{}/avg_{}case_vort_statistics.dat'.format(mag,case_number,case_number),avg_IUFNO_vort_statistics_10case, fmt="%16.7f")
        np.savetxt('./AVG/IUFNO_40ep_mag{}/N{}/avg_{}case_Strms.dat'.format(mag,case_number,case_number),avg_IUFNO_Strms_10case, fmt="%16.7f")
        np.savetxt('./AVG/IUFNO_40ep_mag{}/N{}/avg_{}case_St_PDFs.dat'.format(mag,case_number,case_number),avg_IUFNO_St_PDFs_10case, fmt="%16.7f")
        np.savetxt('./AVG/IUFNO_40ep_mag{}/N{}/avg_{}case_St_statistics.dat'.format(mag,case_number,case_number),avg_IUFNO_St_statistics_10case, fmt="%16.7f")    
        '''
        np.savetxt('./AVG/IUFNO_40ep_mag{}/{}case/avg_{}case_urms.dat'.format(mag,case_number,case_number),avg_IUFNO_urms_10case, fmt="%16.7f")
        np.savetxt('./AVG/IUFNO_40ep_mag{}/{}case/avg_{}case_wrms.dat'.format(mag,case_number,case_number),avg_IUFNO_wrms_10case, fmt="%16.7f")
        np.savetxt('./AVG/IUFNO_40ep_mag{}/{}case/avg_{}case_dissipation.dat'.format(mag,case_number,case_number),avg_IUFNO_dissipation_10case, fmt="%16.7f")
        np.savetxt('./AVG/IUFNO_40ep_mag{}/{}case/avg_{}case_Ek_t.dat'.format(mag,case_number,case_number),avg_IUFNO_Et_10case, fmt="%16.7f")
        np.savetxt('./AVG/IUFNO_40ep_mag{}/{}case/avg_{}case_inc1_PDFs.dat'.format(mag,case_number,case_number),avg_IUFNO_inc1_PDFs_10case, fmt="%16.7f")
        np.savetxt('./AVG/IUFNO_40ep_mag{}/{}case/avg_{}case_vel_spec.dat'.format(mag,case_number,case_number),avg_IUFNO_spectrum_10case, fmt="%16.7f")
        np.savetxt('./AVG/IUFNO_40ep_mag{}/{}case/avg_{}case_structrue2.dat'.format(mag,case_number,case_number),avg_IUFNO_structrue2_10case, fmt="%16.7f")
        np.savetxt('./AVG/IUFNO_40ep_mag{}/{}case/avg_{}case_structrue4.dat'.format(mag,case_number,case_number),avg_IUFNO_structrue4_10case, fmt="%16.7f")
        np.savetxt('./AVG/IUFNO_40ep_mag{}/{}case/avg_{}case_vort_PDFs.dat'.format(mag,case_number,case_number),avg_IUFNO_vort_PDFs_10case, fmt="%16.7f")
        np.savetxt('./AVG/IUFNO_40ep_mag{}/{}case/avg_{}case_vort_statistics.dat'.format(mag,case_number,case_number),avg_IUFNO_vort_statistics_10case, fmt="%16.7f")
        np.savetxt('./AVG/IUFNO_40ep_mag{}/{}case/avg_{}case_Strms.dat'.format(mag,case_number,case_number),avg_IUFNO_Strms_10case, fmt="%16.7f")
        np.savetxt('./AVG/IUFNO_40ep_mag{}/{}case/avg_{}case_St_PDFs.dat'.format(mag,case_number,case_number),avg_IUFNO_St_PDFs_10case, fmt="%16.7f")
        np.savetxt('./AVG/IUFNO_40ep_mag{}/{}case/avg_{}case_St_statistics.dat'.format(mag,case_number,case_number),avg_IUFNO_St_statistics_10case, fmt="%16.7f")   


        '''
        #==========================================================================FNO
        print("F-IUFNO getting dat!")
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
        x_IUFNO_Strms = []
        y_IUFNO_Strms = []
        x_IUFNO_St_PDFs = []
        y_IUFNO_St_PDFs = []
        x_IUFNO_St_statistics = []
        y_IUFNO_St_statistics = []    
        for case_n in range(case_number-1,case_number):
            # print(case_n)
            # 载入后处理文件，包括速度参数，PDFs，能谱，结构函数
            IUFNO_vel_parameter= np.loadtxt('./case{}/Result_LES32_F-IUFNO_40ep_gap200_mag{}/post_result/vel_parameter.dat'.format(case_n+1,mag),dtype=float, comments=['step'])
            IUFNO_ic1_PDFs = np.loadtxt('./case{}/Result_LES32_F-IUFNO_40ep_gap200_mag{}/post_result/inc1_PDFs.dat'.format(case_n+1,mag), dtype=float,comments=['step'])
            IUFNO_spec = np.loadtxt('./case{}/Result_LES32_F-IUFNO_40ep_gap200_mag{}/post_result/spectrum_vel.dat'.format(case_n+1,mag), dtype=float,comments=['variables', 'zone'])
            IUFNO_structrue2 = np.loadtxt('./case{}/Result_LES32_F-IUFNO_40ep_gap200_mag{}/post_result/structure2.dat'.format(case_n+1,mag),dtype=float, comments=['step'])
            IUFNO_structrue4 = np.loadtxt('./case{}/Result_LES32_F-IUFNO_40ep_gap200_mag{}/post_result/structure4.dat'.format(case_n+1,mag),dtype=float, comments=['step'])
            IUFNO_vort_PDFs = np.loadtxt('./case{}/Result_LES32_F-IUFNO_40ep_gap200_mag{}/post_result/vort_PDFs.dat'.format(case_n+1,mag), dtype=float,comments=['variables', 'zone'])
            IUFNO_vort_statistics = np.loadtxt('./case{}/Result_LES32_F-IUFNO_40ep_gap200_mag{}/post_result/vort_statistics.dat'.format(case_n+1,mag),dtype=float, comments=['step'])
            IUFNO_St_PDFs = np.loadtxt('./case{}/Result_LES32_F-IUFNO_40ep_gap200_mag{}/post_result/St_PDFs.dat'.format(case_n+1,mag), dtype=float,comments=['variables', 'zone'])
            IUFNO_St_statistics = np.loadtxt('./case{}/Result_LES32_F-IUFNO_40ep_gap200_mag{}/post_result/St_statistics.dat'.format(case_n+1,mag),dtype=float, comments=['step'])        
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
            x_IUFNO_Strms.append(IUFNO_St_statistics[:,0])  # 只取出第一列数据
            y_IUFNO_Strms.append(IUFNO_St_statistics[:,5]) #只取出第二列数据
            x_IUFNO_St_PDFs.append(IUFNO_St_PDFs[:,0])  # 只取出第一列数据
            y_IUFNO_St_PDFs.append(IUFNO_St_PDFs[:,1]) #只取出第二列数据
            x_IUFNO_St_statistics.append(IUFNO_St_statistics[:,0])  # 只取出第一列数据
            y_IUFNO_St_statistics.append(IUFNO_St_statistics[:,5]) #只取出第二列数据        
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
        x_IUFNO_Strms = np.asarray(x_IUFNO_Strms) #列表转数组
        y_IUFNO_Strms = np.asarray(y_IUFNO_Strms) #列表转数组    
        x_IUFNO_St_PDFs = np.asarray(x_IUFNO_St_PDFs) #列表转数组
        y_IUFNO_St_PDFs = np.asarray(y_IUFNO_St_PDFs) #列表转数组
        x_IUFNO_St_statistics = np.asarray(x_IUFNO_St_statistics) #列表转数组
        y_IUFNO_St_statistics = np.asarray(y_IUFNO_St_statistics) #列表转数组    
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
        x_Strms_avg_case = np.mean(x_IUFNO_Strms,0) #行压缩成一行
        y_Strms_avg_case = np.mean(y_IUFNO_Strms,0) #行压缩成  
        x_St_PDFs_avg_case = np.mean(x_IUFNO_St_PDFs,0) #行压缩成一行
        y_St_PDFs_avg_case = np.mean(y_IUFNO_St_PDFs,0) #行压缩成
        x_St_statistics_avg_case = np.mean(x_IUFNO_St_statistics,0) #行压缩成一行
        y_St_statistics_avg_case = np.mean(y_IUFNO_St_statistics,0) #行压缩成    
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
        avg_IUFNO_Strms_10case=np.dstack((x_Strms_avg_case,y_Strms_avg_case)).squeeze() #拼接
        avg_IUFNO_St_PDFs_10case=np.dstack((x_St_PDFs_avg_case,y_St_PDFs_avg_case)).squeeze() #拼接
        avg_IUFNO_St_statistics_10case=np.dstack((x_St_statistics_avg_case,y_St_statistics_avg_case)).squeeze() #拼接   
        #导出均值
       
        np.savetxt('./AVG/F-IUFNO_40ep_mag{}/N{}/avg_{}case_urms.dat'.format(mag,case_number,case_number),avg_IUFNO_urms_10case, fmt="%16.7f")
        np.savetxt('./AVG/F-IUFNO_40ep_mag{}/N{}/avg_{}case_wrms.dat'.format(mag,case_number,case_number),avg_IUFNO_wrms_10case, fmt="%16.7f")
        np.savetxt('./AVG/F-IUFNO_40ep_mag{}/N{}/avg_{}case_dissipation.dat'.format(mag,case_number,case_number),avg_IUFNO_dissipation_10case, fmt="%16.7f")
        np.savetxt('./AVG/F-IUFNO_40ep_mag{}/N{}/avg_{}case_Ek_t.dat'.format(mag,case_number,case_number),avg_IUFNO_Et_10case, fmt="%16.7f")
        np.savetxt('./AVG/F-IUFNO_40ep_mag{}/N{}/avg_{}case_inc1_PDFs.dat'.format(mag,case_number,case_number),avg_IUFNO_inc1_PDFs_10case, fmt="%16.7f")
        np.savetxt('./AVG/F-IUFNO_40ep_mag{}/N{}/avg_{}case_vel_spec.dat'.format(mag,case_number,case_number),avg_IUFNO_spectrum_10case, fmt="%16.7f")
        np.savetxt('./AVG/F-IUFNO_40ep_mag{}/N{}/avg_{}case_structrue2.dat'.format(mag,case_number,case_number),avg_IUFNO_structrue2_10case, fmt="%16.7f")
        np.savetxt('./AVG/F-IUFNO_40ep_mag{}/N{}/avg_{}case_structrue4.dat'.format(mag,case_number,case_number),avg_IUFNO_structrue4_10case, fmt="%16.7f")
        np.savetxt('./AVG/F-IUFNO_40ep_mag{}/N{}/avg_{}case_vort_PDFs.dat'.format(mag,case_number,case_number),avg_IUFNO_vort_PDFs_10case, fmt="%16.7f")
        np.savetxt('./AVG/F-IUFNO_40ep_mag{}/N{}/avg_{}case_vort_statistics.dat'.format(mag,case_number,case_number),avg_IUFNO_vort_statistics_10case, fmt="%16.7f")
        np.savetxt('./AVG/F-IUFNO_40ep_mag{}/N{}/avg_{}case_Strms.dat'.format(mag,case_number,case_number),avg_IUFNO_Strms_10case, fmt="%16.7f")
        np.savetxt('./AVG/F-IUFNO_40ep_mag{}/N{}/avg_{}case_St_PDFs.dat'.format(mag,case_number,case_number),avg_IUFNO_St_PDFs_10case, fmt="%16.7f")
        np.savetxt('./AVG/F-IUFNO_40ep_mag{}/N{}/avg_{}case_St_statistics.dat'.format(mag,case_number,case_number),avg_IUFNO_St_statistics_10case, fmt="%16.7f")    
        '''
        np.savetxt('./AVG/F-IUFNO_40ep_mag{}/{}case/avg_{}case_urms.dat'.format(mag,case_number,case_number),avg_IUFNO_urms_10case, fmt="%16.7f")
        np.savetxt('./AVG/F-IUFNO_40ep_mag{}/{}case/avg_{}case_wrms.dat'.format(mag,case_number,case_number),avg_IUFNO_wrms_10case, fmt="%16.7f")
        np.savetxt('./AVG/F-IUFNO_40ep_mag{}/{}case/avg_{}case_dissipation.dat'.format(mag,case_number,case_number),avg_IUFNO_dissipation_10case, fmt="%16.7f")
        np.savetxt('./AVG/F-IUFNO_40ep_mag{}/{}case/avg_{}case_Ek_t.dat'.format(mag,case_number,case_number),avg_IUFNO_Et_10case, fmt="%16.7f")
        np.savetxt('./AVG/F-IUFNO_40ep_mag{}/{}case/avg_{}case_inc1_PDFs.dat'.format(mag,case_number,case_number),avg_IUFNO_inc1_PDFs_10case, fmt="%16.7f")
        np.savetxt('./AVG/F-IUFNO_40ep_mag{}/{}case/avg_{}case_vel_spec.dat'.format(mag,case_number,case_number),avg_IUFNO_spectrum_10case, fmt="%16.7f")
        np.savetxt('./AVG/F-IUFNO_40ep_mag{}/{}case/avg_{}case_structrue2.dat'.format(mag,case_number,case_number),avg_IUFNO_structrue2_10case, fmt="%16.7f")
        np.savetxt('./AVG/F-IUFNO_40ep_mag{}/{}case/avg_{}case_structrue4.dat'.format(mag,case_number,case_number),avg_IUFNO_structrue4_10case, fmt="%16.7f")
        np.savetxt('./AVG/F-IUFNO_40ep_mag{}/{}case/avg_{}case_vort_PDFs.dat'.format(mag,case_number,case_number),avg_IUFNO_vort_PDFs_10case, fmt="%16.7f")
        np.savetxt('./AVG/F-IUFNO_40ep_mag{}/{}case/avg_{}case_vort_statistics.dat'.format(mag,case_number,case_number),avg_IUFNO_vort_statistics_10case, fmt="%16.7f")
        np.savetxt('./AVG/F-IUFNO_40ep_mag{}/{}case/avg_{}case_Strms.dat'.format(mag,case_number,case_number),avg_IUFNO_Strms_10case, fmt="%16.7f")
        np.savetxt('./AVG/F-IUFNO_40ep_mag{}/{}case/avg_{}case_St_PDFs.dat'.format(mag,case_number,case_number),avg_IUFNO_St_PDFs_10case, fmt="%16.7f")
        np.savetxt('./AVG/F-IUFNO_40ep_mag{}/{}case/avg_{}case_St_statistics.dat'.format(mag,case_number,case_number),avg_IUFNO_St_statistics_10case, fmt="%16.7f")   
        '''

        print("Done!")