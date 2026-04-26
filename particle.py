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
        f = self.caluclateForce()
        self.v += f / s.m * s.dt
        self.boundaryCheck()
        self.r += self.v * s.dt
        r = self.r
        return r

    def caluclateForce(self):
        Fg = np.array([0, -s.g  * s.m])
        Fb = np.array([0,self.mag_field()])  #want Fg = Fb @ middle. Fb<Fg @ y>middle. Fb>Fg @ y<middle.

        return Fg + Fb
    
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
        E = 1/2 * s.m * np.dot(self.v, self.v)
        r = self.r + self.v * s.dt
        x, y = r
        # angle of incidence
        theta = np.pi / 2 - np.abs(np.arccos(np.dot(self.v, n(x)) / (np.dot(self.v, self.v) * np.dot(n(x), n(x)))))
        cos_term = np.cos(theta)**2
        denom = s.V - E * cos_term
        
        if denom <= 0:
            return False
        else:
            reflectprob = min(1.0, 2 * s.fopt *np.sqrt((E * cos_term) / denom))
            rfp = random.uniform(0, 1)
            return rfp < reflectprob

    def die(self):
        self.dead = True
        print('i died')

    def mag_field(self):
        midline = (s.ymax + s.ymin) / 2
        dst = self.r[1] - midline
        
        if self.r[1] > midline:
            B_high = 0.25 * s.B
            mag_force = self.p * s.mu * B_high
        elif self.r[1] == midline:
            mag_force = self.p * s.mu * s.B
        else:
            B_low = 1.5 * s.B
            mag_force = self.p * s.mu * B_low
        return mag_force

        #I think this might work but changing the y bounds (ymax = #) doesnt effect the bounds in pygame
        #neccessary to change bounds because working off of y position