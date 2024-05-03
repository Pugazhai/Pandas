import pandas as pd
import numpy as np

df = pd.read_csv("Datasets/churn.csv")
print(df.head())

print(df.drop_duplicates('State'))

print(df.drop_duplicates(subset=['State','Area Code']))
