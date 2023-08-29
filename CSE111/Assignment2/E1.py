# -*- coding: utf-8 -*-
"""
Created on Fri Jul 10 22:44:13 2020

@author: BryaN
"""


def easy1(a,b):
    if b==0:
        return 0
    else:  
      c=(a/b)-(a//b)
      return (c)
num1=int(input("Enter your first number: "))
num2=int(input("Enter your second number: "))
print(easy1(num1,num2))
   

