import pandas as pd
import numpy as np

df = pd.read_csv("Datasets/titanic.csv")
df.head()

df["Fare_Mean"] = df.groupby("Pclass")["Fare"].transform('mean')
print(df)

df["Sum_of_allFare"] = df.groupby("Pclass")["Fare"].transform("sum")
print(df)

#cross tabulations
col = df["Pclass"]
row = df["Survived"]
print(pd.crosstab(row,col))

print(pd.crosstab(row,col,margins=["row",'col']))

print(pd.crosstab(row,col,normalize=True))

