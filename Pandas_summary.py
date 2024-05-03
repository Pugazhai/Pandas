import pandas as pd
df = pd.read_csv('Datasets/churn.csv')
print(df)

#Describing the data to print mean, median 25 quartile to 75 quartile min and max
print(df.describe())

from pandas_summary import DataFrameSummary 
dfs = DataFrameSummary(df)
print(dfs.columns_stats)

#provides more information about the catrgorical datas
print(dfs['State'])

#for numerical data use the following method
print(dfs["Account Length"])
