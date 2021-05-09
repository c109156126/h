# -*- coding: utf-8 -*-
"""
Created on Sun May  9 20:13:22 2021

@author: 曾睿恩
"""

a=int(input("輸入班級數:"))
b=[]
for i in range(a):
    c=int(input("人數:"))
    b.append(c)
    b.sort()
print("需要買"+str(b[a-1]))