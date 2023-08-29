# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 12:16:57 2020

@author: BryaN
"""
def hard2(a):
    y=a//365
    m= (a%365)//30
    d=(a%365)%30
    if y<=1 and m>1 and d>1:
        p=str(y)+" year, "+str(m)+" months, "+str(d)+" days."
    elif y<=1 and m<=1 and d>1:
        p=str(y)+" year, "+str(m)+" month, "+str(d)+" days."
    elif y<=1 and m<=1 and d<=1:
        p=str(y)+" year, "+str(m)+" month, "+str(d)+" day."
    elif y>1 and m<=1 and d>1 :
        p=str(y)+" years, "+str(m)+" month, "+str(d)+" days."
    elif y>1 and m<=1 and d<=1:
        p=str(y)+" years, "+str(m)+" month, "+str(d)+" day."       
    elif y>1 and m>1 and d<=1:
        p=str(y)+" years, "+str(m)+" months, "+str(d)+" day."
    elif y<=1 and m>1 and d<=1:
        p=str(y)+" year, "+str(m)+" months, "+str(d)+" day."
    else:
        p=str(y)+" years, "+str(m)+" months, "+str(d)+" days."
    print(p)
days=int(input("Enter the number of days: "))
hard2(days)