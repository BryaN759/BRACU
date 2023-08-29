# -*- coding: utf-8 -*-
"""
Created on Sat Jul 11 21:01:05 2020

@author: BryaN
"""


def med4(a):
    a=a.split()
    a="".join(a)
    if a[::-1]==a:
        print("Palindrome")
    else:
        print("Not a palindrome")

inp= input("Enter your word or phrase: ") 

med4(inp)
