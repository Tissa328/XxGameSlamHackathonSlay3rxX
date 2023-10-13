import pygame
pygame.init()

gameExit = False

(width, height) = (800, 800)
white = (255, 255, 255)
black = (0, 0, 0)
size = 100

gameDisplay = pygame.display.set_mode((width, height))
gameDisplay.fill(white)

while not gameExit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit = True
    for x in range(0, 8):
        if x % 2 == 0:
            for y in range(0, 8, 2):
                pygame.draw.rect(gameDisplay, (0, 0, 0), (x * size, y * size, size, size))
        else:
            for y in range(1, 8, 2):
                pygame.draw.rect(gameDisplay, (0, 0, 0), (x * size, y * size, size, size))
    pygame.display.update()