# -*- coding: utf-8 -*-
"""
Created on Sun May  9 19:10:25 2021

@author: 曾睿恩
"""

c=int(input("組數為:"))
for i in range(1,c+1):
    a=int(input("第"+str(i)+"組為:").split(" "))
    b=int(input("第"+str(i)+"組為:").split(" "))
    sum=(a*250)+(b*175)
    print("第"+str(i)+"組應收費用:"+str(sum))
    