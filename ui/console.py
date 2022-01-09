from domain.cell_validator import OutsideTheSizeException, PositionTakenException, NotTheLowestPositionException


class Console:
    def __init__(self, board_service):
        self.__board_service = board_service

    def run_game(self):
        turn = 0
        self.print_board()
        while True:
            if turn == 0:
                print("Player turn:")
                new_line = input("line=")
                new_column = input("column=")
                try:
                    new_line = int(new_line)
                    new_column = int(new_column)
                except ValueError:
                    print("Invalid input!")
                    continue
                try:
                    if self.__board_service.player_move(new_line, new_column) is True:
                        self.print_board()
                        print("You won!")
                        exit()

                    self.print_board()
                except PositionTakenException as PTE:
                    print(PTE)
                    continue
                except OutsideTheSizeException as OTSE:
                    print(OTSE)
                    continue
                except NotTheLowestPositionException as NTLPE:
                    print(NTLPE)
                    continue

            else:
                print("Computer move:")
                if self.__board_service.computer_move() is True:
                    self.print_board()
                    print('Computer won! You have lost!')
                    exit()
                self.print_board()

            turn = 1 - turn

    def print_board(self):
        rows = self.__board_service.get_rows()
        columns = self.__board_service.get_columns()
        for row in range(rows - 1, -1, -1):
            for column in range(columns - 1, -1, -1):
                print(self.__board_service.get(row, column), end=" ")
            print()
