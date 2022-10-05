#subplots
%matplotlib notebook
import matplotlib.pyplot as plt
import numpy as np
plt.subplot?

plt.figure()
plt.subplot(1,2,1)
linear_data = np.array([1,2,3,4,5,6,7,8])
plt.plot(linear_data, '-o')

exponential_data = linear_data**2
plt.subplot(1,2,1)
plt.plot(exponential_data, '-o')

plt.subplot(1,2,1)
plt.plot(exponential_data, '-x')

plt.figure()
ax1 = plt.subplot(1,2,1)
plt.plot(linear_data, '-o')
ax2 = plt.subplot(1,2,2, sharey = ax1)
plt.plot(exponential_data, '-x')

plt.figure()
plt.subplot(1,2,1) == plt.subplot(121)

fig, ((ax1,ax2,ax3), (ax4,ax5,ax6), (ax7,ax8,ax9)) = plt.subplots(3, 3, sharex = True, sharey = True)
ax5.plot(linear_data, '-')

for ax in plt.gcf().get_axes() :
    for label in ax.get_xticklabels() + ax.get_yticklabels():
        label.set_visible(True)

plt.gcf().canvas.draw()

#histograms
fig, ((ax1,ax2), (ax3,ax4)) = plt.subplots(2, 2, sharex = True)
axs = [ax1, ax2, ax3, ax4]
for n in range(0, len(axs)):
    sample_size = 10**(n+1)
    sample = np.random.normal(loc = 0.0, scale = 1.0, size = sample_size)
    axs[n].hist(sample)
    axs[n].set_title('n = {}'.format(sample_size))
    

#histograms
fig, ((ax1,ax2), (ax3,ax4)) = plt.subplots(2, 2, sharex = True)
axs = [ax1, ax2, ax3, ax4]
for n in range(0, len(axs)):
    sample_size = 10**(n+1)
    sample = np.random.normal(loc = 0.0, scale = 1.0, size = sample_size)
    axs[n].hist(sample, bins = 100)
    axs[n].set_title('n = {}'.format(sample_size))

plt.figure()
Y = np.random.normal(loc = 0.0, scale = 1.0, size = 10000)
X = np.random.normal(size = 10000)
plt.scatter(X,Y)

import matplotlib.gridspec as gridspec
plt.figure()
gspec = gridspec.GridSpec(3,3)
top_histogram = plt.subplot(gspec[0, 1:])
side_histogram = plt.subplot(gspec[1:, 0])
lower_right = plt.subplot(gspec[1:, 1:])


Y = np.random.normal(loc = 0.0, scale = 1.0, size = 10000)
X = np.random.normal(size = 10000)
lower_right.scatter(X,Y)
top_histogram.hist(X, bins = 100)
s = side_histogram.hist(Y, bins = 100, orientation = 'horizontal')

top_histogram.clear()
top_histogram.hist(X, bins = 100, normed = True)
side_histogram.clear()
side_histogram.hist(Y, bins = 100, orientation = 'horizontal', normed = True)

side_histogram.invert_xaxis()

for ax in [top_histogram, lower_right]:
    ax.set_xlim(0,1)
for ax in [side_histogram, lower_right]:
    ax.set_ylim(-5,5)

#boxplots
import pandas as pd
import numpy as np
normal_sample = np.random.normal(loc = 0.0, scale = 1.0, size = 10000)
random_sample = np.random.random(size = 10000)
gamma_sample = np.random.gamma(2, size = 10000)
df = pd.DataFrame({'normal':normal_sample,
                  'random': random_sample,
                  'gamma': gamma_sample})

plt.figure()
_ = plt.boxplot( df['normal'], whis='range')

plt.clf()
_ = plt.boxplot(df['normal'], df['random'], df['gamma'],whis='range')

plt.figure()
_ = plt.hist(df['gamma'], bins = 100)

import mpl_toolkits.axes_grid1.inset_locator as mpl_il
plt.figure()
_ = plt.boxplot(df['normal'], df['random'], df['gamma'],whis='range')
ax2 = mppl_il.inset_axes(plt.gca(), width = '60%', height = '40%', loc = 2)
ax2.hist(df['gamma'], bins = 100)
ax2.margins(x = 0.5)

ax2.yaxis.tick_right()
plt.figure()
_ = plt.boxplot([df['normal'], df['random'], df['gamma']])

#heatmaps
plt.figure()
Y = np.random.normal(loc = 0.0, scale = 1.0, size = 10000)
X = np.random.random(size = 10000)
_ = plt.hist2d(X, Y, bins = 25)

plt.figure()
_ = plt.hist2d(X, Y, bins = 100)

plt.colorbar()

#animation
import matplotlib.animation as animation
n =100
x = np.random.randn(n)

def update(curr):
    if curr == n:
        a.event_source.stop()
        plt.cla()
        bins = np.arange(-4, 4, 0.5)
        plt.hist(x[:curr], bins=bins)
        plt.axis([-4,4,0,30])
        plt.gca().set_title('sampling the normal distribution')
        plt.gca().set_ylabel('frequency')
        plt.gca().set_xlabel('value')
        plt.annotate('n = {}'.format(curr),[3,27])

fig = plt.figure()
a = animation.FuncAnimation(fig, update, interval = 100)

#interactivity
plt.figure()
data = np.random.rand(10)
plt.plot(data)

def onclick(event):
    plt.cla()
    plt.plot(data)
    plt.gca().set_title('event at the pixels {}, {} {} and data {}, {}'.format(event.x,
                                                                              event.y, '\n',
                                                                              event.xdata,
                                                                              event.ydata))
plt.gcf().canvas.mpl_connect('button_press_event', onclick)

from random import shuffle
origins = ['china', 'brazil', 'india', 'usa', 'canada', 'uk', 'germany', 'iraq', 'chile', 'mexico']
shuffle(origins)
df = pd.DataFrame({'height':np.random.rand(10),
                  'weight':np.random.rand(10),
                  'origin':origins})
df

plt.figure()
plt.scatter(df['height'], df['weight'], picker = 5)
plt.gca().set_ylabel('Weight')
plt.gca().set_xlabel('Height')

def onpick(event):
    origin = df.iloc[event.ind[0]]['origin']
    plt.gca().set_title('selected item came from {}'.format(origin))
plt.gcf().canvas.mpl_connect('pick_event', onpick)