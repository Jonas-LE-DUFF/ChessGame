class Board:

    def __init__(self):
        self.board = [[None for _ in range(8)] for _ in range(8)]
        self.setup_board()


    def show(self):
        for row in self.board:
            print(' '.join([piece.symbol if piece else '.' for piece in row]))

    def setup_board(self):
        from pieces.king import King
        self.board[0][4] = King('black')
        self.board[7][4] = King('white')

        from pieces.rook import Rook
        self.board[0][0] = Rook('black')
        self.board[0][7] = Rook('black')
        self.board[7][0] = Rook('white')
        self.board[7][7] = Rook('white')

    def find_piece(self, piece):
        for r in range(8):
            for c in range(8):
                pieceFound = self.board[r][c]
                if pieceFound is not None and pieceFound.symbol == piece.symbol and pieceFound.color == piece.color:
                    return (r, c)
        return None