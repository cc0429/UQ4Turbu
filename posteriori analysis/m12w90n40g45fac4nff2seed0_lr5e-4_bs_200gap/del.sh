#!/bin/bash

# 设置需要删除子文件夹的 case 目录范围
for i in {4..30}; do
    case_dir="/scratch/2025-03-18/mae-zxt/F-IUFNO_post_new/isotropic/m12w90n40g45fac4nff2seed0_lr5e-4_bs5/case$i"
    
    # 确保 case 目录存在
    if [ -d "$case_dir" ]; then
        echo "Deleting all subfolders in $case_dir..."
        
        # 删除 case 目录下的所有子文件夹
        find "$case_dir" -mindepth 1 -type d -exec rm -rf {} +

        echo "All subfolders in $case_dir have been deleted."
    else
        echo "Directory $case_dir does not exist, skipping..."
    fi
done

echo "✅ All specified case folders have been cleaned."
