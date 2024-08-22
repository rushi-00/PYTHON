# -*- coding: utf-8 -*-
"""
Created on Fri Apr  5 08:11:58 2024
@author: rushi

"""
#Properties


import pandas as pd


new_tech1={
      'courses':["python","java","c++","DBMS","Pandas","oracal"],
      'fee':[20000,30000,23000,40000,60000,23000],
      'duration':["30days","40days","55days","25days","90days","45days"],
      "Discount":[2.5,3.6,4.4,5.5,6.7,7.3]}
row_labe=['r1','r2','r3','r4','r5','r6']
df=pd.DataFrame(new_tech1,index=row_labe)

############################################

#shape
#Number of columns and number of rows in datafream called as shape

df.shape

        #(row,col)
#output : (6, 4)

#####################################################

df.size

#output :24

#####################################################

df.columns         #Display Columns name

######################################################

df.columns.values


#######################################################

df.index          #display index values

######################################################

df.dtypes           #Display the dataTypes

########################################################

df.info             #information

########################################################

#Accessing one column content :
    
df['fee']                   #write in string form

########################################################

#Accessing two or more columns

df[['fee','courses']]

##########################################################

cols=['fee','courses']
df[cols]


##########################################################

#df[rows cols]
#df[ :  : ]
#select certain rows and assing it to another dataframe

df2=df[ :2]    #0,1 (row) it not take 2
df2

########################################################### 

df[:6]

###########################################################

#Accessing certain cell from column:
df['duration'] [2]

###########################################################

#substracting specific value from a column

df['fee'][2]=df['fee'][2]+1000000
df['fee'][2]
df['fee']


############################################################

#.describe()

#it will show 5 number summary
#only numarical data 
#mean
#sd
#median

df.describe()

#output : 
'''  
                fee  Discount
count  6.000000e+00  6.000000
mean   3.585000e+05  5.000000
std    8.057667e+05  1.843909
min    1.500000e+04  2.500000
25%    1.975000e+04  3.800000
50%    3.000000e+04  4.950000
75%    5.000000e+04  6.400000
max    2.003000e+06  7.300000

'''


###################################################################

#rename the column

new_tech2={
      'courses':["python","java","c++","DBMS","Pandas","oracal"],
      'fee':[20000,30000,23000,40000,60000,23000],
      'duration':["30days","40days","55days","25days","90days","45days"],
      "Discount":[2.5,3.6,4.4,5.5,6.7,7.3]}
row_labe=['r1','r2','r3','r4','r5','r6']
df=pd.DataFrame(new_tech2,index=row_labe)

###############################################

#first way
df.columns=["A","B","C","D"]
df

###############################################
#second way

df2=df.rename({'A':'a1',"B":'b2'},axis=1)
df2

################################################
#third way

df3=df.rename({'A':'a1',"B":'b2'},axis='columns')
df3

##################################################
#fouth Way

df4=df.rename(columns={'C':'zz',"D":'b2'})
df4

##################################################################

#drop DataFrame Row and Column
#for column axis=0
#for row axis=1

new_tech2={
      'courses':["python","java","c++","DBMS","Pandas","oracal"],
      'fee':[20000,30000,23000,40000,60000,23000],
      'duration':["30days","40days","55days","25days","90days","45days"],
      "Discount":[2.5,3.6,4.4,5.5,6.7,7.3]}
row_labe=['r1','r2','r3','r4','r5','r6']
df5=pd.DataFrame(new_tech1,index=row_labe)

########################

#
#drop row by lable

df5=df5.drop(['r1','r2'])
df5

#########################

# drop row by its position / index

df6=df5.drop(df5.index[2])
df6

#########################

# drop row by its position / index

df6=df5.drop(df5.index[[1,5]])
df6

########################

#delete row by index range

df1=df5.drop(df.index[2:])
df1

########################
#when you have default indexes for row

df10=pd.DataFrame(new_tech1,index=row_labe)

df11=df10.drop(0) 
df11

#######################

df11=df.drop([0,3],axis=0) #it will delete row0  n row3



####################################################################
