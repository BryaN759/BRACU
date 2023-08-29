# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 22:00:48 2020

@author: BryaN
"""


#medium3
import string
ua=string.ascii_uppercase
l=list(ua)
s=input("Enter your string: ")
revs=s[::-1]
for i in s:
    if i in l:
        second=s.find(i)
for i in revs:
    if i in l:
        first=s.find(i)
#print(first)
#print(second)
if first+1==second:
    print("BLANK")
else:
    print(s[first+1:second])        