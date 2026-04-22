import matplotlib.pyplot as plt
import numpy as np

#grid setup
lim = 100
n   = 50
x, y = np.meshgrid(np.linspace(-lim, lim, n), np.linspace(-lim, lim, n))

#quadrupole
mu0 = 4 * np.pi * 1e-7
N   = 25
I   = 0.5
eta = 1
G   = 2 * mu0 * eta * N * I   # gradient prefactor

Bx = G * y
By = G * x

#magnitude colouring
mag = np.hypot(Bx, By)
mag[mag == 0] = np.nan

#normalise arrows
Bx_n = Bx / mag
By_n = By / mag

#figure
fig, ax = plt.subplots(figsize=(7, 7))
ax.set_facecolor('white')

#stream lines (field lines)
ax.streamplot(x, y, Bx, By,
              color=mag, cmap='plasma',
              linewidth=1.4, density=1.4,
              arrowsize=1.2)

# Quiver overlay for direction clarity
ax.quiver(x[::3, ::3], y[::3, ::3],
          Bx_n[::3, ::3], By_n[::3, ::3],
          alpha=0.35, scale=30, color='steelblue')

ax.set_xlim(-lim, lim)
ax.set_ylim(-lim, lim)
ax.set_title('Magnetic Quadrupole Field')
ax.set_xlabel('x (cm)')
ax.set_ylabel('y (cm)')
plt.tight_layout()
plt.show()