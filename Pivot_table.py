import pandas as pd
import numpy as np

df = pd.read_csv("Datasets/titanic.csv")

#pivoting the dataset
row = 'Survived'
col = 'Pclass'
val = 'Age'
pvt = df.pivot_table(index = row,columns = col,values=val,aggfunc = lambda x: np.mean(x))
print(pvt)
