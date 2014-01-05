#!/bin/python
# -*- coding: utf-8 -*-

# PySnake
# A simple snake game using pygame lib
# Author : José Gonçalves

import pygame, sys, time, random
from pygame.locals import *


pygame.init()

#Game settings :
fpsClock = pygame.time.Clock()
playSurface = pygame.display.set_mode((640, 480))
pygame.display.set_caption('PySnake')

## Define some colors :
redColour = pygame.Color(255, 0, 0)
blackColour = pygame.Color(0, 0, 0)
whiteColour = pygame.Color(255, 255, 255)
greyColour = pygame.Color(150, 150, 150)

snakePosition = [100, 100]
snakeSegments = [[100,100], [80, 100], [60,100]]
fruitPosition = [300, 300]
fruitSpawned = 1
direction = 'right'
changeDirection = direction