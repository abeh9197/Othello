from enum import Enum
from typing import List, Tuple


def game_start():
    """Model"""
    game = Game()
    init_board = Board(cells=None, board_size=8)
    draw_board(init_board)
    x, y = game.get_input()
    board = init_board
    board = board.get_from_input(x, y, input_color=0) # NOTE: 色は仮
    draw_board(board)


def draw_board(board):
    return DrawBoard(board)


class Game():
    """Model"""

    def __init__(self):
        self.player = Player()
        
    def get_input(self):
        return self.player.player_input()


class Player:
    """Controller"""
    def __init__(self):
        pass

    def player_input(self) -> Tuple:
        x = int(input('入力してください x : '))
        y = int(input('入力してください y : '))
        return x, y


class TileValue(Enum):
    """Model"""

    blank = {'color': 'blank', 'vis': '□', 'num': -1}
    dark = {'color': 'dark', 'vis': '○', 'num': 0}
    light = {'color': 'light', 'vis': '●', 'num': 1}

    @staticmethod
    def from_number(num: int):
        for t in TileValue:
            if t.value['num'] == num:
                return t
        raise ValueError('Invalid number. Expected number is 0 or 1')


class Tile:
    """Model"""

    def __init__(self, value):
        self.value: TileValue = value

    def __str__(self) -> str:
        return str(self.value.value['vis'])

    def __repr__(self) -> str:
        return str(self)

    def __hash__(self) -> int:
        return int(self.value.value['num'])

    @staticmethod
    def from_number(n: int):
        return Tile(TileValue.from_number(n))


class Board:
    """Model"""
    def __init__(self, cells=None, board_size=8):
        self.board_size = board_size
        if cells is None:
            self.cells = self.init_board()
        else:
            self.cells = cells

    def init_board(self) -> List:
        blank_cell = Tile.from_number(-1)
        board = [[blank_cell for c in range(self.board_size)]
                 for c in range(self.board_size)]
        board[3][3] = Tile.from_number(0)
        board[3][4] = Tile.from_number(1)
        board[4][3] = Tile.from_number(1)
        board[4][4] = Tile.from_number(0)
        self.cells = board
        return self.cells

    @property
    def _board_size(self):
        return self.board_size

    def get_from_input(self, x, y, input_color: int):
        self.cells[x][y] = Tile.from_number(input_color)
        print(self.cells)
        return self


class DrawBoard:
    """View"""
    def __init__(self, board: Board):
        self.board = board.cells
        self.board_size = board.board_size
        self.draw = self.drawboard()

    def drawboard(self):
        """
        NOTE: 盤面を描写する
        """
        """
        FIXME: のちのちrow, colを１〜８にしたい（入力と整合性をとる）
        """
        row = ['\nX', 0, 1, 2, 3, 4, 5, 6, 7]
        col = [0, 1, 2, 3, 4, 5, 6, 7]
        print(*row)
        print(self.board)
        for b in range(self.board_size):
            print(col[b], *self.board[b])


class Round:
    """Model"""
    def __init__(self, players, count) -> None:
        self.players = players
        self.count = count


class Checker:
    """Model"""

    def __init__(self) -> None:
        pass

    def hand_input(self):
        row = int(input())
        col = int(input())
        return (row, col)

    def check_blank(self, board, x, y) -> bool:
        """
        NOTE: 空白のチェック
        """
        position = board[x][y]
        if position.value.value['color'] != 'blank':
            return False
        else:
            return True

    def ops_color(self, input_tile, check_tile):
        if check_tile.value.value['color'] == 'blank':
            return False
        elif check_tile.value.value['color'] == input_tile.value.value['color']:
            return False
        elif check_tile.value.value['color'] != input_tile.value.value['color']:
            return True

    def same_color(self, input_tile, check_tile):
        if check_tile.value.value['color'] == 'blank':
            return False
        elif check_tile.value.value['color'] == input_tile.value.value['color']:
            return True

    def check_up(self, board, x, y, input_tile):
        up = y - 1
        check_tile = board[x][up]
        while self.ops_color(input_tile, check_tile):
            up -= 1
            check_tile = board[x][up]
        if self.same_color(input_tile, check_tile):
            return x, y

    def check_upper_right(self, board, x, y, input_tile):
        right = x + 1
        up = y - 1
        check_tile = board[right][up]
        while self.ops_color(input_tile, check_tile):
            right += 1
            up -= 1
            check_tile = board[right][up]
        if self.same_color(input_tile, check_tile):
            return x, y

    def check_right(self, board, x, y, input_tile):
        right = x + 1
        check_tile = board[right][y]
        while self.ops_color(input_tile, check_tile):
            right += 1
            check_tile = board[right][y]
        if self.same_color(input_tile, check_tile):
            return x, y

    def check_lower_right(self, board, x, y, input_tile):
        right = x + 1
        lower = y + 1
        check_tile = board[right][lower]
        while self.ops_color(input_tile, check_tile):
            right += 1
            lower += 1
            check_tile = board[right][lower]
        if self.same_color(input_tile, check_tile):
            return x, y

    def check_low(self, board, x, y, input_tile):
        low = y + 1
        check_tile = board[x][low]
        while self.ops_color(input_tile, check_tile):
            low += 1
            check_tile = board[x][low]
        if self.same_color(input_tile, check_tile):
            return x, y

    def check_lower_left(self, board, x, y, input_tile):
        left = x - 1
        lower = y + 1
        check_tile = board[left][lower]
        while self.ops_color(input_tile, check_tile):
            left -= 1
            lower += 1
            check_tile = board[left][lower]
        if self.same_color(input_tile, check_tile):
            return x, y

    def check_left(self, board, x, y, input_tile):
        left = x - 1
        check_tile = board[left][y]
        while self.ops_color(input_tile, check_tile):
            left -= 1
            check_tile = board[left][y]
        if self.same_color(input_tile, check_tile):
            return x, y

    def check_upper_left(self, board, x, y, input_tile):
        left = x - 1
        upper = y - 1
        check_tile = board[left][upper]
        while self.ops_color(input_tile, check_tile):
            left -= 1
            upper -= 1
            check_tile = board[left][upper]
        if self.same_color(input_tile, check_tile):
            return x, y

    def adjacent_check(self, board, x, y, input_tile):
        """
        NOTE: 隣りあう石のチェック　もし空白であれば、その石の八方をチェック
        """
        position = []
        if self.check_blank(board, x, y):  # 置きたい場所が空白かチェック
            position.append(self.check_up(board, x, y, input_tile))
            position.append(self.check_upper_right(board, x, y, input_tile))
            position.append(self.check_right(board, x, y, input_tile))
            position.append(self.check_lower_right(board, x, y, input_tile))
            position.append(self.check_low(board, x, y, input_tile))
            position.append(self.check_lower_left(board, x, y, input_tile))
            position.append(self.check_left(board, x, y, input_tile))
            position.append(self.check_upper_left(board, x, y, input_tile))
        return position

    def position(self, board, input_tile):
        """
        置ける場所をリストでリターンする
        """
        checked_list = []
        for x in range(7):
            for y in range(7):
                checked = Checker().adjacent_check(board, x, y, input_tile)
                for i in checked:
                    if i is not None:
                        checked_list.append(i)
        return checked_list
