# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 20:39:16 2020

@author: BryaN
"""

#easy1
n= input("Enter your string: ")
s=["a","e","i","o","u","A","E","I","O","U"]
v=[]
nv=[]
count=0
for i in n:
    if i in s:
        count+=1
        v.append(i)
    else:
        nv.append(i)
j="".join(nv)
print(j+str(count))        
