# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 08:14:52 2024

@author: rushi

"""

#drop column

import pandas as pd
import numpy as np                      

new_tech3={
      'courses':["python","java","c++","DBMS","Pandas","oracal"],
      'fee':[20000,30000,23000,40000,60000,23000],
      'duration':["30days","40days","55days","25days","90days","45days"],
      "Discount":[2.5,3.6,4.4,5.5,6.7,7.3]}
row_labe=['r1','r2','r3','r4','r5','r6']
df6=pd.DataFrame(new_tech3,index=row_labe)

#####################
#using Explicitly parameter name "labels"

df2=df6.drop(labels=["fee"],axis=1)
df2


#######################
#alternate you can aslo use column instead of label

df7=pd.DataFrame(new_tech3,index=row_labe)
df3=df7.drop(columns=["courses"],axis=1)
df3

#############################
#drop column using index

print(df7.drop(df7.columns[1],axis=1))

###################################

new_tech4={
      'courses':["python","java","c++","DBMS","Pandas","oracal"],
      'fee':[20000,30000,23000,40000,60000,23000],
      'duration':["30days","40days","55days","25days","90days","45days"],
      "Discount":[2.5,3.6,4.4,5.5,6.7,7.3]}
row_labe=['r1','r2','r3','r4','r5','r6']
df6=pd.DataFrame(new_tech4,index=row_labe)

df=pd.DataFram(new_tech4)

###################################

#using inplace=True

df.drop(df.columns[2],axis=1,inplace=True)
print(df)

#####################################


#Drop multiple columns by label name


new_tech6={
      'courses':["python","java","c++","DBMS","Pandas","oracal"],
      'fee':[20000,30000,23000,40000,60000,23000],
      'duration':["30days","40days","55days","25days","90days","45days"],
      "Discount":[2.5,3.6,4.4,5.5,6.7,7.3]}

aa=pd.DataFrame(new_tech6)

aa1=aa.drop(["courses","fee"],axis=1)
aa1


##################################################

#drop multiple columns by using index value

new_tech6={
      'courses':["python","java","c++","DBMS","Pandas","oracal"],
      'fee':[20000,30000,23000,40000,60000,23000],
      'duration':["30days","40days","55days","25days","90days","45days"],
      "Discount":[2.5,3.6,4.4,5.5,6.7,7.3]}

aa2=pd.DataFrame(new_tech6)
drop1=aa2.drop(aa2.columns[[1,2]],axis=1)
drop1

#####################################################

#droping lists of columns


new_tech7={
      'courses':["python","java","c++","DBMS","Pandas","oracal"],
      'fee':[20000,30000,23000,40000,60000,23000],
      'duration':["30days","40days","55days","25days","90days","45days"],
      "Discount":[2.5,3.6,4.4,5.5,6.7,7.3]}

aa3=pd.DataFrame(new_tech7)

listofcolumn=["fee","duration"]
df2=aa3.drop(listofcolumn,axis=1)
print(df2)



#####################################################
#iloc ,loc is imp =============[interview]



new_tech1={
      'courses':["python","java","c++","DBMS","Pandas","oracal"],
      'fee':[20000,30000,23000,40000,60000,23000],
      'duration':["30days","40days","55days","25days","90days","45days"],
      "Discount":[2.5,3.6,4.4,5.5,6.7,7.3]}
row_labe=['r1','r2','r3','r4','r5','r6']
df=pd.DataFrame(new_tech1,index=row_labe)
print(df)


#iloc = using index
#in slicing no need to give coma but in iloc it is need to give coma
#syntax =df.iloc[startrow:endrow , startcolumn : endcolumn]

df2=df.iloc[ : , 0:2]
df2

df2=df.iloc[1:5 , 2:4]
df2

df2=df.iloc[2] #select row by index
df2

df2=df.iloc[[1,2,4]]  #select Rowa by index list
df2

df2=df.iloc[1:5] #select rows by integer index Range
df2

df2=df.iloc[:1]  #select first row
df2
 
df2=df.iloc[:3]  #select first 3 row
df2
 
df2=df.iloc[-1:]  #select last rows
df2

#rows by name[index lables] we use loc

df2=df.loc['r2']
df2

df2=df.loc[['r1','r2','r3']]
df2

df2=df.loc['r1' : 'r2']
df2

#----------------------------------------------------------
#loc with column

df2=df.loc[:,["courses", "fee","duration"]]
df2

df2=df.loc[:,["courses" , "fee"]]
df2

df2=df.loc[:,"duration" :]
df2

#select columns by range
#all the columns upto 'duration'

df2=df.loc[:,:"courses"]
df2

#select every alternate column
df2=df.loc[:,::2]
df2

#pandas.dataframe.query() by examples
#query all rows with courses equals 'spark'
df2=df.query("courses=='spark'")
print(df2)


