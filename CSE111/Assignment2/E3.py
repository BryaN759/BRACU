# -*- coding: utf-8 -*-
"""
Created on Sat Jul 11 12:04:22 2020

@author: BryaN
"""


def easy3(a,b,c):
   l=[]
   for i in range(a,b):
       if i%c==0:
           l.append(i)
   s=sum(l)
   return(s)
min=int(input("Enter the minimum: "))
max=int(input("Enter the maximum: "))
d=int(input("Enter the divisor: "))
print(easy3(min,max,d))