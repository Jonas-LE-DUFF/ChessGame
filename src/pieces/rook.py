class Rook:
    def __init__(self, color):
        self.color = color
        self.symbol = 'R' if color == 'white' else 'r'

    def get_valid_moves(self, position, board):
        moves = []
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]  # vertical and horizontal directions
        for direction in directions:
            x, y = position
            while True:
                x += direction[0]
                y += direction[1]
                if 0 <= x < 8 and 0 <= y < 8:  # within board limits
                    if board[x][y] is None:  # empty square
                        moves.append((x, y))
                    elif board[x][y].color != self.color:  # opponent's piece
                        moves.append((x, y))
                        break
                    else:  # own piece
                        break
                else:
                    break
        return moves