class Piece:
    def __init__(self, color):
        self.color = color
        self.symbol = '?'  # Default symbol, should be overridden by subclasses

    def get_legal_moves(self, position, board):
        raise NotImplementedError("This method should be overridden by subclasses")
    
    