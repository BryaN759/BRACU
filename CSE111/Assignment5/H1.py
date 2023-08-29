# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 11:26:48 2020

@author: BryaN
"""

#hard1
n1=input("Enter your first string: ")
#l1=list(n1)
dd1={}
for i in n1:
    dd1[i]=dd1.get(i,0)+1
print(dd1)
n2=input("Enter your second string: ")
#l2=list(n2)
dd2={}
for i in n2:
    dd2[i]=dd2.get(i,0)+1
print(dd2) 
print("")
if dd1==dd2:
     print("Those strings are anagrams.")
else:
     print("Those strings are not anagrams.")
    


