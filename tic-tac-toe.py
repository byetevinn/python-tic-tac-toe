import random
import os


# TicTacToe class
class TicTacToe:
    def __init__(self):
        self.reset()

    def print_board(self):
        print("")
        print(
            " " + self.board[0][0] + " | " + self.board[0][1] + " | " + self.board[0][0]
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
        dict_win = {}

        for i in ["X", "O"]:
            # Hordizontais
            dict_win[i] = self.board[0][0] == self.board[0][1] == self.board[0][2] == i
            dict_win[i] = self.board[1][0] == self.board[1][1] == self.board[1][2] == i
            dict_win[i] = self.board[2][0] == self.board[2][1] == self.board[2][2] == i

            # Verticais
            dict_win[i] = self.board[0][0] == self.board[1][0] == self.board[2][0] == i
            dict_win[i] = self.board[0][1] == self.board[1][1] == self.board[2][1] == i
            dict_win[i] = self.board[0][2] == self.board[1][2] == self.board[2][2] == i

            # Diagonais
            dict_win[i] = self.board[0][0] == self.board[1][1] == self.board[2][2] == i
            dict_win[i] = self.board[2][0] == self.board[1][1] == self.board[0][2] == i

        if dict_win["X"]:
            self.done = "X"
            print("X venceu!")
        elif dict_win["O"]:
            self.done = "O"
            print("O venceu!")

    def get_player_move(self):
        pass

    def make_move(self):
        pass


self = TicTacToe()
self.print_board()
