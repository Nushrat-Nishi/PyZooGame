# 1 - Import library
import pygame
import random

from pygame.locals import *

class Drawing:
    def createMatrix(self):
        # 3 - Load images
        self.cat = pygame.image.load("../resources/images/Cat.png")
        self.dog = pygame.image.load("../resources/images/Dog.png")
        self.dolphin = pygame.image.load("../resources/images/Dolphin.png")
        self.duck = pygame.image.load("../resources/images/Duck.png")
        self.horse = pygame.image.load("../resources/images/Horse.png")
        self.lion = pygame.image.load("../resources/images/Lion.png")
        self.pigeon = pygame.image.load("../resources/images/Pigeon.png")
        self.rabbit = pygame.image.load("../resources/images/Rabbit.png")
        self.swan = pygame.image.load("../resources/images/Swan.png")
        self.tiger = pygame.image.load("../resources/images/Tiger.png")

        w, h = 10, 10;
        Matrix = [[0 for x in range(w)] for y in range(h)]

        Matrix[0][0] = self.cat
        Matrix[0][1] = self.dog
        Matrix[0][2] = self.dolphin
        Matrix[0][3] = self.duck
        Matrix[0][4] = self.horse
        Matrix[0][5] = self.lion
        Matrix[0][6] = self.pigeon
        Matrix[0][7] = self.rabbit
        Matrix[0][8] = self.swan
        Matrix[0][9] = self.tiger

        return Matrix

    def drawingWhiteBoard(self):
        # 2 - Initialize the pyZoo
        pygame.init()
        self.width, self.height = 1000, 700
        screen=pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption('PyZooGame')

        # 5 - clear the screen before drawing it again
        return screen

    def drawAnimalWithKeyEvents(self, screen, matrix, random_index_x, random_index_y):

        x = self.width*0.45
        y = self.height*0.8

        x_change = 0
        while 1:
            # 8 - loop through the events
            for event in pygame.event.get():
                # check if the event is the X button
                if event.type == pygame.QUIT:
                    # if it is quit the pyZoo
                    pygame.quit()
                    quit()
                    exit(0)

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        x_change = -1

                    if event.key == pygame.K_RIGHT:
                        x_change = 1

                if event.type == pygame.KEYUP:
                    if event.key ==pygame.K_LEFT or event.key == pygame.K_RIGHT:
                        x_change = 0

            x += x_change
            white = (255, 255, 255)
            screen.fill(white)
            self.drawAnimalFromMatrix(screen, matrix, random_index_x, random_index_y, x, y)
            pygame.display.update()


    def drawAnimalFromMatrix(self, screen, matrix, random_index_x, random_index_y, x, y):
        screen.blit(matrix[0][0], (0, 0))
        screen.blit(matrix[0][1], (100, 0))
        screen.blit(matrix[0][2], (200, 0))
        screen.blit(matrix[0][3], (300, 0))
        screen.blit(matrix[0][4], (400, 0))
        screen.blit(matrix[0][5], (500, 0))
        screen.blit(matrix[0][6], (600, 0))
        screen.blit(matrix[0][7], (700, 0))
        screen.blit(matrix[0][8], (800, 0))
        screen.blit(matrix[0][9], (900, 0))
        screen.blit(matrix[random_index_x][random_index_y], (x, y))




