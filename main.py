#!/usr/bin/env python
from __future__ import print_function, division
import sys, math
import pygame
from pygame.locals import *
from PointsQueue import PointsQueue
import movementClient
import pointsClient

green=(0,255,0)

line_angle = 0
angle_indx = 0
dist_indx = 1
factor_distance = 1

SCREEN_WIDTH, SCREEN_HEIGHT = (700, 700)
ROBOT_MARKER_RADIUS = 10
RGB_GREEN = (0, 255, 0)
RGB_WHITE = (255, 255, 255)

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


##convert functions
def to_window(x, y):  # coordinate to window
    x, y = int(x), int(y)
    n_x = x + SCREEN_WIDTH // 2
    n_y = SCREEN_HEIGHT // 2 - y
    return ([n_x, n_y])


def to_radian(angle):
    x = (angle * 3.14) / 180
    return (x)


##

##draw function
def convert_to_catarsian(angle, distance):
    distance *= 10 * factor_distance
    angle = to_radian(angle)
    x, y = math.cos(angle) * distance, math.sin(angle) * distance
    pos = to_window(x, y)
    return pos


def draw_point(list_point, screen=screen):
    for point in list_point:
        pygame.draw.circle(screen, green, point, 2)


def draw_circles(screen=screen):
    raduis = 50
    for x in range(1, SCREEN_WIDTH // 2):
        n_raduis = ((x // raduis) + 1) * raduis
        pygame.draw.circle(screen, green, (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2), n_raduis, 2)


def draw_line(angle, screen=screen):
    a = math.tan(to_radian(angle))
    y = SCREEN_HEIGHT // 2
    if a == 0:
        y = 0
        if angle == 0:
            x = SCREEN_WIDTH / 2
        elif angle == 180:
            x = -SCREEN_WIDTH / 2
    else:
        x = y // a
        if angle > 180:
            x = -x

    if angle > 180:
        y = -y

    pos = to_window(x, y)
    pygame.draw.line(screen, green, (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2), pos, 2)


def draw_text(screen, text, t_size):
    fontObj = pygame.font.Font('freesansbold.ttf', t_size)
    textSurface = fontObj.render(text, True, (255, 255, 255))
    screen.blit(textSurface, (0, 0))

def dist_point_to_gui(point):
    l = list(point)
    l[dist_indx] = int(l[dist_indx])
    l[angle_indx] = int(l[angle_indx])
    return tuple(l)


def remove_dup_points(points):
    points_sorted = {}
    for i in points[::-1]:
        if i[angle_indx] in points_sorted:
            print("removed %d" % i[angle_indx])
            continue
        points_sorted.update({i[angle_indx]: i[dist_indx]})

    new_points = points_sorted.items()
    gui_points = []
    for i in new_points:
        gui_points.append(dist_point_to_gui(i))

    return gui_points


def update_screen(points):
    global line_angle
    screen.fill((0, 0, 0))
    draw_circles(screen)
    if len(points) < 1:
        return
    relv_points = remove_dup_points(points)
    screen_points = []
    for i in relv_points:
        screen_points.append(convert_to_catarsian(i[angle_indx], i[dist_indx]))

    print(screen_points)
    draw_point(screen_points)
    line_angle = (line_angle + 5) % 360
    draw_line(line_angle)


background = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
background.fill(RGB_WHITE)
background = background.convert()

# ------- blit the surfaces on the screen to make them visible
screen.blit(background, (0, 0))  # blit the background on the screen (overwriting all)

clock = pygame.time.Clock()
mainloop = True
FPS = 30  # desired framerate in frames per second. try out other values !
playtime = 0.0

speed = 50
leftSpeed = 0
rightSpeed = 0
prevLeftSpeed = 0
prevRightSpeed = 0

points_queue = PointsQueue(1000)
def draw_point(list_point,screen=screen):
    for point in list_point:
        pygame.draw.circle(screen,green,point,2)

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
                leftSpeed = -speed
                rightSpeed = -speed
            elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
                leftSpeed = 0
                rightSpeed = speed
            elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                leftSpeed = speed
                rightSpeed = 0
        elif event.type == pygame.KEYUP:
            if event.key in [pygame.K_UP, event.key == pygame.K_w, pygame.K_DOWN, pygame.K_s, pygame.K_LEFT, pygame.K_a,
                             pygame.K_RIGHT, pygame.K_d]:
                leftSpeed = 0
                rightSpeed = 0
    pygame.display.set_caption("Frame rate: {:0.2f} frames per second."
                               " Playtime: {:.2} seconds".format(
        clock.get_fps(), playtime))
    if leftSpeed != prevLeftSpeed or rightSpeed != prevRightSpeed:
        movementClient.send_movement(leftSpeed, rightSpeed)
        prevLeftSpeed = leftSpeed
        prevRightSpeed = rightSpeed
    else:
        movementClient.send_blank()

    points = pointsClient.get_points()
    points_queue.put(points)
    update_screen(points_queue.get())
    #render points

    pygame.display.flip()  # flip the screen like in a flipbook
