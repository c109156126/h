# -*- coding: utf-8 -*-
"""
Created on Sun May  9 20:21:40 2021

@author: 曾睿恩
"""

a=int(input("請輸入n"))
b=int(input("請輸入k"))
sum=0
remainder1=a//b
sum=a+remainder1

if remainder1>=b:
    remainder2=remainder1//b
    sum+=remainder2


print(sum)