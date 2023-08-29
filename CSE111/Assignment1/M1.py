# -*- coding: utf-8 -*-
"""
Created on Sun Jul  5 00:10:16 2020

@author: BryaN
"""


N = int(input("Fibonacci"))
a=0
b=1
print(a)
print(b)
for i in range (N):
   c=a+b
   if a+b>N:
       break
   else:
       print(a+b)
       a=b
       b=c
    