### Chess Game with Pygame
A simple chess game built using Python and Pygame. This project includes a graphical chessboard, piece movement, sound effects for moves, captures, checks, and pawn promotions, as well as basic game logic like turn-taking and king capture to end the game.
### Features
•	Graphical chessboard with alternating colors.
•	Standard chess piece movements (Pawn, Rook, Knight, Bishop, Queen, King).
•	Pawn promotion to Queen when reaching the opponent’s back rank.
•	Sound effects for regular moves, captures, checks, and pawn promotions.
•	Turn-based gameplay with a timer for each player (15 minutes per side).
•	Game ends when a king is captured (non-standard chess rule).
•	Visual representation of pieces using PNG images.
### Prerequisites
To run this project, you’ll need the following installed on your system:
•	Python 3.x (tested with Python 3.9+)
•	Pygame: Install via pip: 
pip install pygame
•	PulseAudio (for Linux users, if audio is not working): Ensure PulseAudio is installed and running: 
sudo apt install pulseaudio
pulseaudio --start
On other systems, Pygame will use the default audio backend.
### Installation
1.	Clone or download this repository to your local machine.
2.	Ensure all dependencies are installed (see Prerequisites).
3.	Verify the following assets are present:
o	Piece images in the assets/ directory (e.g., white-king.png, black-pawn.png, etc.).
o	Sound files in the assets/sounds/ directory (or pulseaudio/ if you’ve renamed it): 
	move-check.mp3 (for regular moves and checks)
	capture.mp3 (for captures)
	notify.mp3 (for check announcements)
	promote.mp3 (for pawn promotions)
If the sound files are in a different directory (e.g., pulseaudio/), update the paths in main.py:
self.move_sound = pygame.mixer.Sound("pulseaudio/move-check.mp3")
self.capture_sound = pygame.mixer.Sound("pulseaudio/capture.mp3")
self.check_sound = pygame.mixer.Sound("pulseaudio/notify.mp3")
self.promote_sound = pygame.mixer.Sound("pulseaudio/promote.mp3")
### How to Run
1.	Navigate to the project directory: 
cd path/to/chess-game
2.	Run the main script: 
python main.py
3.	The game window will open, displaying the chessboard.
4.	Click on a piece to select it, then click on a destination square to move. The game alternates between white and black turns.
5.	The game ends when a king is captured, and the winner is announced in the console.
### Controls
•	Mouse Click: Select a piece and move it by clicking on the source and destination squares.
•	Close Window: Exit the game by closing the Pygame window.
### Piece Movement Rules
Each piece type has a specific is_legal_move method in pieces.py:
•	Pawn: Moves forward one square (or two from the starting rank), captures diagonally one square. Promotes to a Queen when reaching the opponent’s back rank (row 0 for white, row 7 for black).
•	Rook: Moves horizontally or vertically any number of squares, stopping at the first occupied square (captures if opponent’s piece).
•	Knight: Moves in an L-shape (two squares in one direction, then one perpendicular, or vice versa), jumping over other pieces.
•	Bishop: Moves diagonally any number of squares, stopping at the first occupied square.
•	Queen: Combines Rook and Bishop movements (horizontal, vertical, or diagonal).
•	King: Moves one square in any direction (horizontal, vertical, or diagonal).
 ### Special Features
•	Pawn Promotion: When a Pawn reaches the opponent’s back rank, it automatically promotes to a Queen, and the promote_sound plays.
•	Capture Detection: If a move lands on an opponent’s piece, it’s captured, and the capture_sound plays.
•	Check Detection: After each move, is_in_check checks if the current player’s king is threatened. If so, "Check!" is printed, and the check_sound plays.
•	Sound Effects: Sounds are prioritized: capture > check > regular move > promotion (played in that order if applicable).
•	Game Over: The game ends if a king is captured (unconventional), and the opponent is declared the winner.

### File Structure
•	main.py: Entry point of the game. Initializes Pygame, sets up the game loop, and handles user input.
•	chessboard.py: Defines the ChessBoard class, which manages the game state, piece placement, and movement logic.
•	pieces.py: Contains the Piece class and its subclasses (Pawn, Rook, Knight, Bishop, Queen, King) with movement rules.
•	utils.py: Utility functions, including load_piece_images to load and resize piece images.
•	assets/: Directory containing piece images (e.g., white-king.png, black-pawn.png).
•	assets/sounds/ (or pulseaudio/): Directory for sound files (e.g., move-check.mp3, capture.mp3).
•	error.log: Log file for errors (if generated during runtime).
•	LICENSE: License file for MIT.
•	README.md: This file.
### Note
•	The game uses a non-standard rule where the game ends when a king is captured. Traditional chess ends with checkmate or stalemate, which could be added in future updates.
### Game Crashes
•	Check error.log for details.
•	Ensure all dependencies are installed and Python is up to date.
### License
This project is licensed under the MIT License (or specify your preferred license).
### Acknowledgments
•	Built with Pygame, a Python library for game development.
•	Piece images and sounds by Freedesktop.org
•	Author by Queen Moh

