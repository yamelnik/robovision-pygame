#!/usr/bin/env python
from __future__ import print_function, division
import pygame
import movementClient

SCREEN_WIDTH, SCREEN_HEIGHT = (640, 480)
ROBOT_MARKER_RADIUS = 10
RGB_GREEN = (0, 255, 0)
RGB_WHITE = (255, 255, 255)

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

background = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
background.fill(RGB_WHITE)
background = background.convert()

robot_surface_width = robot_surface_height = ROBOT_MARKER_RADIUS * 2
robot_surface = pygame.Surface((robot_surface_width, robot_surface_height))
robot_surface.fill(RGB_WHITE)
robot_surface_center_point = (robot_surface_width / 2, robot_surface_height / 2)
pygame.draw.circle(robot_surface, RGB_GREEN, robot_surface_center_point, ROBOT_MARKER_RADIUS)
robot_surface = robot_surface.convert()

# ------- blit the surfaces on the screen to make them visible
screen.blit(background, (0, 0))  # blit the background on the screen (overwriting all)
screen.blit(robot_surface, (SCREEN_WIDTH / 2 - robot_surface_width, SCREEN_HEIGHT / 2 - robot_surface_height))
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
