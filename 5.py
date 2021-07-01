import numpy as np

empty = 0
light = 1
dark = -1
wall = 2

class Board:
    def __init__(self):
        self.rawboard = np.zeros((10,10), dtype=int)
        self.rawboard[0, :] = wall
        self.rawboard[:, 0] = wall
        self.rawboard[9, :] = wall
        self.rawboard[:, 9] = wall

        self.rawboard[4, 4] = light
        self.rawboard[5, 5] = light
        self.rawboard[4, 5] = dark
        self.rawboard[5, 4] = dark

        self.turns = 0
        self.currentcolor = dark

board = Board()
print(board.rawboard)

class Putdisks:
    def __init__(self, x, y):
        self.x = x
        self.y = y

hand = Putdisks(3, 4)

class flipdisks:
    def __init__(self, x, y):
        
