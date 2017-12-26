# -*- coding: UTF-8 -*-

import glob
import os
import re
import pickle
import pandas as pd
import numpy as np

apk_path = 'E:\\malcode\\train_mal'
dict_file = 'E:\\malcode\\project\\permission_dict'

f_dict = open(dict_file, 'rb')
permission_dict = pickle.load(f_dict)
f_dict.close()
permission_num = len(permission_dict)

apk_list = glob.glob(apk_path + '\\*')
apk_list = [x.split('\\')[-1] for x in apk_list]

fmap = []
for apk in apk_list:
    vector = [0 for x in range(permission_num)]

    xml_file = glob.glob(os.path.join(apk_path, apk) + '\\*Manifest.xml')[0]
    f = open(xml_file, 'r', encoding='utf-8')
    lines = f.readlines()
    for line in lines:
        m = re.search(r'android\.permission\..*?\"', line)
        if(m):
            permission = m.group(0)[0:-1]
            if(permission in permission_dict):
                vector[permission_dict[permission]] = 1
    f.close()
    fmap.append([apk] + vector)

fmap = pd.DataFrame(np.array(fmap))
fmap.to_csv("permissionft_train_mal.csv", index=False)