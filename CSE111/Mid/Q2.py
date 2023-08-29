# -*- coding: utf-8 -*-
"""
Created on Fri Aug 21 09:55:45 2020

@author: BryaN
"""


txt=input("Enter the text: ")
n=int(input("How many censored words are there? "))
for i in range(n): 
    x,y=input("Enter: ").split() 
    st=txt.split()
    s=''
    for i in st:
        if i==x:
            i=y
        s+=i+' '
    txt=s
print(s)