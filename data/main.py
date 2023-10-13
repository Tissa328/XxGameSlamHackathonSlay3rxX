import pygame
from data.classes.board import drawBoard
pygame.init()

gameExit = False

white = (255, 255, 255)
black = (0, 0, 0)
size = 75

gameDisplay = pygame.display.set_mode((600, 600))

gameDisplay = drawBoard(gameDisplay, size)
gameDisplay.draw_board()


while not gameExit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit = True
    pygame.display.update()
