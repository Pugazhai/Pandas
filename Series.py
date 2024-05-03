#importing the packages
import pandas as pd
import numpy as np

#creating the dataset using random function
df = pd.DataFrame(np.random.randint(1,100,(5,4)),columns=list("abcd"))
print(df)

#Extreacting the single column
print(df["a"])

#slicing the data from the single column
print(df["a"][0:3])

#to convert array values
print(df["a"][0:3].values)

# converting to list by method call tolist()
print(df["a"][0:3].values.tolist())

#Creating the Series Values
data = np.arange(10)
srr = pd.Series(data = data,name = "Numbers")
print(srr)

#set index also by the following of the DataFrame

print(type(srr))

#muliple the values in the Series
print(srr*2)

#Extract the particular element
print(srr[[1,5]])

#Extract the index of the Series
print(srr.index)
print(srr.keys())

#creating the series values using dictonaries
dict1 = {
    'a':2,'b':3
    }
dict2 = {
    'b':2,'c':3
    }
dict1 = pd.Series(dict1)
dict2 = pd.Series(dict2)
print(dict1)

#Adding the Values without dict.values
print(dict1+dict2)

#adding the values with dict.values
print(dict1.values+dict2.values)


#adding the elements with add function with fill values
print(dict1.add(dict2,fill_value=0))
