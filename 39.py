# -*- coding: utf-8 -*-
"""
Created on Sun May  9 20:12:06 2021

@author: 曾睿恩
"""

a=int(input("組數"))
for i in range(a):
    b=input("第"+str(i+1)+"組:").split()
    t1=eval(b[0])*250+eval(b[1])*175
    print(str(t1))