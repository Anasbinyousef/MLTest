# -*- coding: utf-8 -*-
"""Moodify Random forest

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1od_L5uWGjY6sJ9H6Wh4V0qa3XkRKBGbz
"""

# random forest algorithm #
########################### STRESS ###########################

import pandas as pd
import numpy as np
import sklearn 
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn import metrics
from sklearn.metrics import  confusion_matrix
from sklearn import preprocessing
from sklearn.preprocessing import OrdinalEncoder
testdata = pd.read_csv("stress  test - Sheet1.csv")
traindata = pd.read_csv("stress - Sheet1.csv")
testlabel = testdata['results']
trainlabel = traindata['results']
testdata = testdata.drop(['results','15','16'],axis=1)
traindata = traindata.drop(['results','15','16'],axis=1)
encoder = OrdinalEncoder()
trainresult = encoder.fit_transform(traindata)
testresult = encoder.fit_transform(testdata)
reg = RandomForestClassifier()
reg.fit(trainresult, trainlabel)
prediction =reg.predict(testresult)
print("your prediction is:")
print(prediction)
mat = confusion_matrix(prediction, testlabel)
names = np.unique(testlabel)
sns.heatmap(mat, square=True, annot=True, fmt='d', cbar=False, xticklabels=names, yticklabels=names)
plt.xlabel('Truth')
plt.ylabel('Predicted')
plt.show()
print("Accuracy:",metrics.accuracy_score(testlabel, prediction))

################## ADHD ###########################

testdata = pd.read_csv("ADHD test - Sheet1.csv")
traindata = pd.read_csv("ADHD  - Sheet1.csv")
testlabel = testdata['results']
trainlabel = traindata['results']
testdata = testdata.drop(['results','11','12'],axis=1)
traindata = traindata.drop(['results','11','12'],axis=1)
encoder = OrdinalEncoder()
trainresult = encoder.fit_transform(traindata)
testresult = encoder.fit_transform(testdata)
reg = RandomForestClassifier()
reg.fit(trainresult, trainlabel)
prediction =reg.predict(testresult)
print("your prediction is:")
print(prediction)
mat = confusion_matrix(prediction, testlabel)
names = np.unique(testlabel)
sns.heatmap(mat, square=True, annot=True, fmt='d', cbar=False, xticklabels=names, yticklabels=names)
plt.xlabel('Truth')
plt.ylabel('Predicted')
plt.show()
print("Accuracy:",metrics.accuracy_score(testlabel, prediction))

################## BDP ###########################


testdata = pd.read_csv("BDP test - Sheet1.csv")
traindata = pd.read_csv("BPD - Sheet1.csv")
testlabel = testdata['results']
trainlabel = traindata['results']
testdata = testdata.drop('results',axis=1)
traindata = traindata.drop('results',axis=1)
encoder = OrdinalEncoder()
trainresult = encoder.fit_transform(traindata)
testresult = encoder.fit_transform(testdata)
reg = RandomForestClassifier()
reg.fit(trainresult, trainlabel)
prediction =reg.predict(testresult)
print("your prediction is:")
print(prediction)
mat = confusion_matrix(prediction, testlabel)
names = np.unique(testlabel)
sns.heatmap(mat, square=True, annot=True, fmt='d', cbar=False, xticklabels=names, yticklabels=names)
plt.xlabel('Truth')
plt.ylabel('Predicted')
plt.show()
print("Accuracy:",metrics.accuracy_score(testlabel, prediction))

################## OCD ###########################


testdata = pd.read_csv("OCD test - Sheet1.csv")
traindata = pd.read_csv("OCD - Sheet1.csv")
testlabel = testdata['results']
trainlabel = traindata['results']
testdata = testdata.drop(['results','8'],axis=1)
traindata = traindata.drop(['results','8'],axis=1)
encoder = OrdinalEncoder()
trainresult = encoder.fit_transform(traindata)
testresult = encoder.fit_transform(testdata)
reg = RandomForestClassifier()
reg.fit(trainresult, trainlabel)
prediction =reg.predict(testresult)
print("your prediction is:")
print(prediction)
mat = confusion_matrix(prediction, testlabel)
names = np.unique(testlabel)
sns.heatmap(mat, square=True, annot=True, fmt='d', cbar=False, xticklabels=names, yticklabels=names)
plt.xlabel('Truth')
plt.ylabel('Predicted')
plt.show()
print("Accuracy:",metrics.accuracy_score(testlabel, prediction))

