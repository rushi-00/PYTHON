# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 16:37:18 2024

@author: SATYAM
"""
#Exception Handeling
try:
    numerator=50
    denom=int(input("enter the denominator : "))
    quotient=(numerator/denom)
    print(quotient)
    print("Division performed successfully")
except ZeroDivisionError:
    print("oh this is divide by zero error . not allowed")
print("OUTSIDE try..except block")


try:
    numerator=50
    denom=int(input("Enter the denominator : "))
    print(numerator/denom)
    print("Division performed successfully")
except ZeroDivisionError:
    print("denominator as zero is not allowed")
except ValueError:
    print("only INTEGERS should be entered")
    

#Handling Exception without naming the exception

try:
    numerator=50
    denom=int(input("Enter the denominator : "))
    print(numerator/denom)
    print("Division performed successfully")
except ValueError:
    print("only INTEGERS should be entered")
except :
    print("OOPS .......some exception raised")
 

#Handling exception using try...except....else
try:
    numerator=50
    denom=int(input("Enter the denominator : "))
    quotient=(numerator/denom)
    print("Division performed successfully")
except ValueError:
    print("only INTEGERS should be entered")
except :
    print("OOPS .......some exception raised")
else:
    print("The result of division operation is " , quotient)
    
#Handling exception using try...except....else...finally
try:
    numerator=50
    denom=int(input("Enter the denominator : "))
    quotient=(numerator/denom)
    print("Division performed successfully")
except ValueError:
    print("only INTEGERS should be entered")
except :
    print("OOPS .......some exception raised")
else:
    print("The result of division operation is " , quotient)
finally:
    print("OVER AND OUT")
