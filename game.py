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

        # Game state
        self.board = ChessBoard()
        self.selected_piece = None
        self.start_time = time.time()
        self.WHITE_TIME, self.BLACK_TIME = 900, 900
        self.running = True

    def draw_board(self):
        """Draw the chessboard with pieces."""
        colors = [(255, 255, 255), (0, 0, 0)]
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
        if self.selected_piece:
            self.board.move_piece(self.selected_piece, row, col)
            self.selected_piece = None
        else:
            self.selected_piece = self.board.get_piece(row, col)

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

            self.update_timer()

        pygame.quit()
