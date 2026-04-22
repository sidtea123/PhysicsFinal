import numpy as np

def quadrupole(eta, N, I, R0):
    mu = (4 * np.pi) * 10**-7
    gradB = ((2 * mu * eta * N * I) / (R0**2))
    return(gradB)

#positions of poles
rhat_tleft = np.array([0.50, 0.50])

Btleft = quadrupole(1, 25, 0.25, .100**2) * rhat_tleft
Btright = quadrupole(1, 25, 0.25, .100**2)
print(Btleft)
