# -*- coding: utf-8 -*-
"""
Created on Fri Aug 14 10:53:53 2020

@author: BryaN
"""



n=input("Enter names and numbers: ").split(",")
l1=[]
l2=[]
for i in range(0,len(n),2):
    l1.append(n[i])
for i in range(1,len(n),2):
    l2.append(n[i])
for i in range(len(l1)-1):
    for j in range(i+1,len(l1)):
        if l1[i]>l1[j]:
            temp = l1[i]
            l1[i] = l1[j]
            l1[j] = temp
            tem=l2[i]
            l2[i] = l2[j]
            l2[j] = tem
l3 = [j[i] for i in range(len(l2)) for j in [l1, l2]]
print(l3)