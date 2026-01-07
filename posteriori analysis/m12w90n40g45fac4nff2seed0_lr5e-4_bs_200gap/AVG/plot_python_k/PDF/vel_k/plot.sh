#!/bin/bash

scripts=(
	vel_k_error_pdf_GSfit.py
)

for script in "${scripts[@]}"; do
    script_name=$(basename "$script" .py)

    cat <<EOF | bsub
#BSUB -J ${script_name}
#BSUB -q ser
#BSUB -n 20
#BSUB -R "span[ptile=20]"
#BSUB -o stdout_${script_name}.out
#BSUB -e stderr_${script_name}.err

module load cuda/10.0
module load cudnn/7.1.4 
module load intel/2018.4
module load mpi/intel/2018.4
module load python/anaconda3/5.2.0

python -u ${script} > display_${script_name}.log 2>&1
EOF

done
















