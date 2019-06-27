# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 19:59:48 2017

@author: HCHO
"""
#文档合并
import os
txtpath='C:\\Users\\HCHO\\Desktop\\文件夹'
newtxt=open('C:\\Users\\HCHO\\Desktop\\txtword.txt','w')

txtlist=[]
for root , dirs, files in os.walk(txtpath):
    for file in files:
        if "txt" in file:
            txtlist.append(os.path.join(root,file)) 
for i in range(0,52):        
    txtread=open(txtlist[i],'r')
    while True:    
        line = txtread.readline()
        if line:
                newtxt.write(line)
    txtread.close()
newtxt.close()