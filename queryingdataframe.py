# a boolean mask is an array where eahc value consists of true or false.
import pandas as pd
df = pd.read_csv('datasets/Admission_Predict.csv', index_col = 0)
df.columns = [x.lower().strip() for x in df.columns]
df.head()

admit_mask = df['chance of admit'] > 0.7
admit_mask

df.where(admit_mask).head()
df.where(admit_mask).dropna().head()

#they created a shorthand syntax using where() and dropna() both at once.
df[df['chance of admit'] > 0.7].head()
#it can be called with a string parameter to project a single column
df["gre score"].head()

df["gre score","toefl score"].head()
df[df['gre score'] > 320].head()
