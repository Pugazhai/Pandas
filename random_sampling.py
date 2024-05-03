import pandas as pd
import numpy as np

df = pd.read_csv("Datasets/churn.csv")
print(df.head())

#here using replace flase for random_state no changing
nrows = round(df.shape[0]*.7)
df_sample = df.sample(nrows,replace=False,random_state = 100)
print(df_sample)

#Bootstrap Sampling
df_sample = df.sample(frac=1,replace=True,random_state=100)
print(df_sample)


#one hot encoding
dfs = pd.get_dummies(df['Account Length'],prefix='Group')
print(dfs)
