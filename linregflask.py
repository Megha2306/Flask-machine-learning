# -*- coding: utf-8 -*-
"""
Created on Sun Apr  2 15:25:03 2023

@author: ADMIN
"""

import pandas as pd
df = pd.read_csv(r"C:\Users\ADMIN\Downloads\winequality-red.csv")
x=df.iloc[:,7:-1].values
y=df.iloc[:,-1].values
from sklearn.linear_model import LinearRegression
reg = LinearRegression()
reg.fit(x,y)
import pickle

pickle.dump(reg,open('flasklinreg.pkl','wb'))
