import os
import subprocess

with open('SensReader/scannetv2_val.txt', 'r') as r, open('SensReader/val_reconstructed.txt', 'r') as reconstructed:
    lines = sorted(r.readlines())      
    lines_reconstructed = reconstructed.readlines()
    for line in lines:
        if line in lines_reconstructed:
            continue
        print(line)
    # for line in lines:
    #     if int(line[5:9])<551:
    #         continue
    #     print(line)
        proc = subprocess.Popen(["python3", "/home/pejiang_local/download-scannet.py", "--id", line.strip(), "--type", ".sens", "-o", "/opt/datasets"])
        proc.wait()