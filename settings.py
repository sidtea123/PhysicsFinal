import numpy as np

# =============================================================== #
#
#  CONSTANTS
#
# =============================================================== #
mu = -6.0293*10**-8         # actual magnetic moment of neturon is -6.0293e-8 eV
m = 1.67*10**-27            # magnetic moment of neutron
g = 9.8                     # defying grabvity
fopt = 0.08                 # ask benjamin
V = 252                     # complex optical potential of bounds: Beryllium 
B = -2.69*10**-19           # Magnetic Field
# =============================================================== #
#
# simulation variables
#
# =============================================================== #

dt = 0.02                   # timestep
time = 20                   # total time of the simulation (0 - time)
numParts = 1000           # number of Beautiful Ultracold Neutrons

totalSteps = int(time / dt) # DO NOT TOUCH total number of time steps in simulation

# formulas for boundaries
def O(x):
    return 28

def I(x):
    return -28

# returns normals for O, I at (x, f(x))
# you need to manually derive these vectors, have fun!
def nO(x):
    return np.array([0, -1])

def nI(x):
    return np.array([0, 1])

pygameBoundResolution = 50  # how many points to sample for pygame visualization

xmin = 0                    # the min and max x positions for the bound functions and window
xmax = 300                  # m
ymin = -40                  # min and max for window, but not necessarily bound functions
ymax = 40
screenBorderOffset = 10     # cushy bounds to make view not cover bounds
screenScale = 5             # pygame tiny, need to scale

particleRadius = 1.3
particleColor = (70, 175, 245, 255)
backgroundColor = (70, 70, 70)
boundColor = (30, 30, 30)
textColor = (179, 128, 18)
fontSize = 24
textYOffset = 45
boundSize = 2

spawnymin = -26.00          # bounds for the spawn range of the particles
spawnymax = 26.00           # m
spawnxmin = 0.0             # m
spawnxmax = 4.00            # m

midline = (ymax + ymin) / 2 # no touchy

vinimin = 2                 # bounds for the speed and angle of the particles at spawn
vinimax = 7                 # m/s
thetamin = -np.pi/2.5       # radians
thetamax = np.pi/2.5        # radians