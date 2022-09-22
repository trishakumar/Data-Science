import pandas as pd
import numpy as np
df = pd.read_csv('datasets/cwurData.csv')
df.head()

def create_category(ranking):
    if (ranking>=1) & (ranking<=100):
        return "first tier university"
    elif (ranking>=101) & (ranking<=200):
        return "second tier university"
    elif (ranking>=201) & (ranking<=300):
        return"third tier university"
    else:
        return"other tier university"
df['Rank_level'] = df['world_rank'].apply(lambda x : create_category(x))
df.head()

df.pivot_table(values = 'score', index = 'country', columns = 'Rank_level', aggfunc=[np.mean]).head()
df.pivot_table(values = 'score', index = 'country', columns = 'Rank_level', aggfunc=[np.mean,np.max]).head()
df.pivot_table(values = 'score', index = 'country', columns = 'Rank_level', aggfunc=[np.mean,np.max],margins = True).head()

new_df = df.pivot_table(values = 'score', index = 'country', columns = 'Rank_level', aggfunc=[np.mean,np.max],
                        margins = True)
print(new_df.index)
print(new_df.columns)

new_df['mean']['first top tier university'].head()
type(new_df['mean']['first top tier university'].head())
new_df['mean']['first top tier university'].idxmax()

new_df.head()
new_df = new_df.stack()
new_df.head()
new_df.unstack().head()
new_df.unstack().unstack().head()