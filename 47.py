# -*- coding: utf-8 -*-
"""
Created on Sun May  9 20:48:01 2021

@author: 曾睿恩
"""

n=int(input("輸入筆數n:"))
d={}
for i in range(n):
    a,b=input("請輸入對應的中、英文:").split(" ")
    d[a]=b
s=input("輸入欲查詢單字:")
print(s,"中文意思為",d[s])