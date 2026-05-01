import settings as s
import pygame
import numpy as np

screenWidth = (s.xmax - s.xmin) * s.screenScale + s.screenBorderOffset
screenHeight = (s.ymax - s.ymin) * s.screenScale + s.screenBorderOffset

# vector transformation from our simulation to pygame space
def scaleX(x):
    return x * s.screenScale + ((s.spawnxmax - s.spawnxmin) / 2) * s.screenScale + s.screenBorderOffset

def scaleY(y):
    return -y * s.screenScale + screenHeight / 2

def scaleVec(v):
    return np.array([scaleX(v[0]), scaleY(v[1])])

if __name__ == '__main__':
    fileName = 'output.npy'

    print('loading data from file...')

    # loads data from file. this allows us to store longer simulations ahead of time
    # for the time being this only saves position data, so simulation variables and bounds may look weird if changed
    # posMatrix = np.loadtxt(fileName).reshape((s.numParts, s.totalSteps + 1, 2))
    posMatrix = np.load(fileName)
    print('initializing pygame...')
    pygame.display.init()
    pygame.font.init()
    screen = pygame.display.set_mode((screenWidth, screenHeight))
    clock = pygame.time.Clock()

    multScale = np.array([s.screenScale, -s.screenScale])
    addScale = np.array([((s.spawnxmax - s.spawnxmin) / 2) * s.screenScale + s.screenBorderOffset, screenHeight / 2])

    # arrays for bound points
    xVals = np.linspace(s.xmin, s.xmax, s.pygameBoundResolution)
    outerPoints = np.array([(scaleX(x), scaleY(s.O(x)) - s.particleRadius) for x in xVals])
    innerPoints = np.array([(scaleX(x), scaleY(s.I(x)) + s.particleRadius) for x in xVals])

    font = pygame.font.Font('freesansbold.ttf', s.fontSize)

    # heading text
    text = font.render(f'      BUNS\n   {1 / s.dt} FPS\n{s.numParts} Particles', True, s.textColor)
    textRect = text.get_rect()
    textRect.center = (screenWidth // 2, s.textYOffset)

    running = True
    start = False
    tIndex = 0

    # the slug
    slugWidth = 700
    slugImage = pygame.transform.scale(pygame.image.load("Cyber Slugs.png").convert(), (slugWidth, 420))

    # prerendering all the circles
    particle_surf = pygame.Surface((s.particleRadius * 4, s.particleRadius * 4), pygame.SRCALPHA).convert_alpha()
    pygame.draw.circle(particle_surf, s.particleColor, (5, 5), s.particleRadius)
    surfaces_list = [particle_surf] * s.numParts

    print('rendering BUNS')
    while tIndex < (s.totalSteps) and running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            # goes from start slug to render
            elif event.type == pygame.MOUSEBUTTONDOWN:
                start = True

        # fill background
        screen.fill(s.backgroundColor)

        if start:
            # efficiently zipping position matrix to surface list to be blitted, idk how it works tho
            screen.fblits(zip(surfaces_list, posMatrix[tIndex].astype(np.int32)))
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