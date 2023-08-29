# -*- coding: utf-8 -*-
"""
Created on Thu Jul  9 20:18:17 2020

@author: BryaN
"""


num=input("Enter your number ")

l=list()
for i in num:
    if i not in l:
        l.append(i)
print(len(l))        
        