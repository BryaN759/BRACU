# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 22:58:48 2020

@author: BryaN
"""


#hard1
s1=input("Enter the first string: ")
l1=[]
s2=input("Enter the second string: ")
l2=[]
for i in s1:
    if i in s2:
        l1.append(i)
for i in s2:
    if i in s1:
        l2.append(i)
l=l1+l2
x="".join(l)
print(x)
