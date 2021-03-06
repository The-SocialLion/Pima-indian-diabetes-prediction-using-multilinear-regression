# -*- coding: utf-8 -*-
"""Untitled26.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ibu7c4v-2RYuvBZ8A7yA1exiTMT0n_6n
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

dataset=pd.read_csv('pima.csv')
X=dataset.iloc[:,:-1].values
y=dataset.iloc[:,-1].values

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

from sklearn.linear_model import LinearRegression
ML=LinearRegression()
ML.fit(X,y)

y_pred=ML.predict(X_test)
y_pred=abs(y_pred.round())
print(np.concatenate((y_pred.reshape(len(y_pred),1), y_test.reshape(len(y_test),1)),1))

print(ML.coef_)
print(ML.intercept_)