class Knight:
    def __init__(self, color):
        self.color = color
        self.symbol = 'N' if color == 'white' else 'n'

    def get_legal_moves(self, position, board):
        moves = []
        row, col = position
        knight_moves = [
            (2, 1), (2, -1), (-2, 1), (-2, -1),
            (1, 2), (1, -2), (-1, 2), (-1, -2)
        ]
        
        for dr, dc in knight_moves:
            new_row, new_col = row + dr, col + dc
            if 0 <= new_row < 8 and 0 <= new_col < 8:  # within board limits
                if board[new_row][new_col] is None or board[new_row][new_col].color != self.color:
                    moves.append((new_row, new_col))
        
        return moves