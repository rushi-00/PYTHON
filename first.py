print("data science")
a=5
if(a%2==0):
    print("even")
else:
    print("odd")
    
x=20
y=40

z=x+y
print (z)  

#string
age=input("please enter your age :")
print(type(age))
print(age)

"""Data type is by default string.If the input type is not changed string concatination can happen to avoid that user can change to input function to the datatype into int
If User wants input as a int then user needs to change input function to int
This is called type casting"""

#int

age1=int(input("please enter your age :"))
print(type(age1))
print(age1)

age2=int(input("please enter your age :"))
print(type(age2))
print(age2)

age3=age1+age2
print(age3)

#-------------------------------------------------------------
#Float 

int_value = 100
string_value='1.5'
float_value = float(int_value)
print("int value as a float : " , float_value)
print(type(float_value))
float_value = float(string_value)
print("string value as a float : ", float_value)
print(type(float_value))

#-------------------------------------------------------------
#complex numbers

c1 = 1
c2 = 2j
print('c1 :' , c1 , 'c2 : ' , c2)
print(type(c1))
print(type(c2))
print(c1.real)
print(c2.imag)

#boolean value

all_ok = True
print(all_ok)
all_ok = False
print(all_ok)
print(type(all_ok))


status = bool(input("ok it is confirmed. "))
print(status)
print(type(status))

#-------------------------------------------------------

home = 10
away = 15
print(home + away)
print(type(home + away))
print(10 * 4)
print(type(10*4))
goals_for =  10
goals_against = 7
print(goals_for - goals_against)
print(type(goals_for - goals_against))

#---------------------------------------------------

a=5
b=3
print(a**b)

'''Assignments operators are actually referred to as compound operators as they combine together a 
numeric operation with the assignment operator.'''

x=0
x +=1
print(x)

#none value
#python has a special type
#the Nonetype,with a single value, None.
winner=None
print(winner is None)
#Alternatively you can aslo write:
print(winner is not None)
#Which will print true 

#indentation 
num = int(input('enter a number : '))
if num>0:
    print(num)


#else in an if statement
num=int(input('enter yet another number: '))
if num<0:
    print('the number is negative')
else:
    print('the number is positive')
   
#use of elif
savings=float(input('enter how much savings do you have : '))
if savings == 0:
    print('no savings')
elif savings < 500:
    print('less savings')
elif savings < 1000:
    print('decent amount of savings')
elif savings < 5000:
    print('lots of savings')
else:
    print('Welcome')

#while loop exists in almost all programming languages and it used to 
#iterative on or more code statements as long as the test conditions is True

count = 1
print('starting')
while count<=10:
    print(count)
    count+=1

#for loop
#loop over a set of values in a range

print('print out values in a range')
for i in range(2,10):
    print(i)
    print('done')
  
print('only print code if all iterations completed')
num = int(input('enter a number to check for: '))
for i in range(1,20):
    if i ==num:
        break
    print(i)
print("done")


#Anonymous variable
#it does not require any memory allocation
#represented by _ 

for _ in range(0,10):
    print('.......',end='********')
    print()

#python program to print odd numbers in given range

start, end = 4, 19

#iterating each number in list
for num in range(start, end + 1):
    #checking condition
    if num % 2 != 0:
        print(num , end = ' ')

#for even number
       
start, end = 0,100

for num in range(start,end + 1):
    
    if num %2 ==0:
        print(num , end = ' ')
        




    