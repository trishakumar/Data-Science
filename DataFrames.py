import pandas as pd
record1 = pd.Series({"name":"alice",
                    "class":"physics",
                    "score":85})
record2 = pd.Series({"name":"jack",
                    "class":"chem",
                    "score":82})
record3 = pd.Series({"name":"helen",
                    "class":"bio",
                    "score":90})

df = pd.DataFrame([record1,record2,record3], index = ["school1","school2","school1"])
df

students = [{"name":"alice",
            "class":"physics",
            "score":85},
           {"name":"jack",
            "class":"chem",
            "score":82},
            {"name":"helen",
                    "class":"bio",
                    "score":90}]
df = pd.DataFrame(students, index = ["school1","school2","school1"])
df.head()

#you can extract data using iloc and loc attributes
df.loc['school2']

type(df.loc['school2'])

df.loc['school1']

type(df.loc['school1'])

#you can select data based on multiple axes
df.loc['school1','name']

#transposing the matrix
df.T

df.T.loc['name']

#the result of a single projection is a series object
type(df['name'])

# we can chain operations together.
df.loc['school1']['name']

print(type(df.loc['school1']))
print(type(df.loc['school1']['name']))

#chaining tends to cause pandas to return a copy of the data frame instead of veiw on the data frame. It also makes it slower
df.loc[:,['name','score']]

#drop has 2 interesting optional parameters. the first is called inplace, and if its set to true, the dataframe will be
# updated in place instead of a copy being returned
#the second parameter is the axes, which should be dropped
copy_df = df.copy()
copy_df.drop("name",inplace = True, axis =1)
copy_df

del copy_df['class']
copy_df

df['classranking'] = None
df

