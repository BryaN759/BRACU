# -*- coding: utf-8 -*-
"""
Created on Sun Jul 26 13:03:09 2020

@author: BryaN
"""

#hard3
n,k=map(int,input("Enter number of members and championship: ").split())

while True:
    print("Enter the participation history of" ,n,"members")
    a=list(map(int,input("Here: ").split()))
    if len(a)==n:
        #print("Nice")
        l=[]
        for i in range(n):
            s=a[i]+k
            if s<=5:
                l.append(a[i])
        x=len(l)//3
        print(x)
        break
    else:
        print("invalid input.Enter again")
        continue
#print(n)
#print(k)
#print(a)