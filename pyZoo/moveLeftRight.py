import pygame
import random
from pyZoo.drawMain import Drawing
from pygame.locals import *

class MoveManage:
    drawing = Drawing()

    matrix = [[0 for x in range(10)] for y in range(10)]
    matrix = drawing.createMatrix()
    screen = drawing.drawingWhiteBoard()
    clock = pygame.time.Clock()

    random_index_x = 0
    random_index_y = random.choice([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    drawing.drawAnimalWithKeyEvents(screen, matrix, random_index_x, random_index_y)
    clock.tick(60)