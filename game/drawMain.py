# 1 - Import library
import pygame
from pygame.locals import *

class Drawing:
    def drawingBoard(self):
        # 2 - Initialize the game
        pygame.init()
        width, height = 1000, 700
        screen=pygame.display.set_mode((width, height))

        # 3 - Load images
        cat = pygame.image.load("../resources/images/Cat.png")
        dog = pygame.image.load("../resources/images/Dog.png")
        dolphin = pygame.image.load("../resources/images/Dolphin.png")
        duck = pygame.image.load("../resources/images/Duck.png")
        horse = pygame.image.load("../resources/images/Horse.png")
        lion = pygame.image.load("../resources/images/Lion.png")
        pigeon = pygame.image.load("../resources/images/Pigeon.png")
        rabbit = pygame.image.load("../resources/images/Rabbit.png")
        swan = pygame.image.load("../resources/images/Swan.png")
        tiger = pygame.image.load("../resources/images/Tiger.png")


        # 5 - clear the screen before drawing it again
        white = (255, 255, 255)
        screen.fill(white)

        w, h = 10, 10;
        Matrix = [[0 for x in range(w)] for y in range(h)]

        Matrix[0][0] = cat
        Matrix[0][1] = dog
        Matrix[0][2] = dolphin
        Matrix[0][3] = duck
        Matrix[0][4] = horse
        Matrix[0][5] = lion
        Matrix[0][6] = pigeon
        Matrix[0][7] = rabbit
        Matrix[0][8] = swan
        Matrix[0][9] = tiger

        s = 0
        while 1:
            screen.blit(Matrix[0][0], (0, 0))
            screen.blit(Matrix[0][1], (100, 0))
            screen.blit(Matrix[0][2], (200, 0))
            screen.blit(Matrix[0][3], (300, 0))
            screen.blit(Matrix[0][4], (400, 0))
            screen.blit(Matrix[0][5], (500, 0))
            screen.blit(Matrix[0][6], (600, 0))
            screen.blit(Matrix[0][7], (700, 0))
            screen.blit(Matrix[0][8], (800, 0))
            screen.blit(Matrix[0][9], (900, 0))

            pygame.display.flip()


            # 8 - loop through the events
            for event in pygame.event.get():
                # check if the event is the X button
                if event.type == pygame.QUIT:
                    # if it is quit the game
                    pygame.quit()
                    exit(0)

