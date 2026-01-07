#!/bin/bash

# 遍历 case1 到 case30
for i in {1..30}; do
   
	######		
    src_file="dat/wk/m1/FIUFNO32_40ep_uxyz_gap200_case$i.dat"
    dest_dir="case$i/Py24_LES32_F-IUFNO_40ep_gap200_mag1/result"

    # 检查源文件是否存在
    if [ -f "$src_file" ]; then
        # 确保目标目录存在
        mkdir -p "$dest_dir"

        # 移动文件
        mv "$src_file" "$dest_dir/"
        echo "Moved $src_file to $dest_dir/"
    else
        echo "Source file $src_file does not exist."
	fi		

	######		
    src_file="dat/wk/m2/FIUFNO32_40ep_uxyz_gap200_case$i.dat"
    dest_dir="case$i/Py24_LES32_F-IUFNO_40ep_gap200_mag2/result"

    # 检查源文件是否存在
    if [ -f "$src_file" ]; then
        # 确保目标目录存在
        mkdir -p "$dest_dir"

        # 移动文件
        mv "$src_file" "$dest_dir/"
        echo "Moved $src_file to $dest_dir/"
    else
        echo "Source file $src_file does not exist."
	fi		

	######		
    src_file="dat/wk/m5/FIUFNO32_40ep_uxyz_gap200_case$i.dat"
    dest_dir="case$i/Py24_LES32_F-IUFNO_40ep_gap200_mag5/result"

    # 检查源文件是否存在
    if [ -f "$src_file" ]; then
        # 确保目标目录存在
        mkdir -p "$dest_dir"

        # 移动文件
        mv "$src_file" "$dest_dir/"
        echo "Moved $src_file to $dest_dir/"
    else
        echo "Source file $src_file does not exist."
	fi		

	######		
    src_file="dat/wk/m10/FIUFNO32_40ep_uxyz_gap200_case$i.dat"
    dest_dir="case$i/Py24_LES32_F-IUFNO_40ep_gap200_mag10/result"

    # 检查源文件是否存在
    if [ -f "$src_file" ]; then
        # 确保目标目录存在
        mkdir -p "$dest_dir"

        # 移动文件
        mv "$src_file" "$dest_dir/"
        echo "Moved $src_file to $dest_dir/"
    else
        echo "Source file $src_file does not exist."
	fi		


	######		
    src_file="dat/wk/m1/IUFNO32_40ep_uxyz_gap200_case$i.dat"
    dest_dir="case$i/Py24_LES32_IUFNO_40ep_gap200_mag1/result"

    # 检查源文件是否存在
    if [ -f "$src_file" ]; then
        # 确保目标目录存在
        mkdir -p "$dest_dir"

        # 移动文件
        mv "$src_file" "$dest_dir/"
        echo "Moved $src_file to $dest_dir/"
    else
        echo "Source file $src_file does not exist."
	fi		

	######		
    src_file="dat/wk/m2/IUFNO32_40ep_uxyz_gap200_case$i.dat"
    dest_dir="case$i/Py24_LES32_IUFNO_40ep_gap200_mag2/result"

    # 检查源文件是否存在
    if [ -f "$src_file" ]; then
        # 确保目标目录存在
        mkdir -p "$dest_dir"

        # 移动文件
        mv "$src_file" "$dest_dir/"
        echo "Moved $src_file to $dest_dir/"
    else
        echo "Source file $src_file does not exist."
	fi	


	######		
    src_file="dat/wk/m5/IUFNO32_40ep_uxyz_gap200_case$i.dat"
    dest_dir="case$i/Py24_LES32_IUFNO_40ep_gap200_mag5/result"

    # 检查源文件是否存在
    if [ -f "$src_file" ]; then
        # 确保目标目录存在
        mkdir -p "$dest_dir"

        # 移动文件
        mv "$src_file" "$dest_dir/"
        echo "Moved $src_file to $dest_dir/"
    else
        echo "Source file $src_file does not exist."
	fi	
	

	######		
    src_file="dat/wk/m10/IUFNO32_40ep_uxyz_gap200_case$i.dat"
    dest_dir="case$i/Py24_LES32_IUFNO_40ep_gap200_mag10/result"

    # 检查源文件是否存在
    if [ -f "$src_file" ]; then
        # 确保目标目录存在
        mkdir -p "$dest_dir"

        # 移动文件
        mv "$src_file" "$dest_dir/"
        echo "Moved $src_file to $dest_dir/"
    else
        echo "Source file $src_file does not exist."
	fi		

	

	######		
    src_file="dat/wk/m1/IFNO32_uxyz_gap200_case$i.dat"
    dest_dir="case$i/Py24_LES32_IFNO_gap200_mag1/result"

    # 检查源文件是否存在
    if [ -f "$src_file" ]; then
        # 确保目标目录存在
        mkdir -p "$dest_dir"

        # 移动文件
        mv "$src_file" "$dest_dir/"
        echo "Moved $src_file to $dest_dir/"
    else
        echo "Source file $src_file does not exist."
	fi		

	######		
    src_file="dat/wk/m2/IFNO32_uxyz_gap200_case$i.dat"
    dest_dir="case$i/Py24_LES32_IFNO_gap200_mag2/result"

    # 检查源文件是否存在
    if [ -f "$src_file" ]; then
        # 确保目标目录存在
        mkdir -p "$dest_dir"

        # 移动文件
        mv "$src_file" "$dest_dir/"
        echo "Moved $src_file to $dest_dir/"
    else
        echo "Source file $src_file does not exist."
	fi	

	######		
    src_file="dat/wk/m5/IFNO32_uxyz_gap200_case$i.dat"
    dest_dir="case$i/Py24_LES32_IFNO_gap200_mag5/result"

    # 检查源文件是否存在
    if [ -f "$src_file" ]; then
        # 确保目标目录存在
        mkdir -p "$dest_dir"

        # 移动文件
        mv "$src_file" "$dest_dir/"
        echo "Moved $src_file to $dest_dir/"
    else
        echo "Source file $src_file does not exist."
	fi	

	######		
    src_file="dat/wk/m10/IFNO32_uxyz_gap200_case$i.dat"
    dest_dir="case$i/Py24_LES32_IFNO_gap200_mag10/result"

    # 检查源文件是否存在
    if [ -f "$src_file" ]; then
        # 确保目标目录存在
        mkdir -p "$dest_dir"

        # 移动文件
        mv "$src_file" "$dest_dir/"
        echo "Moved $src_file to $dest_dir/"
    else
        echo "Source file $src_file does not exist."
	fi		

done
