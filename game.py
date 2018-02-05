import pygame, sys, launcher
from launcher import *
from pygame.locals import *
from colors import *

HEIGHT = 400
WIDTH = 500
FPS = 30
angle = 90

pygame.init()

surf = pygame.display.set_mode((WIDTH,HEIGHT),0,32)

# define game world
def draw_world(surf):
    # surf is a pygame surface
    pygame.display.set_caption('Launchr: A Game of Wits and Will')

    # fill in sky/base layer
    surf.fill(BACKGROUND)

    # draw ground
    pygame.draw.rect(surf, GREEN, (0, 380, 500, 400))

    # draw game title
    Title = pygame.font.Font('freesansbold.ttf',24)
    TitleObj = Title.render('Launchr 1.0', True, BLACK)
    TitleRectObj = TitleObj.get_rect()
    TitleRectObj.center = (250,30)
    surf.blit(TitleObj, TitleRectObj)
    
def main():
    pygame.init()
    fprClock = pygame.time.Clock()
    surf = pygame.display.set_mode((WIDTH,HEIGHT),0,32)

while True:
    draw_world(surf)
    draw_launcher(surf)
    for event in pygame.event.get():
        pygame.key.get_pressed() == KEYDOWN
        if event.type == KEYDOWN:
            if event.key == pygame.K_UP:
                launcher.changeAngle(3)
            if event.key == pygame.K_DOWN:
                launcher.changeAngle(-3)
            #if event.key == pygame.K_RIGHT:
             #   launcher.changeMagnitude(1.1)
            #if event.key == pygame.K_LEFT:
             #   launcher.changeMagnitude(-1.1)
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        pygame.display.update()
