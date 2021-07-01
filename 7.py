hands_input = (3, 3)

up = (0, -1)
up_right = (1, -1)
right = (1, 0)
down_right = (1, 1)
down = (0, 1)
down_left = (-1, 1)
left = (-1, 0)
up_left = (-1, -1)

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __sub__(self, other):
        return(self.x - other.x, self.y - other.y)

hand = Vector(hands_input[0], hands_input[1])
up_check = Vector(up[0], up[1])

