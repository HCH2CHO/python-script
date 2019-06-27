# -*- coding: utf-8 -*-
"""
Created on Fri May  4 11:07:42 2018

@author: HCHO
"""
#去除换行符。样例在reading help里
before=open('reading help\\before.csv','r',encoding='utf-8')
text=before.readlines()
newtext=''
for item in text:
    newtext+=item.replace('\n','')
after=open('reading help\\after.txt','w')
after.write(newtext)