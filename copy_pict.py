# -*- coding: utf-8 -*-
"""
Created on Sat Jul 21 00:35:33 2018

@author: HCHO
"""

# 获取锁屏jpg图像
import os
import shutil
from PIL import Image
os.popen('')
UserName = "HCHO"
opath = "C:\\Users\\" + UserName + "\\AppData\\Local\\Packages\\Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy\\LocalState\\Assets"
dpath_win = "C:\\Users\\" + UserName + "\\Pictures\\winWallpaper"
dpath_android = "C:\\Users\\" + UserName + "\\Pictures\\androidWallpaper"
all_list = os.listdir(opath)

if not os.path.exists(dpath_win):
    os.mkdir(dpath_win)
if not os.path.exists(dpath_android):
    os.mkdir(dpath_android)
for item in all_list:
    oldpath = opath + '\\' + item
    img = Image.open(oldpath)
    fsize = os.path.getsize(oldpath)/1024
    if(fsize > 200):
        if(img.size[0] > img.size[1]):
            newpath = dpath_win + '\\' + item + '.jpg'
        elif(img.size[0] < img.size[1]):
            newpath = dpath_android + '\\' + item + '.jpg'
        if not (os.path.isfile(newpath)):
            print(newpath)
            shutil.copyfile(oldpath, newpath)
    img.close()
