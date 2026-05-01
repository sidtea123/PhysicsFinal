import numpy as np
import settings as s
from render import scaleVec
from particle import Particle
import random

# array of particles
particles = np.empty(s.numParts, dtype=Particle)
# rank 3 tensor to store positions of particles
positions = np.empty((s.totalSteps + 1, s.numParts, 2))
energies = np.empty(s.totalSteps + 1)

# beefy sim code
def simulate():
    initalizeParticles()
    print('instantiated particles...')
    prev = 0
    # index 0 is the initial state of the system, so start at 1
    for t in range(1, s.totalSteps + 1):
        vTot = 0
        for i, p in enumerate(particles):
            positions[t, i] = scaleVec(p.runTimestep())
            vTot += np.dot(p.v, p.v)
        energies[t] = 0.5 * s.m * vTot

        # nice percentage output, lets you watch progress
        pct = int((t / (s.totalSteps + 1)) * 100)
        if (pct % 5 == 0):
            if (pct != prev):
                print(f'{pct:.0f}% done...')
                prev = pct

    print('100% done...')
    return positions, energies
    
# need to initialize particle and initial position
def initalizeParticles():
    for i in range(s.numParts):
        theta = random.uniform(s.thetamin,s.thetamax)
        vini = random.uniform(s.vinimin,s.vinimax)
        r = np.array([random.uniform(s.spawnxmin,s.spawnxmax),random.uniform(s.spawnymin,s.spawnymax)])
        v = np.array([vini*np.cos(theta),vini*np.sin(theta)])
        particles[i] = Particle(r, v, 1)
        positions[0][i] = r
    energies[0] = 0

# saves code to file, may take a bit for more detailed sims
if __name__ == '__main__':
    positions, energies = simulate()
    
    print('writing to file...')
    # positions.tofile('100k_50FPS_pipe.txt')
    np.save('output.npy', positions)
    np.save('energies.npy', energies)
    # with open('100k_50FPS_pipe.txt', 'w') as outfile:
    #     # formats matrix to readable format in file
    #     outfile.write('# Array shape: {0}\n'.format(positions.shape))
    #     for data_slice in positions:
    #         np.savetxt(outfile, data_slice, fmt='%-7.2f')
    #         outfile.write('# New slice\n')

    print('done writing to file :)')