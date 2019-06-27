# -*- coding: utf-8 -*-
"""
Created on Thu Jan 17 19:27:57 2019

@author: HCHO
"""
#文件后缀重命名
import os
#symbol指文件后缀
def rename(symbol):
    i=31
    dictory = os.path.dirname(__file__)
    for root, dirs, files in os.walk(dictory, topdown=True):  
        for name in files:    
            #print(name)
            postfix=os.path.splitext(name)
            if (postfix[1]==symbol):
                print(name)
                oldname=name
                newname='EditBushouSave'+str(i)+symbol
                os.rename(oldname,newname)
                i+=1
            
rename('.dat')