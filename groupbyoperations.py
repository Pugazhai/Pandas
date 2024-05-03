import pandas as pd
import numpy as np

df = pd.read_csv("Datasets/titanic.csv")
print(df.head())



print(df.groupby("Pclass").agg({'Survived' : [np.mean,np.sum]}))



print(df.groupby(['Sex',"Pclass"]).agg({'Survived' : [np.mean,np.sum]}))

print(df.groupby(['Sex',"Pclass"]).agg({'Survived' : [np.mean,np.sum]}).reset_index())


print(df.groupby(['Sex',"Pclass"]).agg({'Survived': lambda x : np.max(x) - np.min(x) }))

#Using for loop for group by functions
print(df.Pclass)
print(df.Pclass.unique())
print("For loop group by class")
for name,group in df.groupby("Pclass"):
    print("Group Name : ",name)
    print(group,"\n")

#Calculating the logic with the group by functions
for name, group in df.groupby('Pclass'):
    print("Group Name : ",name)
    if name == 2:
        print(group.loc[(group.Sex != "male") & (group.Fare != 0),"Fare"].mean().round(2))
    
    else:
        print(group.Fare.mean().round(2))
#challenge
for name, group in df.groupby("Pclass"):
    print("Group Name : ",name)
    group = group.sort_values("Fare",ascending=False)
    print(group.loc[group.Sex == "female",["Name","Fare"]].head(),'\n\n')
