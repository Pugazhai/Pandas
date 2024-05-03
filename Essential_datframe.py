import pandas as pd
df = pd.read_csv("Datasets/churn.csv")
print(df.head())

#find the unique of the column
print(df['State'].unique())

print("Number of unique values : ")
print(df['State'].nunique())

print("Value Count of the column")
print(df['State'].value_counts())



print("Value Count of the column with Normalize")
print(df['State'].value_counts(normalize=True))

print("Value Count of the column with Normalize to check")
print(df['State'].value_counts(normalize=True).sum())

#sorting the first 5 largest count
print(df.nlargest(5,"Account Length"))


#Droping the collunns
print("Dropping the columns")
df.drop(columns="Churn?",inplace=True)
print(df.head())

print("Dropping the row index")
print(df.drop(index=[0,1,2]))

print("Transposing the Dataset")
print(df.T)
print(df.T.info())
