# -*- coding: utf-8 -*-
"""
Created on Thu Aug  1 08:52:56 2024

@author: rushi
"""

import pandas as pd
import numpy as np
import matplotlib.pylab as plt

Univ1=pd.read_excel("C:/7-Clustering/University_Clustering.xlsx")
a=Univ1.describe()
a

Univ=Univ1.drop(["State"] , axis=1)
#we know that there is scale difference among the columns,
#which we have to remove
#either by using normalization or standardization
#whenever there is mixed data apply normalization

def norm_func(i):
    x=(i-i.min())/(i.max() - i.min())
    return x
#now apply this normalization function to Univ dataframe
#for all the rows and columms from 1 until end
#since 0 the column has university name hence skipped
df_norm=norm_func(Univ.iloc[:,1:])

#you can check the df_norm dataframe which is scaled
#between values from 0 to 1
#you can apply describe function to new data frame

b=df_norm.describe()

#Before you apply clustering, you need to plot dendrogram first 
# Now to create dendrogram, we need to measure distance,
#we have to import linkage

from scipy.cluster.hierarchy import linkage
import scipy.cluster.hierarchy as sch

#linkage function gives us hierarchical or aglomerative clustering
# ref the help for linkage

z=linkage(df_norm, method="complete" , metric="euclidean")
plt.figure(figsize=(15,8));
plt.title("Hierarchical Clustering dendrogram");
plt.xlabel("Index");
plt.ylabel("Distance")

sch.dendrogram(z,leaf_rotation=0,leaf_font_size=10)
plt.show()

#dendogram()
#appying agglomerative clustering choosing 5 as clusters from dendrogram

from sklearn.cluster import AgglomerativeClustering
h_complete=AgglomerativeClustering(n_clusters=3,linkage='complete' , metric='euclidean').fit(df_norm)

h_complete.labels_
cluster_labels=pd.Series(h_complete.labels_)

Univ['clust']=cluster_labels
#assign this series to Univ Dataframe as column and the column name
Univ1=Univ.iloc[:, [7,1,2,3,4,5,6]]

Univ1.iloc[:,2:].groupby(Univ1.clust).mean()



