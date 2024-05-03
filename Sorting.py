import pandas as pd
import numpy as np

df = pd.read_csv("Datasets/churn.csv")
print(df.head())

#Sorting the following Datsets
print(df.sort_values(by = "Day Calls"))

#descendin calls
print(df.sort_values(by = "Account Length",ascending= False))

#performing for both the columns
print(df.sort_values(by = ['Day Calls','Account Length'],
                     ascending = [True,False]).loc[:,["Account Length","Day Calls"]])
