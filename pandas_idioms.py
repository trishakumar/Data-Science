import pandas as pd
import numpy as np
import timeit
df = pd.read_csv('datasets/census.csv')
df.head()

(df.where(df['SUMLEV']==50))
    .dropna()
    .set_index(['STNAME','CTYNAME'])
    .rename(columns = {'ESTIMEBASE2010'='estimate base 2010'})
    
df = df[df['SUMLEV']==50]
df.set_index(['STNAME','CTYNAME'], inplace = True)
df.rename(columns = {'ESTIMEBASE2010'='estimate base 2010'})

def first_approach(): #first method
    global df
    return (df.where(df['SUMLEV']==50))
                .dropna()
                .set_index(['STNAME','CTYNAME'])
                .rename(columns = {'ESTIMEBASE2010'='estimate base 2010'})
df = pd.read_csv('datasets/census.csv')
timeit.timeit(first_approach, number = 10)

def second_approach():
    global df
    new_df = df = df[df['SUMLEV']==50]
    new_df.set_index(['STNAME','CTYNAME'], inplace = True)
    return new_df.rename(columns = {'ESTIMEBASE2010'='estimate base 2010'})
df = pd.read_csv('datasets/census.csv')
timeit.timeit(second_approach, number = 10)

def min_max(row):
    data = row[['POPESTIMATE2010',
               'POPESTIMATE2011',
               'POPESTIMATE2012',
               'POPESTIMATE2013',
               'POPESTIMATE2014',
               'POPESTIMATE2015']]
    return pd.Series({'min'=np.min(data), 'max'=np.max(data)})
df.apply(min_max, axis = 'columns').head()

def min_max(row):
    data = row[['POPESTIMATE2010',
               'POPESTIMATE2011',
               'POPESTIMATE2012',
               'POPESTIMATE2013',
               'POPESTIMATE2014',
               'POPESTIMATE2015']]
    
    row['max'] = np.max(data)
    row['min'] = np.min(data)
    return row
df.apply(min_max, axis = 'columns')

rows = ['POPESTIMATE2010','POPESTIMATE2011','POPESTIMATE2012','POPESTIMATE2013','POPESTIMATE2014','POPESTIMATE2015']
df.apply(lambda x: np.max(x[rows]),axis = 1).head()

def get_state_region(x):
    northeast = ['connecticut','maine','masachusets',' new hampshire','rhode island','vermont','new york','new jersey',
                'pennsylvania']
    midwest = ['illinois','indiana','michigan','ohio','wisconsin','iowa','kansas','minestota','missouri','nebraska',
              'south dakota','north dakota']
    south = []
    west = []
    if x in northeast :
        return 'northeast'
    elif x in midwest:
        return 'midwest'
    elif x in south :
        return 'south'
    else :
        return 'west'
    
    