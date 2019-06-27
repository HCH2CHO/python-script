# -*- coding: utf-8 -*-
"""
Created on Sat Jul 21 00:35:33 2018

@author: HCHO
"""
#获取锁屏jpg图像
import os
import shutil
os.popen('')
#C:\Users\HCHO\AppData\Local\Packages\Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy\LocalState\Assets
oname="C:\\Users\\HCHO\\AppData\\Local\\Packages\\Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy\\LocalState\\Assets"
dname="C:\\Users\\HCHO\\Pictures\\Focusion"
alllist=os.listdir(oname)

for item in alllist:
        oldname=oname+'\\'+item
        newname=dname+'\\'+item+".jpg"
        fsize = os.path.getsize(oldname)/1024
        if(fsize>200):
            shutil.copyfile(oldname,newname)