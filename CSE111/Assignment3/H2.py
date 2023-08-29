# -*- coding: utf-8 -*-
"""
Created on Wed Jul 22 11:32:11 2020

@author: BryaN
"""
#hard2
s = input("Enter your string: ")
l=[]
res = [s[i: j] for i in range(len(s)) 
          for j in range(i + 1, len(s) + 1)]
ddd=dict()
for i in res:
    ddd[i]=ddd.get(i,0)+1
#print(ddd)
d_items=ddd.items()
for key,value in ddd.items():
    if value>2:
        l.append(key)
#print(l)
try:        
    for i in l:
        if s.startswith(i):
            if s.endswith(i):
                x=i
    if len(x)>0:
        print(x)
except:
    print("Not Palindrome Substring")
          

        
        