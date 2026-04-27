import numpy as np
import settings as s
from particle import Particle
import random

# array of particles
particles = np.empty(s.numParts, dtype=Particle)
# rank 3 tensor to store positions of particles
positions = np.empty((s.numParts, s.totalSteps + 1, 2))

def simulate():
    initalizeParticles()

    # index 0 is the initial state of the system, so start at 1
    for t in range(1, s.totalSteps + 1):
        for i, p in enumerate(particles):
            positions[i, t] = p.runTimestep()

    return positions
    
# need to initialize particle and initial position
def initalizeParticles():
    for i in range(s.numParts):
        theta = random.uniform(s.thetamin,s.thetamax)
        vini = random.uniform(s.vinimin,s.vinimax)
        r = np.array([random.uniform(s.spawnxmin,s.spawnxmax),random.uniform(s.spawnymin,s.spawnymax)])
        v = np.array([vini*np.cos(theta),vini*np.sin(theta)])
        particles[i] = Particle(r, v, 1)
        positions[i][0] = r


# reflects vector v across surface normal n, returns reflected
def reflect(v, n):
    return v - 2 * np.dot(v, n) * n