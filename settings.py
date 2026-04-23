import numpy as np
# =============================================================== #
#
#  particle variables
#
# =============================================================== #
mu = 1
m = 1

# =============================================================== #
#
# environment variables
#
# =============================================================== #
g = 3

# =============================================================== #
#
# simulation variables
#
# =============================================================== #

dt = 0.05         # timestep
time = 10        # total time of the simulation (0 - time)
numParts = 50  #number of Chill Ass Newtrons
yMin = -10  #m
yMax = 10  #m
xmin = 0  #m
xmax = 100  #m
screenBorderOffset = 10 # cushy bounds to make view not cover bounds
screenScale = 10 # pygame tiny, need to scale

particleRadius = 3
particleColor = (70, 175, 245)
backgroundColor = (70, 70, 70)
boundColor = (30, 30, 30)

spawnymin = -9.99  #m
spawnymax = 9.99  #m
spawnxmin = 0.1  #m
spawnxmax = 5  #m

vinimin = 2 #m/s
vinimax = 6  #m/s
thetamin = -np.pi/4 #radians
thetamax = np.pi/4  #radians
