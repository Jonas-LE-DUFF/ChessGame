class Pawn:
    def __init__(self, color):
        self.color = color
        self.symbol = 'P' if color == 'white' else 'p'

    def get_legal_moves(self, position, board):
        moves = []
        row, col = position
        direction = -1 if self.color == 'white' else 1  # white moves up, black moves down

        # Move forward
        if 0 <= row + direction < 8:
            if board[row + direction][col] is None:  # empty square
                moves.append((row + direction, col))
                # First move can be two squares
                if (self.color == 'white' and row == 6) or (self.color == 'black' and row == 1):
                    if board[row + 2 * direction][col] is None:
                        moves.append((row + 2 * direction, col))

        # Capture diagonally
        for dc in [-1, 1]:
            if 0 <= col + dc < 8 and 0 <= row + direction < 8:
                target_square = board[row + direction][col + dc]
                if target_square is not None and target_square.color != self.color:
                    moves.append((row + direction, col + dc))

        return moves
