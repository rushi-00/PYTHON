# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 08:05:43 2024

@author: SATYAM


class Human:
    def __init__(self , n, o):
        self.name=n
        self.occupation = o
        
    def do_work(self):
        if self.occupation == 'tennis player':
            print(self.name, 'plays tennis')
        elif self.occupation == 'actor':
            print(self.name, 'shoots films')
            
    def speaks(self):
        print(self.name,'says how are you?')
        
tom = Human('tom cruise' , 'actor')
tom.do_work()
tom.speaks()

#INHERITANCE

class Vehicle:
    def general_usage(self):
        print("general use:tranportation")
        
class Car(Vehicle):
    def __init__(self):
        print("I am car")
        self.wheels = 4
        self.has_roof = True
        
    def specific_usage(self):
        self.general_usage()
        print("specific use: comute to work, vacation with ")
        
class MotorCycle(Vehicle):
    def __init__(self):
        print("i am motorcycle")
        self.wheels = 2
        self.has_roof = False
        
    def specific_usage(self):
        self.general_usage()
        print("specific use:local commutation, racing")
        
c = Car()
m = MotorCycle()
c.specific_usage()
m.specific_usage()
    
"""

#multiple inheritance

class Father():
    def skills(self):#this aint a constructor
        print(" i like gardening and teaching")
        
class mother():
    def skills(self):#this aint a constructor
        print(" i like cooking and shopping")
        
class son(Father,mother):
    def skills(self):
        Father.skills(self)
        mother.skills(self)
        print(" i like sports")
        
s=son()
s.skills()


    