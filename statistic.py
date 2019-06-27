# -*- coding: utf-8 -*-
"""
Created on Thu Jun 27 09:08:26 2019

@author: HCHO
"""

#代码行数统计
import os
#def statistic():
num=0
for  root, dirs, files in os.walk('C:\\Users\\HCHO\\Desktop\\iau_ros_map'):
    for name in files:  
        postfix=name.split('.')[1]
        if postfix=='c' or postfix=='cpp' or postfix=='h' or postfix=='hpp':
            path=os.path.join(root, name)
            file=open(path,'rb')
            line=file.readlines()
            num+=len(line)
   