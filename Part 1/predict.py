import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
import matplotlib.pyplot as plt
from sklearn import preprocessing
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.metrics import plot_confusion_matrix

le = preprocessing.LabelEncoder()
df = pd.read_csv("dataset.csv")
df['type'] = le.fit_transform(df['type'])
df['nameOrig'] = le.fit_transform(df['nameOrig'])

X=df[['type','nameOrig','amount','oldbalanceOrg','oldbalanceDest']]
y=df[['isFraud']]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)

dtclf = DecisionTreeClassifier()
rfclf = RandomForestClassifier(n_estimators=100)

dtclf.fit(X_train, y_train.values.ravel())
rfclf.fit(X_train, y_train.values.ravel())

plot_confusion_matrix(dtclf, X_test, y_test)  
plt.show() 

plot_confusion_matrix(rfclf, X_test, y_test) 
plt.show() 