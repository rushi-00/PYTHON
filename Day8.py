# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 08:18:42 2024

@author: rushi
"""

from numpy import array
#define matrix
A = array([
    [1,2],
    [3,4],
    [5,6]])
print(A)

C=A.T
print(C)

#-----------------------------------------------------
#inverse matrix
from numpy import array
from numpy.linalg import inv
A=array([
    [1.0 , 2.0],
    [3.0,4.0]])
print(A)

B=inv(A)
print(B)

#multiply A and B
I = A.dot(B)
print(I)

#------------------------------------------------------
#sparse matrix

from numpy import array
from scipy.sparse import csr_matrix
#create dense matrix

A=array([
    [1,0,0,1,0,0],
    [0,0,2,0,0,1],
    [0,0,0,2,0,0]])
print(A)

#convert to sparse matrix (CSR matrix)
S = csr_matrix(A)
print(S)

#Reconstruct dense matrix
B = S.todense()
print(B)






