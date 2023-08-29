# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 22:03:04 2020

@author: BryaN
"""


def hard3(text):
    import re
    splt= re.split('([.!?] *)', text)
    cap= [x.capitalize() for x in splt]
    j= ' '.join(cap)
    i=j.replace(" i ", " I ")   
    return(i)
passage= input("Enter your text: ")
print(hard3(passage))