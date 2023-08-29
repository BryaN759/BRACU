# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 11:08:29 2020

@author: BryaN
"""

#medium3
n=input("Enter your keys and values separated by comma: ")
ddd = dict(i.split(':') for i in n.split(','))
#rev_d={value : key for key, value in ddd.items()}
#print(rev_d)
#print(ddd)
rev_d= {}  
for key, value in ddd.items(): 
    if value not in rev_d: 
        rev_d[value] = [key] 
    else: 
        rev_d[value].append(key)
print(rev_d)
