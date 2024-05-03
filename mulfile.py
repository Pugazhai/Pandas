import pandas as pd
df = pd.read_csv("Datasets\churn.csv")
df2 = []
df2.append(df.iloc[:,1:3].head())
df2.append(df.iloc[:,3:4].head())
print(df2)
print(pd.concat(df2))
"""   Account Length  Area Code     Phone
0           128.0      415.0       NaN
1           107.0      415.0       NaN
2           137.0      415.0       NaN
3            84.0      408.0       NaN
4            75.0      415.0       NaN
0             NaN        NaN  382-4657
1             NaN        NaN  371-7191
2             NaN        NaN  358-1921
3             NaN        NaN  375-9999
4             NaN        NaN  330-6626"""
