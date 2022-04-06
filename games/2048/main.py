from array import array
import random
from abc import ABC, abstractclassmethod
from time import sleep

class BoardInterface(ABC):
    @abstractclassmethod
    def create():
        pass

    @abstractclassmethod
    def show():
        pass

    @abstractclassmethod
    def update():
        pass

    @abstractclassmethod
    def is_game_over():
        pass

class Board(BoardInterface):
    def __init__(self, row, column):
        self.row = row
        self.column = column
        self.random_row = None
        self.random_column = None
        self.arrow = None

    def create(self):
        self.board = list()
        for _ in range(0, self.column):
            self.board.append([0] * self.row)
        self.__generate_random_postion()
        self.__set_new_number()
    
    def show(self):
        row_len = len(self.board)
        column_len = len(self.board[0])
        print("---------------------------------", end="\n")
        if self.arrow == None:
            print("Welcome to 2048 game!", end="\n")
        else:
            print("new data inserted at: (" + str(self.random_row) + ", " + str(self.random_column) + ")")
            print("Inputed key: " + str(self.arrow))

        for row in range(row_len):
            for column in range(column_len):
                if column < column_len - 1:
                    print(self.board[row][column], end=" ")
                else:
                    print(self.board[row][column], end="\n")
        print("---------------------------------", end="\n")

    def update(self):
        self.__generate_random_postion()
        self.__set_new_number()

        self.arrow = input("Input key [w,a,s,d]: ")

    def __set_new_number(self):
        self.board[self.random_row][self.random_column] = 2
    
    def __generate_random_postion(self):
        self.random_row = random.randint(0, self.row-1)
        self.random_column = random.randint(0, self.column-1)

    def is_game_over(self):
        return False

class BoardGame():
    def __init__(self, board: BoardInterface):
        self.board = board
    
    def play(self):
        self.board.create()
        self.board.show()
        while self.board.is_game_over() == False:
            self.board.update()
            self.board.show()

if __name__ == '__main__':
    board = Board(row = 4, column = 4)
    game = BoardGame(board)
    game.play()
