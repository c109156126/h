# -*- coding: utf-8 -*-
"""
Created on Sun May  9 20:31:12 2021

@author: 曾睿恩
"""

a=float(input("輸入路程公里數"))
b=(a*1000)-(1.5*1000)
if a<=1.5:
    c=75
if a>1.5:
    if (b%250)==0:
        c=75+(b//250)*5
    if (b%250)!=0:
        c=75+((b//250)+1)*5
    if b<250:
        c=80
print("所需車資為:",c)