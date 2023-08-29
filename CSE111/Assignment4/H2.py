# -*- coding: utf-8 -*-
"""
Created on Wed Jul 22 15:58:16 2020

@author: BryaN
"""


#hard2
import string
d=list(string.digits)
dl=[]
u=list(string.ascii_uppercase)
ul=[]
l=list(string.ascii_lowercase)
ll=[]
s=input("Enter yout string: ")
for i in s:
    if i in l:
        ll.append(i)
    elif i in u:
        ul.append(i)
    else:
        dl.append(i)
ll.sort()
ul.sort()
odd=[]
even=[]
for i in dl:
    if int(i)%2==1:
        odd.append(i)
    else:
        even.append(i)
lst=ll+ul+odd+even
final="".join(lst)
print(final)
        
        