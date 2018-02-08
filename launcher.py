import pygame, sys
from pygame.locals import *
from colors import *
import numpy as np
import math

pygame.init()

MAX_MAG = 100
MIN_MAG = 10
MAX_ANGLE = 90
MIN_ANGLE = 0
global angle
angle = 90

LAUNCHER_LENGTH = 30

#define launcher object
class Launcher:
    def __init__(self,x,y):
       self.y = y
       self.x = x
       self.angle = 45
       self.mag = 100
       self.width = 5
       self.color = LAUNCHER

    def changeMagnitude(self,delta):
        self.mag += delta
        if(self.mag<MIN_MAG):
            self.mag = MIN_MAG
        if(self.mag>MAX_MAG):
            self.mag = MAX_MAG

    def fire(self,rock):
        rock.v_x = self.mag*np.cos(self.angle*np.pi/180)
        rock.v_y = self.mag*np.sin(self.angle*np.pi/180)

    def changeAngle(self,delta):
        self.angle+=delta
        if(self.angle<MIN_ANGLE):
            self.angle = MIN_ANGLE
        if(self.angle>MAX_ANGLE):
            self.angle = MAX_ANGLE

    def draw_launcher(self,surf):    
        dx = self.mag*np.cos(self.angle*np.pi/180)
        dy = self.mag*np.sin(self.angle*np.pi/180)
        my_launcher = pygame.draw.line(surf,self.color,(self.x,self.y),(self.x+dx,self.y-dy),self.width)

        #pygame.draw.line(surf,self.color,(self.x,self.y),(self.x+dx,self.y-dy),self.width)


        
