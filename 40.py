# -*- coding: utf-8 -*-
"""
Created on Sun May  9 20:45:26 2021

@author: 曾睿恩
"""

  
a=int(input("搭了幾次電梯:"))
b=0
c=0
d=0
e=0
s=1
for i in range(a):
    n=int(input(""))
    if n>s:
        up=(n-s)*20
        b=b+d
        s=n
    elif n<s:
        e=(s-n)*10
        c=c+e
        s=n
fee=c+b
print(fee)   