################## PTSD ###########################


testdata = pd.read_csv("PTSD test - Sheet1 (1).csv")
traindata = pd.read_csv("PTSD  - Sheet1.csv")
testlabel = testdata['results']
trainlabel = traindata['results']
testdata = testdata.drop(['results','15','14'],axis=1)
traindata = traindata.drop(['results','15','14'],axis=1)
encoder = OrdinalEncoder()
trainresult = encoder.fit_transform(traindata)
testresult = encoder.fit_transform(testdata)
reg = RandomForestClassifier()
reg.fit(trainresult, trainlabel)
prediction =reg.predict(testresult)
print("your prediction is:")
print(prediction)
mat = confusion_matrix(prediction, testlabel)
names = np.unique(testlabel)
sns.heatmap(mat, square=True, annot=True, fmt='d', cbar=False, xticklabels=names, yticklabels=names)
plt.xlabel('Truth')
plt.ylabel('Predicted')
plt.show()
print("Accuracy:",metrics.accuracy_score(testlabel, prediction))

################## ANOREXIA ###########################


testdata = pd.read_csv("anorexia test - Sheet1.csv")
traindata = pd.read_csv("anorexia - Sheet1.csv")
testlabel = testdata['results']
trainlabel = traindata['results']
testdata = testdata.drop('results',axis=1)
traindata = traindata.drop('results',axis=1)
encoder = OrdinalEncoder()
trainresult = encoder.fit_transform(traindata)
testresult = encoder.fit_transform(testdata)
reg = RandomForestClassifier()
reg.fit(trainresult, trainlabel)
prediction =reg.predict(testresult)
print("your prediction is:")
print(prediction)
mat = confusion_matrix(prediction, testlabel)
names = np.unique(testlabel)
sns.heatmap(mat, square=True, annot=True, fmt='d', cbar=False, xticklabels=names, yticklabels=names)
plt.xlabel('Truth')
plt.ylabel('Predicted')
plt.show()
print("Accuracy:",metrics.accuracy_score(testlabel, prediction))

################## ANXIETY ###########################


testdata = pd.read_csv("anxiety test - Sheet1.csv")
traindata = pd.read_csv("anxiety - Sheet1.csv")
testlabel = testdata['results']
trainlabel = traindata['results']
testdata = testdata.drop(['results','15','16'],axis=1)
traindata = traindata.drop(['results','15','16'],axis=1)
encoder = OrdinalEncoder()
trainresult = encoder.fit_transform(traindata)
testresult = encoder.fit_transform(testdata)
reg = RandomForestClassifier()
reg.fit(trainresult, trainlabel)
prediction =reg.predict(testresult)
print("your prediction is:")
print(prediction)
mat = confusion_matrix(prediction, testlabel)
names = np.unique(testlabel)
sns.heatmap(mat, square=True, annot=True, fmt='d', cbar=False, xticklabels=names, yticklabels=names)
plt.xlabel('Truth')
plt.ylabel('Predicted')
plt.show()
print("Accuracy:",metrics.accuracy_score(testlabel, prediction))

################## BIPOLAR DISORDER ###########################


testdata = pd.read_csv("bipolar disorder test - Sheet1.csv")
traindata = pd.read_csv("bipolar disorder - Sheet1.csv")
testlabel = testdata['results']
trainlabel = traindata['results']
testdata = testdata.drop(['results','11','12'],axis=1)
traindata = traindata.drop(['results','11','12'],axis=1)
encoder = OrdinalEncoder()
trainresult = encoder.fit_transform(traindata)
testresult = encoder.fit_transform(testdata)
reg = RandomForestClassifier()
reg.fit(trainresult, trainlabel)
prediction =reg.predict(testresult)
print("your prediction is:")
print(prediction)
mat = confusion_matrix(prediction, testlabel)
names = np.unique(testlabel)
sns.heatmap(mat, square=True, annot=True, fmt='d', cbar=False, xticklabels=names, yticklabels=names)
plt.xlabel('Truth')
plt.ylabel('Predicted')
plt.show()
print("Accuracy:",metrics.accuracy_score(testlabel, prediction))

