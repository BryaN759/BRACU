# -*- coding: utf-8 -*-
"""
Created on Sat Jul 18 11:44:59 2020

@author: BryaN
"""


#medium1
l=[]
while True:
    n=input("Enter your numbers one by one: ")
    if n=="STOP":
        break
    l.append(n)
l2=[]
for i in l:
    if i not in l2:
        l2.append(i)
l2.sort()        
for i in range(0,len(l2)):
    print(l2[i],"-",l.count(l2[i]),"times")
    
#a=[[x,l.count(x)] for x in set(l)]
#print(a)