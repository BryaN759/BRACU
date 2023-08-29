# -*- coding: utf-8 -*-
"""
Created on Sat Jul 11 14:35:47 2020

@author: BryaN
"""


def med3(a):
    count=0
    vow= []
    l= ["a","e","i","o","u","A","E","I","O","U"]
    for i in a:
        if i in l:
            count=count+1   
            vow.append(i) 
    if count>0:
        print("Vowels: ",vow,". Total number of vowels: ",count)
    else:
        print("No vowels in our name.")
          
        
name=input("Enter your name: ")
med3(name)

