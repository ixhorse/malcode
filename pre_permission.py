#-*-coding:utf-8-*-

import pickle, pprint

permission_file = 'E:\\malcode\\project\\permission_all.txt'
dict_file = 'E:\\malcode\\project\\permission_dict'

permission_dict = {}
count = 0

f = open(permission_file, 'r', encoding='utf-8')
lines = f.readlines()
for line in lines:
    permission_name = line.split('\t')[-1].split('，')[0]
    permission_dict[permission_name] = count
    count += 1
f.close()

f = open(dict_file, 'wb')
pickle.dump(permission_dict, f)
f.close()

f = open(dict_file, 'rb')
dict = pickle.load(f)
pprint.pprint(dict)
f.close()