# -*- coding: utf-8 -*-
"""
Created on Tue Aug 13 15:57:10 2019

@author: HCHO
"""
#调整列序
#利用pandas进行excel表操作
import pandas as pd

path="route0813.csv"
data=pd.read_csv(path)
cols = data.columns.tolist()
data=data[[cols[0],cols[3],cols[1],cols[2]]]
data.to_csv("route.txt")