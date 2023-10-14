# Among Us Diagonal Chess

![Among Us Diagonal Chess Logo](https://example.com/amongus-diagonal-chess-logo.png)

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Game rules](#game-rules)
- [Requirements](#requirements)
- [Installation](#installation)
- [How to Play](#how-to-play)
- [Contributing](#contributing)
- [License](#license)

## Introduction

Among Us Diagonal Chess is a fun and exciting twist on the traditional game of chess, combining the popular game Among Us with the classic strategy of chesss. This open-source project aims to provide a unique and entertaining gaming experience for both chess and Among Us fans.

The game features a unique board design and rule set that brings a fresh perspective to chess while incorporating the fun and suspense of Among Us.

Whether you are an experienced chess player or new to the game, Among Us Diagonal Chess offers a thrilling and challenging experience.

![Game Screenshot](https://example.com/amongus-diagonal-chess-screenshot.png)

## Features

- Unique Among Us-inspired chess board.
- A blend of traditional chess rules and Among Us-themed elements.
- Multiplayer support, play with friends or online opponents.
- Intuitive user interface for easy gameplay.
- Customizable game settings for varied experiences.
- Ongoing development and updates to enhance gameplay.

## Game rules

The Board:

Among Us Diagonal Chess is played on an 8x8 grid, consisting of 64 alternating light and dark squares, with 4 vent positions located on specific black squares.

![Among Us Diagonal Chess Beginning Position](https://example.com/amongus-diagonal-chess-beginning-location.png)  

The Pieces:

King: The most important piece. It moves one square in any direction.
Queen: The most powerful piece. It can move diagonally, horizontally, or vertically any number of squares.
Rook: Moves horizontally or vertically any number of squares.
Bishop: Moves diagonally any number of squares.
Knight: Doesn't exist in our game.
Camel: It's C for Camel.
Pawn: Moves forward one square but captures straight(only forward). On its first move, a pawn has the option to move forward two squares. Pawns promote to any other piece (except a king) when they reach the opponent's back rank.
Plane: A piece that often catches people of guard. When two rooks are located next to each other any player can fly a plane trough them capturing both pieces.

Objective:

The primary goal is to checkmate your opponent's king, which means putting the king in a position where it is under attack and cannot move to a safe square.

Special Moves:

Castling: This is a move involving the king and either rook, which allows you to move the king two squares toward the rook and then move the rook to the square the king crossed. There are some conditions for castling:
Neither the king nor the chosen rook has moved before.
There are no pieces between the king and the chosen rook.
The king is not in check, and the squares the king crosses and lands on are not attacked by the opponent.
En Passant: If a pawn moves two squares forward from its starting position and lands beside an opponent's pawn, the opponent can capture the moving pawn as if it had only moved one square forward.
Pawn Promotion: When a pawn reaches the opponent's back rank, it is promoted to any other piece (except a king) of the player's choice.
Venting: When any piece (except a king) can move to a Square with a vent on it they can move to any other square with a vent on it that isn't already occupied.

Rules and Constraints:

A player must make a legal move during their turn.
The king is not allowed to move into or through a square that is under attack by the opponent.
Players take turns moving their pieces.
If a player's king is in check, they must make a move that removes the check. They can do this by moving the king, capturing the attacking piece, or blocking the attack.
Stalemate: If a player has no legal moves left and their king is not in check, the game results in a draw called a stalemate.

 O # O # X
###########
 X # X # O  
###########
 O # O # X

## Requirements

- Python 3.7 or higher
- [pygame](https://www.pygame.org/) library

## Installation

1. Clone the repository to your local machine:
   ```shell
   git clone https://github.com/Mithril64/XxGameSlamHackathonSlay3rxX.git
   ```

2. Install the required Python libraries using pip:
   ```shell
   pip install pygame
   ```

3. Run the game by executing `main.py`:
   ```shell
   python main.py
   ```

## How to Play

1. Launch the game using the installation instructions above.

2. Select your preferred game mode: single player, local multiplayer, or online multiplayer.

3. Start a new game, and the Among Us Diagonal Chess board will appear on your screen.

4. Use your mouse to select and move pieces following the standard chess rules.

5. Enjoy the game, strategize, and have fun!

## Contributing

We welcome contributions to enhance the game, fix bugs, or add new features. To contribute, follow these steps:

1. Fork this repository.

2. Create a new branch for your feature or bug fix:

   ```shell
   git checkout -b feature/your-feature-name
   ```

3. Make your changes.

4. Submit a pull request (PR) to the `main` branch of this repository.

## License

Among Us Diagonal Chess is released under the Creative Commons Zero v1.0 Universal
. You are free to use and modify the code as long as you follow the terms of the license.

Have fun playing Among Us Diagonal Chess! If you encounter any issues or have suggestions, please feel free to create an issue on this repository.
