#!/bin/bash
echo "ready ! "
file1=/scratch/2025-03-18/mae-zxt/F-IUFNO_post_new/isotropic/m12w90n40g45fac4nff2seed0_lr5e-4_bs5

for i in {1..30}
do
    echo $i
    sed -i "22c /scratch/2025-03-18/mae-zxt/F-IUFNO_post_new/isotropic/m12w90n40g45fac4nff2seed0_lr5e-4_bs5/case${i}/Py24_LES32_IFNO_gap200_mag1/result" ${file1}/case${i}/Result_LES32_IFNO_gap200_mag1/parameter.d
    sed -i "23c /scratch/2025-03-18/mae-zxt/F-IUFNO_post_new/isotropic/m12w90n40g45fac4nff2seed0_lr5e-4_bs5/case${i}/Result_LES32_IFNO_gap200_mag1/vor_con_result" ${file1}/case${i}/Result_LES32_IFNO_gap200_mag1/parameter.d
    cd ${file1}/case${i}/Result_LES32_IFNO_gap200_mag1
    make
    sleep 7s
    bsub<submit_debug.lsf
    #-----------------------------------
    sleep 1s
    echo "done $i ! "
done


for i in {1..30}
do
    echo $i
    sed -i "22c /scratch/2025-03-18/mae-zxt/F-IUFNO_post_new/isotropic/m12w90n40g45fac4nff2seed0_lr5e-4_bs5/case${i}/Py24_LES32_IFNO_gap200_mag2/result" ${file1}/case${i}/Result_LES32_IFNO_gap200_mag2/parameter.d
    sed -i "23c /scratch/2025-03-18/mae-zxt/F-IUFNO_post_new/isotropic/m12w90n40g45fac4nff2seed0_lr5e-4_bs5/case${i}/Result_LES32_IFNO_gap200_mag2/vor_con_result" ${file1}/case${i}/Result_LES32_IFNO_gap200_mag2/parameter.d
    cd ${file1}/case${i}/Result_LES32_IFNO_gap200_mag2
    make
    sleep 7s
    bsub<submit_debug.lsf
    #-----------------------------------
    sleep 1s
    echo "done $i ! "
done


for i in {1..30}
do
    echo $i
    sed -i "22c /scratch/2025-03-18/mae-zxt/F-IUFNO_post_new/isotropic/m12w90n40g45fac4nff2seed0_lr5e-4_bs5/case${i}/Py24_LES32_IFNO_gap200_mag5/result" ${file1}/case${i}/Result_LES32_IFNO_gap200_mag5/parameter.d
    sed -i "23c /scratch/2025-03-18/mae-zxt/F-IUFNO_post_new/isotropic/m12w90n40g45fac4nff2seed0_lr5e-4_bs5/case${i}/Result_LES32_IFNO_gap200_mag5/vor_con_result" ${file1}/case${i}/Result_LES32_IFNO_gap200_mag5/parameter.d
    cd ${file1}/case${i}/Result_LES32_IFNO_gap200_mag5
    make
    sleep 7s
    bsub<submit_debug.lsf
    #-----------------------------------
    sleep 1s
    echo "done $i ! "
done


for i in {1..30}
do
    echo $i
    sed -i "22c /scratch/2025-03-18/mae-zxt/F-IUFNO_post_new/isotropic/m12w90n40g45fac4nff2seed0_lr5e-4_bs5/case${i}/Py24_LES32_IFNO_gap200_mag10/result" ${file1}/case${i}/Result_LES32_IFNO_gap200_mag10/parameter.d
    sed -i "23c /scratch/2025-03-18/mae-zxt/F-IUFNO_post_new/isotropic/m12w90n40g45fac4nff2seed0_lr5e-4_bs5/case${i}/Result_LES32_IFNO_gap200_mag10/vor_con_result" ${file1}/case${i}/Result_LES32_IFNO_gap200_mag10/parameter.d
    cd ${file1}/case${i}/Result_LES32_IFNO_gap200_mag10
    make
    sleep 7s
    bsub<submit_debug.lsf
    #-----------------------------------
    sleep 1s
    echo "done $i ! "
done

