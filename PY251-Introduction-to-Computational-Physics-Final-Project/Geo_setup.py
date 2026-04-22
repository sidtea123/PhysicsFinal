import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
#global variable list
subd = 10000
topwall = np.array(25)
bottomwall = np.array(5)

#random angle of entry
mu, sigma = 0, 10
theta = np.random.normal(mu, sigma, 1000)

#graph of random numbers
#count, bins, ignored = plt.hist(theta, 30, density=True)
#plt.plot(bins, 1/(sigma * np.sqrt(2 * np.pi)) * np.exp(-(bins - mu) **2 / (2 * sigma**2)))
#plt.title('Theta Values')
#plt.show()

#geometry def
ytwall = np.linspace(topwall,topwall,subd)
ybwall = np.linspace(bottomwall,bottomwall, subd)
x = np.linspace(0,100, 10000)

#plot
fig, ax = plt.subplots()
ax.set_xlim(0, 100), ax.set_ylim(0, 30)
twall = ax.plot(x, ytwall, color='black')
bwall = ax.plot(x, ybwall, color='black')
point, = ax.plot([], [], 'ro', markersize=2)

#animation
def update(frame):
    point.set_data([frame], [15])
    return point,

def init():
    point.set_data([0], [15])
    return point,
ani = FuncAnimation(fig, update, frames=range(100), interval=33, init_func=init, blit=True)

plt.show()