# -*- coding: utf-8 -*-
"""
Created on Sun May  9 20:00:45 2021

@author: 曾睿恩
"""

A=int(input("月:"))
B=int(input("日:"))
C=(A*2+B)%3
if C==0:
    print("普通")
elif C==1:
    print("吉")
elif C==2:
    print("大吉")