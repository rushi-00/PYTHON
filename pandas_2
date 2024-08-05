# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 08:16:42 2024

@author: rushi

"""
#Pandas data frame ?
#two dimensional data structure
#an immutale .hetreogeneous tabular
#data structure with labeled axes rows and columns

import pandas as pd


#create using constructor
#create pandas Dataframe from list

technologies=[["Spark",20000,"30days"],["pandas",20000,"40days"]]
df=pd.DataFrame(technologies)
print(df)


########################################################################

#column name and row name  for DataFrame
#by defult it gives incremental order  of number 

column_name=["courses","fee","duration"]
row_lable=["a","b"]
df=pd.DataFrame(technologies,columns=column_name,index=row_lable)
print(df)


######################################################################

df.dtypes

######################################################################
#you can also assing the dat type to columns.

tech={
      'courses':["python","java","c++","DBMS","Pandas","oracal"],
      'fee':[20000,30000,23000,40000,60000,23000],
      'duration':["30days","40days","55days","25days","90days","45days"],
      "Discount":[2.5,3.6,4.4,5.5,6.7,7.3]}
index_name=["a","b","c","d","e","f"]
dd=pd.DataFrame(tech,index=index_name)
print(dd)

##########################################################################

#converting data type of columns :
df2=df.convert_dtypes(str)   #object=> string
print(df2.dtypes)



#change all columns into same type :
df=df.astype(str)  #string=>object
print(df.dtypes)


#changeing one or more columns
df=df.astype({"fee":int,"Discount":float})
print(df.dtypes)


####################################################################
#converting Data types for all Columns n a list

df=pd.DataFrame(tech)
df.dtypes
cols=["fee","Discount"]
df[cols]=df[cols].astype('float')
df.dtypes



################################################################
#ignores errors
df=df.astype({"courses":int},errors='ignore')
df.dtypes


################################################################
#converts feed column to numeric type using  [ to_numaric ] :'
#in this methon ot convert into float form not in int form

df=df.astype(str)
print(df.dtypes)
df['Discount']=pd.to_numeric(df['Discount'])
df.dtypes


################################################################


new_tech={
      'courses':["python","java","c++","DBMS","Pandas","oracal"],
      'fee':[20000,30000,23000,40000,60000,23000],
      'duration':["30days","40days","55days","25days","90days","45days"],
      "Discount":[2.5,3.6,4.4,5.5,6.7,7.3]}

################################################################

#to convert Data Frame into .csv file

df.to_csv("data_frame.csv")


################################################################

#pandas Data Frame= basic Operations
#explicit row name 

import pandas as pd
import numpy as np

new_tech1={
      'courses':["python","java","c++","DBMS",None,"Pandas","oracal"],
      'fee':[20000,30000,23000,40000,60000,np.nan,23000],
      'duration':["30days","40days","55days","25days","90days"," ","45days"],
      "Discount":[2.5,3.6,4.4,5.5,6.7,None,7.3]}
row_labe=['r1','r2','r3','r4','r5','r6','r7']
df=pd.DataFrame(new_tech1,index=row_labe)
print(df)

#Dataframe properties
df.shape
#(8,4)
df.size
#32
df.columns
df.columns.values
df.index
df.dtypes
df.info

#--------------------------------------------------------------------
#accessing one column contents
df['fee']
#accessing two columns contents
cols=['fee','duration']
df[cols]


#select certain rows and assign it to another dataframe
df2=df[6:]
df2=df[:6]
df2

#Accessing certain cell from column:
df['duration'] [2]

#subtracting specific value from a column

df['fee'][4]=df['fee']+10000000
df['fee'][4]

#pandas to manipulate dataframe
#describe dataframe
#describe dataframe for all numeric columns
df.describe
#It will show 5 numbers summary
#--------------------------------------------------------------------

#Rename()- renames pandas dataframe columns
df = pd.DataFrame(new_tech1, index=row_labe)
#assign new header by setting new column names.
df.columns=['A','B','C','D']
df



#rename column names using rename() method

df = pd.DataFrame(new_tech1, index=row_labe)
df.columns = ['A','B','C','D']
df2 = df.rename({'A' : 'c1' , 'B' : 'c2'}, axis=1)
df2 = df.rename({'C' : 'c3' , 'D' : 'c4'}, axis='columns')
df2 = df.rename(columns={'A' : 'c1' , 'B' : 'c2'})

#--------------------------------------------------------------------  
#Drop dataframe rows and columns
df = pd.DataFrames(new_tech1, index=row_labe)

#Drop rows by labels
df1 = df.drop(['r1','r2'])
df1
#Delete Rows by position/index
df1=df.drop(df.index[1])
df1
df1=df.drop(df.index[[1,3]])
df1

#delete rows by index range
df1=df.drop(df.index[2:])
df1

#when you have default indexes for row









