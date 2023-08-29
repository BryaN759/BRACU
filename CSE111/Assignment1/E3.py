# -*- coding: utf-8 -*-
"""
Created on Sat Jul  4 23:24:43 2020

@author: BryaN
"""


M = int(input("Enter your marks"))
grade=""
if M>= 90:
   grade="A"
elif ((M>=85) and (M<=89)):
   grade="A-"
elif ((M>=80) and (M<=84)):
   grade="B+"
elif ((M>=75) and (M<=79)):
   grade="B"
elif ((M>=70) and (M<=74)):
   grade="B-"
elif ((M>=65) and (M<=69)):
   grade="C+"
elif ((M>=60) and (M<=64)):
   grade="C"
elif ((M>=57) and (M<=59)):
   grade+"c-"
elif ((M>=55) and (M<=56)):
   grade="D+"
elif ((M>=52) and (M<=54)):
   grade="D"
elif ((M>=50) and (M<=51)):
   grade="D-"
else:
   grade="F"
print(grade)
    