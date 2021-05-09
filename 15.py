# -*- coding: utf-8 -*-
"""
Created on Sun May  9 20:34:28 2021

@author: 曾睿恩
"""

a=str(input('輸入:'))
c=str((int(a[0])+7)%10)
d=str((int(a[1])+7)%10)
e=str((int(a[2])+7)%10)
f=str((int(a[3])+7)%10)
g=str()
g=g+e+f+c+d
print(g)