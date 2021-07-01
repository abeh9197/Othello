light = 0
dark = 1

board_size = 8

class ReversiBoard(object):
    def __init__(self):
        self.cells = []
        for i in range(board_size):
            self.cells.append([None for i in range(board_size)])
            

board = ReversiBoard()
print(board.cells)