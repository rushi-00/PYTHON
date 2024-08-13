# -*- coding: utf-8 -*-
"""
Created on Fri Apr 12 09:07:34 2024

@author: rushi
"""

import pandas as pd
import numpy as np

new_tech1={
      'courses':["python","java","c++","DBMS","Pandas","oracal"],
      'fee':[20000,30000,23000,40000,60000,23000],
      'duration':["30days","40days","55days","25days","90days","45days"],
      "Discount":[2.5,3.6,4.4,5.5,6.7,7.3]}
df=pd.DataFrame(new_tech1)


#add new column to the dataframe using .assign() method

tutors=['ram','sham','ghansham','sai','ganesh',None]
df2=df.assign(tutor=tutors)
df2

#adding multiple columns in dataframe

student=['rj','rushi','akash','aniket','pranit','abhishek']
tutors=['ram','sham','ghansham','sai','ganesh',None]
breaak=[12,12,12,2,2,2]

df2=df.assign(breaks=breaak,tutor=tutors,student=student)
df2

#derive new column from existing column
df = pd.DataFrame(new_tech1)
df2 = df.assign(after_discount=lambda x:x.fee*x.Discount/100)
print(df2)

#append the column to existing pandas dataframe
#add new colummn to existing dataframe

df = pd.DataFrame(new_tech1)
df["new_tutors"] = tutors
print(df)


#adding column in any location

df=pd.DataFrame(new_tech1)
tutors=['ram','sham','ghansham','sai','ganesh',None]
df.insert(1,"new_tutor",tutors)

#counting rows and columns in a dataframe
#IMP FOR INTERVIEW 10/10 asked question

row_count=len(df.index)
row_count
row_count=len(df.axes[0])
row_count
column_count=len(df.axes[1])
column_count

#---------------------------------------------------
df=pd.DataFrame(new_tech1)
row_count=df.shape[0]        #return no.of rows 
row_count
col_count=df.shape[1]       #return no.of cols
print(row_count)
print(col_count)

#pandas apply function to a column
#below are quick examples
#using dataframe.apply() to apply function add column

import pandas as pd
import numpy as np

data={"a":[1,2,3],
      "b":[4,5,6],
      "c":[7,8,9]
      }

df=pd.DataFrame(data)
print(df)

def add(x):
    return x+3
df2=df.apply(add)
df2

df2=((df.a).apply(add))
df2

#using apply function to single column
def add(x):
    return x+4
df["b"]=df["b"].apply(add)
df["b"]

#apply to multiple columns

df[['b','c']]=df[['b','c']].apply(add)
df

#apply lambda function to single column

df['a']=df['a'].apply(lambda x:x-2)
print(df)

#using pandas.Dataframe.transform() to apply function column
#using dataframe.transform()

def add(x):
    return x+2
df=df.transform(add)
print(df)

#Using pandas.dataframe.map() to single column

df['a']=df['a'].map(lambda A: A/2)
print(df)

#using numpy function on single column
#using dataframe.apply() & [] operator

df=pd.DataFrame(data)
import numpy as np
df['a']=df['a'].apply(np.square)
print(df)


#pandas groupby() with examples

new_tech1={
      'courses':["python","java","c++","DBMS","Pandas","oracal"],
      'fee':[20000,30000,23000,40000,60000,23000],
      'duration':["30days","40days","55days","25days","90days","45days"],
      "Discount":[2.5,3.6,4.4,5.5,6.7,7.3]}
row_labe=['r1','r2','r3','r4','r5','r6']
df=pd.DataFrame(new_tech1,index=row_labe)
print(df)

df2=df.groupby(["courses"]).sum()
df2


#pandas shuffle dataframe rows

import pandas as pd
new_tech1={
      'courses':["python","java","c++","DBMS","Pandas","oracal"],
      'fee':[20000,30000,23000,40000,60000,23000],
      'duration':["30days","40days","55days","25days","90days","45days"],
      "Discount":[2.5,3.6,4.4,5.5,6.7,7.3]}

df=pd.DataFrame(new_tech1)
print(df)

#pandas shuffle Dataframe rows
#shuffle the dataframe rows and return all rows

df1=df.sample(frac=1)
print(df1)


df1=df.sample(frac=0.1)
print(df1)

#create a new index starting from zero
df1=df.sample(frac=1).reset_index()
print(df1)

#drop shuffle index
df1=df.sample(frac=1).reset_index(drop=True)
df1


new_tech1={
      'courses':["python","java","c++","DBMS","Pandas","oracal"],
      'fee':[20000,30000,23000,40000,60000,23000],
      'duration':["30days","40days","55days","25days","90days","45days"]
      }
      
row_labe=['r1','r2','r3','r4','r5','r6']
df=pd.DataFrame(new_tech1,index=row_labe)

new_tech2 = {
    'courses' : ['python' , 'pandas' , 'c++' , 'javascript'],
    'Discount' : [1200,2334,3455,6543]
    }

row_labe2=['r1','r6','r3','r5']
df2=pd.DataFrame(new_tech1,index=row_labe)

#pandas join

df3=df.join(df2,lsuffix="_left",rsuffix="_right")
print(df3)

#pandas inner join dataframes
df3=df.join(df2,lsuffix="_left",rsuffix="_right",how="inner")
print(df3)

#left join
df3=df.join(df2,lsuffix="_left",rsuffix="_right",how="left")
print(df3)

#right join
df3=df.join(df2,lsuffix="_left",rsuffix="_right",how="right")
print(df3)


#using pandas.merge()
df3=pd.merge(df1,df2)
print(df3)

#using dataframe.merge()
df3=df1.merge(df2)
print(df3)

#use pandas.concat() to concat two dataframes
import pandas as pd
df = pd.DataFrame({'courses':["python","java","c++","DBMS","Pandas","oracal"],
      'fee':[20000,30000,23000,40000,60000,23000]})

df1 = pd.DataFrame({'courses' :['pandas' , 'hadoop' , 'hyperion' , 'java'],
                    'fee' : [23333,23342,64545,13234]})

#using pandas.concat() to concat two dataframes
data=[df,df1]
df2=pd.concat(data)
df2


#concat multiple dataframe using pandas.concat
df = pd.DataFrame({'courses':["python","java","c++","DBMS","Pandas","oracal"],
      'fee':[20000,30000,23000,40000,60000,23000]})

df1 = pd.DataFrame({'courses' :['pandas' , 'hadoop' , 'hyperion' , 'java'],
                    'fee' : [23333,23342,64545,13234]})

df2=pd.DataFrame({'duration':["30days","40days","55days","25days","90days","45days"],
                  "Discount":[2.5,3.6,4.4,5.5,6.7,7.3]})

#-----------------------------------------------------


#Write dataframe to excel file
import pandas as pd
df = pd.read_excel("E:/DATA SCIENCE 24/1-Python/Python_for_data_science/Sample.xlsx")
print(df)


#-----------------------------------------------------------------
new_tech1={
      'courses':["python","java","c++","DBMS","Pandas","oracal"],
      'fee':[20000,30000,23000,40000,60000,23000],
      'duration':["30days","40days","55days","25days","90days","45days"],
      "Discount":[2.5,3.6,4.4,5.5,6.7,7.3]}
df=pd.DataFrame(new_tech1)
col_list = df.courses.values
print(col_list)

#using series.value.tolist()

col_list = df.courses.values.tolist()
print(col_list)

#using series.values.tolist()
col_list = df["courses"].values.tolist()
print(col_list)

#using list functiob
col_list = list(df["courses"])
print(col_list)

#convert to numpy array
import numpy as np
col_list = df['courses'].to_numpy()
print(col_list)



