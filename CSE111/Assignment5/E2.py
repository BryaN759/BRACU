# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 23:36:09 2020

@author: BryaN
"""

#easy2
n=input("Enter your keys and values separated by comma: ")
ddd = dict(i.split(':') for i in n.split(','))
for key,value in ddd.items():
    ddd[key]=int(value)
#print(ddd)
key_list = list(ddd.keys()) 
val_list = list(ddd.values())
#print(key_list,val_list)
v=ddd.values()
mini=key_list[val_list.index(min(v))]
maxi=key_list[val_list.index(max(v))]
print("Minimum:",mini)
print("Maximum:",maxi)
    