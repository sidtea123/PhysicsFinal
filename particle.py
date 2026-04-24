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
    
    #def boundaryCheckbounce(self):
        #if (self.r + self.v * s.dt)[1] > 10:
            #self.v[1] = -self.v[1]
        #elif (self.r + self.v * s.dt)[1] < -10:
            #self.v[1] = -self.v[1]

    # wall is made of Beryllium due to high optical potential of 252NeV
    # now using custom bounds formulas in settings
    def boundaryCheck(self):
        if (self.r + self.v * s.dt)[1] > 10:
            self.v[1] = -self.v[1]
        elif (self.r + self.v * s.dt)[1] < -10:
            self.v[1] = -self.v[1]
        E = 1/2 * s.m * np.dot(self.v, self.v) #I think there is an issue with the energy calculation and how it interacts with the potential energy of the walls
        r = self.r + self.v * s.dt
        x, y = r
        if (y > s.O(x)):
            theta_Itop = np.arccos(np.abs((np.dot(self.v , s.nO(x)))) / (np.linalg.norm(self.v) * np.linalg.norm(s.nO(x))))
            cos_term = np.cos(2 * theta_Itop - np.pi)**2
            denom = s.V - E * cos_term
            if denom <= 0:
                self.dead = True
            else:
                reflectprob = min(1.0, 2 * s.fopt * np.sqrt((E * cos_term) / denom))
                rfp = random.uniform(0, 1)
                if (rfp >= reflectprob):
                    self.v = c.reflect(self.v, s.nO(x))
                else:
                    self.dead = True
        elif (y < s.I(x)):
            theta_Ibot = np.arccos(np.abs((np.dot(self.v , s.nI(x)))) / (np.linalg.norm(self.v) * np.linalg.norm(s.nI(x))))
            cos_term = np.cos(2 * theta_Ibot - np.pi)**2
            denom = s.V - E * cos_term
            if denom <= 0:
                self.dead = True
            else:
                reflectprob = min(1.0, 2 * s.fopt *np.sqrt((E * cos_term) / denom))
                rfp = random.uniform(0, 1)
                if (rfp >= reflectprob):
                    self.v = c.reflect(self.v, s.nI(x))
                else:
                    self.dead = True
        self.r = r

    #def calculateGradientForce(self):
        #gradient = np.array([0,self.r[1]])      TS IS BUNS DONT USE
        #return self.p * s.mu * s.B * gradient

    def mag_field(self):
        if self.r[1] > 0.5 * s.ymax:
            B_high = 0.25 * s.B
            mag_force = self.p * s.mu * B_high
        if self.r[1] == 0.5 * s.ymax:
            mag_force = self.p * s.mu * s.B
        if self.r[1] < 0.5 * s.ymax:
            B_low = 1.25 * s.B
            mag_force = self.p * s.mu * B_low
        return mag_force

        #I think this might work but changing the y bounds (ymax = #) doesnt effect the bounds in pygame
        #neccessary to change bounds because working off of y position