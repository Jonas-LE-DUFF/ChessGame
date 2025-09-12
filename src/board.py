from pieces.king import King
from pieces.rook import Rook
from pieces.pawn import Pawn
from pieces.queen import Queen
from pieces.bishop import Bishop
from pieces.knight import Knight

import pygame

class Board:

    def __init__(self):
        self.board = [[None for _ in range(8)] for _ in range(8)]
        self.setup_board()
        black_queen = pygame.image.load('assets/png/black_queen.png')
        black_queen = pygame.transform.scale(black_queen, (80, 80))
        white_queen = pygame.image.load('assets/png/white_queen.png')
        white_queen = pygame.transform.scale(white_queen, (80, 80))
        black_king = pygame.image.load('assets/png/black_king.png')
        black_king = pygame.transform.scale(black_king, (80, 80))
        white_king = pygame.image.load('assets/png/white_king.png')
        white_king = pygame.transform.scale(white_king, (80, 80))
        black_pawn = pygame.image.load('assets/png/black_pawn.png')
        black_pawn = pygame.transform.scale(black_pawn, (80, 80))
        white_pawn = pygame.image.load('assets/png/white_pawn.png')
        white_pawn = pygame.transform.scale(white_pawn, (80, 80))
        black_rook = pygame.image.load('assets/png/black_rook.png')
        black_rook = pygame.transform.scale(black_rook, (80, 80))
        white_rook = pygame.image.load('assets/png/white_rook.png')
        white_rook = pygame.transform.scale(white_rook, (80, 80))
        black_bishop = pygame.image.load('assets/png/black_bishop.png')
        black_bishop = pygame.transform.scale(black_bishop, (80, 80))
        white_bishop = pygame.image.load('assets/png/white_bishop.png')
        white_bishop = pygame.transform.scale(white_bishop, (80, 80))
        black_knight = pygame.image.load('assets/png/black_knight.png') 
        black_knight = pygame.transform.scale(black_knight, (80, 80))
        white_knight = pygame.image.load('assets/png/white_knight.png')
        white_knight = pygame.transform.scale(white_knight, (80, 80))
        self.piece_to_image = {
            'q': black_queen,
            'Q': white_queen,
            'k': black_king,
            'K': white_king,
            'p': black_pawn,
            'P': white_pawn,
            'r': black_rook,
            'R': white_rook,
            'b': black_bishop,
            'B': white_bishop,
            'n': black_knight,
            'N': white_knight
        }


    def show(self):
        for row in self.board:
            print(' '.join([piece.symbol if piece else '.' for piece in row]))

    def getImage(self, piece):
        for letter in self.piece_to_image:
            if piece.symbol == letter:
                return self.piece_to_image[letter]
        

    def showpygame(self, screen):
        for r in range(8):
            for c in range(8):
                if(r + c) % 2 == 0:
                    pygame.draw.rect(screen, (186, 146, 108), (c * 80, r * 80, 80, 80))  # Draw black square
                else:
                    pygame.draw.rect(screen, (255, 255, 255), (c * 80, r * 80, 80, 80))  # Draw white square

                piece = self.board[r][c]
                if piece is not None:
                    image = self.getImage(piece)
                    screen.blit(image, (c * 80, r * 80))
        pygame.display.flip()

    def setup_board(self):
        self.board[0][4] = King('black')
        self.board[7][4] = King('white')

        self.board[0][0] = Rook('black')
        self.board[0][7] = Rook('black')
        self.board[7][0] = Rook('white')
        self.board[7][7] = Rook('white')

        for col in range(8):
            self.board[6][col] = Pawn('white')

        for col in range(8):
            self.board[1][col] = Pawn('black')
        
        self.board[0][3] = Queen('black')
        self.board[7][3] = Queen('white')

        self.board[0][2] = Bishop('black')
        self.board[0][5] = Bishop('black')
        self.board[7][2] = Bishop('white')
        self.board[7][5] = Bishop('white')

        self.board[0][1] = Knight('black')
        self.board[0][6] = Knight('black')
        self.board[7][1] = Knight('white')
        self.board[7][6] = Knight('white')

    def find_piece(self, piece):
        for r in range(8):
            for c in range(8):
                pieceFound = self.board[r][c]
                if pieceFound is not None and pieceFound.symbol == piece.symbol and pieceFound.color == piece.color:
                    return (r, c)
        return None