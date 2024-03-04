#!/bin/bash

if [ -d "ckpt" ]; then
    echo "Removing existing ckpt folder..."
    rm -rf ckpt
fi



models=(
  CNN DANN CORAL MSSA ACDANN DAN CDAN ADACL BSP MCD MFSAN
  IBN IRM
)

source=CWRU_0
target=CWRU_1

cuda_device=0
batch_size=4
max_epoch=30

for model in "${models[@]}"; do
  python train.py --model_name "$model" --source $source --target $target --train_mode single_source --cuda_device $cuda_device --batch_size $batch_size --max_epoch $max_epoch
done

python competing.py --File_name "CWRU_Performance.csv"