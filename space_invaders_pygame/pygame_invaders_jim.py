import pygame
import os
from pygame.locals import *
from random import randint
from sys import exit

#
pygame.init()
clock = pygame.time.Clock()
laser = pygame.mixer.Sound("sounds\\laser.mp3  ")
laser.play()


while pygame.mixer.get_busy():
    clock.tick()

