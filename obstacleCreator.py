import pygame
import pointsClient

RGB_BLACK = (0, 0, 0)
OBSTACLE_POINT_RADIUS = 3


def draw_obstacles(surface, obstacles):
    for obstacle in obstacles:
        point = (obstacle["x"], obstacle["y"])
        pygame.draw.circle(surface, RGB_BLACK, point, OBSTACLE_POINT_RADIUS)
