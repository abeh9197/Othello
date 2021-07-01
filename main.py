class Stone:
    dark = '○'
    light = '●'

class Cell:
    dark = Stone.dark
    light = Stone.light
    empty = '□'
    none = None

class Board:
    board_size = 8
    index = range(board_size)
    def __init__(self):
        self.cells = [[Cell.empty] * Board.board_size for _ in Board.index]
        self.cells[3][3] = Cell.light
        self.cells[4][4] = Cell.light
        self.cells[3][4] = Cell.dark
        self.cells[4][3] = Cell.dark

    #⇨self.cells[3][2] = Cell.dark
class Player:
    def __init__(self):
        pass

    def put(self, board, x, y):
        pass



class Input:
    def __init__(self):
        self.board = Board()
        self.cells = Cell()

    def keyboard_input(self, x, y):
        x = 3
        y = 2
        board.cells[x][y]
        print(*self.cells, sep ='\n')

board = Board()
print(*board.cells, sep ='\n')

board2 = Input()
board2.keybord_input()