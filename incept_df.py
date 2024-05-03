import pandas as pd
import numpy as np

df = pd.read_csv("https://raw.githubusercontent.com/albayraktaroglu/Datasets/master/churn.csv")
print(df)

#Finding the rows and columsn in the dataset
print(df.shape)

print(df.head(6))

print(df.tail(10))

#finding the data types in all types of columns
print(df.info())

#Finding the memory usages of the each column
print(df.memory_usage(deep=True))

#print only the data types
print(df.dtypes)

#finally change the types of the columns and datas
#check the it is not working properly
df['Churn?'] = df['Churn?'].astype('int')
print(df.info())
print(df.head(10))
