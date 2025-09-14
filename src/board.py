from pieces.king import King
from pieces.rook import Rook
from pieces.pawn import Pawn
from pieces.queen import Queen
from pieces.bishop import Bishop
from pieces.knight import Knight

import pygame

class Board:
    class SelectedPiece:
        def __init__(self, piece=None, position=None, legal_moves=[]):
            self.piece = piece
            self.position = position
            self.legal_moves = legal_moves

    def __init__(self):
        self.board = [[None for _ in range(8)] for _ in range(8)]
        self.setup_board()
        self.selected_piece = self.SelectedPiece()
        
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
                if(self.selected_piece.position == (r, c)):
                    pygame.draw.rect(screen, (0, 255, 0), (c * 80, r * 80, 80, 80), 5)  # Highlight selected piece
                if (r, c) in self.selected_piece.legal_moves:
                    pygame.draw.rect(screen, (0, 0, 255), (c * 80 + 30, r * 80 + 30, 20, 20))  # Draw legal move indicator
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
    
    def select_piece(self, position, legal_moves=[]):
        row, col = position
        piece = self.board[row][col]
        if piece is None:
            print("No piece at the selected position.")
            return
        self.selected_piece = self.SelectedPiece(piece, position, legal_moves)
        print("Piece selected:", piece.symbol)

    #considering a piece is selected and can be moved to given position
    def move_selected_piece(self, to_pos):
        print("move_piece called with from_pos:", self.selected_piece.position, "to_pos:", to_pos)
        self.board[to_pos[0]][to_pos[1]] = self.selected_piece.piece
        self.board[self.selected_piece.position[0]][self.selected_piece.position[1]] = None
        self.selected_piece = self.SelectedPiece()  # Deselect piece after moving


