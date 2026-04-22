import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
#important numbers
mn = 1.6749 * 10**-27 #kg
g = -9.81
mu = 4 * np.pi * 10**-7

r_from_wall = np.array([[3], [0.29]])
mag_of_r = np.linalg.norm(r_from_wall)
r_hat = r_from_wall / mag_of_r

#top and bottom bounds(used for hit detection)
topwall = 0.30 
bottom = 0

#B field defs(monopole)
def Bfield1(qm, r, rhat): #qm should be set to 10^-15 or so(mess with this a little)
    B1 = (qm/(r**2)) * rhat
    return B1
def Bfield2(qm , r, rhat):
    B2 = (qm/(r**2)) * rhat
    return B2

#print('rhat=',r_hat)
#print('B field is =',Bfield1((1*10**-15), topwall - r_from_wall, r_hat))

def gradient_Bfield(qm, r, rhat):
    gradB = (-2 * qm / r**3) * rhat
    return gradB

#print('gradient =',gradient_calc(1*10**-15, topwall - r_from_wall, r_hat))

def force(m, g, p, mu, gradB):
    Fnet = m * g + p * mu * gradB
    return Fnet

def velocity(g, t_max, mu, gradB,):
    def acceleration(v, t):
        F = mu * gradB
        a = F / mn
        return a.flatten()
    v0 = np.zeros(2)
    t = np.linspace(0, t_max, 10000)
    vel = odeint(acceleration, v0, t)
    return vel

#caculate netforce on neutron at the position above
fnet_on_neutron = force(mn, g, 1, mu, gradient_Bfield(1*10**-15, topwall - r_from_wall, r_hat))
print('fnet is ', fnet_on_neutron)
print('velocity = ', velocity(g, 40, mu, gradient_Bfield(1*10**-15, topwall - r_from_wall, r_hat)))

plt.plot(velocity(g, 40, mu, gradient_Bfield(1*10**-15, topwall - r_from_wall, r_hat))[:,0],velocity(g, 40, mu, gradient_Bfield(1*10**-15, topwall - r_from_wall, r_hat))[:,1])
plt.show()