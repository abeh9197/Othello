class Stone:
    dark = ' ○'
    light = ' ●'

class Cell:
    dark = Stone.dark
    light = Stone.light
    empty = ' □'
    none = None

class Board:
    edge = 8
    index = range(edge)

    def __init__(self):
        self.cells = [[Cell.empty] * self.edge for _ in self.index]
        center = self.edge // 2
        self.cells[center - 1][center - 1] = Cell.light
        self.cells[center - 1][center - 0] = Cell.dark
        self.cells[center - 0][center - 1] = Cell.dark
        self.cells[center - 0][center - 0] = Cell.light

    def __getitem__(self, xy):
        x, y = xy
        if x in self.index and y in self.index:
            return self.cells[y][x]
        return Cell.none

    def __setitem__(self, xy, stone):
        x, y = xy
        self.cells[y][x] = stone

    def empties(self):
        return((x, y)
                for x in self.index
                for y in self.index
                if self[x, y] == Cell.empty)

    def count(self, stone):
        return sum(row.count(stone) for row in self.cells)

    def draw(self):
        print("n\YX", *[f"{x:>2}" for x in self.index])
        for y, row in enumerate(self.cells):
            print(f"{y:>2}", *row)

class Player:
    dir = [(x, y) for x in (-1, 0, 1) for y in (-1, 0, 1) if not x == y == 0]

    def __init__(self, name, self_stone, enemy_stone):
        self.name = name
        self.stone = self_stone
        self.enemy = enemy_stone
        self.putables = {}

    def __str__(self) -> str:
        return self.name

    def update(self, board):
        self.putables = {}
        for x, y in board.empties():
            reversibles = []
            for dx, dy in self.dir:
                ex = x + dx
                ey = y + dy
                if board[ex, ey] != self.enemy:
                    continue
                enemies = [(ex, ey)]
                for _ in board.index:
                    ex += dx
                    ey += dy
                    cell = board[ex, ey]
                    if cell == self.stone:
                        reversibles.extend(enemies)
                        break
                    if cell != self.enemy:
                        break
                    enemies.append((ex, ey))
            if reversibles:
                self.putables[x, y] = reversibles

    def playable(self): #置ける場所があればTrue、なければFalse
            return len(self.putables) > 0

    def play(self, board):
        if not self.putables:
            print('置ける場所がないのでパスします')
            return
        print('置ける場所: ', *(f"[{x} {y}]" for x, y in self.putables))
        while True:
            try:
                x, y = map(int, (input("位置指定 [X Y] >>").split()))
                if self.put(board, x, y):
                    return
            except ValueError:
                pass
            print("---Invalid Position---")

    def put(self, board, x, y): #置ければ石をひっくり返してTrueを返す　そうでなければFalse
        if(x, y) in self.putables:
            board[x, y] = self.stone
            for rx, ry in self.putables[x, y]:
                board[rx, ry] = self.stone
            return True
        return False

class Othello:

    def __init__(self):
        self.board = Board()
        self.dark = Player("黒", Stone.dark, Stone.light)
        self.light = Player("白", Stone.light, Stone.dark)
        self.player = self.dark
        self.turn = {self.light : self.dark,
                     self.dark : self.light}

    def playable(self):
        self.light.update(self.board)
        self.dark.update(self.board)
        return self.light.playable or self.dark.playable

    def play(self):
        while self.playable():
            self.board.draw()
            print(f"\n{self.player}のターン")
            self.player.play(self.board)
            self.player = self.turn[self.player]
        self.board.draw()
        self.judge()

    def judge(self):
        light = self.board.count(Stone.light)
        dark = self.board.count(Stone.dark)
        print('\n黒 >> ', dark,  '    白 >> ', light)
        if dark > light:
            print('黒の勝ち')
        elif light > dark:
            print('白の勝ち')
        else:
            print('引き分け')

def main():
    othello = Othello()
    othello.play()

if __name__ == '__main__':
    main()