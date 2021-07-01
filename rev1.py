from reversi.reversi import UPPER_RIGHT
import numpy as np

empty = 0
dark = 1
light = -1
wall = 2

board_size = 8

#動かせる方向
none = 0
up = 1
upper_right = 2
right = 3
lower_right = 4
lower = 5
lower_left = 6
left = 7
upper_left = 8


class Board:
    def __init__(self):
        self.cells = np.zeros((board_size + 2, board_size + 2), dtype=int)
        
        self.cells[0, :] = wall
        self.cells[:, 0] = wall
        self.cells[board_size + 1, :] = wall
        self.cells[:, board_size + 1] = wall

        self.cells[4,4] = light
        self.cells[5,5] = light
        self.cells[4,5] = dark
        self.cells[5,4] = dark

        self.turns = 0

        self.currentturn = dark

    def flipdisks(self, x, y):
        self.cells[x, y] = self.currentturn

    def flip_directions(self, x, y): #(xが縦、yが横)

        directions = []
        temp_x = x
        temp_y = y
        #すでに石がある場合はFalse
        if self.cells[x, y] != empty:
            return directions
        
        #up の石を確認
        while self.cells[x - 1, y] == - self.currentturn: #接している石が自分のものでない間は続く
            temp_x -= 1
        if self.cells[temp_x, y] == self.currentturn:
            directions.append(1)
        
        
            


    def put(self, x, y):
        
        #置けない場所はFalse
        if x < 1 or board_size < x:
            return False
        elif y < 1 or board_size < y:
            return False
        

        self.flipdisks(x, y)

        #ターン更新
        self.turns += 1
        self.currentturn = - self.currentturn

        return True

board = Board()
print(board.turns)
print(board.currentturn)
print(board.put(3, 4))
print(board.cells)
print(board.turns)
print(board.currentturn)