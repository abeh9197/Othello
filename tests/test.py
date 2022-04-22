import unittest
from othello import Board, DrawBoard, Tile, Game, TileValue, Checker


class UnitTest(unittest.TestCase):
    def test_get_position_from_input(self):
        g = Game()
