import pygame
import os
from engine import ChessEngine
from ai import ChessAI


WIDTH, HEIGHT = 890, 890
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
FPS = 1
pygame.display.set_caption("chess")
GREY = (72, 72, 72)
CREAM = (250, 229, 210)

WR = pygame.image.load(os.path.join("assets", "White Rook.png")).convert_alpha()
BR = pygame.image.load(os.path.join("assets", "Black Rook.png")).convert_alpha()

WC = pygame.image.load(os.path.join("assets", "White Castle.png")).convert_alpha()
BC = pygame.image.load(os.path.join("assets", "Black Castle.png")).convert_alpha()

WH = pygame.image.load(os.path.join("assets", "White Horse.png")).convert_alpha()
BH = pygame.image.load(os.path.join("assets", "Black Horse.png")).convert_alpha()

WB = pygame.image.load(os.path.join("assets", "White Bishop.png")).convert_alpha()
BB = pygame.image.load(os.path.join("assets", "Black Bishop.png")).convert_alpha()

WQ = pygame.image.load(os.path.join("assets", "White Queen.png")).convert_alpha()
BQ = pygame.image.load(os.path.join("assets", "Black Queen.png")).convert_alpha()

WK = pygame.image.load(os.path.join("assets", "White King.png")).convert_alpha()
BK = pygame.image.load(os.path.join("assets", "Black King.png")).convert_alpha()


def draw_background():
    '''
    Draws the background checkboard
    '''
    x = 5
    y = 5
    grey = False
    for _ in range(8):
        for _ in range(8):
            if grey:
                pygame.draw.rect(WIN, GREY, pygame.Rect(x, y, 110, 110))
            else:
                pygame.draw.rect(WIN, CREAM, pygame.Rect(x, y, 110, 110))
            x += 110
            grey = not grey
        grey = not grey
        y += 110
        x = 5

    pygame.display.update()


def draw_window(board):
    '''
    Draws the window onto the screen given a 2D array of the board
    '''

    i = 10
    j = 10
    for x, v_x in enumerate(board):
        for y, v_y in enumerate(v_x):
            if v_y != "":
                exec(f"WIN.blit({v_y}, ({i}, {j}))")
            i += 110
        j += 110
        i = 10

    pygame.display.update()


def main():
    engine = ChessEngine()        # Creates a new instance of the game engine object that will be used to store the current game state
    clock = pygame.time.Clock()
    run = True

    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        draw_background()
        draw_window(engine.board)

    pygame.quit()

if __name__ == "__main__":
    main()