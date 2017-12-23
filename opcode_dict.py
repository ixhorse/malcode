#-*-coding:utf-8-*-

import pickle, pprint

opcode_file = 'E:\\malcode\\project\\dalvik_opcode.txt'
dict_file = 'E:\\malcode\\project\\opcode_dict'

f = open(opcode_file, 'r')
lines = f.readlines()

linenum = 0
code_class = {}

while(linenum < len(lines)):
    if(lines[linenum][0] == '-'):
        class_name = lines[linenum][2]
        code_class[class_name] = []
        linenum += 1
        while(lines[linenum] != '\n'):
            code_class[class_name].append(lines[linenum].strip('\n'))
            linenum += 1
            if(not linenum < len(lines)):
                break
        linenum += 1

f.close()

temp = {}
for (desc, op) in code_class.items():
    for x in op:
        temp[x] = desc

f = open(dict_file, 'wb')
pickle.dump(temp, f)
f.close()

f = open(dict_file, 'rb')
dict = pickle.load(f)
pprint.pprint(dict)