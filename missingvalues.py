#missing values are pretty common in data cleaning activities. If the missing value is an omission it is called
# **missing at random** if there are other variables that might be used to predict the variable which is missing. 
import pandas as pd
#sometimes missing values are not labeled clearly.
df = pd.read_csv('datasets/class_grades.csv')
df.head()

#we can use the function isnull() to crreate a boolean mask of the whole dataframe.This effectively broadcats the isnull()
# function to every cell of data.
mask = df.isnull()
mask.head(10)

#this can be useful for proecessing rows based on certain columns of data. dropna() function is used to drop all teh rows
#that have missing data. 
df.dropna().head(10)

# the filling function fillna() takes a number or parameters. 
df.fillna(0, inplace=True)
df.head(10)

#method parameter(). the two common fill values are ffill and bfill. ffill is for forward filling and it updates an na value 
# for a particular cell with the value for the previous row. bfill is for backward filling which is the opposite of forward 
#filling. it fills the missing values with the next valid value. 
df = df.set_index('time')
df = df.sort_index()
df.head(20)

df = df.reset_index()
df = df.set_index(['time','user'])
df.head(10)

df = df.fillna(method = 'ffill')
df.head()

import pandas as pd
df = pd.DataFrame({'A':[1,2,3],
                  'B':[4,5,6],
                  'C': ['a','b','c']})
df

df.replace([1,3],[100,300])