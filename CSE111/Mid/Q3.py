# -*- coding: utf-8 -*-
"""
Created on Fri Aug 21 11:15:18 2020

@author: BryaN
"""


def totalCost(*args):
    l=list(args)
    nl=[]
    sum1=l[0]
    for i in range(1,len(l)):
        sum1+=l[i]
        nl.append(sum1)
    sum2=nl[0]
    for j in range(1,len(nl)):
        sum2+=nl[j]
    print(sum2)
totalCost(3,6,2,9)