# -*- coding: utf-8 -*-
"""
Created on Sun May  9 20:52:13 2021

@author: 曾睿恩
"""

a=(input("輸入值為:"))
b=a.replace(',','')
m=sorted(b,reverse=True)
n=sorted(b,reverse=False)
ma=''
mi=''
for i in m:
    ma +=str(i)
for j in n:
    mi +=str(j)

print("最大值數列與最小值數列差值為:"+str(int(ma)-int(mi)))
