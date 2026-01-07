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
for j,case_number in enumerate(case_number_list):
    #-------------------------------------------------------------读入数据，
    #######avg case#########
    fDNS= np.loadtxt("../../fDNS/{}case/avg_fDNS_{}case_Ek_t.dat".format(case_number,case_number),dtype=float)
    fDNS_time_avg=[0.0]
    for i in range(time_steps):

        fDNS_time_avg=fDNS_time_avg+fDNS[i, 1]
    fDNS_time_avg=fDNS_time_avg/time_steps
    np.savetxt('fDNS_time_avg_Ek_{}case.dat'.format(case_number), fDNS_time_avg, fmt='%.16f')

###########

