# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 22:51:02 2020

@author: BryaN
"""


#medium4
s=input("Enter your string: ")
too=s.find("too")
good=s.find("good")
if good>too:
    rep=s.replace("too good","excellent")
    print(rep)
else:
    print(s)