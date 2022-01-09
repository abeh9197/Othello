from enum import Enum
from typing import List, Protocol, Tuple


def game_start():
    """Model"""
    game = Game()
    init_board = Board(cells=None)
    game.draw(init_board)
    while game.not_done:
        x, y = game.get_input()
        board = init_board
        board = board.get_from_input(x, y, input_color=game.status.current_player)
        game.status.change_player()
        game.draw(board)

class Game:
    """Model"""

    def __init__(self):
        self.player = Player()
        self.drawboard = DrawBoard()
        self.status = Status()

    @property
    def not_done(self):
        done = 0
        return done == 0

    def get_input(self):
        return self.player.player_input()
    
    def draw(self, board):
        return self.drawboard.draw(board=board, input_tile=Tile.from_number(self.status.current_player))



class Player:
    """Controller"""

    def __init__(self):
        pass

    def player_input(self) -> Tuple:
        """
        TODO: need assertion error
        """
        x = int(input("入力してください x : "))
        y = int(input("入力してください y : "))
        return x, y


class TileValue(Enum):
    """Model"""

    BLANK = {"color": "blank", "vis": "□", "num": -1}
    DARK = {"color": "dark", "vis": "○", "num": 0}
    LIGHT = {"color": "light", "vis": "●", "num": 1}

    @staticmethod
    def from_number(num: int):
        for t in TileValue:
            if t.value["num"] == num:
                return t
        raise ValueError("Invalid number. Expected number is 0 or 1")


class Tile:
    """Model"""

    def __init__(self, value):
        self.value: TileValue = value

    def __str__(self) -> str:
        return str(self.value.value["vis"])

    def __repr__(self) -> str:
        return str(self)

    def __hash__(self) -> int:
        return int(self.value.value["num"])

    @staticmethod
    def from_number(n: int):
        return Tile(TileValue.from_number(n))


class Board:
    """Model"""

    def __init__(self, cells=None):
        self.board_size: int = 8
        self.manager = Manager()
        if cells is None:
            self.cells = self.init_board()
        else:
            self.cells = cells

    def init_board(self) -> List:
        blank_cell = Tile.from_number(-1)
        board = [
            [blank_cell for c in range(self.board_size)] for c in range(self.board_size)
        ]
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
        self.cells[y][x] = Tile.from_number(input_color)
        return self

    def where_you_can_put(self, board, input_tile: Tile) -> List[Tuple]:
        return self.manager.where_you_can_put(board, input_tile=input_tile)

class DrawBoard:
    """View"""

    def __init__(self):
        pass

    def draw(self, board: Board, input_tile: Tile):
        """
        NOTE: 盤面を描写する
        """
        """
        FIXME: のちのちrow, colを１〜８にしたい（入力と整合性をとる）
        """
        row = ["\nX", 0, 1, 2, 3, 4, 5, 6, 7]
        col = [0, 1, 2, 3, 4, 5, 6, 7]
        print(*row)
        # print(self.board)
        for b in range(board.board_size):
            print(col[b], *board.cells[b])
        
        print(board.where_you_can_put(board=board, input_tile=input_tile))


class Status:
    """Model"""

    def __init__(self) -> None:
        self.turn: int = 0
        self.current_player: int = 0
    
    def change_player(self):
        if self.current_player == 0:
            self.current_player = 1
        elif self.current_player == 1:
            self.current_player = 0


