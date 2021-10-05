import os

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


# read_path = '/opt/datasets/test/extracted/scene0025_01/_info.txt'
# write_path = '/opt/datasets/test/extracted/scene0025_01/calib.txt'
base_dir = '/opt/datasets/train/extracted'
for dir in os.listdir(base_dir):
    read_path = os.path.join(base_dir, dir, '_info.txt')
    write_path = os.path.join(base_dir, dir, 'calib.txt')
    print(dir)
    write_calib(read_path, write_path)