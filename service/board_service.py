from domain.BorderValidator import BoardValidator
from domain.Cell import Cell
from domain.cell_validator import CellValidator


class BoardService:
    def __init__(self, board):
        self.__board = board
        self.__last_player_cell = Cell
        # self.__strategy = strategy
        self.number_of_steps = 0
        self._number_of_cells_to_win = 4

    def player_move(self, line, column):
        if CellValidator(self.__board, line, column).validate() is True:
            self.__board.set_value(line, column, 'R')
            self.__last_player_cell = Cell(line, column, 'R')
            self.number_of_steps += 1
            return self.check_for_winning(line, column)

    def computer_move(self):
        computer_cell = self.simple_strategy()
        if computer_cell is not None:
            self.__board.set_value(computer_cell.row, computer_cell.column, 'Y')
        else:
            return False
        self.number_of_steps += 1
        return self.check_for_winning(computer_cell.row, computer_cell.column)

    # self.complex_strategy()

    def check_for_winning(self, row, column):
        quantity = 4

        is_row_good_for_win = (self.move_in_direction(row, column, quantity, 1, 0) + self.move_in_direction(row, column,
                                                                                                            quantity,
                                                                                                            -1,
                                                                                                            0) - 1) >= self._number_of_cells_to_win
        is_column_good_for_win = (self.move_in_direction(row, column, quantity, 0, 1) + self.move_in_direction(row,
                                                                                                               column,
                                                                                                               quantity,
                                                                                                               0,
                                                                                                               -1) - 1) >= self._number_of_cells_to_win

        is_main_diagonal_good_for_win = (self.move_in_direction(row, column, quantity, 1, 1) + self.move_in_direction(
            row, column, quantity,
            -1, -1) - 1) >= self._number_of_cells_to_win

        is_second_diagonal_good_for_win = (self.move_in_direction(row, column, quantity, -1,
                                                                  1) + self.move_in_direction(row, column, quantity,
                                                                                              1,
                                                                                              -1) - 1) >= self._number_of_cells_to_win

        return is_row_good_for_win or is_column_good_for_win or is_main_diagonal_good_for_win or is_second_diagonal_good_for_win

    def move_in_direction(self, row, column, quantity, row_factor=1, column_factor=1):
        good_cells_for_win: int = 1
        for displacement in range(1, quantity):
            new_row = row + displacement * row_factor
            new_column = column + displacement * column_factor
            if BoardValidator.validate(new_row, new_column, self.__board) is True and self.__board.get_value(new_row,
                                                                                                             new_column) != 0:
                if self.__board.get_value(new_row, new_column) == self.__board.get_value(row, column):
                    good_cells_for_win += 1
                else:
                    break
            else:
                break

        return good_cells_for_win

    def simple_strategy(self):
        cell = None
        for row in range(0, self.__board.get_rows()):
            for column in range(0, self.__board.get_columns()):
                if self.__board.get_value(row, column) == 0:
                    # lets say our board [row,column] becomes  Yellow
                    if row >= 1 and self.__board.get_value(row - 1, column) == 0:
                        continue

                    self.__board.set_value(row, column, 'R')
                    if self.check_for_winning(row, column) is True:
                        cell = Cell(row, column, 'Y')

                    self.__board.set_value(row, column, 'Y')
                    if self.check_for_winning(row, column) is True:
                        self.__board.set_value(row, column, 'Y')
                        return Cell(row, column, 'Y')

                    self.__board.set_value(row, column, 0)

        if cell is None:
            possible_cells = self.get_last_player_move_neighbours()
            if len(possible_cells) == 0:
                get_the_first_free_position = self.get_the_first_free_cell()
                return get_the_first_free_position
            cell = possible_cells[0]

        return cell

    def get_last_player_move_neighbours(self):
        solutions = []
        if BoardValidator.validate(self.__last_player_cell.row + 1, self.__last_player_cell.column,
                                   self.__board) is True:
            solutions.append(Cell(self.__last_player_cell.row + 1, self.__last_player_cell.column, 'Y'))

        directions = [-1, 0, 1]

        for direction in directions:
            new_line = self.__last_player_cell.row + direction
            left_column = self.__last_player_cell.column + 1
            right_column = self.__last_player_cell.column - 1
            if BoardValidator.validate(new_line, left_column, self.__board) is True and BoardValidator.validate(
                    new_line - 1, left_column, self.__board) and self.__board.get_value(new_line - 1,
                                                                                        left_column) != 0 and self.__board.get_value(
                new_line, left_column) == 0:
                solutions.append(Cell(new_line, left_column, 'Y'))

            if BoardValidator.validate(new_line, right_column,
                                       self.__board) is True and BoardValidator.validate(new_line - 1, right_column,
                                                                                         self.__board) and self.__board.get_value(
                new_line - 1,
                right_column) != 0 and self.__board.get_value(
                new_line, right_column) == 0:
                solutions.append(Cell(new_line, right_column, 'Y'))

        return solutions

    def get_the_first_free_cell(self):
        for row in range(0, self.get_rows()):
            for column in range(self.get_columns()-1,-1,-1):
                if BoardValidator.validate(row, column, self.__board) is True and self.get(row, column) == 0:
                    if row == 0:
                        return Cell(row, column, 'Y')
                    elif self.get(row - 1, column) != 0:
                        return Cell(row, column, 'Y')
        return None

    def get_number_of_steps(self):
        return self.number_of_steps

    def get(self, row, column):
        return self.__board.get_value(row, column)

    def get_rows(self):
        return self.__board.get_rows()

    def get_columns(self):
        return self.__board.get_columns()

    def clear_board(self):
        self.number_of_steps = 0
        self.__board.clear()
