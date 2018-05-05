#!/usr/bin/env python
from __future__ import print_function, division
import pygame
import movementClient

pygame.init()

screenWidth, screenHeight = (640, 480)
screen = pygame.display.set_mode((screenWidth, screenHeight))

background = pygame.Surface((screenWidth, screenHeight))
background.fill((255, 255, 255))  # fill the background white
background = background.convert()

robotSurface = pygame.Surface((20, 20))
robotSurface.fill((255, 255, 255))
pygame.draw.circle(robotSurface, (0, 255, 0), (10, 10), 10)
robotSurface = robotSurface.convert()

# ------- blit the surfaces on the screen to make them visible
screen.blit(background, (0, 0))  # blit the background on the screen (overwriting all)
screen.blit(robotSurface, (screenWidth / 2 - 20, screenHeight / 2 - 20))
clock = pygame.time.Clock()
mainloop = True
FPS = 30  # desired framerate in frames per second. try out other values !
playtime = 0.0

speed = 50
leftSpeed = 0
rightSpeed = 0

while mainloop:
    milliseconds = clock.tick(FPS)  # do not go faster than this frame rate
    playtime += milliseconds / 1000.0
    # ----- event handler -----
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            movementClient.disconnect()
            mainloop = False  # pygame window closed by user
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                mainloop = False  # user pressed ESC
            elif event.key == pygame.K_UP or event.key == pygame.K_w:
                leftSpeed = speed
                rightSpeed = speed
            elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                leftSpeed = speed
                rightSpeed = speed
            elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
                leftSpeed = 0
                rightSpeed = speed
            elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                leftSpeed = speed
                rightSpeed = 0
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                leftSpeed = 0
                rightSpeed = 0
            elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                leftSpeed = 0
                rightSpeed = 0
            elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
                leftSpeed = 0
                rightSpeed = 0
            elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                leftSpeed = 0
                rightSpeed = 0
    pygame.display.set_caption("Frame rate: {:0.2f} frames per second."
                               " Playtime: {:.2} seconds".format(
        clock.get_fps(), playtime))
    movementClient.send_movement(leftSpeed, rightSpeed)
    pygame.display.flip()  # flip the screen like in a flipbook
