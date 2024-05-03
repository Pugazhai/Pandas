import pandas as pd
import numpy as np
import os

df = pd.read_csv("Datasets/hungary_chickenpox.csv")
print(df)

print(df.describe())

def Zscore(x):
    return ((x-np.mean(x))/np.std(x))

f = df.drop("Date",axis='columns').apply(Zscore,axis='rows')
print(f)
