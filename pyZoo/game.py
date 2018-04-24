# 1 - Import library
import pygame
from pygame.locals import *

# 2 - Initialize the pyZoo
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

# 6 - draw the screen elements
screen.blit(cat, (0,0))
screen.blit(dog, (100,0))
screen.blit(dolphin, (200,0))
screen.blit(duck, (300,0))
screen.blit(horse, (400,0))
screen.blit(lion, (500,0))
screen.blit(pigeon, (600,0))
screen.blit(rabbit, (700,0))
screen.blit(swan, (800,0))
screen.blit(tiger, (900,0))

# 4 - keep looping through
while 1:
    # 7 - update the screen
    pygame.display.flip()
    # 8 - loop through the events
    for event in pygame.event.get():
        print("event.type value: ", event.type)
        print("pygame.QUIT value: ", pygame.QUIT)
        # check if the event is the X button
        if event.type==pygame.QUIT:
            # if it is quit the pyZoo
            pygame.quit()
            exit(0)

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                screen.fill(0)
                screen.blit(cat, (100, 100))
            if event.key == pygame.K_RIGHT:
                screen.fill(0)
                screen.blit(dog, (500, 100))



w, h = 8, 5;
Matrix = [[0 for x in range(w)] for y in range(h)]

Matrix[0][0] = 1
Matrix[6][0] = 3 # error! range...
Matrix[0][6] = 3 # valid

print (Matrix[0][0]) # prints 1
x, y = 0, 6
print (Matrix[x][y]) # prints 3; be careful with indexing!