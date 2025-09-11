class King:
    def __init__(self, color):
        self.color = color
        self.symbol = 'K' if color == 'white' else 'k'

    def get_legal_moves(self, position, board):
        legal_moves = []
        row, col = position
        directions = [(-1, -1), (-1, 0), (-1, 1),
                      (0, -1),          (0, 1),
                      (1, -1), (1, 0), (1, 1)]
        
        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            if (0 <= new_row < 8 and 0 <= new_col < 8):
                target_square = board[new_row][new_col]
                if target_square is None or target_square.color != self.color:
                    legal_moves.append((new_row, new_col))
            
        return legal_moves