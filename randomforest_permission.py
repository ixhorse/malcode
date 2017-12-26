# -*- coding : utf-8 -*-

import pandas as pd
import os
from sklearn.ensemble import RandomForestClassifier as RF
from sklearn import model_selection
from sklearn.metrics import *

csv_path = 'E:\\malcode\\project'
ben_name = 'permissionft_ben.csv'
mal_name = 'permissionft_mal.csv'

train_ben = pd.read_csv(os.path.join(csv_path, ben_name))
train_mal = pd.read_csv(os.path.join(csv_path, mal_name))

train_ben['label'] = 0
train_mal['label'] = 1

train = train_mal.append(train_ben)

labels = train['label']

train.drop(['label'], axis=1, inplace=True)
train.drop(train.columns[0], axis=1, inplace=True)
train = train.as_matrix()



score = []
for i in range(10):
    X_train, X_test, y_train, y_test = model_selection.train_test_split(train, labels, test_size=0.3)
    srf = RF(n_estimators=350, n_jobs=-1)
    srf.fit(X_train,y_train)
    # print(srf.score(X_test,y_test))
    y_pred = srf.predict(X_test)
    print(confusion_matrix(y_test, y_pred))
    print(accuracy_score(y_test, y_pred))
    print(precision_recall_fscore_support(y_test, y_pred))
    score.append(accuracy_score(y_test, y_pred))
print(sum(score) / len(score))