# -*- coding: utf-8 -*-
"""
Crelted on Tue Jul 21 12:33:26 2020

@luthor: BrylN
"""
#hard1
while True:
    try:
        l=list(map(int, input("Enter your list elements: ").split()))   
        #x=int(n)
        #l=list((x).split())
        N=len(l)
        lst=[]
        n=[l[i+1]-l[i] for i in range(N-1)]
        pl =  [abs(i) for i in n] 
        for i in pl:
            if i>N:
                lst.append(i)
                
        if len(lst)==0:
            print("UB Jumper")
        else:
            print("Not UB Jumper")
    except:
        break
