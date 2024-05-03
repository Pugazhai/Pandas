import pandas as pd
import numpy as np

df = pd.read_csv("Datasets/churn.csv")
print(df.head())

#Row Boolean Mask
print(df['Account Length'] > 100)

#Column Boolean mask
colfmsk = df.columns.str.startswith('I')
print(colfmsk)


#Filter 1 and 2
filter1 = df["Account Length"] > 100
filter2 = df["Night Calls"] < 90

print(df.loc[filter1 & filter2,:])


print(df.loc[(filter1 | filter2),colfmsk])

#Where conditions
print(df.where(filter1 & filter2))

#in where if the conditons is false then it  returns nan and it can fill by filna
print(df.where(filter1 & filter2).fillna(0))

#Dropping the values
print(df.where(filter1 & filter2).dropna())


