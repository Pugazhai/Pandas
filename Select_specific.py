import pandas as pd
import numpy as np

df = pd.read_csv("Datasets/churn.csv")
print(df.head())

print(df.State)

df.State_No = 1
print(df.State_No)

print(df.columns)

print(type(df.State))

#using loc and iloc

print(df.loc[0:4,'State':'Area Code'])

#Now dot iloc

print(df.iloc[[0,1,2],[1,2,3]])#one way
print(df.iloc[1:3,0:2])#Another Way


#at and iat
print(df.at[1,"Account Length"])

print(df.iat[1,1])

