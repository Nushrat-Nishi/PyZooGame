from game.drawMain import *

class moveManage:
    drawing = Drawing()
    drawing.drawingBoard()

    p = 500
    screen.blit(Matrix[0][0], (p, 500))

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            screen.blit(Matrix[0][0], (p + 100, 500))
        if event.key == pygame.K_RIGHT:
            screen.blit(Matrix[0][0], (p - 100, 500))