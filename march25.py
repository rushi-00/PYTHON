
#Itertools 
lst=[]
for num in range(0,10):
    lst.append(num)
print(lst)

#list comprehension [interveiw]
#we can write same method using list comprehension
#code optimization
lst=[num for num in range (0,10)]
print(lst)


# [ name_of_list.capitalize() for name in names]
names = ["dada" , " mama" , "kaka"]
lst=[name.capitalize() for name in names]
print(lst)

#list comprehension using if statement
def is_even(num):
    return num%2==0
lst=[num for num in range(10) if is_even(num)]
print(lst)


lst=[f"{x}{y}" for x in range (5) for  y  in range(5)]
print(lst)

#Dictionary comprehension
#use {} base
#business logic left hand side
dict={x : x*x for x in range(3)}
print(dict)

#Generator
#It is another way of creating iterators in a simple way where it uses the keyword "yeild"
#allows to return multiple values

gen=(x for x in range(3))
print(gen)
for num in gen:
    print(num)
    

#function that returns multiple values
def range_even(end):
    for num in range(0, end , 2):
        yield num
for num in range_even(6):
    print(num)
    
#now instead of using for loop we can write our own generator

gen=range_even(6)
next(gen)
next(gen)

#chaining generators
def lengths(itr):
    for ele in itr:
        yield len(ele)
def hide(itr):
    for ele in itr:
        yield ele*'*'
        
        
'''
"ele*" appears to be a placeholder for an element from an 
iterable.The asterisk(*) is likely jsut a  character used to represent a placeholder or a wildcard
for instance, if you re iterating over a list of elements,
"ele*" could symbolize any element in that list.
Its a generic representation that dosent correspond to any specific syntax in python or itertools
'''

passwords=["not-good" , "give'm-pass" , "00100=100"]

for passwords in hide(lengths(passwords)):
    print(passwords)
    
def length(itr):
    for ele in itr:
        yield len(ele)
def hide(itr):
    for ele in itr:
        yield ele*"*"

li=[]
passwords=input("enter your password :")
li.append(passwords)
for passwords in hide(length(li)):
    print(passwords)
    
#Enumerate 
#printing list with index
lst=["milk" , "egg" , "bread"]
for index in range(len(lst)):
    print(f'{index+1} {lst[index]}')
    
#same code can be implemented using enumerate
lst=["milk" , "egg" , "bread"]
for index, item in enumerate(lst,start=1):
    print(f"{index}  {item}")
    
    
#use of zip function
#access 2 list using zip function
#zip is important for machine learning
name=['dada' , 'mama' , 'kaka']
info=[3232,2543,6543,7652]
for nm,inf in zip(name,info):
    print(nm,inf)
    
#use of zip function with mismatch item in name
#i.e : baba

name=['dada' , 'mama' , 'kaka' , 'baba']
info=[3232,2543,6543]
for nm,inf in zip(name,info):
    print(nm,inf)
#it will not display excess mismatch item in name
    

    
#zip longest
from itertools import zip_longest
name=['dada' , 'mama' , 'kaka' , 'baba']
info=[3232,2543,6543]
for nm,inf in zip_longest(name,info):
    print(nm,inf)
    
#use of all(), if all the values are 
#true then it will produce output
lst=[2,3,-6,8,9]
if all(lst):
    print('all values are true')
else:
    print('there are null values')

lst=[2,3,0,8,9]
if all(lst):
    print('all values are true')
else:
    print('there are null values')
    
#use of any
lst=[0,0,0,0,0]
if any(lst):
    print('It has some value')
else:
    print('all values are zero in the list')
    

#count()
#not frequently used , but still a usefull concept in ml
from itertools import count
counter=count()
print(next(counter))
print(next(counter)) 
print(next(counter))

#count from 1
from itertools import count
counter=count(start=1) 
print(next(counter))
print(next(counter)) 
print(next(counter))

#cycle()
#suppose you have repeated tasks to be done, then you
import itertools

instructions=("eat" , "game" , "sleep")
for intruction in itertools.cycle(instructions):
    print(intruction)
    
#repeat()
#if you want to repeat a sentence many times use repeat().
from itertools import repeat
for msg in repeat("keep patience", times=3):
    print(msg)

#combinations()
from itertools import combinations
players=['john' , 'jani','janardhan']
for i in combinations(players,2):
    print(i)
    
from itertools import combinations
players=['john' , 'jani','janardhan' , 'dhoni' , 'rajwardhan' 'virat' , 'rohit' , 'shami']
for i in combinations(players,2):
    print(i)
    
#permutations
from itertools import permutations
players=['john' , 'jani','janardhan']
for seat in permutations(players,2):
    print(seat)
    
#product
from itertools import product
teama=['john' , 'jani','janardhan']
teamb=['ani' , 'aki' , 'yashi']
for pair in product(teama,teamb):
    print(pair)
                             
                                                                                                                                                                                                      
#Assignment operation
#this will create a new variable with the same reference
list_a = [1,2,3,4,5]
list_b=list_a

list_a[0] = -10
print(list_a)
print(list_b)



    