# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 12:22:15 2020

@author: BryaN
"""

#hard2
ddd={'.':'1',',':'11','?':'111','!':'1111',':':'11111','a':'2','b':'22','c':'222','d':'3','e':'33','f':'333','g':'4','h':'44','i':'444','j':'5','k':'55','l':'555','m':'6','n':'66','o':'666','p':'7','q':'77','r':'777','s':'7777','t':'8','u':'88','v':'888','w':'9','x':'99','y':'999','z':'9999',' ':'0'}
n=input("Enter your string: ").lower()
#print(ddd)
#nl=list(n)
#print(nl)
l=[]
for  i in n:
    l.append(ddd.get(i))
x="".join(l)
print(x)