# -*- coding: utf-8 -*-
"""
Created on Sat Jul  4 23:47:31 2020

@author: BryaN
"""


num = int(input("Enter your number please"))
for i in range(2,num):
    if num%i==0:
        print("Not Prime")
        break
else: 
    print("Prime")