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
g = 1

# =============================================================== #
#
# simulation variables
#
# =============================================================== #

dt = 1          # timestep
time = 5        # total time of the simulation (0 - time)
numParts = 2  #number of Chill Ass Newtrons
yMin = -10  #m
yMax = 10  #m
xmin = 0  #m
xmax = 100  #m

spawnymin = -9.99  #m
spawnymax = 9.99  #m
spawnxmin = 0.1  #m
spawnxmax = 5  #m

vinimin = 2 #m/s
vinimax = 6  #m/s
thetamin = -np.pi/4 #radians
thetamax = np.pi/4  #radians
