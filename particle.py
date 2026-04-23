import settings as s
import numpy as np

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
    
    
#wall is made of Beryllium due to high optical potential of 252NeV
    def boundaryCheck(self):
        if (self.r + self.v * s.dt)[1] > s.yMax:
            self.v[1] = -self.v[1]
        elif (self.r + self.v * s.dt)[1] < s.yMin:
            self.v[1] = -self.v[1]

    def calculateGradientForce(self):
        gradient = np.array([0,self.r[1]])
        return self.p * s.mu * s.B * gradient
