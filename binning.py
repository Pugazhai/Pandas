import pandas as pd
import numpy as np

df = pd.read_csv('Datasets/hungary_chickenpox.csv')
print(df.head())

#Devide the dataset into 4 groups
print(pd.qcut(df['BUDAPEST'],q=4))

df['BUDAPEST_Q'] = pd.qcut(df['BUDAPEST'],q=4,labels=['Low','Medium','High','Very High'])
print(df)

#using the cut method
print(pd.cut(df['BUDAPEST'],bins=[0,10,50,100,1000]))

print(pd.cut(df['BUDAPEST'],bins=[0,10,50,100,1000],labels=[1,2,3,4]))

#using the value count
print(pd.cut(df['BUDAPEST'],bins=[0,10,50,100,1000],labels=[1,2,3,4]).value_counts())
