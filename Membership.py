import pandas as pd
import numpy as np

df = pd.read_csv("Datasets/churn.csv")
print(df.head())

#isin between ~ any all
filter1 = df.State.isin(["KS","OH"])
print(df.loc[filter1,:].head())

filter1 = ~df.State.isin(["KS","OH"])
print(df.loc[filter1,:].head())

filter2 = df['Day Mins'].between(100,120)
print(df.loc[filter2,:])

#using any and all
test = pd.DataFrame(np.random.randint(0,2,(2,12)),
                    columns = ["ID"+str(i) for i in range(1,13)],
                    index = ["Samples1","Samples2"])
print(test)
print(test.all())
print(test.any())
