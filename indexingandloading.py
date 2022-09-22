!cats datasets/Admission_Predict.csv

import pandas as pd
df = pd.read_csv('datasets/Admission_Predict.csv')
df.head()

df = pd.read_csv('datasets/Admission_Predict.csv', index_col = 0)
df.head()

new_df = df.rename(columns = {})
new_df.head()

new_df.columns()
new_df = new_df.rename(columns = {"lor":"letter ishdugsh"})
new_df.head()

#strip() removes white spaces
new_df = new_df.rename(mapper = str.strip, axis = 'columns')
new_df.head()

df.columns

cols = list(df.columns)
cols = [x.lower().strip() for x in cols]
df.column = cols
df.head()