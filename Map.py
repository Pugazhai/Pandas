import pandas as pd
import numpy as np

df = pd.read_csv("Datasets/tips.csv")
print(df)

#This is one method which is used to create a new column
#df.loc[:,'Tipy'] = 2
#print(df)


#dfs = df.assign(tips_perc = lambda x : x^2, tips_pre_person = lambda x : x/2)

#Here using a map method to change the values of the columns
ctos = {'Female':'F','Male':'M'}
df['sex'] = df['sex'].map(ctos)
print(df)

#using the map method with lambda functions
df['ccno'] = 12345678
print(df)

print(df['ccno'].map(lambda x:"X"+str(x)[-4:]))

#with condtions
#print(df['ccno'].map(lambda x:"X"+str(x)[-4:] if lenstr(x) == 16 else 'XXX'))

#it apply the changes for all the fields and rows
print(df.applymap(lambda x : str(x).upper()[0] if str(x).isalpha() else x))


