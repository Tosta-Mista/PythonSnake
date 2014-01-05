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
playerScore = 0


def gameOver():
    """
    Name : gameOver()
    Desc : GameOver() write the words "Game Over" during 5 seconds and quit the game.
    """
    gameOverFont = pygame.font.Font('freesansbold.ttf', 72)
    gameOverSurf = gameOverFont.render('Game Over', True, greyColour)
    gameOverRect = gameOverSurf.get_rect()
    gameOverRect.midtop = (320, 10)
    gameOverScore = gameOverFont.render('Score :' + str(playerScore), True, redColour)
    scoreRect = gameOverScore.get_rect()
    scoreRect.midtop = (320, 100)
    playSurface.blit(gameOverScore, scoreRect)
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
            # Key Bindings :
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

    # Key Binding comparaison :
    if changeDirection == 'right' and not direction == 'left':
        direction = changeDirection
    if changeDirection == 'left' and not direction == 'right':
        direction = changeDirection
    if changeDirection == 'up' and not direction == 'down':
        direction = changeDirection
    if changeDirection == 'down' and not direction == 'up':
        direction = changeDirection

    # Movement settings :
    if direction == 'right':
        snakePosition[0] += 20
    if direction == 'left':
        snakePosition[0] -= 20
    if direction == 'up':
        snakePosition[1] -= 20
    if direction == 'down':
        snakePosition[1] += 20

    # Initiate Snake Segments, each time python reach this line
    # it will increase the length of the snake's body :
    snakeSegments.insert(0, list(snakePosition))

    # The first instruction check if the X and Y coordinates of
    # the snake's head to see if it matches the X and Y coordinates
    # of the fruit the target player is chasing. If the values match
    # the fruit is cosidered to have been eaten by the snake.
    if snakePosition[0] == fruitPosition[0] and snakePosition[1] == fruitPosition[1]:
        fruitSpawned = 0
        playerScore += 10
    else:
        snakeSegments.pop()

    # Create fruit Spawn:
    if fruitSpawned == 0:
        x = random.randrange(1, 32)
        y = random.randrange(1, 24)
        fruitPosition = [int(x * 20), int(y * 20)]
    fruitSpawned = 1

    # Draw something at the screen:
    playSurface.fill(blackColour)
    for position in snakeSegments:
        pygame.draw.rect(playSurface, whiteColour, Rect(position[0], position[1], 20, 20))
        pygame.draw.rect(playSurface, redColour, Rect(fruitPosition[0], fruitPosition[1], 20, 20))
    pygame.display.flip()

    # When the player die :
    if snakePosition[0] > 620 or snakePosition[0] < 0:
        gameOver()
    if snakePosition[1] > 460 or snakePosition[1] < 0:
        gameOver()

    for snakeBody in snakeSegments[1:]:
        if snakePosition[0] == snakeBody[0] and snakePosition[1] == snakeBody[1]:
            gameOver()

    # Set control speed for the game :
    fpsClock.tick(10)