from domain.board import Board
from service.board_service import BoardService
from ui.console import Console
from ui.gui import Gui


def main():
    board = Board(6, 7)
    board_service = BoardService(board)
    console = Console(board_service)
    gui = Gui(board_service)
    # console.run_game()
    gui.start()


if __name__ == '__main__':
    main()
