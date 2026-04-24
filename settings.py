import numpy as np
# =============================================================== #
#
#  particle variables
#
# =============================================================== #
mu = -6.0293*10**-8  #actual magnetic moment of neturon is -6.0293e-8 eV
m = 1.67*10**-27
# =============================================================== #
#
# environment variables
#
# =============================================================== #
g = 9.8
fopt = 0.08 * 10**-5
V = 252 * 10**-9
# =============================================================== #
#
# simulation variables
#
# =============================================================== #

dt = 0.05       # timestep
time = 30       # total time of the simulation (0 - time)
numParts = 100   # number of Chill Ass Newtrons

# formulas for boundaries
def O(x):
    return 10

def I(x):
    return -10

# returns normals for O, I at (x, f(x))
# you need to manually derive these vectors, have fun!
def nO(x):
    return np.array([0, -1])

def nI(x):
    return np.array([0, 1])

pygameBoundResolution = 50 # how many points to sample for pygame visualization

xmin = 0  # the min and max x positions for the bound functions and window
xmax = 100  #m
ymin = -15 # min and max for window, but not necessarily bound functions
ymax = 15
screenBorderOffset = 10 # cushy bounds to make view not cover bounds
screenScale = 10 # pygame tiny, need to scale

particleRadius = 3
particleColor = (70, 175, 245)
backgroundColor = (70, 70, 70)
boundColor = (30, 30, 30)
textColor = (179, 128, 18)
fontSize = 24
textYOffset = 45
boundSize = 2

spawnymin = 0.11  #m
spawnymax = 9.00  #m
spawnxmin = 0.1  #m
spawnxmax = 5  #m

vinimin = 2 #m/s
vinimax = 6  #m/s
thetamin = -np.pi/4 #radians
thetamax = np.pi/4  #radians


# Magnetic Field
B = -2.69*10**-19 * 0.5