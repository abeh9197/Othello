import unittest
from reversi import Board, DrawBoard, Tile, Game, TileValue, Checker

class UnitTest(unittest.TestCase):

    def test_drawboard(self):
        b = DrawBoard().drawboard()


    # def test_color(self):
    #     b = DrawBoard().board
    #     print(b[2][2].value.value['color'])

    
    # def test_blank(self):
    #     t = Tile.from_number(1)
    #     self.assertFalse(Player().check_blank(t))

    # def test_input(self):
    #     p = Player()
    #     r, c = p.input()
    #     b = DrawBoard().board
    #     print(b[r][c])

    # def test_ops_color(self):
    #     t = Tile.from_number(1)
    #     b = t.ops_color()
    #     print(b)
    #     print(type(b))

    # def test_check_up(self):
    #     b = DrawBoard().board
    #     input_tile = Tile.from_number(1)
        # print(Checker().check_up(b, 4, 5, input_tile))

    def test_Checker(self):
        b = DrawBoard().board
        input_tile = Tile.from_number(1)
        for x in range(7):
            for y in range(7):
                print(Checker().adjacent_check(b, x, y, input_tile))

