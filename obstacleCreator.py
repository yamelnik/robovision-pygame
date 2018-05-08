import pygame
import pointsClient

RGB_BLACK = (0, 0, 0)
OBSTACLE_POINT_RADIUS = 3


def get_obstacles():
    """
    Translate points from client to screen coordinates
    :return: An array of screen coordinates.
    """
    return pointsClient.get_points()


def draw_obstacles(surface):
    obstacles = get_obstacles()
    for obstacle in obstacles:
        point = (obstacle["x"], obstacle["y"])
        pygame.draw.circle(surface, RGB_BLACK, point, OBSTACLE_POINT_RADIUS)
