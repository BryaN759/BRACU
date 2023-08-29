# -*- coding: utf-8 -*-
"""
Created on Sun Jul  5 00:52:32 2020

@author: BryaN
"""


num =int(input("Enter your number"))
sum=0
for i in range(1,num):
    if num%i==0:
        sum=sum+i
if sum==num:
    print("Perfect number")
else:
    print("Not Perfect number")