# -*- coding: utf-8 -*-
"""
Created on Sat Jul 11 14:19:11 2020

@author: BryaN
"""


def replace_domain(a,b,c="kaaj.com"):
    if c in a:
        old=a.find("kaaj.com")
        dom=a[0:old]
        return(dom+b)
    else:
        return(a)
e=input("Enter your Email: ")
n=input("Enter new domain: ")
o=input("Enter old domain: ")
print(replace_domain(e,n,o))