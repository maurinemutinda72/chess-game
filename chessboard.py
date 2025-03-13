from pieces import Pawn, Rook, Knight, Bishop, Queen, King

class ChessBoard:
    def __init__(self):
        """Initializes the chessboard with all pieces."""
        self.board = [[None for _ in range(8)] for _ in range(8)]
        self.turn = "white"
        self.game_over = False
        self.setup_board()

    def setup_board(self):
        """Places pieces on the board."""
        piece_order = [Rook, Knight, Bishop, Queen, King, Bishop, Knight, Rook]
        for col, piece_class in enumerate(piece_order):
            self.board[0][col] = piece_class("black", 0, col)
            self.board[7][col] = piece_class("white", 7, col)

        for col in range(8):
            self.board[1][col] = Pawn("black", 1, col)
            self.board[6][col] = Pawn("white", 6, col)

    def get_piece(self, row, col):
        """Returns the piece at a given position."""
        return self.board[row][col] if 0 <= row < 8 and 0 <= col < 8 else None

    def move_piece(self, piece, row, col, move_sound=None, capture_sound=None, check_sound=None, promote_sound=None):
        """Moves a piece if the move is legal, handles promotion and check, and plays sounds."""
        old_row, old_col = piece.row, piece.col

        if not piece.is_legal_move(self.board, old_row, old_col, row, col):
            return False

        # Check if the move captures a piece
        target_piece = self.board[row][col]
        
        # Move the piece temporarily to check for check
        self.board[row][col] = piece
        self.board[old_row][old_col] = None
        piece.row, piece.col = row, col

        # Pawn promotion
        promoted = False
        if isinstance(piece, Pawn):
            if (piece.color == "white" and row == 0) or (piece.color == "black" and row == 7):
                print(f"Pawn promoted to Queen at ({row}, {col})!")
                self.board[row][col] = Queen(piece.color, row, col)
                promoted = True
                if promote_sound:
                    promote_sound.play()

        # Check for check
        in_check = self.is_in_check(self.turn)  # Turn has not switched yet, so check the opponent's king

        # Play sounds in order of priority: capture > check > regular move
        if target_piece and capture_sound:
            capture_sound.play()
        elif in_check and check_sound:
            print("Check!")
            check_sound.play()
        elif move_sound:
            move_sound.play()  # Play move sound if no capture or check

        # Finalize move
        if target_piece and isinstance(target_piece, King):
            self.game_over = True

        self.turn = "black" if self.turn == "white" else "white"
        return True

    def is_in_check(self, color):
        """Check if the king of the given color is in check."""
        # Find the king
        king_row, king_col = None, None
        for r in range(8):
            for c in range(8):
                piece = self.board[r][c]
                if piece and isinstance(piece, King) and piece.color == color:
                    king_row, king_col = r, c
                    break
            if king_row is not None:
                break

        if king_row is None:
            return False  # King not found (shouldn't happen in a valid game)

        # Check if any opponent piece can capture the king
        opponent_color = "black" if color == "white" else "white"
        for r in range(8):
            for c in range(8):
                piece = self.board[r][c]
                if piece and piece.color == opponent_color:
                    if piece.is_legal_move(self.board, piece.row, piece.col, king_row, king_col):
                        return True
        return False