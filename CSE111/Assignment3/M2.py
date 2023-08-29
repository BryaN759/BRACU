# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 21:38:02 2020

@author: BryaN
"""
#medium2
import string
a=string.ascii_letters
al=list(a)
acount=0
d=string.digits
dl=list(d)
dcount=0
s=input("Enter your string: ")
for i in s:
    if i in al:
        acount+=1
    else:
        dcount+=1
if acount>0 and dcount>0:
    print("MIXED")
elif acount>0 and dcount==0:
    print("WORD")
else:
    print("NUMBER")