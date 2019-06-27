# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 09:52:56 2019

@author: HCHO
"""
#积分计算
import numpy as np
import matplotlib.pyplot
import scipy.integrate as sci

def f(x):
    return np.sin(x) + 0.5*x

a = 0
b = 1
x = np.linspace(0, 1,num=5)
y=f(x)

xi=sci.fixed_quad(f, a, b)[0]