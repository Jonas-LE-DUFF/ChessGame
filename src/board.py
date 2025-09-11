class Board:

    def __init__(self):
        self.board = [[None for _ in range(8)] for _ in range(8)]
        self.setup_board()


    def show(self):
        for row in self.board:
            print(' '.join([piece.symbol if piece else '.' for piece in row]))

    def setup_board(self):
        from pieces.king import King
        # Add other pieces similarly
        self.board[0][4] = King('black')
        self.board[7][4] = King('white')
        # Add other pieces similarly

    def find_piece(self, piece):
        for r in range(8):
            for c in range(8):
                if self.board[r][c] == piece:
                    return (r, c)
        return None