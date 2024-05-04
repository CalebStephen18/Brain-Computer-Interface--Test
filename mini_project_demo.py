# -*- coding: utf-8 -*-
"""Mini Project DEMO.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Jcm91Pe5GsAwjPQese3rXLQDtYODL9mm
"""

from google.colab import drive
drive.mount('/content/drive',force_remount=True)

path = 'drive/My Drive/Colab Notebooks/final.csv'

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn.metrics import classification_report
from sklearn.metrics import balanced_accuracy_score
from sklearn.metrics import accuracy_score,f1_score,precision_score,recall_score
from sklearn.model_selection import cross_val_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
df = pd.read_csv(path)
df = df.dropna()
X = df.drop('label', axis=1)
y = df['label']
X = X.astype(int)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.10, random_state = 0)
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

df.head()

from sklearn.ensemble import GradientBoostingClassifier
clf = GradientBoostingClassifier(random_state=0,n_estimators = 1000,max_features=3)
clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)
print("Accuracy: ",(metrics.accuracy_score(y_test, y_pred) * 100),'%')

print(classification_report(y_test,y_pred))

clf = RandomForestClassifier(n_estimators = 1000,random_state=0,verbose = 1,max_features = 3)
clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)
print("Accuracy: ",(metrics.accuracy_score(y_test, y_pred) * 100),'%')
print(classification_report(y_test,y_pred))

from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
pipe = make_pipeline(StandardScaler(), LogisticRegression(solver='newton-cg',C=227,max_iter=1000))
pipe.fit(X_train, y_train)
print("Accuracy: ",(pipe.score(X_test, y_test) * 100),"%")

y_pred = pipe.predict(X_test)

print(classification_report(y_test,y_pred))

from sklearn.neighbors import KNeighborsClassifier
clf = KNeighborsClassifier(n_neighbors = 1,weights = 'distance',algorithm = 'auto',p=1)
clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)
print("Accuracy: ",(metrics.accuracy_score(y_test, y_pred) * 100),'%')

print(classification_report(y_test,y_pred))

from sklearn.ensemble import VotingClassifier

clf1 = GradientBoostingClassifier(random_state=0,n_estimators = 1000,max_features=3)
clf2 = RandomForestClassifier(n_estimators = 1000,random_state=0,verbose = 1,max_features = 3)

eclf1 = VotingClassifier(estimators=[('gb', clf1), ('rf', clf2)], voting='hard')

eclf1 = eclf1.fit(X_train, y_train)

y_pred = eclf1.predict(X_test)

print("Accuracy: ",(metrics.accuracy_score(y_test, y_pred) * 100),'%')
print(classification_report(y_test,y_pred))
