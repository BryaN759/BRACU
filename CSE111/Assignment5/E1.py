# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 23:36:08 2020

@author: BryaN
"""


#easy1
n=input("Enter your keys and values separated by comma: ")
ddd = dict(i.split(':') for i in n.split(','))
while True:
    num=input("Enter number: ")
    if num=="STOP":
        break
    else:
        x=num in ddd.values()
        print(x)

