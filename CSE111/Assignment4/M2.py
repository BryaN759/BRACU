# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 12:49:52 2020

@author: BryaN
"""

#medium2
N=int(input("Enter the number of lists: "))
l=[]
highest=int()
while len(l)<N:
    n=list(map(int, input("Enter your lists: ").split()))
    s=sum(n)
    if highest< s:
        highest= s
        hl=n        
    l.append(s)  
print(highest)
print(hl)