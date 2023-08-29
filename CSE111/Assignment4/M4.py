# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 15:25:19 2020

@author: BryaN
"""
#medium4
def nest_list(a, b):
    a=l.split(",")
    return [a[i::b] for i in range(b)]
N=int(input("Enter list number: "))
l=input("Enter the list elements: ")
print(nest_list(l,N))