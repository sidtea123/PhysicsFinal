import settings as s
from computation import simulate
import pygame
import numpy as np

print('running simulation...')
posMatrix = simulate()
print('finished sim, initializing pygame...')

pygame.display.init()
pygame.font.init()

screenWidth = (s.xmax - s.xmin) * s.screenScale + s.screenBorderOffset
screenHeight = (s.ymax - s.ymin) * s.screenScale + s.screenBorderOffset
screen = pygame.display.set_mode((screenWidth, screenHeight))
clock = pygame.time.Clock()

# vector transformation from our simulation to pygame space
def scaleX(x):
    return (x + (s.spawnxmax - s.spawnxmin) / 2) * s.screenScale + s.screenBorderOffset

def scaleY(y):
    return -y * s.screenScale + screenHeight / 2

xVals = np.linspace(s.xmin, s.xmax, s.pygameBoundResolution)
outerPoints = np.array([(scaleX(x), scaleY(s.O(x)) - s.particleRadius) for x in xVals])
innerPoints = np.array([(scaleX(x), scaleY(s.I(x)) + s.particleRadius) for x in xVals])

font = pygame.font.Font('freesansbold.ttf', s.fontSize)

text = font.render(f'      BUNS\n   {1 / s.dt} FPS\n{s.numParts} Particles', True, s.textColor)
textRect = text.get_rect()
textRect.center = (screenWidth // 2, s.textYOffset)

running = True
start = False
tIndex = 0

slugWidth = 900
slugImage = pygame.transform.scale(pygame.image.load("Cyber Slugs.png").convert(), (slugWidth, 490))

print('rendering BUNS')
while tIndex < len(posMatrix[0]) and running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            start = True

    
    screen.fill(s.backgroundColor)

    if start:

        # draw particles
        for p in posMatrix:
            rPygame = (scaleX(p[tIndex][0]), scaleY(p[tIndex][1]))
            pygame.draw.circle(screen, s.particleColor, rPygame, s.particleRadius)
            
        # draw bounds
        pygame.draw.lines(screen, s.boundColor, False, outerPoints, s.boundSize)
        pygame.draw.lines(screen, s.boundColor, False, innerPoints, s.boundSize)

        # draw title text
        screen.blit(text, textRect)

        # update time index
        tIndex += 1
        # ensuring constant FPS
    else:
        screen.blit(slugImage, ((screenWidth - slugWidth) / 2 , 0))
    
    pygame.display.flip()
    clock.tick(1 / s.dt)