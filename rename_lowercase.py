# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 16:21:23 2019

@author: HCHO
"""

#文件重命名,大写字母改为小写
import os
#symbol指文件后缀
def rename():
    dictory = os.path.dirname(__file__)
    for root, dirs, files in os.walk(dictory, topdown=True):  
        for name in files:    
            #print(name)
            
            print(name)
            oldname=name
            newname=oldname.lower()
            os.rename(oldname,newname)
           
rename()