class Manager:
    """Model"""

    def __init__(self) -> None:
        pass

    def hand_input(self):
        row = int(input())
        col = int(input())
        return (row, col)

    def check_blank(self, board: List[Tile], row: int, col: int) -> bool:
        """
        NOTE: 空白のチェック
        """
        position: Tile = board[col][row]
        return position.value.value["color"] == "blank"

    def valid_cell(self, x: int , y: int) -> bool:
        return 0 <= x <= 7 and 0 <= y <= 7

    def ops_color(self, input_tile: Tile, check_tile: Tile) -> bool:
        if check_tile.value.value["color"] == ["blank"]:
            return False
        else:
            if input_tile.value.value["color"] == ["dark"]:
                return check_tile.value.value["color"] == ["light"]
            elif input_tile.value.value["color"] == ["light"]:
                return check_tile.value.value["color"] == ["dark"]

    def same_color(self, input_tile: Tile, check_tile: Tile) -> bool:
        if check_tile.value.value["color"] == ["blank"]:
            return False
        else:
            return check_tile.value.value["color"] == input_tile.value.value["color"]

    def check_upper_middle(self, board: List[Tile], row: int, col: int, input_tile: Tile) -> bool:
        """
        となりに相手色の色があるという変数
        かつその向こうに自分の色があるという変数
        """
        up = col - 1
        if self.valid_cell(row, up):
            check_tile = board[up][row]
            while self.ops_color(input_tile, check_tile):
                up -= 1
                check_tile = board[up][row]
            return self.same_color(input_tile, check_tile)

    def check_upper_right(self, board: List[Tile], row: int, col: int, input_tile: Tile) -> bool:
        right = row + 1
        upper = col - 1
        if self.valid_cell(upper, right):
            check_tile = board[upper][right]
            while self.ops_color(input_tile, check_tile):
                right += 1
                upper -= 1
                check_tile = board[upper][right]
            return self.same_color(input_tile, check_tile)

    def check_middle_right(self, board: List[Tile], row: int, col: int, input_tile: Tile) -> bool:
        right = row + 1
        if self.valid_cell(col, right):
            check_tile = board[col][right]
            while self.ops_color(input_tile, check_tile):
                right += 1
                check_tile = board[col][right]
            return self.same_color(input_tile, check_tile)

    def check_lower_right(self, board: List[Tile], row: int, col: int, input_tile: Tile) -> bool:
        right = row + 1
        lower = col + 1
        if self.valid_cell(lower, right):
            check_tile = board[lower][right]
            while self.ops_color(input_tile, check_tile):
                right += 1
                lower += 1
                check_tile = board[lower][right]
            return self.same_color(input_tile, check_tile)

    def check_lower_middle(self, board: List[Tile], row: int, col: int, input_tile: Tile) -> bool:
        lower = col + 1
        if self.valid_cell(lower, row):
            check_tile = board[lower][row]
            while self.ops_color(input_tile, check_tile):
                lower += 1
                check_tile = board[lower][row]
            return self.same_color(input_tile, check_tile)

    def check_lower_left(self, board: List[Tile], row: int, col: int, input_tile: Tile) -> bool:
        left = row - 1
        lower = col + 1
        if self.valid_cell(lower, left):
            check_tile = board[lower][left]
            while self.ops_color(input_tile, check_tile):
                left -= 1
                lower += 1
                check_tile = board[lower][left]
            return self.same_color(input_tile, check_tile)

    def check_middle_left(self, board: List[Tile], row: int, col: int, input_tile: Tile) -> bool:
        left = row - 1
        check_tile = board[col][left]
        if self.valid_cell(col, left):
            while self.ops_color(input_tile, check_tile):
                left -= 1
                check_tile = board[col][left]
            return self.same_color(input_tile, check_tile)

    def check_upper_left(self, board: List[Tile], row: int, col: int, input_tile: Tile) -> bool:
        left = row - 1
        upper = col - 1
        if self.valid_cell(upper, left):
            check_tile = board[upper][left]
            while self.ops_color(input_tile, check_tile):
                left -= 1
                upper -= 1
                check_tile = board[upper][left]
            return self.same_color(input_tile, check_tile)

    def adjacent_check(self, board: List[Tile], row: int, col: int, input_tile: Tile):
        """
        NOTE: 隣りあう石のチェック もし空白であれば、その石の八方をチェック
        """
        print("CHECK ROW COL", row, col)
        position = []
        if self.check_blank(board, row, col):  # 置きたい場所が空白かチェック
            if self.check_upper_middle(board, row=row, col=col, input_tile=input_tile):
                print("upper_middle", row, col)
                position.append((row, col))
            if self.check_upper_right(board, row=row, col=col, input_tile=input_tile):
                print("upper_right", row, col)
                position.append((row, col))
            if self.check_middle_right(board, row=row, col=col, input_tile=input_tile):
                print("middle_right", row, col)
                position.append((row, col))
            if self.check_lower_right(board, row=row, col=col, input_tile=input_tile):
                print("lower_right", row, col)
                position.append((row, col))
            if self.check_lower_middle(board, row=row, col=col, input_tile=input_tile):
                print("lower_middle", row, col)
                position.append((row, col))
            if self.check_lower_left(board, row=row, col=col, input_tile=input_tile):
                print("lower_left", row, col)
                position.append((row, col))
            if self.check_middle_left(board, row=row, col=col, input_tile=input_tile):
                print("middle_left", row, col)
                position.append((row, col))
            if self.check_upper_left(board, row=row, col=col, input_tile=input_tile):
                print("upper_left", row, col)
                position.append((row, col))
        return position

    def where_you_can_put(self, board: Board, input_tile: Tile) -> List[Tuple]:
        checked_list = []
        for row in range(8):
            for col in range(8):
                checked = self.adjacent_check(board.cells, row, col, input_tile)
                for i in checked:
                    if i is not None:
                        checked_list.append(i)
        return checked_list
