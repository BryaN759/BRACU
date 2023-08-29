# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 21:06:18 2020

@author: BryaN
"""


#easy3
s=input("Enter your string: ")
length=len(s)
if length>4:
    f=s.find("ful")
    if f>-1:
        print(s+"ly")
    else:
        print(s+"ful")
else:
    print(s)