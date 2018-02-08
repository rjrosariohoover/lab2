#!/usr/bin.python

import pygame, sys
from pygame.locals import *
import numpy as np
import math

import launcher
import rock
from colors import *


HEIGHT = 400
WIDTH = 500
FPS = 30



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
    fpsClock = pygame.time.Clock()
    surf = pygame.display.set_mode((WIDTH,HEIGHT),0,32)
    my_launcher = launcher.Launcher(0,HEIGHT-20)
    my_rock = rock.Rock(0, HEIGHT-20) #TODO

    while True:
        for event in pygame.event.get():            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    my_launcher.changeAngle(3)
                if event.key == pygame.K_DOWN:
                    my_launcher.changeAngle(-3)
                if event.key == pygame.K_RIGHT:
                    my_launcher.changeMagnitude(5)
                if event.key == pygame.K_LEFT:
                    my_launcher.changeMagnitude(-5)
                if (event.key == pygame.K_SPACE) and (not my_rock.ismoving()):
                    my_launcher.fire(my_rock)
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
                
        #2. Do game logic
        my_rock.move(1.0/FPS)
        

        # 3. Draw everything
        draw_world(surf)
        my_launcher.draw_launcher(surf)
        my_rock.draw(surf)
        pygame.display.update()
        fpsClock.tick(FPS)
main()
