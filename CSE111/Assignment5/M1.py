# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 01:14:11 2020

@author: BryaN
"""

#medium1
n1=input("Enter your keys and values separated by comma: ")
dd1 = dict(i.split(':') for i in n1.split(','))
for key,value in dd1.items():
    dd1[key]=int(value)
n2=input("Enter your keys and values separated by comma: ")
dd2 = dict(i.split(':') for i in n2.split(','))
for key,value in dd2.items():
    dd2[key]=int(value)
for key in dd1:
    if key in dd2:
        dd1[key]=dd1[key]+dd2[key]
for key,value in dd2.items():
    if key not in dd1.keys():
        dd1.update({key : value})
print(dd1)
import operator
sd= dict(sorted(dd1.items(), key=operator.itemgetter(1)))
l=list(sd.values())
print("Values:",tuple(l))
 
  
        