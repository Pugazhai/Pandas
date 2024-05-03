import pandas as pd
import numpy as np

df = pd.read_csv("Datasets/churn.csv")
print(df.head())

#Learning Query and Eval
q1 = df.query("State in ('KS','OH') and `VMail Plan` == 'yes' ")
print(q1)

min_day_calls = 120
q2 = df.query("State in ('KS','OH') and `Day Calls` > @min_day_calls")

print(q2)

#Eval
q1 = df.eval("State in ('KS','OH') and `Day Calls` > @min_day_calls")
print(q1)
#it returns the boolean musk
print(df.loc[q1,:])

df.eval("minites = 0",inplace=True)
print(df)
