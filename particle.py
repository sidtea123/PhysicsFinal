import settings as s
import numpy as np
import random

# holds data for particle, functionality for update
class Particle:
    def __init__(self, r, v, p):
        self.r = r
        self.v = v
        self.p = p
        # starts out alive, glass half full if you will
        self.dead = False

    # ran every frame
    def runTimestep(self):
        # if its dead render it somewhere offscreen
        if (self.dead):
            return np.array([-1000, -1000])
        self.v += self.caluclateForce() / s.m * s.dt
        self.boundaryCheck()
        self.r += self.v * s.dt
        return self.r

    # Fg + F(b field)
    def caluclateForce(self):
        return np.array([0, -s.g * s.m]) + self.mag_field()
    
    # wall is made of Beryllium due to high optical potential of 252NeV
    # now using custom bounds formulas in settings
    def boundaryCheck(self):
        x, y = self.r + self.v * s.dt
        if (y > s.O(x)):
            if (self.tryLoss(s.nO)):
                self.die()
            else:
                self.v = self.reflect(self.v, s.nO(x))
        elif (y < s.I(x)):
            if (self.tryLoss(s.nI)):
                self.die()
            else:
                self.v = self.reflect(self.v, s.nI(x))

    # for each collision, theres a change the neutron scatters depending on its energy and the bound's parameters
    def tryLoss(self, n):
        E = 1/2 * s.m * np.dot(self.v, self.v) * 6.242e18 * 10**9 # joules to neV
        if E > s.V:
            return True
        
        x = (self.r + self.v * s.dt)[0]
        # angle of incidence calculation
        # we taking the cosine of the arccosine of something, may as well simplify
        cos_term = (np.dot(self.v, n(x)) / (np.dot(self.v, self.v) * np.dot(n(x), n(x))))**2
        denom = s.V - E * cos_term
        
        if denom <= 0:
            return False
        else:
            # calculates true probability of loss
            reflectprob = 2 * s.fopt * np.sqrt(E * cos_term / denom)
            rfp = random.uniform(0, 1)
            # rolls the dice
            return rfp < reflectprob

    # kills off particle
    def die(self):
        self.dead = True
        self.v = np.array([0,0])

    # gavin's mag field, makes particles oscillate about midpoint of bounds
    def mag_field(self):
        if self.r[1] > s.midline:
            return np.array([0, self.p * s.mu * 0.25 * s.B])
        
        return np.array([0, self.p * s.mu * 1.5 * s.B])
    
    # reflects vector v across surface normal n, returns reflected
    def reflect(self, v, n):
        return v - 2 * np.dot(v, n) * n