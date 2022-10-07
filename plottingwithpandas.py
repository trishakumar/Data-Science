import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
%matplotlib notebook

plt.style.available
plt.style.use('seaborn-colorblind')

np.random.seed(123)
df = pd.DataFrame({'A':np.random.randn(365).cumsum(0),
                  'B':np.random.randn(365).cumsum(0) + 20,
                  'C':np.random.randn(365).cumsum(0) - 20},
                  index = pd.date_range('1/1/2017', periods = 365))
df.head()
df.plot()

df.plot('A','B', kind = 'scatter')

df.plot.scatter('A', 'C', c = 'B', s = df['B'], colormap = 'viridis')

ax = df.plot.scatter('A', 'C', c = 'B', s = df['B'], colormap = 'viridis')
ax.set_aspect('equal')

df.plot.box();

df.plot.hist(alpha = 0.7);

df.plot.kde(); #kernel density estimation

iris = pd.read_csv('iris.csv')
iris.head()

pd.tools.plotting.scatter_matrix(iris);

plt.figure()
pd.tools.plotting.parallel_coordinates(iris, 'Name');

