# -*- coding: utf-8 -*-
"""
Created on Sun May  9 20:38:55 2021

@author: 曾睿恩
"""

a=input("輸入撲克牌數字:").split()
ans=0
for i in range(len(a)):
    if a[i]==chr(65) :
        ans+=1
    elif a[i]==chr(74) :
        ans+=11
    elif a[i]==chr(81) :
        ans+=12
    elif a[i]==chr(75) :
        ans+=13
    else  :
        ans+=eval(a[i])
print(ans)