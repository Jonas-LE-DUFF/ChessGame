from board import Board

class App:
    def __init__(self):
        self.board = Board()
        self.board.show()
        self.player_turn = 'white'

    def select_piece(self, position):
        row, col = position
        piece = self.board.board[row][col]
        if piece is None:
            print("No piece at the selected position.")
            print(self.board.find_piece('k'))
            return []
        if piece.color != self.player_turn:
            print(f"It's {self.player_turn}'s turn. Please select your own piece.")
            return []
        return piece.get_legal_moves(position, self.board.board)
        
    def switch_turn(self):
        self.player_turn = 'black' if self.player_turn == 'white' else 'white'
        print(f"It's now {self.player_turn}'s turn.")
    

    def run(self):
        while True:
            step_selectpiece = False
            while not step_selectpiece:
                user_input = input("Enter piece position (e.g., 'e2') or 'exit' to quit: ")
                if user_input.lower() == 'exit' or user_input.lower() == 'quit':
                    return
                try:
                    col = ord(user_input[0].lower()) - ord('a')
                    row = 8 - int(user_input[1])
                    print("in run ", col, ' ', row)
                    moves = self.select_piece((row, col))
                    print(f"Valid moves: {moves}")
                    if(len(moves) > 0):
                        step_selectpiece = True
                        
                except (ValueError):
                    print("Invalid input. Please enter a valid position.", ValueError.args)

            step_movepiece = False
            while not step_movepiece:
                user_input_move = input("Enter move position (e.g., 'e4'): ")
                col_move = ord(user_input_move[0].lower()) - ord('a')
                row_move = 8 - int(user_input_move[1])
                if (row_move, col_move) in moves:
                    piece = self.board.board[row][col]
                    self.board.board[row_move][col_move] = piece
                    self.board.board[row][col] = None
                    self.board.show()
                    step_movepiece = True
                else:
                    print("Invalid move.")
            self.switch_turn()

    
        
self = App()
self.run()