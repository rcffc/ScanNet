import os
import subprocess

with open('./scannetv2_train.txt', 'r') as r:
    lines = sorted(r.readlines())      
    for line in lines:
        # if not int(line[5:9]) == 521 and not int(line[5:9]) == 522:
        # if int(line[5:9])<624:
        #     continue
        print(line)
        proc = subprocess.Popen(["python3", "/home/pejiang_local/download-scannet.py", "--id", line.strip(), "--type", ".sens", "-o", "/opt/datasets"])
        proc.wait()