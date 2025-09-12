class Piece:
    def __init__(self, color):
        self.color = color
        self.symbol = '?'  # Default symbol, should be overridden by subclasses

    def get_legal_moves(self, position, board):
        raise NotImplementedError("This method should be overridden by subclasses")
    
    def draw(self, position, screen):
        from utilities import load_image  # Import here to avoid circular imports
        image = load_image(self.symbol)
        screen.blit(image, (position[1] * 80, position[0] * 80))  # Assuming each square is 80x80 pixels