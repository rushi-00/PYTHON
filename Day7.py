# -*- coding: utf-8 -*-
"""
Created on Fri Apr 19 09:28:21 2024

@author: rushi
"""

#create numpy array
from numpy import empty
a = empty([3,3])
print(a)

'''[[0.0000e+000 0.0000e+000 0.0000e+000]
 [0.0000e+000 0.0000e+000 1.8636e-320]
 [0.0000e+000 0.0000e+000 0.0000e+000]]
'''

#create zero array
from numpy import zeros
a = zeros([3,5])
print(a)
'''[[0. 0. 0. 0. 0.]
 [0. 0. 0. 0. 0.]
 [0. 0. 0. 0. 0.]]'''

#create one array
from numpy import ones
a = ones([5])
print(a)
#[1. 1. 1. 1. 1.]

#create array with vstack(vertical)
from numpy import array
from numpy import vstack

a1=array([1,2,3])
print(a1)

a2=array([4,5,6,])
print(a2)

a3=vstack((a1,a2))
print(a3)
print(a3.shape)


#create array with hstack(horizontal)
from numpy import array
from numpy import hstack

a1=array([1,2,3])
print(a1)

a2=array([4,5,6,])
print(a2)

a3=hstack((a1,a2))
print(a3)
print(a3.shape)









