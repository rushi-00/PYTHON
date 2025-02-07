# -*- coding: utf-8 -*- 
"""
Created on Thu Apr 18 08:17:39 2024

@author: rushi
"""
#Array in NumPy
#create ndarray
import numpy as np
arr = np.array([10,20,30])
print(arr)

#multi-dimensional array
arr = np.array([10,20,30],[40,50,60])
print(arr)

#represent the minimum dimensions
#use ndmin param to specify how many minimum
#dimensions you wanted to create an array with minimum dimension

arr=np.array([10,20,30,40],ndmin=3)
print(arr)

#change the datatype
arr=np.array([10,20,30,40],dtype=complex)
print(arr)


#--------------------------------------------------------------
#get the dimensions of array

arr = np.array([[1,2,3,4],[5,5,6,3],[8,6,7,2]])
print(arr. ndim)
print(arr)

#finding the size of each item in the array
arr = np.array([10,20,30])
print("each item contain in bytes : " , arr.itemsize)

#get shape and size of array
arr = np.array([[1,2,3,4],[5,5,6,3],[8,6,7,2]])
print("array size : ", arr.size)
print("shape : ",arr.shape)

#create numpy array from list
#creation of arrays
arr = np.array([10,20,30])
print("array : ",arr)

#-----------------------------------------------------------------
#creating array from list with type float
arr = np.array([[1,2,3,4],[5,5,6,3],[8,6,7,2]],dtype=float)
print("array created using list : ",arr)

#creating sequence of integers using arrange()
#create a sequence of integers
#from 0 to 20 with steps of 3
arr=np.arange(0,20,3) 
#          (range = 0-20)
print(arr)

#array indexing in numpy
arr = np.array([10,20,30])

print(arr[-1])

#multi dimensional array indexing

arr = np.array([[1,2,3,4,56,23,23],[3,23,8,6,7,2,0]])
print(arr)

print(arr.shape)

print(arr[1,-1])
#0

print(arr[0,4])
#56

print(arr[1,1])
#23

#access array element using slicing
arr = np.array([0,1,2,3,4,5,6,7,8,9])
x=arr[1:8:3]
print(x)
# [1 4 7]

x=arr[-2:3:-1]
print(x)
#[8 7 6 5 4]

#indexing in numpy
multi_arr = np.array([[10,20,30,40],
    [40,50,70,90],
        [60,10,40,50],
    [30,60,90,10]])
multi_arr


#slicing array

multi_arr [1,2]
multi_arr[1,:]
multi_arr[:,1]

x=multi_arr[:3 , ::2]
print(x)

#interger array indexing

arr=np.arange(35).reshape(5,7)#vertical columns horizontal rows
print(arr)

#-----------------------------------------------------

import numpy as np
arr=np.arange(12).reshape(3,4)
print(arr)

#output
#[[ 0  1  2  3]
#[ 4  5  6  7]
#[ 8  9 10 11]]


rows=np.array([True,False,True])
rows
wanted_rows=arr[rows , : ]
print(wanted_rows)
#output
#[[ 0  1  2  3]
#[ 8  9 10 11]]

#------------------------------------------------------------------
list=[20,40,60,80]
array=np.asarray(list)
print(array)
print(type(array))
#output: array:[20 40 60 80]

#-----------------------------------------------------------------

#to get the shape of Numpy array use numpy

#Shape
array=np.array([[1,2,3],[4,5,6]])
array
print(array.shape)
#(2,3)

#anothe way
array=np.array([[1,2,3],[4,5,6]])
new=array.reshape(3,2)
print(new)

#---------------------------------------------------------------------
#adding of tow array
#.add()

arr1=np.arange(16).reshape(4,4)
arr2=np.array([1,2,3,4])
print(arr1)

add_arr=np.add(arr1,arr2)
print(f"Adding two arrays : \n{add_arr}")

sub_arr=np.subtract(arr1,arr2)
print(f"Subtracting two arrays : \n{sub_arr}")

mul_arr=np.multiply(arr1,arr2)
print(f"multiplying two arrays : \n{mul_arr}")

div_arr=np.divide(arr1,arr2)
print(f"dividing two arrays : \n{div_arr}")

#numpy.reciprocol()

#this function returns the reciprocal of argument
#element-wise.  for example with absolute values
#larger than 1, the result is always 0 because of the way in which

arr1=np.array([50,10.3,5,1,200])
rep_arr1=np.reciprocal(arr1)
print(f"after applying reciprocal function to array:\n{rep_arr1}")


#numpy .power()
arr1=np.array([3,10,5])
pow_arr1=np.power(arr1,3)
print(f"after applying power function to array:\n{pow_arr1}")


arr2=np.array([3,2,1])
print("My second array:\n",arr2)
pow_arr2=np.power(arr1,arr2)
print(f"after applying power function to array:\n{pow_arr2}")

#to perform mod function on numpy array
import numpy as pd
arr1=np.array([7,20,13])
arr2=np.array([3,5,2])
arr1
arr1.dtype

#mod()
mod_arr=np.mod(arr1,arr2)
print(f"after applying mod function to array:\n{mod_arr}")































