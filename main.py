import settings as s
from computation import simulate
import pygame
import numpy as np

posMatrix = simulate()

pygame.init()

screenWidth = (s.xmax - s.xmin + s.screenBorderOffset) * s.screenScale
screenHeight = (s.ymax - s.ymin + s.screenBorderOffset) * s.screenScale
screen = pygame.display.set_mode((screenWidth, screenHeight))
clock = pygame.time.Clock()

def scaleX(x):
    return x * s.screenScale + s.screenBorderOffset + (s.spawnxmax - s.spawnxmin) / 2

def scaleY(y):
    return -y * s.screenScale + screenHeight / 2

xVals = np.linspace(s.xmin, s.xmax, s.pygameBoundResolution)
outerPoints = np.array([(scaleX(x), scaleY(s.O(x)) - s.particleRadius) for x in xVals])
innerPoints = np.array([(scaleX(x), scaleY(s.I(x)) + s.particleRadius) for x in xVals])

running = True
tIndex = 0
while tIndex < len(posMatrix[0]) and running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(s.backgroundColor)

    for p in posMatrix:
         rPygame = (scaleX(p[tIndex][0]), scaleY(p[tIndex][1]))
         pygame.draw.circle(screen, 
                            s.particleColor, rPygame, s.particleRadius)
    # pygame.draw.line(screen, 
    #                  s.boundColor, 
    #                  (s.screenBorderOffset, yOffset), 
    #                  (screenWidth - s.screenBorderOffset, yOffset))
    # pygame.draw.line(screen, 
    #                  s.boundColor, 
    #                  (s.screenBorderOffset, screenHeight - yOffset), 
    #                  (screenWidth - s.screenBorderOffset, screenHeight - yOffset))
    pygame.draw.lines(screen, s.boundColor, False, outerPoints, s.boundSize)
    pygame.draw.lines(screen, s.boundColor, False, innerPoints, s.boundSize)
    
    pygame.display.flip()

    tIndex += 1
    clock.tick(1 / s.dt)