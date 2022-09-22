import pandas as pd
import numpy as np

#timestamp
pd.Timestamp('21/09/2022 12:02 pm')

pd.Timestamp(2019, 12, 20, 0, 0).isoweekday()

pd.Timestamp(2019, 12, 20, 0, 20).second

#period
pd.Period('1/2016')

pd.Period('3/5/2016')

pd.Period('1/2016') + 5

#datetime index and period index
t1 = pd.Series(list('abc'), [pd.Timestamp('2016/09/01'), pd.Timestamp('2016/09/02'), pd.Timestamp('2016/09/03')])
t1

type(t1.index)

t2 = pd.Series(list('def'), [pd.Timestamp('2016/09'), pd.Timestamp('2016/10'), pd.Timestamp('2016/11')])
t2

#converting to datetime
d1 = ['2nd june 2013', '4th july, 2014', '205-06-09', '7/12/16']
ts3 = pd.DataFrame(np.random.randint(10, 100, (4,2)), index = d1, columns = list('ab'))
ts3

ts3.index = pd.to_datetime(ts3.index)
ts3

pd.to_datetime('4.7.12', dayfirst = True)

#timedeltas
pd.Timestamp('9/3/2016') - pd.Timestamp('9/1/2016')

#offset
pd.Timestamp('9/4/2016')+ pd.offsets.Week()
pd.Timestamp('9/4/2016')+ pd.offsets.MonthEnd()