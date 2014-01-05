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
snakeSegments = [[100, 100], [80, 100], [60, 100]]
fruitPosition = [300, 300]
fruitSpawned = 1
direction = 'right'
changeDirection = direction


def gameOver():
    """
    Name : gameOver()
    Desc : GameOver() write the words "Game Over" during 5 seconds and quit the game.
    """
    gameOverFont = pygame.font.Font('freesansbold.ttf', 72)
    gameOverSurf = gameOverFont.render('Game Over', True, greyColour)
    gameOverRect = gameOverSurf.get_rect()
    gameOverRect.midtop = (320, 10)
    playSurface.blit(gameOverSurf, gameOverRect)
    pygame.display.flip()
    time.sleep(5)
    pygame.quit()
    sys.exit()


# Main loop :
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN:
            if event.key == K_RIGHT or event.key == ord('d'):
                changeDirection = 'right'
            if event.key == K_LEFT or event.key == ord('a'):
                changeDirection = 'left'
            if event.key == K_UP or event.key == ord('w'):
                changeDirection = 'up'
            if event.key == K_DOWN or event.key == ord('s'):
                changeDirection = 'down'
            if event.key == K_ESCAPE:
                pygame.event.post(pygame.event.Event(QUIT))