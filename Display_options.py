import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randint(1,100,(80,25)))
print(df)

#Reset
pd.reset_option("display.max_rows")
pd.reset_option("display.max_columns")
pd.reset_option("display.precision")
pd.reset_option("display.float_format")

print(pd.options.display.max_rows)
print(pd.options.display.max_columns)

#setting the options
pd.set_option("display.max_rows",100)
pd.set_option("display.max_columns",30)
print(df)


#precision

arr = np.random.rand(10)
df = pd.DataFrame(arr)
print(df)

pd.set_option("display.precision",3)
print(df)

#change float formate
pd.set_option("display.float_format",'{:.2f}F'.format)
print(df)
