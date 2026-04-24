import settings as s
import numpy as np
import computation as c
import random

class Particle:
    def __init__(self, r, v, p):
        self.r = r
        self.v = v
        self.p = p

    def runTimestep(self):
        f = self.caluclateForce()
        self.v += f / s.m * s.dt
        self.boundaryCheck()
        self.r += self.v * s.dt
        r = self.r
        return r

    def caluclateForce(self):
        Fg = np.array([0, -s.g  * s.m])
        Fb = self.calculateGradientForce()  #want Fg = Fb @ middle. Fb<Fg @ y>middle. Fb>Fg @ y<middle.

        return Fg + Fb
    
    
    # wall is made of Beryllium due to high optical potential of 252NeV
    # now using custom bounds formulas in settings
    def boundaryCheck(self):
        r = self.r + self.v * s.dt
        x, y = r
        if (y > s.O(x)):
            self.v = c.reflect(self.v, s.nO(x))
        elif (y < s.I(x)):
            self.v = c.reflect(self.v, s.nI(x))

    def LossProb(self):
        E = 1/2 * s.m * self.v**2
        reflectprob = 2 * s.f * ((E * np.cos(2 * c.theta - np.pi)**2) / (s.V - E * np.cos(2 * c.theta - np.pi)**2))**(0.5)
        r = random.uniform(0, 1)
        return reflectprob, r
        # in order to implement this we need to say that if r >= reflectprob then the neutron survives and if r < reflectprob then we delete the neutron
        # I believe this must be done in the pygame but I'm scared to touch Sid's work of art
        # as you should be

    def calculateGradientForce(self):
        gradient = np.array([0,self.r[1]])
        return self.p * s.mu * s.B * gradient
