import settings as s
from computation import simulate
import pygame

posMatrix = simulate()

pygame.init()

screenWidth = (s.xmax - s.xmin + s.screenBorderOffset) * s.screenScale
screenHeight = (s.yMax - s.yMin + s.screenBorderOffset) * s.screenScale
screen = pygame.display.set_mode((screenWidth, screenHeight))
clock = pygame.time.Clock()

yOffset = s.screenBorderOffset * s.screenScale / 2 - s.particleRadius

running = True
tIndex = 0
while tIndex < len(posMatrix[0]):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(s.backgroundColor)

    for p in posMatrix:
         rPygame = (p[tIndex][0] * s.screenScale + s.screenBorderOffset + (s.spawnxmax - s.spawnxmin) / 2,
                    -p[tIndex][1] * s.screenScale + screenHeight / 2)
         pygame.draw.circle(screen, 
                            s.particleColor, rPygame, s.particleRadius)
    pygame.draw.line(screen, 
                     s.boundColor, 
                     (s.screenBorderOffset, yOffset), 
                     (screenWidth - s.screenBorderOffset, yOffset))
    pygame.draw.line(screen, 
                     s.boundColor, 
                     (s.screenBorderOffset, screenHeight - yOffset), 
                     (screenWidth - s.screenBorderOffset, screenHeight - yOffset))
    
    pygame.display.flip()

    tIndex += 1
    clock.tick(1 / s.dt)