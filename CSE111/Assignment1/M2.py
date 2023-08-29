# -*- coding: utf-8 -*-
"""
Created on Sun Jul  5 00:44:47 2020

@author: BryaN
"""


N = int(input("Enter your number "))
d=0
rev=0
while(N!=0):
    d=N%10
    rev=rev*10+d
    N=N//10
print(rev)