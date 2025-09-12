from pieces.king import King
from pieces.rook import Rook
from pieces.pawn import Pawn
from pieces.queen import Queen
from pieces.bishop import Bishop
from pieces.knight import Knight
class Board:

    def __init__(self):
        self.board = [[None for _ in range(8)] for _ in range(8)]
        self.setup_board()


    def show(self):
        for row in self.board:
            print(' '.join([piece.symbol if piece else '.' for piece in row]))

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