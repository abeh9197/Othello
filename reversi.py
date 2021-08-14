from enum import Enum

class Game():

    def __init__(self):
        pass


class TileValue(Enum):

    dark = {'color': 'dark', 'num': 0}
    light = {'color': 'light', 'num': 1}

    
    @staticmethod
    def from_number(num: int):
        for t in TileValue:
            if t.value['num'] == num:
                return t
        raise ValueError('Invalid number. Expected number is 0 or 1')


class Tile:

    def __init__(self, value):
        self.value: TileValue = value


    def __str__(self) -> str:
        return str(self.value.value['color'])


    def __repr__(self) -> str:
        return str(self)


    def __hash__(self) -> int:
        return int(self.value.value['num'])

    @staticmethod
    def from_number(n: int):
        return Tile(TileValue.from_number(n))


class Board:

    def __init__(self, cells=None, board_size=8):
        self.cells = cells
        self.board_size = board_size


    def board(self):
        board = [[self.cells for c in range(self.board_size)] for c in range(self.board_size)]
        board[3][3] = Tile.from_number(0)
        board[3][4] = Tile.from_number(1)
        board[4][3] = Tile.from_number(1)
        board[4][4] = Tile.from_number(0)
        return board


class BoardView:
    def __init__(self, board=None):
        board = Board(cells=None, board_size=8)


    def draw_board(self):
        for c in self.board:
            if c == None:
                print('□')
            elif c == Tile.from_number(0):
                print('●')
            elif c == Tile.from_number(1):
                print('○')
        return self.board()
        

class Round:
    
    def __init__(self, players, count) -> None:
        self.players = players
        self.count = count

    
    def players():
        player1 = 'A'
        player2 = 'B'
        players = [player1, player2]
        return players

class Player:
    def __init__(self) -> None:
        pass