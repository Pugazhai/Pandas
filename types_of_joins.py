#Types of jons
import pandas as pd
import numpy as np

df = pd.read_csv("Datasets/mtcars.csv")

df1 = df.head()
df2 = df.tail()
print(df1,df2)

print(pd.merge(df1,df2,on="gear", how="left"))

print(pd.merge(df1,df2,on="gear", how="right"))

print(pd.merge(df1,df2,on="gear", how="inner"))

print(pd.merge(df1,df2,on="gear", how="outer"))

print(df1.merge(df2,on="gear", how="left"))

#using the concate for rows and columns
print(pd.concat([df1,df2],axis='rows'))
print(pd.concat([df1,df2],axis='columns'))


#Representing the missing values using pandas and numpy
print(np.nan == np.nan)

print(np.nan)

print(pd.NA)

print(pd.NAT)

print(pd.NA == pd.NA)


print(pd.NAT == pd.Nat)

