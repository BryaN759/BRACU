# -*- coding: utf-8 -*-
"""
Created on Sat Jul  4 22:57:49 2020

@author: BryaN
"""


A = int(input("Enter first number"))
B = int(input("Enter second number"))
C = int(input("Enter third number"))
if A>=B and A>=C:
    print(A)
elif B>=A and B>=C:
    print(B)
else :
    print(C)
    