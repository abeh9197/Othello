class Stone:
    WHITE = " ○"
    BLACK = " ●"


class Cell:
    WHITE = Stone.WHITE
    BLACK = Stone.BLACK
    EMPTY = " □"
    NONE = None


class Board:
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
        if x in self.INDEX and y in self.INDEX:
            return self.cells[y][x]
        return Cell.NONE

    def __setitem__(self, xy, stone):
        x, y = xy
        self.cells[y][x] = stone

    def empties(self):
        return ((x, y)
                for x in self.INDEX
                for y in self.INDEX
                if self[x, y] == Cell.EMPTY)

    def count(self, stone):
        return sum(row.count(stone) for row in self.cells)

    def draw(self):
        print("\nYX", *[f"{x:>2}" for x in self.INDEX])
        for y, row in enumerate(self.cells):
            print(f"{y:>2}", *row)


class Player:
    DIR = [(x, y) for x in (-1, 0, 1) for y in (-1, 0, 1) if not x == y == 0]

    def __init__(self, name, self_stone, enemy_stone):
        self.name = name
        self.stone = self_stone
        self.enemy = enemy_stone
        self.putables = {}

    def __str__(self):
        return self.name

    def update(self, board):
        """置ける場所を更新"""
        self.putables = {}
        for x, y in board.empties():
            reversibles = []
            for dx, dy in self.DIR:
                ex = x + dx
                ey = y + dy
                if board[ex, ey] != self.enemy:
                    continue  # 隣が敵石でないのでひっくり返せない
                enemies = [(ex, ey)]
                for _ in board.INDEX:
                    ex += dx
                    ey += dy
                    cell = board[ex, ey]
                    if cell == self.stone:  # 自石で挟めばひっくり返せる
                        reversibles.extend(enemies)
                        break
                    if cell != self.enemy:  # 敵石がなくなればひっくり返せない
                        break
                    enemies.append((ex, ey))
            if reversibles:
                self.putables[x, y] = reversibles

    def playable(self):
        """置ける場所があればTrue、なければFalse"""
        return len(self.putables) > 0

    def play(self, board):
        if not self.putables:
            print("置ける場所がないのでパスします。")
            return
        print("置ける場所:", *(f"[{x} {y}]" for x, y in self.putables))
        while True:
            try:
                x, y = map(int, input("位置指定 [X Y] >> ").split())
                if self.put(board, x, y):
                    return
            except ValueError:
                pass
            print("---Invalid Position---")

    def put(self, board, x, y):
        """置ければ石をひっくり返してTrueを返す、さもなくばFalse"""
        if (x, y) in self.putables:
            board[x, y] = self.stone
            for rx, ry in self.putables[x, y]:
                board[rx, ry] = self.stone
            return True
        return False


class Othello:

    def __init__(self):
        self.board = Board()
        self.black = Player("黒", Stone.BLACK, Stone.WHITE)
        self.white = Player("白", Stone.WHITE, Stone.BLACK)
        self.player = self.black
        self.turn = {self.white: self.black,
                     self.black: self.white}

    def playable(self):
        self.white.update(self.board)
        self.black.update(self.board)
        return self.white.playable() or self.black.playable()

    def play(self):
        while self.playable():
            self.board.draw()
            print(f"\n{self.player}のターン")
            self.player.play(self.board)
            self.player = self.turn[self.player]
        self.board.draw()
        self.judge()

    def judge(self):
        white = self.board.count(Stone.WHITE)
        black = self.board.count(Stone.BLACK)
        print("\n黒 >> ", black, "   白 >> ", white)
        if black > white:
            print("黒の勝ち")
        elif white > black:
            print("白の勝ち")
        else:
            print("引き分け")


def main():
    othello = Othello()
    othello.play()

if __name__ == "__main__":
    main()