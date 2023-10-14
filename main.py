import pygame

# Initialize Pygame
pygame.init()

# Set the dimensions of the screen
screen_width = 640
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

# Set the title of the window
pygame.display.set_caption("Chess Board")

# Define colors
white = (0,120,255)
black = (1,255,31)

# Set the size of each square on the board
square_size = screen_width // 8

# Create the chess board
chess_board = []
for row in range(8):
    chess_board.append([])
    for column in range(8):
        if (row + column) % 2 == 0:
            chess_board[row].append(white)
        else:
            chess_board[row].append(black)

# Set up the pieces
pieces = [
    [" ", " ", " ", "P", "K", "R", "N", "K"],
    [" ", " ", " ", "P", "P", " ", "Q", "B"],
    [" ", " ", " ", " ", "P", "B", " ", "R"],
    ["p", "p", " ", " ", " ", "P", "P", "N"],
    ["n", "p", "p", " ", " ", " ", "P", "P"],
    ["r", " ", "b", "p", " ", " ", " ", " "],
    ["b", "q", " ", "p", "p", " ", " ", " "],
    ["k", "n", "r", " ", "p", " ", " ", " "]
]

# Load the images for the pieces
piece_images = {
    "R": pygame.image.load("assets/Chess_rlt60.png"),
    "N": pygame.image.load("assets/Chess_nlt60.png"),
    "B": pygame.image.load("assets/Chess_blt60.png"),
    "Q": pygame.image.load("assets/Chess_qlt60.png"),
    "K": pygame.image.load("assets/Chess_klt60.png"),
    "P": pygame.image.load("assets/Chess_plt60.png"),
    "r": pygame.image.load("assets/Chess_rdt60.png"),
    "n": pygame.image.load("assets/Chess_ndt60.png"),
    "b": pygame.image.load("assets/Chess_bdt60.png"),
    "q": pygame.image.load("assets/Chess_qdt60.png"),
    "k": pygame.image.load("assets/Chess_kdt60.png"),
    "p": pygame.image.load("assets/Chess_pdt60.png")
}

# Draw the chess board and pieces
for row in range(8):
    for column in range(8):
        pygame.draw.rect(screen, chess_board[row][column], (column * square_size, row * square_size, square_size, square_size))
        piece = pieces[row][column]
        if piece != " ":
            screen.blit(piece_images[piece], (column * square_size + 10, row * square_size + 10))

# Update the screen
pygame.display.update()

# Run the game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

# Quit Pygame
pygame.quit()
