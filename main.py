import settings as s
from computation import simulate

posMatrix = simulate()

for i, particlePositions in enumerate(posMatrix):
    print(particlePositions)