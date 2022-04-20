from typing import List, Tuple
from models.Tile import Tile
from models.Board import Board
import itertools
from copy import copy
from utils.log import logger

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

        if check_tile.value.value["color"] == "blank":
            return False
        else:
            if input_tile.value.value["color"] == "dark":
                return check_tile.value.value["color"] == "light"
            elif input_tile.value.value["color"] == "light":
                return check_tile.value.value["color"] == "dark"

    def same_color(self, input_tile: Tile, check_tile: Tile) -> bool:
        if check_tile.value.value["color"] == "blank":
            return False
        else:
            return check_tile.value.value["color"] == input_tile.value.value["color"]

    def check_upper_middle(self, board: List[Tile], row: int, col: int, input_tile: Tile) -> bool:
        up = col - 1
        if self.valid_cell(row, up):
            check_tile = board[up][row]
            if self.ops_color(input_tile, check_tile):
                while self.ops_color(input_tile, check_tile):
                    up -= 1
                    check_tile = board[up][row]
                return self.same_color(input_tile, check_tile)

    def check_upper_right(self, board: List[Tile], row: int, col: int, input_tile: Tile) -> bool:
        right = row + 1
        upper = col - 1
        if self.valid_cell(upper, right):
            check_tile = board[upper][right]
            if self.ops_color(input_tile, check_tile):
                while self.ops_color(input_tile, check_tile):
                    right += 1
                    upper -= 1
                    check_tile = board[upper][right]
                return self.same_color(input_tile, check_tile)

    def check_middle_right(self, board: List[Tile], row: int, col: int, input_tile: Tile) -> bool:
        right = row + 1
        if self.valid_cell(col, right):
            check_tile = board[col][right]
            if self.ops_color(input_tile, check_tile):
                while self.ops_color(input_tile, check_tile):
                    right += 1
                    check_tile = board[col][right]
                return self.same_color(input_tile, check_tile)

    def check_lower_right(self, board: List[Tile], row: int, col: int, input_tile: Tile) -> bool:
        right = row + 1
        lower = col + 1
        if self.valid_cell(lower, right):
            check_tile = board[lower][right]
            if self.ops_color(input_tile, check_tile):
                while self.ops_color(input_tile, check_tile):
                    right += 1
                    lower += 1
                    check_tile = board[lower][right]
                return self.same_color(input_tile, check_tile)

    def check_lower_middle(self, board: List[Tile], row: int, col: int, input_tile: Tile) -> bool:
        lower = col + 1
        if self.valid_cell(lower, row):
            check_tile = board[lower][row]
            if self.ops_color(input_tile, check_tile):
                while self.ops_color(input_tile, check_tile):
                    lower += 1
                    check_tile = board[lower][row]
                return self.same_color(input_tile, check_tile)

    def check_lower_left(self, board: List[Tile], row: int, col: int, input_tile: Tile) -> bool:
        left = row - 1
        lower = col + 1
        if self.valid_cell(lower, left):
            check_tile = board[lower][left]
            if self.ops_color(input_tile, check_tile):
                while self.ops_color(input_tile, check_tile):
                    left -= 1
                    lower += 1
                    check_tile = board[lower][left]
                return self.same_color(input_tile, check_tile)

    def check_middle_left(self, board: List[Tile], row: int, col: int, input_tile: Tile) -> bool:
        left = row - 1
        if self.valid_cell(col, left):
            check_tile = board[col][left]
            if self.ops_color(input_tile, check_tile):
                while self.ops_color(input_tile, check_tile):
                    left -= 1
                    check_tile = board[col][left]
                return self.same_color(input_tile, check_tile)

    def check_upper_left(self, board: List[Tile], row: int, col: int, input_tile: Tile) -> bool:
        left = row - 1
        upper = col - 1
        if self.valid_cell(upper, left):
            check_tile = board[upper][left]
            if self.ops_color(input_tile, check_tile):
                while self.ops_color(input_tile, check_tile):
                    left -= 1
                    upper -= 1
                    check_tile = board[upper][left]
                return self.same_color(input_tile, check_tile)

    def adjacent_check(self, board: List[Tile], row: int, col: int, input_tile: Tile):
        """
        NOTE: 隣りあう石のチェック もし空白であれば、その石の八方をチェック
        """
        position = []
        if self.check_blank(board, row, col):  # 置きたい場所が空白かチェック
            if self.check_upper_middle(board, row=row, col=col, input_tile=input_tile):
                position.append((row, col))
            if self.check_upper_right(board, row=row, col=col, input_tile=input_tile):
                position.append((row, col))
            if self.check_middle_right(board, row=row, col=col, input_tile=input_tile):
                position.append((row, col))
            if self.check_lower_right(board, row=row, col=col, input_tile=input_tile):
                position.append((row, col))
            if self.check_lower_middle(board, row=row, col=col, input_tile=input_tile):
                position.append((row, col))
            if self.check_lower_left(board, row=row, col=col, input_tile=input_tile):
                position.append((row, col))
            if self.check_middle_left(board, row=row, col=col, input_tile=input_tile):
                position.append((row, col))
            if self.check_upper_left(board, row=row, col=col, input_tile=input_tile):
                position.append((row, col))
        return position

    def where_you_can_put(self, board: Board, input_tile: Tile) -> List[Tuple]:
        checked_list = []
        for col in range(8):
            for row in range(8):
                checked = self.adjacent_check(board.cells, row, col, input_tile)
                for i in checked:
                    if i:
                        checked_list.append(i)
        return checked_list

    def positions_tile_flipped(self, board: Board, row: int, col: int, input_tile: Tile) -> List[Tuple]:
        positions_tile_flipped: List[List[Tuple]] = []
        upper_middle_tiles_flipped = self.flip_upper_middle(board, row=row, col=col, input_tile=input_tile)
        if upper_middle_tiles_flipped:
            positions_tile_flipped.append(upper_middle_tiles_flipped)
        upper_right_tiles_flipped = self.flip_upper_right(board, row=row, col=col, input_tile=input_tile)
        if upper_right_tiles_flipped:
            positions_tile_flipped.append(upper_right_tiles_flipped)
        middle_right_tiles_flipped = self.flip_middle_right(board, row=row, col=col, input_tile=input_tile)
        if middle_right_tiles_flipped:
            positions_tile_flipped.append(middle_right_tiles_flipped)
        lower_right_tiles_flipped = self.flip_lower_right(board, row=row, col=col, input_tile=input_tile)
        if lower_right_tiles_flipped:
            positions_tile_flipped.append(lower_right_tiles_flipped)
        lower_middle_tiles_flipped = self.flip_lower_middle(board, row=row, col=col, input_tile=input_tile)
        if lower_middle_tiles_flipped:
            positions_tile_flipped.append(lower_middle_tiles_flipped)
        lower_left_tiles_flipped = self.flip_lower_left(board, row=row, col=col, input_tile=input_tile)
        if lower_left_tiles_flipped:
            positions_tile_flipped.append(lower_left_tiles_flipped)
        middle_left_tiles_flipped = self.flip_middle_left(board, row=row, col=col, input_tile=input_tile)
        if middle_left_tiles_flipped:
            positions_tile_flipped.append(middle_left_tiles_flipped)
        upper_left_tiles_flipped = self.flip_upper_left(board, row=row, col=col, input_tile=input_tile)
        if upper_left_tiles_flipped:
            positions_tile_flipped.append(upper_left_tiles_flipped)
        return list(itertools.chain.from_iterable(positions_tile_flipped))

    def flip_upper_middle(self, board: List[Tile], row: int, col: int, input_tile: Tile) -> List[Tuple]:
        positions_tile_flipped: List[Tuple] = []
        up = col - 1
        if not self.valid_cell(up, row):
            return positions_tile_flipped
        flip_tile = board[up][row]
        if self.ops_color(input_tile, flip_tile):
            positions_tile_flipped.append((up, row))
            while self.ops_color(input_tile, flip_tile):
                up -= 1
                if not self.valid_cell(up, row):
                    return positions_tile_flipped
                flip_tile = board[up][row]
                if self.ops_color(input_tile, flip_tile):
                    positions_tile_flipped.append((up, row))
                if self.same_color(input_tile, flip_tile):
                    return positions_tile_flipped

    def flip_upper_right(self, board: List[Tile], row: int, col: int, input_tile: Tile) -> List[Tuple]:
        positions_tile_flipped: List[Tuple] = []
        upper = col - 1
        right = row + 1
        if not self.valid_cell(upper, right):
            return positions_tile_flipped
        flip_tile = board[upper][right]
        if self.ops_color(input_tile, flip_tile):
            positions_tile_flipped.append((upper, right))
            while self.ops_color(input_tile, flip_tile):
                upper -= 1
                right += 1
                if not self.valid_cell(upper, right):
                    return positions_tile_flipped
                flip_tile = board[upper][right]
                if self.ops_color(input_tile, flip_tile):
                    positions_tile_flipped.append((upper, right))
                if self.same_color(input_tile, flip_tile):
                    return positions_tile_flipped

    def flip_middle_right(self, board: List[Tile], row: int, col: int, input_tile: Tile) -> List[Tuple]:
        positions_tile_flipped: List[Tuple] = []
        right = row + 1
        if not self.valid_cell(col, right):
            return positions_tile_flipped        
        flip_tile = board[col][right]
        if self.ops_color(input_tile, flip_tile):
            positions_tile_flipped.append((col, right))
            while self.ops_color(input_tile, flip_tile):
                right += 1
                if not self.valid_cell(col, right):
                    return positions_tile_flipped
                flip_tile = board[col][right]
                if self.ops_color(input_tile, flip_tile):
                    positions_tile_flipped.append((col, right))
                if self.same_color(input_tile, flip_tile):
                    return positions_tile_flipped

    def flip_lower_right(self, board: List[Tile], row: int, col: int, input_tile: Tile) -> List[Tuple]:
        positions_tile_flipped: List[Tuple] = []
        lower = col + 1
        right = row + 1
        if not self.valid_cell(lower, right):
            return positions_tile_flipped
        flip_tile = board[lower][right]
        if self.ops_color(input_tile, flip_tile):
            positions_tile_flipped.append((lower, right))
            while self.ops_color(input_tile, flip_tile):
                lower += 1
                right += 1
                if not self.valid_cell(lower, right):
                    return positions_tile_flipped
                flip_tile = board[lower][right]
                if self.ops_color(input_tile, flip_tile):
                    positions_tile_flipped.append((lower, right))
                if self.same_color(input_tile, flip_tile):
                    return positions_tile_flipped

    def flip_lower_middle(self, board: List[Tile], row: int, col: int, input_tile: Tile) -> List[Tuple]:
        positions_tile_flipped: List[Tuple] = []
        lower = col + 1
        if not self.valid_cell(lower, row):
            return positions_tile_flipped
        flip_tile = board[lower][row]
        if self.ops_color(input_tile, flip_tile):
            positions_tile_flipped.append((lower, row))
            while self.ops_color(input_tile, flip_tile):
                lower += 1
                if not self.valid_cell(lower, row):
                    return positions_tile_flipped
                flip_tile = board[lower][row]
                if self.ops_color(input_tile, flip_tile):
                    positions_tile_flipped.append((lower, row))
                if self.same_color(input_tile, flip_tile):
                    return positions_tile_flipped

    def flip_lower_left(self, board: List[Tile], row: int, col: int, input_tile: Tile) -> List[Tuple]:
        positions_tile_flipped: List[Tuple] = []
        lower = col + 1
        left = row - 1
        if not self.valid_cell(lower, left):
            return positions_tile_flipped
        flip_tile = board[lower][left]
        if self.ops_color(input_tile, flip_tile):
            positions_tile_flipped.append((lower, left))
            while self.ops_color(input_tile, flip_tile):
                lower += 1
                left -= 1
                if not self.valid_cell(lower, left):
                    return positions_tile_flipped
                flip_tile = board[lower][left]
                if self.ops_color(input_tile, flip_tile):
                    positions_tile_flipped.append((lower, left))
                if self.same_color(input_tile, flip_tile):
                    return positions_tile_flipped

    def flip_middle_left(self, board: List[Tile], row: int, col: int, input_tile: Tile) -> List[Tuple]:
        positions_tile_flipped: List[Tuple] = []
        left = row - 1
        if not self.valid_cell(col, left):
            return positions_tile_flipped
        flip_tile = board[col][left]
        if self.ops_color(input_tile, flip_tile):
            positions_tile_flipped.append((col, left))
            while self.ops_color(input_tile, flip_tile):
                left -= 1
                if not self.valid_cell(col, left):
                    return positions_tile_flipped
                flip_tile = board[col][left]
                if self.ops_color(input_tile, flip_tile):
                    positions_tile_flipped.append((col, left))
                if self.same_color(input_tile, flip_tile):
                    return positions_tile_flipped

    def flip_upper_left(self, board: List[Tile], row: int, col: int, input_tile: Tile) -> List[Tuple]:
        positions_tile_flipped: List[Tuple] = []
        upper = col - 1
        left = row - 1
        if not self.valid_cell(upper, left):
            return positions_tile_flipped
        flip_tile = board[upper][left]
        if self.ops_color(input_tile, flip_tile):
            positions_tile_flipped.append((upper, left))
            while self.ops_color(input_tile, flip_tile):
                upper -= 1
                left -= 1
                if not self.valid_cell(upper, left):
                    return positions_tile_flipped
                flip_tile = board[upper][left]
                if self.ops_color(input_tile, flip_tile):
                    positions_tile_flipped.append((upper, left))
                if self.same_color(input_tile, flip_tile):
                    return positions_tile_flipped

    def flip_tiles(self, board: Board, row: int, col: int, input_tile: Tile) -> Board:
        tiles_flipped:List[Tuple] = self.positions_tile_flipped(board.cells, row, col, input_tile)
        board_tiles_flipped = copy(board)
        for p in tiles_flipped:
            col, row = p
            board_tiles_flipped.cells[col][row] = input_tile

        return board_tiles_flipped