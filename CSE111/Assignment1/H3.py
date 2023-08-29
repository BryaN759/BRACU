# -*- coding: utf-8 -*-
"""
Created on Thu Jul  9 20:36:35 2020

@author: BryaN
"""

num=int(input("Enter a number:"))
num=bin(num)
num=num.replace("0b","")
num=num.replace("0","")
num=int(num,2)
print(num)