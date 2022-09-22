import pandas as pd
df = pd.DataFrame(['A+','A','A-','B+','B','B-','C+','C','C-','D+','D-'],
                 index = ['excellent', 'excellent', 'excellent',  'good', 'good', 'good', 'ok','ok', 'ok', 'poor', 'poor'],
                 columns = ['Grades'])
df

df.dtypes

df['Grades'].astype('category').head()

my_categories = pd.CategoricalDtype(categories = ['D-','D+','C-','C','C+','B-','B','B+','A-','A','A+'], ordered = True)
df['Grades'].astype(my_categories).head()

df[df['Grades']>'C']

import numpy as np
df = pd.read_csv('datasets/census.csv')
df = df[df['SUMLEV']==50]
pd.cut(df,10)

