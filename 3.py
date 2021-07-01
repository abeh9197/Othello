class Stone: #石
    WHITE = " ○"
    BLACK = " ●"


class Cell: #マス目を表現
    WHITE = Stone.WHITE
    BLACK = Stone.BLACK
    EMPTY = " □"
    NONE = None


class Board: #盤面
    EDGE = 8  # 1辺の個数
    INDEX = range(EDGE)

    def __init__(self):
        self.cells = [[Cell.EMPTY] * self.EDGE for _ in self.INDEX]
        center = self.EDGE // 2
        self.cells[center - 1][center - 1] = Cell.WHITE
        self.cells[center - 1][center - 0] = Cell.BLACK
        self.cells[center - 0][center - 1] = Cell.BLACK
        self.cells[center - 0][center - 0] = Cell.WHITE

    def __getitem__(self, xy):
        x, y = xy
        if x in range(self.INDEX) and y in range(self.INDEX):
            return self[y][x]
        return Cell.None



class Player: #プレーヤーができること
    DIR = [(x, y) for x in (-1, 0, 1) for y in (-1, 0, 1) if not x == y == 0]

    def __init__(self) -> None:
        pass



board = Board()
print(board.cells)