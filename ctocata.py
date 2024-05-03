import pandas as pd
import numpy as np

df = pd.read_csv("Datasets/ToothGrowth.csv")
print(df.head())

#changing to catagorical data from object data
df['supp'] = df['supp'].astype('category')
print(df)
print(df.info())

print(df.supp.dtype)
#print(df.supp.codes)
