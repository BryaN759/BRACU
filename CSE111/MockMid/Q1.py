# -*- coding: utf-8 -*-
"""
Created on Fri Aug 14 09:37:06 2020

@author: BryaN
"""



lc='abcdefghijklmnopqrstuvwxyz'
st=''
s=input("Enter your string: ")
count=0
for i in s:
    if i in lc:
        st+i
        count+=1
print("Number of lower case letters:",count)