for i in {1..30}
do
    echo $i
    sed -i "22c /scratch/2025-03-18/mae-zxt/F-IUFNO_post_new/isotropic/m12w90n40g45fac4nff2seed0_lr5e-4_bs5/case${i}/Py24_LES32_IUFNO_40ep_gap200_mag1/result" ${file1}/case${i}/Result_LES32_IUFNO_40ep_gap200_mag1/parameter.d
    sed -i "23c /scratch/2025-03-18/mae-zxt/F-IUFNO_post_new/isotropic/m12w90n40g45fac4nff2seed0_lr5e-4_bs5/case${i}/Result_LES32_IUFNO_40ep_gap200_mag1/vor_con_result" ${file1}/case${i}/Result_LES32_IUFNO_40ep_gap200_mag1/parameter.d
    cd ${file1}/case${i}/Result_LES32_IUFNO_40ep_gap200_mag1
    make
    sleep 7s
    bsub<submit_debug.lsf
    #-----------------------------------
    sleep 1s
    echo "done $i ! "
done


for i in {1..30}
do
    echo $i
    sed -i "22c /scratch/2025-03-18/mae-zxt/F-IUFNO_post_new/isotropic/m12w90n40g45fac4nff2seed0_lr5e-4_bs5/case${i}/Py24_LES32_IUFNO_40ep_gap200_mag2/result" ${file1}/case${i}/Result_LES32_IUFNO_40ep_gap200_mag2/parameter.d
    sed -i "23c /scratch/2025-03-18/mae-zxt/F-IUFNO_post_new/isotropic/m12w90n40g45fac4nff2seed0_lr5e-4_bs5/case${i}/Result_LES32_IUFNO_40ep_gap200_mag2/vor_con_result" ${file1}/case${i}/Result_LES32_IUFNO_40ep_gap200_mag2/parameter.d
    cd ${file1}/case${i}/Result_LES32_IUFNO_40ep_gap200_mag2
    make
    sleep 7s
    bsub<submit_debug.lsf
    #-----------------------------------
    sleep 1s
    echo "done $i ! "
done


for i in {1..30}
do
    echo $i
    sed -i "22c /scratch/2025-03-18/mae-zxt/F-IUFNO_post_new/isotropic/m12w90n40g45fac4nff2seed0_lr5e-4_bs5/case${i}/Py24_LES32_IUFNO_40ep_gap200_mag5/result" ${file1}/case${i}/Result_LES32_IUFNO_40ep_gap200_mag5/parameter.d
    sed -i "23c /scratch/2025-03-18/mae-zxt/F-IUFNO_post_new/isotropic/m12w90n40g45fac4nff2seed0_lr5e-4_bs5/case${i}/Result_LES32_IUFNO_40ep_gap200_mag5/vor_con_result" ${file1}/case${i}/Result_LES32_IUFNO_40ep_gap200_mag5/parameter.d
    cd ${file1}/case${i}/Result_LES32_IUFNO_40ep_gap200_mag5
    make
    sleep 7s
    bsub<submit_debug.lsf
    #-----------------------------------
    sleep 1s
    echo "done $i ! "
done


for i in {1..30}
do
    echo $i
    sed -i "22c /scratch/2025-03-18/mae-zxt/F-IUFNO_post_new/isotropic/m12w90n40g45fac4nff2seed0_lr5e-4_bs5/case${i}/Py24_LES32_IUFNO_40ep_gap200_mag10/result" ${file1}/case${i}/Result_LES32_IUFNO_40ep_gap200_mag10/parameter.d
    sed -i "23c /scratch/2025-03-18/mae-zxt/F-IUFNO_post_new/isotropic/m12w90n40g45fac4nff2seed0_lr5e-4_bs5/case${i}/Result_LES32_IUFNO_40ep_gap200_mag10/vor_con_result" ${file1}/case${i}/Result_LES32_IUFNO_40ep_gap200_mag10/parameter.d
    cd ${file1}/case${i}/Result_LES32_IUFNO_40ep_gap200_mag10
    make
    sleep 7s
    bsub<submit_debug.lsf
    #-----------------------------------
    sleep 1s
    echo "done $i ! "
done


