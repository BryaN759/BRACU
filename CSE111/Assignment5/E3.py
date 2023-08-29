# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 14:37:28 2020

@author: BryaN
"""

#easy3
ddd = {}
n = 0
while n<10:
    x = int(input("Enter a number: "))
    if ddd.get(x) is None:
        ddd[x] = 1
        #print(ddd)
        n+=1
    else:
        print("Duplicate")
for i in ddd:
    print(i, end = " ")