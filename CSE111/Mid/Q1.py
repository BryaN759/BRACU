# -*- coding: utf-8 -*-
"""
Created on Fri Aug 21 09:47:38 2020

@author: BryaN
"""


n=input('Enter your string: ')
d='1234567890'
s=''
for i in n:
    if i in d:
        s+=i
print(s)