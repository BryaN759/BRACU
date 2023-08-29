# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 23:15:47 2020

@author: BryaN
"""
#hard3
import string
ul=list(string.ascii_uppercase)
uc=0
ll=list(string.ascii_lowercase)
lc=0
dl=list(string.digits)
dc=0
sl=["_","$","#","@"]
sc=0
p=input("Enter your password: ")
for i in p:
    if i in ul:
        uc+=1
    elif i in ll:
        lc+=1
    elif i in dl:
        dc+=1
    else:
        sc+=1
if uc>0 and lc>0 and dc>0 and sc>0:
    print("OK")
elif uc>0 and lc>0 and dc>0 and sc==0:
    print("Special character missing")
elif uc>0 and lc>0 and dc==0 and sc>0:
    print("Digit is missing")
elif uc>0 and lc==0 and dc>0 and sc>0:
    print("Lowercase character missing")
elif uc==0 and lc>0 and dc>0 and sc>0:
    print("Uppercase character is missing")
elif uc==0 and lc>0 and dc==0 and sc>0:
    print("Uppercase character, Digit missing")
elif uc>0 and lc==0 and dc==0 and sc>0:
    print("Lowercase character, Digit missing")
elif uc>0 and lc>0 and dc==0 and sc==0:
    print("Digit, Special character missing")
elif uc>0 and lc==0 and dc>0 and sc==0:
    print("Lowercase character, Special character missing")
elif uc==0 and lc>0 and dc>0 and sc==0:
    print("Uppercase character, Special character missing")
elif uc==0 and lc==0 and dc>0 and sc>0:
    print("Uppercase character, Lowercase character missing")
elif uc==0 and lc==0 and dc==0 and sc>0:
    print("Uppercase character,Lowercase character,digit missing")
elif uc>0 and lc==0 and dc==0 and sc==0:
    print("Lowercase character,Digit,Special character missing")
elif uc==0 and lc>0 and dc==0 and sc==0:
    print("Uppercase character,Digit,Special character missing")
elif uc==0 and lc==0 and dc>0 and sc==0:
    print("Uppercase character,Lowercase character,Special character missing")
else:
    print("kisu na deyar mane ki?")
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    