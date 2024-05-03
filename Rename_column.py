import pandas as pd
import numpy as np

#importing the Datasets
df = pd.read_csv("Datasets/churn.csv")
print(df)

#To know the column name
print("Listing the column name")
print(df.columns)

#Rename the certain column in differet formate
df.rename(columns={'Account Length' : "Account_Length"})
print(df.rename(columns={'Account Length' : "Account_Length"}))

#While we print the df ,it is stille unaffected to overcome this
df.rename(columns={"Account Length": "account_length"},inplace=True)
print("After using the inplace method\n",df)
print(df.columns)

#Replacin the every column name into unpper case or lower
print(df.rename(str.upper,axis='columns').head())

#Rename the column names using lambda functions
print(df.rename(lambda x: x.replace(' ','_'),axis='columns'))

#Challenge case to  change the columns name to title case
print(df.rename(lambda x : x.title() , axis='columns',inplace=True))
print(df.columns)

#my own challenge is to rename the index name
print("Renaming the columns names : \n")
print(df.rename(lambda x : x + 1,axis="index"))
