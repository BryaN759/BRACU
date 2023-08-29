# -*- coding: utf-8 -*-
"""
Created on Wed Jul  8 20:41:32 2020

@author: BryaN
"""

N = int(input("Enter the number of rows: "))
for row in range(1,N+1):
    for col in range(1,N*2):
        if row==N or col+row==N+1 or col-row==N-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()      
for row in range(N-1,0,-1):
    for col in range(1,N*2):
        if col+row==N+1 or col-row==N-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
    