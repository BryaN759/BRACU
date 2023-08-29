# -*- coding: utf-8 -*-
"""
Created on Fri Jul 10 23:04:55 2020

@author: BryaN
"""
def easy2(h,w):
    return(w/(h/100)**2)
nh=int(input("Enter your height(in cm): "))
nw=int(input("Enter your weight(in kg): "))
bmi=easy2(nh,nw)
if bmi<18.5:
    print("Score is",("{:3.1f}".format(bmi))," You are Underweight")
elif bmi>=18.5 and bmi<=24.9:
    print("Score is",("{:3.1f}".format(bmi))," You are Normal")
elif bmi>=25 and bmi<=30:
    print("Your score is",("{:3.1f}".format(bmi))," You are Overweight")
else:
    print("Score is",("{:3.1f}".format(bmi))," You are Obese")