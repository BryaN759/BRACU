# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 16:39:40 2020

@author: BryaN
"""


def hard1(*args):
    count=0
    while count<len(args):
        from datetime import datetime
        tday=datetime.today().date()
        jday=datetime.strptime(args[count+2],'%Y-%m-%d').date()
        dif=tday-jday
        tld=dif.days
        if tld<1826:
            x=(args[count+1]*0.1)
        elif tld>=1826 and tld<=3652:
            x=(args[count+1]*0.1)+5000
        else:
            x=(args[count+1]*0.15)+15000
        print(args[count],":",x)
        count+=3
while True:
    n=input("Enter your name: ")
    #user has to input 'Exit' or 'Done' to stop the program
    if n == "Exit" or n == "Done":
        break
    s=float(input("Enter your salary: "))
    d=input("Enter your joining date(yyyy-mm-dd): ") 
    hard1(n,s,d)