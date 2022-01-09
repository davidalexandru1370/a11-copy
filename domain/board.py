class Board:
    def __init__(self, rows, columns):
        self.__rows = rows
        self.__columns = columns
        self.__board = [[0] * columns for i in range(rows)]

    def get_columns(self):
        return self.__columns

    def get_rows(self):
        return self.__rows

    def set_value(self, line, column, value):
        self.__board[line][column] = value

    # def __getitem__(self, item):
    #     return self.__board[item]
    #
    # def __setitem__(self, key, value):
    #     self.__board[key[0]][key[1]] = value

    def get_value(self, line, column):
        return self.__board[line][column]

    def get_board(self):
        return self.__board

    def clear(self):
        self.__board = [[0] * self.get_columns() for i in range(self.get_rows())]