################## DEPRESSION ###########################


testdata = pd.read_csv("depression test - Sheet1.csv")
traindata = pd.read_csv("depression - Sheet1.csv")
testlabel = testdata['results']
trainlabel = traindata['results']
testdata = testdata.drop(['results','15','16'],axis=1)
traindata = traindata.drop(['results','15','16'],axis=1)
encoder = OrdinalEncoder()
trainresult = encoder.fit_transform(traindata)
testresult = encoder.fit_transform(testdata)
reg = RandomForestClassifier()
reg.fit(trainresult, trainlabel)
prediction =reg.predict(testresult)
print("your prediction is:")
print(prediction)
mat = confusion_matrix(prediction, testlabel)
names = np.unique(testlabel)
sns.heatmap(mat, square=True, annot=True, fmt='d', cbar=False, xticklabels=names, yticklabels=names)
plt.xlabel('Truth')
plt.ylabel('Predicted')
plt.show()
print("Accuracy:",metrics.accuracy_score(testlabel, prediction))

################## INSOMNIA ###########################


testdata = pd.read_csv("insomnia test.csv")
traindata = pd.read_csv("insomnia train.csv")
testlabel = testdata['results']
trainlabel = traindata['results']
testdata = testdata.drop('results',axis=1)
traindata = traindata.drop('results',axis=1)
encoder = OrdinalEncoder()
trainresult = encoder.fit_transform(traindata)
testresult = encoder.fit_transform(testdata)
reg = RandomForestClassifier()
reg.fit(trainresult, trainlabel)
prediction =reg.predict(testresult)
print("your prediction is:")
print(prediction)
mat = confusion_matrix(prediction, testlabel)
names = np.unique(testlabel)
sns.heatmap(mat, square=True, annot=True, fmt='d', cbar=False, xticklabels=names, yticklabels=names)
plt.xlabel('Truth')
plt.ylabel('Predicted')
plt.show()
print("Accuracy:",metrics.accuracy_score(testlabel, prediction))

################## SCHIZOID PERSONALITY DISORDER ###########################


testdata = pd.read_csv("schizoid personality disorder test - Sheet1.csv")
traindata = pd.read_csv("schizoid personality disorder - Sheet1.csv")
testlabel = testdata['results']
trainlabel = traindata['results']
testdata = testdata.drop('results',axis=1)
traindata = traindata.drop('results',axis=1)
encoder = OrdinalEncoder()
trainresult = encoder.fit_transform(traindata)
testresult = encoder.fit_transform(testdata)
reg = RandomForestClassifier()
reg.fit(trainresult, trainlabel)
prediction =reg.predict(testresult)
print("your prediction is:")
print(prediction)
mat = confusion_matrix(prediction, testlabel)
names = np.unique(testlabel)
sns.heatmap(mat, square=True, annot=True, fmt='d', cbar=False, xticklabels=names, yticklabels=names)
plt.xlabel('Truth')
plt.ylabel('Predicted')
plt.show()
print("Accuracy:",metrics.accuracy_score(testlabel, prediction))

################## SCHIZOPHERNIA ###########################


testdata = pd.read_csv("schizophernia test - Sheet1.csv")
traindata = pd.read_csv("schizophernia - Sheet1.csv")
testlabel = testdata['results']
trainlabel = traindata['results']
testdata = testdata.drop(['results','14'],axis=1)
traindata = traindata.drop(['results','14'],axis=1)
encoder = OrdinalEncoder()
trainresult = encoder.fit_transform(traindata)
testresult = encoder.fit_transform(testdata)
reg = RandomForestClassifier()
reg.fit(trainresult, trainlabel)
prediction =reg.predict(testresult)
print("your prediction is:")
print(prediction)
mat = confusion_matrix(prediction, testlabel)
names = np.unique(testlabel)
sns.heatmap(mat, square=True, annot=True, fmt='d', cbar=False, xticklabels=names, yticklabels=names)
plt.xlabel('Truth')
plt.ylabel('Predicted')
plt.show()
print("Accuracy:",metrics.accuracy_score(testlabel, prediction))