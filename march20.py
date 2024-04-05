# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 08:29:54 2024

@author: Rushi
"""
x,y,z = 5,6,7
print(x)
print(y)
print(z)
x,y,z = 5,6,7
print(x)
print(y)
print(z)

#global variables

x="awesome"
def my_function():
    x="fantastic"
    print("python is "+x)
my_function()

#global and local variable
x="awesome"
def my_function():
    x="fantastic"
    print("python is "+x)
my_function()

#dictionary

x=range(6)
print(type(x))
x={"name":"Rumshi"}
print(type(x)) 
a=2
z=a+3j
print(type(z))   

#
x=1
z=float(x)
print(z)

str1="hello"
str2=2
str3=str1+str2

#here you will get error:can only concatenate str not int 

#multiple strings
x="""Aniket is Gay"""
print(x)

#string slicing
x="""Elvish bhai ke aage koyi bol sakta hai kya"""
print(x[3:20])

#slicing from the start
print(x[:3])

#slicing at the end
print(x[4:])

#negative indexing

print(x[-5:-2])

#modify string
print(x.upper())

x=x.upper()
print(x.lower())

#remove white space, removes white spaces from initial to start of string 

x=" This is python"
print(x.strip())

print(x.replace("python","anaconda"))
#split
print(x.split(","))

x="hello world"
string1=x[:: -2]
print(string1)


x="THIS IS PYTHON AND IT IS VERY POWERFULL"
print(x.find("AND"))

x="hello"
y="world"
print(x+y)

print(x+ " "+y)


x=34
y="my name is rushi"
print(x+y)
#it will give error

print(f"my name is rushi and my age is {x}")

###################
quantity=3
item_no=54
price=67
print(f"I want {quantity} peices and item number is {item_no}, its price is {price}")


my_order="I want{} pieces and item number is{}, its price is {}"
print(my_order.format(quantity,item_no,price))

quantity=3
item_number=54
price=67

my_order="I want{1} pieces and item number is{1}, its price is {15}"
print(my_order.format(quantity,item_no,price))

quantity=3
item_no=54
price=67



#the escape character allows you to use double quotes when
text="this is funfair and it has got big \"round rigo\""
print(text)


a=20
b=10
print(a!=b)

print(3*3+3/3-3)

"""
Rule for mathematical operations
PEMDAS
P:paranthesis
E:Exponential
M:Multiplication
D:Division
A:Addition
S:Subtraction
"""

#identity operators
print(a is b)
print(a is not b)


#python list

lst=["cheery","banana","apple"]
print(lst)


print(lst[0])
print(lst[2])


#append() adds an element at the end of the list
lst=["cheery", "banana","apple"]
lst.append("mango")
print(lst)

#clear removes all the elemens from the list
lst=["cheery", "banana","apple"]
lst.clear()
print(lst)

#copy() method
lst=["cheery", "banana","apple"]
lst2=lst.copy()
print(lst2)


#Features of list
#mixed datatypes 
#mutable datatypes

#count() return the number of times the value "cheery" has occured
lst=["cheery","cheery","banana"]
lst.count("cheery")

#extend() Add the element to cars to the fruits 
lst=[1,2,3]
lst1=[4,5,6]
lst.extend(lst1)
print(lst)


#insert method, insert the value in the list
lst=["cheery","cheery","banana"]
lst.insert(1 , "mango")
print(lst)

#pop() method , removes element from a specified position
lst=["cheery","cheery","banana"]
lst.pop(2)
print(lst)

#remove() method , removes the item with the specified value from the list
lst=["cheery","cheery","banana"]
lst.remove("banana")
print(lst)

#reverse method , change the order of the list in reverse order
lst=["cheery","cheery","banana"]
lst.reverse()
print(lst)

#sort() sort the list alphabetically
lst=["cheery", "orange","watermelon"]
lst.sort()
print(lst)


#tuples
tup=("cheery","cheery","banana")
print(tup)
print(tup[2])

#once a tuple is created, you cannot change the value of the tuple
x=("apple" , "banana","cheery")
x[1]="kiwi"
 
y=list(x)
y[1]="kiwi"
 
#convert list to tuple
x=tuple(y)
print(x)


#To join two or more tuples you can use the +operator
tuple1 = ("a" , "b" , "c")
tuple2 = (1 ,2 ,3)
tup1=tuple1+tuple2
print(tup1)


#Dictionary
dict1={"brand" : "Audi" , "model" : " rs7", "colour": "black" , "year" : 2023}
print(dict1)
print(len(dict1))
print(type(dict1))


dict={
      "Brand":["Maruti" , "Mahindra", "Toyota"],
      "Model":["a", "b" ,"c"],
      "Year":[2011 , 2013 , 2022]
      }
print(dict)


car = {
 "brand" : "ford",
 "model" : "Mustang",
 "year" : 1963
 }
      
x=car.keys()
print(x)
car["color"]="white"
car
x=car.keys()
print(x)

#Removing the dictionary element
car = {
 "brand" : "ford",
 "model" : "Mustang",
 "year" : 1963
 }

car.pop("model")
print(car)

#Accessing keys in the dictionary

for x in car:  
    print(x)    #accessing  key
  
for x in car:
    print(car[x])  #accessing value
    
#if you want to acceses both key and value

for key , value in car.items():
    print("%s == %s" %(key, value))
    
    
#copying distionary

car = {
 "brand" : "ford",
 "model" : "Mustang",
 "year" : 1963
 }
car2=car.copy()
car2
 
#another way to copy
 
thisdict = {
 "brand" : "ford",
 "model" : "Mustang",
 "year" : 1963
}

dict1=dict(thisdict)
dict1

#A dictionary can contain dictionaries,
#this is called nested dictionaries.

our_family={
    "child1" : {
        "Name" : "pranit",
        "Dob" : "08-09-2003"
        },
    "child2" : {
        "Name" : "Akash",
        "DOB" : "01-01-2000"
        
        }
    
    }

#Clear() method : Remove all elements
car = {
 "brand" : "ford",
 "model" : "Mustang",
 "year" : 1963
 }
car.clear()
car

#fromkey()
#create a dictionary with 3 keys
x={'key1' , 'key2' , 'key3'}
y=0
thisdict=dict.fromkeys(x,y)
thisdict


#get() : to get the value of dictionary
car = {
 "brand" : "ford",
 "model" : "Mustang",
 "year" : 1963
 }
car.get("model")

#displays all the items in the dictionary
car = {
 "brand" : "ford",
 "model" : "Mustang",
 "year" : 1963
 }
car.items()

#display the value of the pair not the key
car = {
 "brand" : "ford",
 "model" : "Mustang",
 "year" : 1963
 }

car.values()

#update(): Insert an item to the dictionary
car = {
 "brand" : "ford",
 "model" : "Mustang",
 "year" : 1963
 }
car.update({"color" : "black"})
car

#for loop

fruits=["apple" , "banana" , "orange"] #this is a list
for i in fruits:
    print(i)
    
    
#use of break statement    
fruits=["apple" , "banana" , "orange"] #this is a list
for i in fruits:
    if(i=="banana"):
        break
    print(i)
    
    
#continue statement

fruits=["apple" , "banana" , "orange"] 
for x in fruits:    
    if x == "banana":
        continue
    print(x)
    
    
for x in range(2,30,3):
    print(x)    
    
    
#nested loop(loop inside loop)

colors=["green" , "red" , "yellow"]
fruits=["guava" , "apple" , "banana"]    
for x in colors:
    for y in fruits:
        print(x,y)
        