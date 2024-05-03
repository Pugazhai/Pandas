import pandas as pd
import numpy as np

#cat.codes
#cat.categories

ser = pd.Series(['a','b','c','d','a','b'],dtype='category')
print(ser)
print(ser.cat.categories)

ser = ser.cat.add_categories('missing')
print(ser)

#since missing is the unused catagories it should be delete
ser.cat.remove_unused_categories()
print(ser.cat.remove_unused_categories())

print(ser.cat.remove_categories('d'))
