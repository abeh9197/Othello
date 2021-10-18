from enum import Enum

class Game():

    def __init__(self):
        self.player = Player()
        self.drawboard = DrawBoard().drawboard()


class TileValue(Enum):

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

    def __init__(self, cells=None, board_size=8):
        self.board_size = board_size
        if cells is None:
            self.cells = self.init_board()
        else:
            self.cells = cells
        
    def init_board(self):
        blank_cell = Tile.from_number(-1)
        board = [[blank_cell for c in range(self.board_size)] for c in range(self.board_size)]
        board[3][3] = Tile.from_number(0)
        board[3][4] = Tile.from_number(1)
        board[4][3] = Tile.from_number(1)
        board[4][4] = Tile.from_number(0)
        return board

    def color_cell(self, x, y, input_color):
        self.cells[x][y] = input_color
        return self


class DrawBoard:

    def __init__(self, board=None, board_size=8):
        self.board = Board().init_board()
        self.board_size = board_size

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
        for b in range(self.board_size):
            print(col[b], *self.board[b])

        
class Player:

    def __init__(self):
        pass

    def player_input(self):
        x = input('入力してください x : ')
        y = input('入力してください y : ')
        return x, y


class Round:
    
    def __init__(self, players, count) -> None:
        self.players = players
        self.count = count


class Checker:
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
        if self.check_blank(board, x, y): #置きたい場所が空白かチェック
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
                    if i != None:
                        checked_list.append(i)
        return checked_list


def main():
    game_start()

if __name__ == '__main__':
    main()


def game_start():
    game = Game()
    game.player.player_input()

print('hoge')