for i in {1..30}
do
    echo $i
    sed -i "22c /scratch/2025-03-18/mae-zxt/F-IUFNO_post_new/isotropic/m12w90n40g45fac4nff2seed0_lr5e-4_bs5/case${i}/Py24_LES32_F-IUFNO_40ep_gap200_mag1/result" ${file1}/case${i}/Result_LES32_F-IUFNO_40ep_gap200_mag1/parameter.d
    sed -i "23c /scratch/2025-03-18/mae-zxt/F-IUFNO_post_new/isotropic/m12w90n40g45fac4nff2seed0_lr5e-4_bs5/case${i}/Result_LES32_F-IUFNO_40ep_gap200_mag1/vor_con_result" ${file1}/case${i}/Result_LES32_F-IUFNO_40ep_gap200_mag1/parameter.d
    cd ${file1}/case${i}/Result_LES32_F-IUFNO_40ep_gap200_mag1
    make
    sleep 7s
    bsub<submit_debug.lsf
    #-----------------------------------
    sleep 1s
    echo "done $i ! "
done


for i in {1..30}
do
    echo $i
    sed -i "22c /scratch/2025-03-18/mae-zxt/F-IUFNO_post_new/isotropic/m12w90n40g45fac4nff2seed0_lr5e-4_bs5/case${i}/Py24_LES32_F-IUFNO_40ep_gap200_mag2/result" ${file1}/case${i}/Result_LES32_F-IUFNO_40ep_gap200_mag2/parameter.d
    sed -i "23c /scratch/2025-03-18/mae-zxt/F-IUFNO_post_new/isotropic/m12w90n40g45fac4nff2seed0_lr5e-4_bs5/case${i}/Result_LES32_F-IUFNO_40ep_gap200_mag2/vor_con_result" ${file1}/case${i}/Result_LES32_F-IUFNO_40ep_gap200_mag2/parameter.d
    cd ${file1}/case${i}/Result_LES32_F-IUFNO_40ep_gap200_mag2
    make
    sleep 7s
    bsub<submit_debug.lsf
    #-----------------------------------
    sleep 1s
    echo "done $i ! "
done


for i in {1..30}
do
    echo $i
    sed -i "22c /scratch/2025-03-18/mae-zxt/F-IUFNO_post_new/isotropic/m12w90n40g45fac4nff2seed0_lr5e-4_bs5/case${i}/Py24_LES32_F-IUFNO_40ep_gap200_mag5/result" ${file1}/case${i}/Result_LES32_F-IUFNO_40ep_gap200_mag5/parameter.d
    sed -i "23c /scratch/2025-03-18/mae-zxt/F-IUFNO_post_new/isotropic/m12w90n40g45fac4nff2seed0_lr5e-4_bs5/case${i}/Result_LES32_F-IUFNO_40ep_gap200_mag5/vor_con_result" ${file1}/case${i}/Result_LES32_F-IUFNO_40ep_gap200_mag5/parameter.d
    cd ${file1}/case${i}/Result_LES32_F-IUFNO_40ep_gap200_mag5
    make
    sleep 7s
    bsub<submit_debug.lsf
    #-----------------------------------
    sleep 1s
    echo "done $i ! "
done

for i in {1..30}
do
    echo $i
    sed -i "22c /scratch/2025-03-18/mae-zxt/F-IUFNO_post_new/isotropic/m12w90n40g45fac4nff2seed0_lr5e-4_bs5/case${i}/Py24_LES32_F-IUFNO_40ep_gap200_mag10/result" ${file1}/case${i}/Result_LES32_F-IUFNO_40ep_gap200_mag10/parameter.d
    sed -i "23c /scratch/2025-03-18/mae-zxt/F-IUFNO_post_new/isotropic/m12w90n40g45fac4nff2seed0_lr5e-4_bs5/case${i}/Result_LES32_F-IUFNO_40ep_gap200_mag10/vor_con_result" ${file1}/case${i}/Result_LES32_F-IUFNO_40ep_gap200_mag10/parameter.d
    cd ${file1}/case${i}/Result_LES32_F-IUFNO_40ep_gap200_mag10
    make
    sleep 7s
    bsub<submit_debug.lsf
    #-----------------------------------
    sleep 1s
    echo "done $i ! "
done