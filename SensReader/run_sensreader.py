import os
import subprocess

output_dir = '/opt/datasets/train/extracted'
# output_dir = '/opt/datasets/val/extracted'
scans_dir = '/opt/datasets/scans/'

def write_calib(read_path, write_path):
    with open(read_path, 'r') as r, open(write_path, 'w') as w:
        temp = ''
        lines = r.readlines()
        for line in lines:
            line = line.strip().split(' ')
            if line[0].startswith('m_colorWidth'):
                temp = line[2]
            if line[0].startswith('m_colorHeight'):
                w.write(temp + ' ' + line[2] + '\n')
                temp = ''
            if line[0].startswith('m_calibrationColorIntrinsic'):
                w.write(line[1+1] + ' ' + line[1+6] + '\n')
                w.write(line[1+3] + ' ' + line[1+7] + '\n')
                w.write('\n')

        for line in lines:
            line = line.strip().split(' ')
            if line[0].startswith('m_depthWidth'):
                temp = line[2]
            if line[0].startswith('m_depthHeight'):
                w.write(temp + ' ' + line[2] + '\n')
                temp = ''
            if line[0].startswith('m_calibrationDepthIntrinsic'):
                w.write(line[1+1] + ' ' + line[1+6] + '\n')
                w.write(line[1+3] + ' ' + line[1+7] + '\n')
                w.write('\n')

        for line in lines:
            line = line.strip().split(' ')
            if line[0].startswith('m_calibrationColorExtrinsic'):
                for x, i in enumerate(line[2:]):
                    if x%4==0:
                        temp = str(float(i))
                    else:
                        temp = temp + ' ' + str(float(i))
                    if x%4==3:
                        w.write(temp + '\n')
                        temp = ''


for dir in sorted(os.listdir(scans_dir)):
    # print(dir)
    # Is directory?
    if not os.path.isdir(os.path.join(scans_dir, dir)):
        continue

    # Already extracted?
    if dir in os.listdir(output_dir):
        print('skip ' + dir)
        continue

    # Sens file downloaded?
    filename = os.path.join(scans_dir, dir, dir + '.sens')
    if not os.path.exists(filename):
        continue

    # # Skip already reconstructed
    # # if not int(dir[5:9]) == 613:
    # if int(dir[5:9])<=613:
    #     continue

    # # Remaining val scenes
    # with open('SensReader/scannetv2_val.txt', 'r') as r, open('SensReader/val_reconstructed.txt', 'r') as reconstructed:
    #     lines_val =[s.strip() for s in r.readlines()]    
    #     lines_reconstructed = [s.strip() for s in reconstructed.readlines()]
    #     if not(dir in lines_val and not dir in lines_reconstructed):
    #         print(dir)
    #         continue
    
    proc = subprocess.Popen(["/home/pejiang_local/repos/ScanNet/SensReader/c++/sens", filename, os.path.join(output_dir, dir)])
    proc.wait()
    os.remove(filename)

    # write_calib
    read_path = os.path.join(output_dir, dir, '_info.txt')
    write_path = os.path.join(output_dir, dir, 'calib.txt')
    write_calib(read_path, write_path)