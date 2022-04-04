import random

class Board:
    def __init__(self, row, column):
        self.row = row
        self.column = column
        self.board = self.create_board()
    
    def generate_random_postion(self):
        self.random_row = random.randint(0, self.row-1)
        self.random_column = random.randint(0, self.column-1)
        print(self.random_row, self.random_column)

    def create_board(self):
        board = list()
        for _ in range(0, self.column):
            board.append([0] * self.row)
        return board
    
    def show_board(self):
        row_len = len(self.board)
        column_len = len(self.board[0])

        for row in range(row_len):
            for column in range(column_len):
                if column < column_len - 1:
                    print(self.board[row][column], end=" ")
                else:
                    print(self.board[row][column], end="\n")

    def set_new_number(self):
        self.generate_random_postion()
        self.board[self.random_row][self.random_column] = 2

if __name__ == '__main__':
    board = Board(row = 4, column = 4)
    board.show_board()
    print()
    board.set_new_number()
    board.show_board()
