import pandas as pd
import numpy as np

df = pd.read_csv("Datasets/hungary_chickenpox.csv")
print(df)

print(df.drop(columns="Date"))
#max_case = df.drop(columns="Date").apply(lambda x : print(x),axis='columns')
print("After using drop method")
max_case = df.drop(columns="Date").apply(np.max,axis='columns')
print(max_case)

#using the for  loop options
result = []
for i,row in enumerate(df.iterrows()):
    result.append(np.max(row[1][1:]))
print(result[:5])

print(df.drop(columns="Date").apply(np.median,axis='rows'))
