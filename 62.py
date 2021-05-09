# -*- coding: utf-8 -*-
"""
Created on Sun May  9 20:29:58 2021

@author: 曾睿恩
"""

a={"蘋果":"紅色","香蕉":"黃色","葡萄":"紫色","藍莓":"藍色","橘子":"橘色"}
print(a.keys())
fruit=input("請輸入水果")
print(fruit,"是",a.get(fruit))