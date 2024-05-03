import numpy as np
import pandas as pd

#Creating a Numpy Array or List
#np.random.seed(100)
arr = np.random.randint(0,100,(5,3))
print(arr)

#Converting to DataFrame
df = pd.DataFrame(arr)
print(df)

#type of the dataset
print(type(df))

#Naming the rows and columns
rowname = ["Mon","Tue","wed","Thu","Fri"]
colname = ["jan","Feb","Mar"]

df = pd.DataFrame(arr,index=rowname,columns=colname)
print(df)


#Creating the Dataframe from the dictonaries
mydict = {
    "Name" : ['Ravi','Ram','Ragul'],
    "CGPA" : [10,9.5,8.6]
    }
df = pd.DataFrame(mydict,index=[1,2,3])
print(df)

#Specifying the order of the data columns
df = pd.DataFrame(mydict,index=[1,2,3],columns=['CGPA',"Name"])
print(df)

#Reading the Data From the Files
path = "Datasets/ToothGrowth.csv"
df = pd.read_csv(path)
print(df)

print(df.head())
print(df.tail())

#To find the no of rows and columns
print(df.shape)

# to change the dataset to numpy objects
print(df.values)

#read the values in the txt documnet
#df = pd.read_table(path,sep=",")

#Read the file direcctly from the github
print("Reading the File from the Github")
df = pd.read_csv("https://raw.githubusercontent.com/vincentarelbundock/Rdatasets/master/csv/datasets/ToothGrowth.csv")
print(df)

#Read the data from the clipboard
print("Reading the file from copyied clipboard")
df = pd.read_clipboard(sep=",")
print(df)

