import unittest
from domain.board import Board
from domain.cell_validator import PositionTakenException, NotTheLowestPositionException, OutsideTheSizeException
from service.board_service import BoardService


class test_border_service(unittest.TestCase):
    def setUp(self) -> None:
        self._board = Board(6, 7)
        self._board_service = BoardService(self._board)

    def test_player_move(self):
        self._board_service.player_move(0, 1)
        self.assertEqual(self._board_service.get(0, 1), 'R')

        with self.assertRaises(OutsideTheSizeException):
            self._board_service.player_move(0, 15)

        with self.assertRaises(PositionTakenException):
            self._board_service.player_move(0, 1)

        with self.assertRaises(NotTheLowestPositionException):
            self._board_service.player_move(5, 2)

        with self.assertRaises(OutsideTheSizeException):
            self._board_service.player_move(6, 8)

        with self.assertRaises(OutsideTheSizeException):
            self._board_service.player_move(-1, -1)

        with self.assertRaises(NotTheLowestPositionException):
            self._board_service.player_move(1, 0)

        self._board_service.player_move(0, 0)
        self.assertEqual(self._board_service.get(0, 0), 'R')

        self._board_service.player_move(1, 0)
        self.assertEqual(self._board_service.get(1, 0), 'R')

        self._board_service.player_move(2, 0)
        self.assertEqual(self._board_service.get(2, 0), 'R')

        self.assertEqual(self._board_service.player_move(3, 0), True)

    def test_check_for_winning_line(self):
        self._board_service.player_move(0, 1)
        self._board_service.player_move(1, 1)
        self._board_service.player_move(2, 1)
        self._board_service.player_move(3, 1)

        self.assertEqual(self._board_service.check_for_winning(0, 1), True)
        self.assertEqual(self._board_service.check_for_winning(1, 1), True)
        self.assertEqual(self._board_service.check_for_winning(2, 1), True)
        self.assertEqual(self._board_service.check_for_winning(3, 1), True)
        self.assertEqual(self._board_service.check_for_winning(4, 1), False)

    def test_check_for_winning_second_diagonal(self):
        self._board.set_value(0, 3, 'R')
        self._board.set_value(1, 2, 'R')
        self._board.set_value(2, 1, 'R')
        self._board.set_value(3, 0, 'R')

        self.assertEqual(self._board_service.check_for_winning(0, 3), True)
        self.assertEqual(self._board_service.check_for_winning(1, 2), True)
        self.assertEqual(self._board_service.check_for_winning(2, 1), True)
        self.assertEqual(self._board_service.check_for_winning(3, 0), True)
        self.assertEqual(self._board_service.check_for_winning(3, 1), False)

    def test_check_for_winning_main_diagonal(self):
        self._board.set_value(0, 2, 'R')
        self._board.set_value(1, 3, 'R')
        self._board.set_value(2, 4, 'R')
        self._board.set_value(3, 5, 'R')

        self.assertEqual(self._board_service.check_for_winning(0, 2), True)
        self.assertEqual(self._board_service.check_for_winning(1, 3), True)
        self.assertEqual(self._board_service.check_for_winning(2, 4), True)
        self.assertEqual(self._board_service.check_for_winning(3, 5), True)
        self.assertEqual(self._board_service.check_for_winning(4, 6), False)

    def test_check_for_winning_column(self):
        self._board.set_value(0, 0, 'R')
        self._board.set_value(1, 0, 'R')
        self._board.set_value(2, 0, 'R')
        self._board.set_value(3, 0, 'R')

        self.assertEqual(self._board_service.check_for_winning(0, 0), True)
        self.assertEqual(self._board_service.check_for_winning(1, 0), True)
        self.assertEqual(self._board_service.check_for_winning(2, 0), True)
        self.assertEqual(self._board_service.check_for_winning(3, 0), True)
        self.assertEqual(self._board_service.check_for_winning(4, 0), False)

    def test_computer_move(self):
        self._board_service.player_move(0, 0)
        self.assertEqual(self._board_service.get(0, 0), 'R')

        self._board_service.player_move(1, 0)
        self._board_service.player_move(2, 0)
        self._board_service.computer_move()
        self.assertEqual(self._board_service.get(3, 0), 'Y')

        self._board_service.player_move(0, 1)
        self._board_service.player_move(0, 2)
        self._board_service.computer_move()
        self.assertEqual(self._board_service.get(0, 3), 'Y')

        self._board_service.player_move(1, 1)
        self._board_service.computer_move()
        self.assertEqual(self._board_service.get(2, 1), 'Y')

        self.assertEqual(self._board_service.computer_move(), True)

    def test_get_the_first_free_cell(self):
        self._board_service.player_move(0, 2)
        self._board_service.computer_move()

        self._board_service.player_move(0, 1)
        self._board_service.computer_move()

        self._board_service.player_move(0, 0)
        self._board_service.computer_move()

        self.assertEqual(self._board_service.get(0, 3), 'Y')

        self._board_service.player_move(1, 0)
        self._board_service.computer_move()
        self._board_service.player_move(3, 0)
        self._board_service.computer_move()
        self._board_service.player_move(5, 0)
        self._board_service.computer_move()

        self.assertEqual(self._board_service.get(0, 3), 'Y')
