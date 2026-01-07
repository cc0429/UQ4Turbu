"""
@author: admin
"""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import os
import matplotlib as mpl

time_steps = 600
case_number_list =[1,10,20,30]
period = 10

for k,case_number in enumerate(case_number_list):
    #-------------------------------------------------------------读入数据，
    #######avg case#########
    fDNS= np.loadtxt("../../fDNS/{}case/avg_fDNS_{}case_vel_spec.dat".format(case_number,case_number),dtype=float)


    fDNS_time_avg = [0.0] * period
    for i in range(time_steps):
        for j in range(period):
            fDNS_time_avg[j]=fDNS_time_avg[j]+fDNS[i*10+j, 1]

    for i in range(period):
        fDNS_time_avg[i] = fDNS_time_avg[i]/time_steps

    first_column = np.arange(1, 11)
    fDNS_ta = np.column_stack((first_column, fDNS_time_avg))
    np.savetxt('fDNS_time_avg_vel_spec_{}case.dat'.format(case_number), fDNS_ta, fmt='%d %.16f')

    ###########

