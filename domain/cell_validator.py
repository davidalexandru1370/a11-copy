class NotTheLowestPositionException(Exception):
    def __init__(self, message):
        super().__init__(message)


class PositionTakenException(Exception):
    def __init__(self, message):
        super().__init__(message)


class OutsideTheSizeException(Exception):
    def __init__(self, message):
        super().__init__(message)


class CellValidator:
    def __init__(self, board, pos_x, pos_y):
        self.__board = board
        self.__pos_x = pos_x
        self.__pos_y = pos_y

    def validate(self):
        if self.__pos_x < 0 or self.__pos_x >= self.__board.get_rows():
            raise OutsideTheSizeException("Outside the board")

        if self.__pos_y < 0 or self.__pos_y >= self.__board.get_columns():
            raise OutsideTheSizeException("Outside the board!")

        if self.__board.get_value(self.__pos_x, self.__pos_y) != 0:
            raise PositionTakenException("Position already taken")

        if self.__pos_x != 0 and self.__board.get_value(self.__pos_x - 1, self.__pos_y) == 0:
            raise NotTheLowestPositionException("This position is not the lowest!")

        return True
