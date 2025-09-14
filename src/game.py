from board import Board
from pieces.king import King
from endGame import EndGame

import pygame
from pygame.locals import *

class Game:
    def __init__(self):
        self.board = Board()
        self.board.show()
        self.player_turn = 'white'

    def get_legal_moves(self, position):
        row, col = position
        piece = self.board.board[row][col]
        if piece is None:
            print("No piece at the selected position.")
            return []
        if piece.color != self.player_turn:
            print(f"It's {self.player_turn}'s turn. Please select your own piece.")
            return []
        return piece.get_legal_moves(position, self.board.board)
        
    def switch_turn(self):
        self.player_turn = 'black' if self.player_turn == 'white' else 'white'
        print(f"It's now {self.player_turn}'s turn.")
    

    def run(self):
        
        EndGame().show_winning_screen("white")  # Temporary call to show winning screen
         # Initialise screen
        pygame.init()
        screen = pygame.display.set_mode((640, 640))
        pygame.display.set_caption('Basic Pygame program')
    
        # Fill background
        background = pygame.Surface(screen.get_size())
        background = background.convert()
        background.fill((250, 250, 250))

        # Blit everything to the screen
        screen.blit(background, (0, 0))
        pygame.display.flip()
    
        # Event loop
        self.board.showpygame(screen)
        moves = []
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    return
                if event.type == MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    col = pos[0] // 80
                    row = pos[1] // 80
                    print(f"Mouse clicked at pixel {pos}, grid position {(row, col)}")
                    print("piece selected: ", self.board.selected_piece.piece)
                    if self.board.selected_piece.piece != None:
                        if (row, col) in moves:
                            print(f"Moving piece to {(row, col)}")
                            self.board.move_selected_piece((row, col))
                            winner = self.checkWinner()
                            if winner:
                                if not EndGame().show_winning_screen(winner):
                                    return
                                else:
                                    self.board = Board()
                                    self.player_turn = 'white'
                            else:
                                self.switch_turn()
                            self.board.showpygame(screen)
                        else:
                            print("Invalid move. Try again.")
                    
                    moves = self.get_legal_moves((row, col))
                    print(f"Valid moves: {moves}")
                    if(len(moves) > 0):
                        self.board.select_piece((row, col), moves)
                        self.board.showpygame(screen)

            pygame.display.flip()
        
            
    def checkWinner(self):
        if self.board.find_piece(King('white')) is None:
            print("Black wins!")
            return 'black'
        if self.board.find_piece(King('black')) is None:
            print("White wins!")
            return 'white'
        return False