# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 12:28:01 2020

@author: BryaN
"""

#easy2
a=input("Enter the first list elements: ")
b=input("Enter the second list elements: ")
l1=a.split(",")
l2=b.split(",")
l1.pop()
s=l1+l2
print(s)