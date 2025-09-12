# Chess Game

This is a simple chess game implemented in Python. The game allows two players to play chess against each other, with a focus on implementing the core mechanics of chess.

## Project Structure

```
chess-game
├── src
│   ├── main.py          # Entry point of the chess game
│   ├── board.py         # Contains the Board class for managing the chessboard
│   ├── pieces           # Directory containing piece classes
│   │   ├── __init__.py  # Initializes the pieces module
│   │   ├── pawn.py      # Defines the Pawn class
│   │   ├── rook.py      # Defines the Rook class
│   │   ├── knight.py    # Defines the Knight class
│   │   ├── bishop.py    # Defines the Bishop class
│   │   ├── queen.py     # Defines the Queen class
│   │   └── king.py      # Defines the King class
├── tests                # Directory containing test files
│   ├── test_board.py    # Unit tests for the Board class
│   ├── test_pieces.py   # Unit tests for the piece classes
│   └── __init__.py      # Initializes the tests module
├── requirements.txt      # Lists the dependencies required for the project
└── README.md             # Documentation for the project
```

## Setup Instructions

1. Clone the repository:
   ```
   git clone <repository-url>
   cd chess-game
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Run the game:
   ```
   python src/main.py
   ```

## Gameplay Rules

- The game follows standard chess rules.
- Players take turns to move their pieces.
- The objective is to checkmate the opponent's king.

## Contributing

Feel free to submit issues or pull requests if you would like to contribute to the project!