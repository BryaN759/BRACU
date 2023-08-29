# -*- coding: utf-8 -*-
"""
Created on Sat Jul 11 13:38:54 2020

@author: BryaN
"""


def med1(a,b="Mohakhali"):
    if b!="Mohakhali":
        if a=="BBQ Chicken Cheese Burger":
            t=250+60+(250*(8/100))
        elif a=="Beef Burger":
            t=170+60+(170*(8/100))
        elif a=="Naga Drums":
            t=200+60+(200*(8/100))
    else:
        if a=="BBQ Chicken Cheese Burger":
            t=250+40+(250*(8/100))
        elif a=="Beef Burger":
            t=170+40+(170(8/100))
        elif a=="Naga Drums":
            t=200+40+(200(8/100))
    return(t)

order=input("Please enter your order: ")
place=input("Please enter your location: ")
print(med1(order,place))