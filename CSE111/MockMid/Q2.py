# -*- coding: utf-8 -*-
"""
Created on Fri Aug 14 10:00:44 2020

@author: BryaN
"""

def primeCheck(a):
    a=int(a)
    for i in range(2,a):
        if a%i==0:
            x ="Not Prime"
            break
    else:
         x="Prime"
    return(x)
num=int(input("Enter yout number: "))
print(primeCheck(num))
    