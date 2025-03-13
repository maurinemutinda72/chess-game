import pygame
import time
from chessboard import ChessBoard
from utils import load_piece_images

class ChessGame:
    def __init__(self):
        pygame.init()
        self.WIDTH, self.HEIGHT = 800, 800
        self.SQUARE_SIZE = self.WIDTH // 8
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("Chess")

        # Load assets
        self.piece_images = load_piece_images(self.SQUARE_SIZE)
        
        # Initialize sound
        pygame.mixer.init()
        self.move_sound = pygame.mixer.Sound("assets/sounds/move-check.mp3")  # Sound for all moves
        self.capture_sound = pygame.mixer.Sound("assets/sounds/capture.mp3")  # Sound for captures
        self.check_sound = pygame.mixer.Sound("assets/sounds/notify.mp3")  # Sound for check
        self.promote_sound = pygame.mixer.Sound("assets/sounds/promote.mp3")  # Sound for pawn promotion

        # Game state
        self.board = ChessBoard()
        self.selected_piece = None
        self.start_time = time.time()
        self.WHITE_TIME, self.BLACK_TIME = 900, 900
        self.running = True

    def draw_board(self):
        """Draw the chessboard with pieces."""
        colors = [(255, 206, 158), (209, 139, 71)]
        for row in range(8):
            for col in range(8):
                pygame.draw.rect(self.screen, colors[(row + col) % 2],
                                 (col * self.SQUARE_SIZE, row * self.SQUARE_SIZE, self.SQUARE_SIZE, self.SQUARE_SIZE))
                piece = self.board.get_piece(row, col)
                if piece:
                    self.screen.blit(self.piece_images[piece.image_name()],
                                     (col * self.SQUARE_SIZE, row * self.SQUARE_SIZE))

    def handle_click(self, row, col):
        """Handles piece selection and movement."""
        piece = self.board.get_piece(row, col)

        if self.selected_piece:
            # Store the target piece before moving
            target_piece = self.board.get_piece(row, col)
            # Pass the sound objects to move_piece to play sounds at the right time
            if self.board.move_piece(self.selected_piece, row, col, 
                                   move_sound=self.move_sound, 
                                   capture_sound=self.capture_sound, 
                                   check_sound=self.check_sound, 
                                   promote_sound=self.promote_sound):
                print(f"Moved {self.selected_piece.__class__.__name__} to ({row}, {col})")
                self.selected_piece = None
                self.update_timer()
            else:
                print("Invalid move, try again.")
        elif piece and piece.color == self.board.turn:
            self.selected_piece = piece
            print(f"Selected {piece.__class__.__name__} at ({row}, {col})")

    def update_timer(self):
        """Updates the game timer."""
        elapsed = time.time() - self.start_time
        if self.board.turn == "white":
            self.WHITE_TIME -= elapsed
        else:
            self.BLACK_TIME -= elapsed
        self.start_time = time.time()

    def run(self):
        """Main game loop."""
        while self.running:
            self.draw_board()
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = pygame.mouse.get_pos()
                    row, col = y // self.SQUARE_SIZE, x // self.SQUARE_SIZE
                    self.handle_click(row, col)

            if self.board.game_over:
                winner = "Black" if self.board.turn == "white" else "White"
                print(f"Game over! {winner} wins by capturing the opponent's king!")
                self.running = False

        pygame.quit()

if __name__ == "__main__":
    game = ChessGame()
    game.run()