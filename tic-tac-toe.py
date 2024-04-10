import random
import os


# TicTacToe class
class TicTacToe:
    def __init__(self):
        self.reset()

    def print_board(self):
        print("")
        print(
            " " + self.board[0][0] + " | " + self.board[0][1] + " | " + self.board[0][2]
        )
        print("--------")
        print(
            " " + self.board[1][0] + " | " + self.board[1][1] + " | " + self.board[1][2]
        )
        print("--------")
        print(
            " " + self.board[2][0] + " | " + self.board[2][1] + " | " + self.board[2][2]
        )

    def reset(self):
        self.board = [["", "", ""], ["", "", ""], ["", "", ""]]
        self.done = ""

    def check_win_or_draw(self):
        pass

    def get_player_move(self):
        pass

    def make_move(self):
        pass


self = TicTacToe()
self.print_board()
