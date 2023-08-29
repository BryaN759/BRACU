# -*- coding: utf-8 -*-
"""
Created on Tue Sep 15 01:17:17 2020

@author: BryaN
"""


class Student:
    ID=0
    def __init__(self,name,department,age,cg):
        self.name=name
        self.department=department
        self.age=age
        self.cg=cg
    def get_details(self):
        Student.ID+=1
        print("Name: ",self.name)
        print("Department: ",self.department)
        print("Age: ",self.age)
        print("CGPA: ",self.cg)
    def from_string(self,s):
        self.s.split('-')
        self
        
        
s1 = Student("Samin", "CSE", 21, 3.91)
s1.get_details()
print("-----------------------")
s2 = Student("Fahim", "ECE", 21, 3.85)
s2.get_details()
print("-----------------------")
s3 = Student("Tahura", "EEE", 22, 3.01)
s3.get_details()
print("-----------------------")
s4 = Student.from_String("Sumaiya-BBA-23-3.96")
s4.get_details()
print()
print('instance variables can have different values for each instance of the' 
      ' class, whereas class variables are the same across all instances.')
print()
print("Instance methods need a class instance and can access the instance"
     " through self . Class methods don't need a class instance. They can't" 
     " access the instance ( self ) but they have access to the class itself" 
     " via ( cls ) .")