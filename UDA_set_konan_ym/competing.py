import os
import pandas as pd
import argparse

def parse_args():
    parser = argparse.ArgumentParser(description='From github.com/Feaxure-fresh/TL-Bearing-Fault-Diagnosis')
 
    # basic parameters
    parser.add_argument('--File_name', type=str, default='HUST_Performance.csv')
    args = parser.parse_args()
    return args
    
    
args = parse_args()

    
base_dir = '/home/workspace/TL-Bearing-Fault-Diagnosis/ckpt'

data = []

for model_name in os.listdir(base_dir):

    model_dir = os.path.join(base_dir, model_name)

    if os.path.isdir(model_dir):  
            single_source_dir = os.path.join(model_dir, 'single_source')
            if os.path.exists(single_source_dir): 
                
                
                log_files = [file for file in os.listdir(single_source_dir) if file.endswith('.log')]
                file_path = os.path.join(single_source_dir, log_files[0])
        
                with open(file_path, 'r') as log_file:
                     lines = log_file.readlines()
                epochs = []
                
                for line in lines:
                 
                    if "Train-Acc Source Data" in line:

                        train_acc_source = float(line.split(": ")[1])
                  
                    elif "Val-Acc Target Data" in line:
                        val_acc_target = float(line.split(": ")[1])
                        
                        epochs.append((train_acc_source, val_acc_target))
     
                
                best_epoch = max(epochs, key=lambda x: x[1])
        
                data.append([model_name, best_epoch[0], best_epoch[1]])
         
df = pd.DataFrame(data, columns=['Model Name', 'Train-Acc Source', 'Val-Acc Target'])

df_sorted = df.sort_values(by='Val-Acc Target', ascending=False)
df_sorted.to_csv(args.File_name, index=False)
# CWRU val_acc_target가 계속 1일때 best_epoch룰 Train_loss기준으로 바꿔줘야함 (나중에)