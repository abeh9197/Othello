import numpy as np

empty = 0
light = -1
dark = 1
wall = 2

board_size = 8

NONE = 0
LEFT = 2**0 # =1
UPPER_LEFT = 2**1 # =2 
UPPER = 2**2 # =4
UPPER_RIGHT = 2**3 # =8
RIGHT = 2**4 # =16
LOWER_RIGHT = 2**5 # =32
LOWER = 2**6 # =64
LOWER_LEFT = 2**7 # =128

IN_ALFABET = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
IN_NUMBER = ['1', '2', '3', '4', '5', '6', '7', '8', ]

class Board:
    def __init__(self):
        self.rawboard = np.zeros((board_size + 2, board_size + 2), dtype=int)
        self.rawboard[0, :] = wall
        self.rawboard[:, 0] = wall
        self.rawboard[board_size + 1, :] = wall
        self.rawboard[:, board_size + 1] = wall

        self.rawboard[4,4] = light
        self.rawboard[5,5] = light
        self.rawboard[4,5] = dark
        self.rawboard[5,4] = dark

        self.turns = 0

        self.currentturn = dark

        self.movablepos = np.zeros((board_size + 2, board_size + 2), dtype=int)
        self.movabledir = np.zeros((board_size + 2, board_size + 2), dtype=int)

        self.initmovable()

    def checkmobility(self, x, y, color):
        
        dir = 0

        #空いているか
        if(self.rawboard[x, y] != empty):
            return dir

        #左
        if((self.rawboard[x - 1, y] == - color)):
            x_temp = x - 2
            y_temp = y

            while self.rawboard[x_temp, y_temp] == - color:
                x_temp -= 1

            if self.rawboard[x_temp, y_temp] == color:
                dir = dir | LEFT

        #左上
        if((self.rawboard[x - 1, y - 1] == - color)):
            x_temp = x - 2
            y_temp = y - 2

            while self.rawboard[x_temp, y_temp] == - color:
                x_temp -= 1
                y_temp -= 1

            if self.rawboard[x_temp, y_temp] == color:
                dir = dir | UPPER_LEFT

        #上
        if((self.rawboard[x, y - 1] == - color)):
            x_temp = x
            y_temp = y - 2

            while self.rawboard[x_temp, y_temp] == - color:
                y_temp -= 1

            if self.rawboard[x_temp, y_temp] == color:
                dir = dir | UPPER

        #右上
        if((self.rawboard[x + 1, y - 1] == - color)):
            x_temp = x + 2
            y_temp = y - 2

            while self.rawboard[x_temp, y_temp] == - color:
                x_temp += 1
                y_temp -= 1

            if self.rawboard[x_temp, y_temp] == color:
                dir = dir | UPPER_RIGHT

        #右
        if((self.rawboard[x + 1, y] == - color)):
            x_temp = x + 2
            y_temp = y

            while self.rawboard[x_temp, y_temp] == - color:
                x_temp += 1
            
            if self.rawboard[x_temp, y_temp] == color:
                dir = dir | RIGHT        

        #右下
        if((self.rawboard[x + 1, y + 1] == - color)):
            x_temp = x + 2
            y_temp = y + 2

            while self.rawboard[x_temp, y_temp] == - color:
                x_temp += 1
                y_temp += 1

            if self.rawboard[x_temp, y_temp] == color:
                dir = dir | LOWER_RIGHT

        #下
        if((self.rawboard[x, y + 1] == - color)):
            x_temp = x
            y_temp = y + 2

            while self.rawboard[x_temp, y_temp] == - color:
                y_temp += 1

            if self.rawboard[x_temp, y_temp] == color:
                dir = dir | LOWER
        
        #左下
        if((self.rawboard[x - 1, y + 1] == - color)):
            x_temp = x - 2
            y_temp = y + 2

            while self.rawboard[x_temp, y_temp] == - color:
                x_temp -= 1
                y_temp += 1

            if self.rawboard[x_temp, y_temp] == color:
                dir = dir | LOWER_LEFT

        return dir


    def flipdisks(self, x, y):
        self.rawboard[x, y] = self.currentturn

        dir = self.movabledir[x, y]

        if dir & LEFT:
            x_temp = x - 1
            while self.rawboard[x_temp, y] == - self.currentturn:
                self.rawboard[x_temp, y] = self.currentturn
                x_temp -= 1

        if dir & UPPER_LEFT:
            x_temp = x - 1
            y_temp = y - 1
            while self.rawboard[x_temp, y_temp] == - self.currentturn:
                self.rawboard[x_temp, y_temp] = self.currentturn
                x_temp -= 1
                y_temp -= 1

        if dir & UPPER:
            y_temp = y - 1
            while self.rawboard[x, y_temp] == - self.currentturn:
                self.rawboard[x, y_temp] = self.currentturn
                y_temp -= 1

        if dir & UPPER_RIGHT:
            x_temp = x + 1
            y_temp = y - 1
            while self.rawboard[x_temp, y_temp] == - self.currentturn:
                self.rawboard[x_temp, y_temp] = self.currentturn
                x_temp += 1
                y_temp -= 1        

        if dir & RIGHT:
            x_temp = x + 1
            while self.rawboard[x_temp, y] == - self.currentturn:
                self.rawboard[x_temp, y] = self.currentturn
                x_temp += 1

        if dir & LOWER_RIGHT:
            x_temp = x + 1
            y_temp = y + 1
            while self.rawboard[x_temp, y_temp] == - self.currentturn:
                self.rawboard[x_temp, y_temp] = self.currentturn
                x_temp += 1
                y_temp += 1

        if dir & LOWER:
            y_temp = y + 1
            while self.rawboard[x, y_temp] == - self.currentturn:
                self.rawboard[x, y_temp] = self.currentturn
                y_temp += 1            

        if dir & LOWER_LEFT:
            x_temp = x - 1
            y_temp = y + 1
            while self.rawboard[x_temp, y_temp] == - self.currentturn:
                self.rawboard[x_temp, y_temp] = self.currentturn
                x_temp -= 1
                y_temp += 1

    def move(self, x, y):
        if x < 1 or board_size < x:
            return False
        if y < 1 or board_size < y:
            return False
        if self.movabledir[x, y] == 0:
            return False

        self.flipdisks(x, y)

        self.turns += 1
        self.currentturn = - self.currentturn

        self.initmovable()

        return True

    def initmovable(self):
        self.movablepos[:, :] = 0

        for x in range(1, board_size + 1):
            for y in range(1, board_size + 1):
                dir = self.checkmobility(x, y, self.currentturn)

                self.movabledir[x, y] = dir

                if dir != 0:
                    self.movablepos[x, y] = 1

    def display(self):
        print(' a b c d e f g h')
        for y in range(1, 9):
            print(y, end="")
            for x in range(1, 9):
                grid = self.rawboard[x, y]

                if grid == empty:
                    print("□ ", end="")
                elif grid == light:
                    print("● ", end="")
                elif grid == dark:
                    print("○ ", end="")
            
            print()

    def checkIN(self, IN):
        if not IN:
            return False
        
        if IN[0] in IN_ALFABET:
            if IN[1] in IN_NUMBER:
                return True
        
        return False

    def isgameover(self):
        if self.turns >= 60:
            return True
        
        if self.movablepos[:, :].any():
            return False

        for x in range(1, board_size):
            for y in range(1, board_size):
                if self.checkmobility(x, y, - self.currentturn ) != 0:
                    return False

        return True


        

board = Board()

while True:
    
    board.display()
    if board.currentturn == dark:
        print('黒の番')
    else:
        print('白の番')
    
    IN = input()
    print()

    if board.checkIN(IN):
        x = IN_ALFABET.index(IN[0]) + 1
        y = IN_NUMBER.index(IN[1]) + 1
    else:
        print('入力し直してください')
        continue

    if not board.move(x, y):
        print('そこには打てません。入力し直してください。')
        continue

    if board.isgameover():
        board.display()
        print('終わり')
        break

    if not board.movablepos[:, :].any():
        board.currentturn = - board.currentturn
        board.initmovable()
        print('パスしました')
        print()
        continue

countdark = np.count_nonzero(board.rawboard[:, :] == dark)
countlight = np.count_nonzero(board.rawboard[:, :] == light)

print('黒 :' + str(countdark))
print('白 :' + str(countlight))

if countlight > countdark:
    print('白の勝ち')
elif countdark > countlight:
    print('黒の勝ち')
else:
    print('引き分け')


# print(board.rawboard)
# print(board.movablepos)
# print(board.movabledir)