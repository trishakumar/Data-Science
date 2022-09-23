import numpy as np
import pandas as pd
from scipy import stats

df = pd.read_csv('datasets/grades.csv')
df.head()

print("there are () rows and () columns",format(df.shape[0],df.shape[1]))
early_finishers = df[pd.to_datetime(df['assignment1_submission'])<'2016']
early_finishers.head()

late_finishers = df[-df.index.isin(early_finishers.index)]
late_finishers.head()
print(early_finishers['assignment1_grade'].mean())
print(late_finishers['assignment1_grade'].mean())

from scipy.stats import ttest_ind
ttest_ind(early_finishers['assignment1_grade'], late_finishers['assignmenr1_grade']
print(ttest_ind(early_finishers['assignment2_grade'], late_finishers['assignment2_grade'])
print(ttest_ind(early_finishers['assignment3_grade'], late_finishers['assignment3_grade'])
print(ttest_ind(early_finishers['assignment4_grade'], late_finishers['assignment4_grade'])
print(ttest_ind(early_finishers['assignment5_grade'], late_finishers['assignment5_grade'])
print(ttest_ind(early_finishers['assignment6_grade'], late_finishers['assignment6_grade'])

df1 = pd.DataFrame([np.random.random(100) for x in range(100)])
df2 = pd.DataFrame([np.random.random(100) for x in range(100)])
df2.head()
def test_columns(alpha = 0.1):
    num_diff = 0
    for col in df1.columns:
        teststat,pval = ttest_ind(df1[col],df2[col])
        if pval <= alpha:
            print("col () is statistically significantly different at alpha=(), pval=()",format(col,alpha,pval))
            num_diff = num_diff+1
    print("total number different was (), which is ()%",format(num_diff, float(num_diff)/len(df1.columns)*100))
test_columns()
    