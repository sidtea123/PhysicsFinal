import settings as s
import numpy as np
import computation as c
import random

class Particle:
    def __init__(self, r, v, p):
        self.r = r
        self.v = v
        self.p = p
        self.dead = False

    def runTimestep(self):
        if (self.dead):
            return self.r
        self.v += self.caluclateForce() / s.m * s.dt
        self.boundaryCheck()
        self.r += self.v * s.dt
        return self.r

    def caluclateForce(self):
        return np.array([0, -s.g * s.m + self.mag_field()])
    
    # wall is made of Beryllium due to high optical potential of 252NeV
    # now using custom bounds formulas in settings
    def boundaryCheck(self):
        if (self.r[1] > s.O(self.r[0])):
            if (self.tryLoss(s.nO)):
                self.die()
            else:
                self.v = c.reflect(self.v, s.nO(self.r[0]))
        elif (self.r[1] < s.I(self.r[0])):
            if (self.tryLoss(s.nI)):
                self.die()
            else:
                self.v = c.reflect(self.v, s.nI(self.r[0]))

    def tryLoss(self, n):
        E = 1/2 * s.m * np.dot(self.v, self.v) * 6.242e18 * 10**9 # joules to neV

        if E > s.V:
            return True
        
        x = (self.r + self.v * s.dt)[0]
        # angle of incidence
        theta = np.abs(np.pi / 2 - np.abs(np.arccos(np.dot(self.v, n(x)) / (np.dot(self.v, self.v) * np.dot(n(x), n(x))))))
        cos_term = np.cos(theta)**2
        denom = s.V - E * cos_term
        
        if denom <= 0:
            return False
        else:
            reflectprob = 2 * s.fopt * np.sqrt(E * cos_term / denom)
            rfp = random.uniform(0, 1)
            return rfp < reflectprob

    def die(self):
        self.dead = True
        self.v = np.array([0,0])

    def mag_field(self):
        if self.r[1] > s.midline:
            return self.p * s.mu * 0.25 * s.B
        
        return self.p * s.mu * 1.5 * s.B