import pandas as ps
import numpy as np
df = pd.read_csv('datasets\census.csv')
df = df[df['SUMLEV']==50]
df.head()

%%timeit -n 3
for state in df['STNAME'].unique():
    avg = np.average(df.where(df['STNAME']==state).dropna()['CENSUS2010POP'])
    print("counties in state " + state +
         "have an avergae population of " + str(avg))
    
%%timeit -n 3
for group, frame in df.groupby('STNAME'):
    avg = np.average(frame['CENSUS2010POP'])
    print("counties in state " + group +
         "have an avergae population of " + str(avg))

df = df.set_index('STNAME')
def set_batch_number(item):
    if item[0]<'M':
        return 0
    if item[0] < 'Q':
        return 1
    return 2
for group, frame in df.groupby(set_batch_number):
    print('There are ' + str(len(frame) + "records in group "+ str(grp)+ "for processing"))
    
df = pd.read_csv('datasets/listings.csv')
pd.head()

for group, frame in df.groupby(level=(0,1)):
    print(group)
    
def grouping_fun(item):
    if item[1] == 10.0:
        return (item[0], "10.0")
    else:
        return (item[0], "not 10.0")
for group, frame in df.groupby(by = grouping_fun):
    print(group)
df.head()

#aggregation
# we can pass a dictionary of columns we are interested in aggregating along with the function we are looking to aggregate
df = df.reset_index()
df.groupby("cancellation policy").agg({"reveiw_scoers_value":np.average})


df.groupby("cancellation policy").agg({"reveiw_scoers_value":np.nanmean})

#transformation
# transform() returns an object that is the same size as the group. 
cols = ['cancellation_policy','reveiw_scores_value']
transform_df = df[cols].groupby("cancellation policy").transform(np.nanmean)
transform_df.head()


#filtering
# The filter() function takes in a function which it applies to each group dataframe and returns either a true or false, 
# depending on whether that group should be included in the result.
df.groupby('cancellation_policy').filter(lambda x: np.nanmean(x['reveiw_scores_value'])>9.2)

#applying
#this allows you to apply an arbitrary function to each group and stitch the results back for each apply() into a single 
# dataframe where the index is preserved.
df = pd.read_csv('datasets/listings.csv')
df = df[['cancellation_policy','reveiw_scores_value']]
df.head()