# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 21:16:41 2020

@author: BryaN
"""
#medium1
import string
uc=string.ascii_uppercase
l1=list(uc)
lc=string.ascii_lowercase
l2=list(lc)
uppercount=0
lowercount=0
s=input("Enter your string: ")
for i in s:
    if i in l1:
        uppercount+=1
    else:
        lowercount+=1
if uppercount>lowercount:
    print(s.upper())
else:
    print(s.lower())