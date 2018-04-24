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
    x = 500
    y = 600
    print("random random_index_x : ", random_index_x)
    print("random random_index_y : ", random_index_y)
    print("x : ", x)
    print("y : ", y)

    #drawing.drawAnimalList(screen, matrix, random_index_x, random_index_y, x, y)
    drawing.drawPlayer(screen, matrix, random_index_x, random_index_y, x, y)