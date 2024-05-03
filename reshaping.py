#converting wide dataframe to long data frame
import pandas as pd
import numpy as np

df = pd.read_csv("Datasets/titanic.csv")
print(df.head())

df_melted = pd.melt(df,id_vars=['PassengerId',"Name"],value_vars = ["Survived","Pclass"])
print(df_melted)

df_pivot = pd.pivot(df_melted,index=['PassengerId',"Name"],columns=['variable'],values="value")
print(df_pivot)

#joining the Data Frame:

df_avgfare = df.groupby("Pclass").agg({"Fare":lambda x: np.round(np.mean(x),2)})
df_avgfare.rename(columns={"Fare" : "Avg_Fare"},inplace=True)
print(df_avgfare)

#using  the merge function
print(pd.merge(df,df_avgfare,on="Pclass"))

#using the transform method
print(df.groupby("Pclass")["Fare"].transform(np.mean))
