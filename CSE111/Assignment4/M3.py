# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 13:58:17 2020

@author: BryaN
"""
#medium3
l1=list(map(int, input("Enter your first list: ").split()))
l2=list(map(int, input("Enter your second list: ").split()))
l=[]
gen = ((x, y) for x in l1 for y in l2)

for u, v in gen:
    s=u*v
    l.append(s)
print(l)