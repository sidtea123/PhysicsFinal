import matplotlib.pyplot as plt
import numpy as np

#mesh
x, y = np.meshgrid(np.linspace(-100,100,50), np.linspace(-100, 100, 50))

r = np.array([3, 3])
mag = np.linalg.norm(r)
r_hat = r / mag

#quadrupole setup
def quadrupolex(eta, N, I, x, y):
    mu = (4 * np.pi) * 10**-7
    gradB = ((2 * mu * eta * N * I) / (np.sqrt((x**2) + (y**2)))**2) * r_hat[0]
    return(gradB)

#quadrupole setup
def quadrupoley(eta, N, I, x, y):
    mu = (4 * np.pi) * 10**-7
    gradB = ((2 * mu * eta * N * I) / (np.sqrt((x**2) + (y**2)))**2) * r_hat[1]
    return(gradB)

u = -quadrupoley(1, 25, 0.5, x, y)
v = -quadrupolex(1, 25, 0.5, x, y)

plt.quiver(x, y, u, v, color='blue')
plt.title('Vector Field')
plt.show()