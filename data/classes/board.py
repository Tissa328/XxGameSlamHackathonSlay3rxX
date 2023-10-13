import pygame

gameDisplay = pygame.display.set_mode((600, 600))
gameDisplay.fill((0, 0, 0))
size = 75
class drawBoard:
    def __init__(self, gameDisplay, size):
        self.gameDisplay = pygame.display.set_mode((600, 600))
        self.size = 75
        self.gameDisplay.fill((0, 0, 0))
    def draw_board(self):
        for x in range(0, 8):
            if x % 2 == 0:
                for y in range(0, 8, 2):
                    pygame.draw.rect(self.gameDisplay, (255, 255, 255), (x * self.size, y * self.size, self.size, self.size))
            else:
                for y in range(1, 8, 2):
                    pygame.draw.rect(self.gameDisplay, (255, 255, 255), (x * self.size, y * self.size, self.size, self.size))
