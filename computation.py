import numpy as np
import settings as s
from particle import Particle
import random

# array of particles
particles = np.empty(s.numParts, dtype=Particle)
# rank 3 tensor to store positions of particles
positions = np.empty((s.numParts, s.totalSteps + 1, 2))

# beefy sim code
def simulate():
    initalizeParticles()
    print('instantiated particles...')
    prev = 0
    # index 0 is the initial state of the system, so start at 1
    for t in range(1, s.totalSteps + 1):
        for i, p in enumerate(particles):
            positions[i, t] = p.runTimestep()

        # nice percentage output, lets you watch progress
        pct = int((t / (s.totalSteps + 1)) * 100)
        if (pct % 5 == 0):
            if (pct != prev):
                print(f'{pct:.0f}% done...')
                prev = pct

    print('100% done...')
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

# saves code to file, may take a bit for more detailed sims
if __name__ == '__main__':
    positions = simulate()
    
    print('writing to file...')
    with open('output.txt', 'w') as outfile:
        # formats matrix to readable format in file
        outfile.write('# Array shape: {0}\n'.format(positions.shape))
        for data_slice in positions:
            np.savetxt(outfile, data_slice, fmt='%-7.2f')
            outfile.write('# New slice\n')

    print('done writing to file :)')