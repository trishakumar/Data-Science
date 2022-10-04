%matplotlib notebook
import matplotlib as mpl
mpl.get_backend()
import matplotlib.pyplot as plt
plt.plot?

plt.plot(3,2)
plt.plot(3,2,'.')
from matplotlib.backends.backend_agg import FigureCanvasAgg
from matplotlib.figure import Figure

fig = Figure()
canvas = FigureCanvasAgg(fig)
ax = fig.add_subplot(111)
ax.plot(3,2,'.')
canvas.print_png('test.png')
%%html
<img src = 'test.png'/>
plt.figure()
plt.plot(3,2,'o')
ax = plt.gca()
ax.axis([0,6,0,10])
plt.figure()
plt.plot(1.5,1.5,'o')
plt.plot(2,2,'o')
plt.plot(2.5,2.5,'o')

ax = plt.gca()
ax.get_children()

#scatterplots
import numpy as np
x = np.array([1,2,3,4,5,6,7,8])
y = x
plt.figure()
plt.scatter(x,y)

import numpy as np
x = np.array([1,2,3,4,5,6,7,8])
y = x
colors = ['green']*(len(x)-1)
colors.append('red')
plt.figure()
plt.scatter(x,y, s=100, c = colors)

zip_generator = zip([1,2,3,4,5],[6,7,8,9,10])
list(zip_generator)

zip_generator = zip([1,2,3,4,5],[6,7,8,9,10])
x,y = zip(*zip_generator)
print(x)
print(y)

plt.figure()
plt.scatter(x[:2],y[:2], s =100, c = 'red', label = 'Tall students')
plt.scatter(x[2:],y[2:], s =100, c = 'blue', label = 'Short students')

plt.xlabel("the number of times the child kicked the ball")
plt.ylabel("the grade of the student")
plt.title("relationship between ball kicking and grades")

plt.legend()
plt.legend(loc = 4, frameon = False, title = 'Legend')
plt.gca().get_children()

legend = plt.gca().get_children()[-2]
legend.get_children()[0].get_children()[1].get_children()[0].get_children()
from matplotlib.artist import Artist
def rec_gc(art, depth = 0):
    if isinstance(art, Artist):
        print("  " * depth + str(art))
        for child in art.get_children():
            rec_gc(child,depth+2)
rec_gc(legend)

#lineplots
import numpy as np
linear_data = np.array([1,2,3,4,5,6,7,8])
quadratic_data = linear_data ** 2
plt.figure()
plt.plot(linear_data, 'o', quadratic_data, '-o')

plt.plot([22,44,55],'--r')

plt.xlabel('some data')
plt.ylabel('some other data')
plt.title('a title')
plt.legend(['baseline','competition','us'])

plt.gca().fill_between(range(len(linear_data)),
                      linear_data, quadratic_data,
                      facecolor = 'blue',
                      alpha = 0.25)

plt.figure()
observation_dates = np.arange('2017-01-01','2017-01-09', dtype = 'datetime64[D]')
plt.plot(observation_dates, linear_data, '-o',
        observation_dates, quadratic_data, '-o')

import pandas as pd
plt.figure()
observation_dates = np.arange('2017-01-01','2017-01-09', dtype = 'datetime64[D]')
observation_dates = map(pd.to_datetime, observation_dates)
plt.plot(observation_dates, linear_data, '-o',
        observation_dates, quadratic_data, '-o')

plt.figure()
observation_dates = np.arange('2017-01-01','2017-01-09', dtype = 'datetime64[D]')
observation_dates = list(map(pd.to_datetime, observation_dates))
plt.plot(observation_dates, linear_data, '-o',
        observation_dates, quadratic_data, '-o')

x = plt.gca().xaxis
for item in x.get_ticklabels():
    item.set_rotation(45)
plt.subplots_adjust(bottom = 0.25)

ax = plt.gca()
ax.set_xlabel('date')
ax.set_ylabel('units')
ax.set_title('Quadartic vs Linear performance')

#bar charts
plt.figure()
xvals = range(len(linear_data))
plt.bar(xvals, linear_data, width = 0.3)

new_xvals = []
for item in xvals:
    new_xvals.append(item+0.3)
    
plt.bar(new_xvals, quadratic_data, width = 0.3, color = 'red')

from random import randint
linear_err = [randint(0,15) for x in range(len(linear_data))]
plt.bar(xvals, quadratic_data, width = 0.3, yerr = linear_err)


plt.figure()
xvals = range(len(linear_data))
plt.bar(xvals, linear_data, width = 0.3, color = 'b')
plt.bar(xvals, quadratic_data, width = 0.3, bottom = linear_data, color = 'r')

plt.figure()
xvals = range(len(linear_data))
plt.barh(xvals, linear_data, height = 0.3, color = 'b')
plt.barh(xvals, linear_data, height = 0.3, left = linear_data,color = 'r')

