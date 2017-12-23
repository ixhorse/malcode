#-*-coding:utf-8-*-

import os
import glob
import multiprocessing
from math import ceil
import  pickle

core = 4

apk_path = 'E:\\malcode\\apk'
out_path = 'E:\\malcode\\opcode'
op_dict_path = 'E:\\malcode\\project\\opcode_dict'

dict_file = open(op_dict_path, 'rb')
op_dict = pickle.load(dict_file)
dict_file.close()

apk_list = glob.glob(apk_path + '\\*')
apk_list = [x.split('\\')[-1] for x in apk_list]

def worker(apk_split):
    for apk in apk_split:
        opcode_str = ''
        for root, dirs, files in os.walk(os.path.join(apk_path, apk)):
            for file in files:
                if(file[-5:] != 'smali'):
                    continue
                f = open(os.path.join(root, file), 'r')
                lines = f.readlines()
                f.close()
                for line in lines:
                    line = line.lstrip(' ')
                    if(len(line) == 0):
                        continue
                    if(line[0] == '.' or line[0] == ':' or line[0] == '#'):
                        continue

                    code = line.split(' ')[0]
                    if(code in op_dict):
                        opcode_str += op_dict[code]
        f = open(os.path.join(out_path, apk+'.txt'), 'w')
        f.write(opcode_str)
        f.close()
        print(apk, 'write success.')

if __name__ == '__main__':
    record = []
    length = len(apk_list)
    temp = ceil(length / core)
    for i in range(core):
        start = i * temp
        end = (i+1) * temp if (i+1)*temp < length else length
        if(start >= end):
            break
        process = multiprocessing.Process(target=worker, args=(apk_list[start:end], ))
        process.start()
        record.append(process)

    for process in record:
        process.join()