import numpy as np
import settings as s
from particle import Particle

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
        # particle spawning, for now just one
        if (i == 0):
            r = np.array([0.0, 0.0])
            v = np.array([0.0, 0.0])
            particles[i] = Particle(r, v, 1)
            positions[i][0] = r.copy()
        else:
            r = np.array([5.0, 5.0])
            v = np.array([0.0, 0.0])
            particles[i] = Particle(r, v, 1)
            positions[i][0] = r.copy()