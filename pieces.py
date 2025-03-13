class Piece:
    def __init__(self, color, row, col):
        self.color = color
        self.row = row
        self.col = col

    def image_name(self):
        return f"{self.color}-{self.__class__.__name__.lower()}.png"

    def is_legal_move(self, board, start_row, start_col, end_row, end_col):
        raise NotImplementedError("This method should be overridden by subclasses")

class Pawn(Piece):
    def is_legal_move(self, board, start_row, start_col, end_row, end_col):
        direction = -1 if self.color == "white" else 1
        if start_col == end_col and end_row == start_row + direction and not board[end_row][end_col]:
            return True
        if start_col == end_col and start_row == (6 if self.color == "white" else 1) and \
           end_row == start_row + 2 * direction and not board[end_row][end_col] and not board[start_row + direction][start_col]:
            return True
        if abs(start_col - end_col) == 1 and end_row == start_row + direction and \
           board[end_row][end_col] and board[end_row][end_col].color != self.color:
            return True
        return False

class Rook(Piece):
    def is_legal_move(self, board, start_row, start_col, end_row, end_col):
        if start_row != end_row and start_col != end_col:
            return False
        step_row = 0 if start_row == end_row else (1 if end_row > start_row else -1)
        step_col = 0 if start_col == end_col else (1 if end_col > start_col else -1)
        row, col = start_row + step_row, start_col + step_col
        while row != end_row or col != end_col:
            if board[row][col]:
                return False
            row += step_row
            col += step_col
        target = board[end_row][end_col]
        return not target or target.color != self.color

class Knight(Piece):
    def is_legal_move(self, board, start_row, start_col, end_row, end_col):
        if (abs(start_row - end_row), abs(start_col - end_col)) not in [(2, 1), (1, 2)]:
            return False
        target = board[end_row][end_col]
        return not target or target.color != self.color

class Bishop(Piece):
    def is_legal_move(self, board, start_row, start_col, end_row, end_col):
        if abs(start_row - end_row) != abs(start_col - end_col):
            return False
        step_row = 1 if end_row > start_row else -1
        step_col = 1 if end_col > start_col else -1
        row, col = start_row + step_row, start_col + step_col
        while row != end_row:
            if board[row][col]:
                return False
            row += step_row
            col += step_col
        target = board[end_row][end_col]
        return not target or target.color != self.color

class Queen(Piece):
    def is_legal_move(self, board, start_row, start_col, end_row, end_col):
        return Rook(self.color, start_row, start_col).is_legal_move(board, start_row, start_col, end_row, end_col) or \
               Bishop(self.color, start_row, start_col).is_legal_move(board, start_row, start_col, end_row, end_col)

class King(Piece):
    def is_legal_move(self, board, start_row, start_col, end_row, end_col):
        row_diff = abs(start_row - end_row)
        col_diff = abs(start_col - end_col)
        if row_diff > 1 or col_diff > 1 or (row_diff == 0 and col_diff == 0):
            return False
        target = board[end_row][end_col]
        return not target or target.color != self.color