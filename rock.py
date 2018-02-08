import pygame
from colors import *

class Rock:
    def __init__(self, x, y):
        #TODO figure out parameters
        self.x = x
        self.y = y
        self.v_x = 0
        self.v_y = 0

    def move(self,time):
        self.x = self.x + self.v_x*time
        self.y = self.y - self.v_y*time       
    
    def ismoving(self):
        if (self.v_x != 0 or self.v_y !=0):
            return True
        else:
            return False
        

    def draw(self, surf):
        #TODO, draw to surface
        r = pygame.Rect((0,0,10,10))
        r.center = (self.x, self.y)
        pygame.draw.rect(surf,ROCK_COLOR,r)
