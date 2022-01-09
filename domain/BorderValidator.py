class BoardValidator:
    @staticmethod
    def validate(row, column, board):
        rows = board.get_rows()
        columns = board.get_columns()
        if row < 0 or row >= rows:
            return False
        if column < 0 or column >= columns:
            return False

        return True
