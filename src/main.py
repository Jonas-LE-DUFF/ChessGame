from board import Board

class App:
    def __init__(self):
        self.board = Board()
        self.board.show()

    def select_piece(self, position):
        row, col = position
        piece = self.board.board[row][col]
        if piece is None:
            print("No piece at the selected position.")
            print(self.board.find_piece('k'))
            return []
        return piece.get_legal_moves(position, self.board.board)

    def run(self):
        while True:
            user_input = input("Enter piece position (e.g., 'e2') or 'exit' to quit: ")
            if user_input.lower() == 'exit' or user_input.lower() == 'quit':
                break
            try:
                col = ord(user_input[0].lower()) - ord('a')
                row = 8 - int(user_input[1])
                print("in run ", col, ' ', row)
                moves = self.select_piece((row, col))
                print(f"Valid moves: {moves}")
            except (ValueError):
                print("Invalid input. Please enter a valid position.", ValueError.args)
                
        
        
self = App()
self.run()