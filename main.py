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
white = (227,255,0)
black = (1,255,31)
green = (0, 255, 0)

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
    [" ", " ", " ", "P", " ", "R", "N", "K"],
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

# Create a dictionary to map piece names to their values
piece_values = {
    "R": 5,
    "N": 3,
    "B": 3,
    "Q": 9,
    "K": 1000,
    "P": 1,
    "r": -5,
    "n": -3,
    "b": -3,
    "q": -9,
    "k": -1000,
    "p": -1
}

# Create a list to store the positions of the pieces
piece_positions = []
for row in range(8):
    piece_positions.append([])
    for column in range(8):
        piece = pieces[row][column]
        if piece != " ":
            piece_positions[row].append((piece, piece_values[piece]))
        else:
            piece_positions[row].append(None)


# Create a function to get the row and column of a square given its x and y coordinates
def get_row_column(x, y):
    row = y // square_size
    column = x // square_size
    return row, column


# Create a function to get the piece at a given row and column
def get_piece(row, column):
    return piece_positions[row][column]


# Create a function to set the piece at a given row and column
def set_piece(row, column, piece):
    piece_positions[row][column] = piece


# Create a function to remove the piece at a given row and column
def remove_piece(row, column):
    piece_positions[row][column] = None


# Draw the chess board and pieces
for row in range(8):
    for column in range(8):
        pygame.draw.rect(screen, chess_board[row][column],
                         (column * square_size, row * square_size, square_size, square_size))
        piece = pieces[row][column]
        if piece != " ":
            screen.blit(piece_images[piece], (column * square_size, row * square_size))

# Update the screen
pygame.display.update()

# Run the game loop
selected_piece = None
selected_piece_row = None
selected_piece_column = None
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            row, column = get_row_column(x, y)
            piece = get_piece(row, column)
            if piece is not None:
                selected_piece = piece
                selected_piece_row = row
                selected_piece_column = column
        elif event.type == pygame.MOUSEBUTTONUP:
            if selected_piece is not None:
                x, y = event.pos
                row, column = get_row_column(x, y)
                if row != selected_piece_row or column != selected_piece_column:
                    set_piece(row, column, selected_piece)
                    remove_piece(selected_piece_row, selected_piece_column)
                selected_piece = None
                selected_piece_row = None
                selected_piece_column = None

    # Draw the chess board and pieces
    for row in range(8):
        for column in range(8):
            pygame.draw.rect(screen, chess_board[row][column],
                             (column * square_size, row * square_size, square_size, square_size))
            piece = get_piece(row, column)
            if piece is not None:
                screen.blit(piece_images[piece[0]], (column * square_size, row * square_size))

    # Highlight the selected piece
    if selected_piece is not None:
        pygame.draw.rect(screen, green, (
        selected_piece_column * square_size, selected_piece_row * square_size, square_size, square_size), 3)

    # Update the screen
    pygame.display.update()

# Quit Pygame
pygame.quit()