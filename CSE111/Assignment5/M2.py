# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 01:42:07 2020

@author: BryaN
"""
#medium2
ddd={}
l=[]
while True:
    n=input("Enter number: ")
    if n=="STOP":
        break
    else:
        l.append(n)
for i in l:
    ddd[i]=ddd.get(i,0)+1
#print(ddd)
for key,value in ddd.items():
    print(key,"-",value,"times")
    
        