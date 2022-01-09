from tkinter import *


class Gui:
    def __init__(self, board_service):
        self._board_service = board_service
        self._root = Tk()
        self._canvas = Canvas(width=960, height=668)
        self._label = Label()
        # self._frame= Frame(self._root)
        self._computer_or_player_turn = 0
        self._width = 100
        self._height = 100
        self._user_shapes_canvas = Canvas(width=960, height=668)
        self._computer_shapes_canvas = Canvas(width=960, height=668)
        self.draw_grid()
        self._stop_after_won_or_tie = False
        self._restart_game_button = Button(self._root, text="Play again", command=self.gui_restart_game)

        # computer turn = 1
        # player turn = 0

    def start(self):
        self._root.title = "Connect Four"
        self._root.geometry("960x668")
        self._root.mainloop()

    def draw_grid(self):
        rows = self._board_service.get_rows()
        columns = self._board_service.get_columns()
        self._canvas.pack(fill="both")
        tag = 0

        def execute(tag):
            words = tag.split(',')
            row = int(words[0])
            column = int(words[1])
            self._canvas.tag_bind(tag, "<Button-1>", lambda e: self.rectangle_user_click(row, column))

        index = 0
        for row in range(rows - 1, -1, -1):
            for column in range(columns):
                x = column * self._width
                y = index * self._height
                displacement = 10
                rectangle_tag = str(row) + "," + str(column)
                color = "white"
                if self._board_service.get(row, column) == "R":
                    color = "red"
                if self._board_service.get(row, column) == "Y":
                    color = "yellow"

                self._canvas.create_rectangle(x + displacement, y + displacement, x + self._width + displacement,
                                              y + self._height + displacement, outline='red', tags=rectangle_tag,
                                              fill=color)

                execute(rectangle_tag)
                tag += 1
            index += 1

    def rectangle_user_click(self, row, column):
        if self._stop_after_won_or_tie is True:
            return

        if self._board_service.player_move(row, column) is True:
            self._stop_after_won_or_tie = True
            self._label = Label(self._root, text="You won the game!")
            self._label.place(x=730, y=200)

        elif self._board_service.computer_move() is True:
            self._stop_after_won_or_tie = True
            self._label = Label(self._root, text="You lost the game!", font=("Arial", 15))
            self._label.place(x=730, y=200)

        elif self._board_service.get_number_of_steps() == (
                self._board_service.get_rows() * self._board_service.get_columns()):
            self._stop_after_won_or_tie = True
            self._label = Label(self._root, text="Nobody won the game!", font=("Arial", 15))
            self._label.place(x=730, y=200)

        if self._stop_after_won_or_tie is True:
            self._restart_game_button = Button(self._root, text="Play again", command=self.gui_restart_game)
            self._restart_game_button.place(x=800, y=300)

        self._canvas.delete("all")
        self.draw_grid()

    def gui_restart_game(self):
        self._board_service.clear_board()
        self._canvas.delete("all")
        self.draw_grid()
        self._stop_after_won_or_tie = False
        self._label.destroy()
        self._restart_game_button.destroy()
