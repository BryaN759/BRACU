# -*- coding: utf-8 -*-
"""
Created on Sat Jul 18 11:15:04 2020

@author: BryaN
"""

#easy1
l=[]
maximum= 10
while len(l)<maximum:
    n=int(input("Enter your numbers to the list: "))
    l.append(n)
l.reverse()
print(l)