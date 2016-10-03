import matplotlib.pyplot as plt

circle1 = plt.Circle((0, 0), 2, color='r')
circle2 = plt.Circle((5, 5), 0.5, color='blue', fill=False)
circle3 = plt.Circle((10, 10), 2, color='g', clip_on=False)

fig, ax = plt.subplots() # note we must use plt.subplots, not plt.subplot
# (or if you have an existing figure)
# fig = plt.gcf()
ax = fig.gca()
ax.cla()   # clean

ax.set_xlim((0,10))
ax.set_ylim((0,10))

# draw the center
ax.plot((5), (5), 'o', color='y')

ax.add_artist(circle1)
ax.add_artist(circle2)
ax.add_artist(circle3)

fig.savefig('plotcircles.png')
plt.show()
