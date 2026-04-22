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
        self.r += self.v * s.dt
        r = self.r
        return r

    def caluclateForce(self):
        return np.array([0, -s.g  * s.m])