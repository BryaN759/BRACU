# -*- coding: utf-8 -*-
"""
Created on Sat Jul 18 11:30:49 2020

@author: BryaN
"""

#easy3
l=[]
highest=10
while len(l)<highest:
    n=input("Enter your numbers for the list: ")
    if n not in l:
        l.append(n)
    else:
        print("Duplicate number not allowed. Please enter another number below")
        continue
print(l)
    