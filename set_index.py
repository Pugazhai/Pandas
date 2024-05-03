import pandas as pd
import numpy as np

df  = pd.read_csv("Datasets/hungary_chickenpox.csv")
print(df)

#setting the index
df.set_index('Date',inplace=True)
print(df)

#Setting the index to  the column names

#df['Date'] = df.index
#print(df)

#using the insert method to insert the columns in desiered postion
df.insert(0,'date',df.index)
print(df)

#reseting the index values

print(df.reset_index())
