from models.Board import Board
from models.Tile import Tile
from models.Manager import Manager
from models.Status import Status
from utils.log import logger


class DrawBoard:
    """View"""

    def __init__(self):
        self.manager = Manager()
        self.status = Status()

    def draw(self, board: Board, input_tile: Tile):
        """
        NOTE: 盤面を描写する
        """
        print("   1  2  3  4  5  6  7  8")
        print("  ------------------------")
        for i in range(board.board_size):
            print(i+1, "|", end="")
            for j in range(8):
                print(board.cells[i][j], "|", end="")
            print("\n  ------------------------")

        where_you_can_put = list(
            set(self.manager.where_you_can_put(board=board, input_tile=input_tile))
        )
        where_you_can_put = [(position[0] + 1, position[1] + 1) for position in where_you_can_put]

        if len(where_you_can_put) > 0:
            logger.info(f"残り {self.status.count_cell_type(board=board)}")
            logger.info(f"置ける場所 {where_you_can_put}")
        else:
            logger.info(f"置ける場所がありません")
