hands_input1 = int(input())
hands_input2 = int(input())
hands_input = (hands_input1, hands_input2)



enemy_stone = (4, 4)
my_stone = (3, 3)
empty = (5, 2)


up = (0, -1)
up_right = (1, -1)
right = (1, 0)
down_right = (1, 1)
down = (0, 1)
down_left = (-1, 1)
left = (-1, 0)
up_left = (-1, -1)

around_hands = [(hands_input[0] - up[0], hands_input[1] - up[1]), (hands_input[0] - up_right[0], hands_input[1] - up_right[1]),\
      (hands_input[0] - right[0], hands_input[1] - right[1]),(hands_input[0] - down_right[0], hands_input[1] - down_right[1]),\
      (hands_input[0] - down[0], hands_input[1] - down[1]), (hands_input[0] - down_left[0], hands_input[1] - down_left[1]),\
      (hands_input[0] - left[0], hands_input[1] - left[1]), (hands_input[0] - up_left[0], hands_input[1] - up_left[1]) ]

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __sub__(self, other):
        return(self.x - other.x, self.y - other.y)

a = Vector(4, 4)
b = Vector(2, 2)
print(a - b)


for i in around_hands:
    if i == enemy_stone:
        print('置ける')
    elif i == my_stone:
        print('置けない')
    elif i == empty:
        print('置ける')

