import pandas as pd
import numpy as np

nrow = 10000
arr = np.random.randint(0,100,(nrow,3))
df = pd.DataFrame(arr,columns=['A','B','C'])
print(df.head())

#.at and .iat
def hypotenuse(a,b):
    return np.sqrt(a^2 + b^2)

#using .at
for i in range(nrow):
    A = df.at[i,'A']
    B = df.at[i,'B']
    df.at[i,'C'] = hypotenuse(A,B)
print(df.head())

#using .iat
for i in range(nrow):
    A = df.iat[i,0]
    B = df.iat[i,1]
    df.iat[i,2] = hypotenuse(A,B)
print(df.head())


#vectorization method df['C']
df['C'] = np.sqrt(df.loc[:,'A']^2 + df.loc[:,'B']^2)

print(df.head())

#which is faster > vectorization > at > iat >loc >iloc
