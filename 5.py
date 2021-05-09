# -*- coding: utf-8 -*-
"""
Created on Sun May  9 19:57:00 2021

@author: 曾睿恩
"""

a=b=1
m=int(input("請輸入正整數m的值："))
while(a<=m):
    b+=1
    a*=b
print("超過M為%d的最小階層N值為：%d" % (m,b))