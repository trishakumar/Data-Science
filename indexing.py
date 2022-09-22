#the set_index() function is a destructive process and it doesnt keep the current index. 
#if you want to keep the index, you need to manually create a new column and copy into it values from the index attribute.
import pandas as pd
df = pd.read_csv('datasets/Admission_Predict.csv', index_col = 0)
df.head()

#we copy the indexed data into its own column
df['serial number'] = df.index
#then we set the index to another column
df = df.set_index('chance of admit')
df.head()

#we can get rid of the index completely by calling the function reset_index(). This promotes the index into a column and 
#creates a default numbered index
df = df.reset_index()
df.head()

#multi level indexing is similar to composite keys in relationcal database systems. We call set_index() and give it a list of 
#columns we are promoting to an index.
df = pd.read_csv('datasets\census.csv')
df.head()

df['SUMLEV'].unique()

df = df[df['SUMLEV']==50]
df.head()

columns_to_keep = ['']
df = df[columns_to_keep]
df.head()

df = df.set_index(['STNAME','COUNTNME'])
df.head()