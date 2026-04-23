import numpy as np
import settings as s
from particle import Particle
import random

particles = [0 for _ in range(s.numParts)]
positions = [[0] * int(s.time / s.dt + 1) for _ in range(s.numParts)]

def simulate():
    initalizeParticles()

    times = np.linspace(0, s.time, int(s.time / s.dt))

    for t in range(times.size):
        for i, p in enumerate(particles):
            r = p.runTimestep()
            positions[i][t + 1] = r.copy()

    return positions
    
# need to initialize particle and initial position
def initalizeParticles():
    for i in range(s.numParts):
        theta = random.uniform(s.thetamin,s.thetamax)
        vini = random.uniform(s.vinimin,s.vinimax)
        r = np.array([random.uniform(s.spawnxmin,s.spawnxmax),random.uniform(s.spawnymin,s.spawnymax)])
        v = np.array([vini*np.cos(theta),vini*np.sin(theta)])
        particles[i] = Particle(r, v, 1)
        positions[i][0] = r.copy()

