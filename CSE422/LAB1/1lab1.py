# -*- coding: utf-8 -*-
"""
Created on Fri Jun 24 17:04:38 2022

@author: BryaN
"""

with open('1input1.txt', 'r') as file:
   lines = file.readlines()
mtx=[]
for line in lines:
    #print(line)
    for word in line:
        x = line.split()
    mtx.append(x)

#print(mtx)

def regSize(matrix,row,column,vis,l):
    #size=0
    if [row,column] not in vis:
        l.append(0)
        for r in range(-1, 2):
            for c in range(-1,2):
                if row+r < 0 or column+c < 0 or row+r >= len(matrix) or column+c >= len(matrix[0]) or matrix[row+r][column+c] == 'N':  # check if out of bound
                    False
                else:
                    if [row+r,column+c] not in vis:
                        vis.append([row+r,column+c])
                       #size+=1
                        l[-1]+=1
                        #print(l)
                    else:
                        for i in range(len(l)-1):
                            l[i]+=1
                            #print(l)
def findMaxReg(matrix):
    l=[]
    vis=[]
    for row in range(len(matrix)):
        #print(len(matrix[row]))
        for column in range(len(matrix[row])):
            if matrix[row][column]=='Y':
               regSize(matrix,row,column,vis,l)
    print(max(l))




findMaxReg(mtx)