from models.Board import Board
from models.Tile import Tile
from models.Manager import Manager
from utils.log import logger

class DrawBoard:
    """View"""

    def __init__(self):
        self.manager = Manager()

    def draw(self, board: Board, input_tile: Tile):
        """
        NOTE: 盤面を描写する
        """
        """
        FIXME: のちのちrow, colを1〜8にしたい（入力と整合性をとる）
        """
        row = ["\nX", 0, 1, 2, 3, 4, 5, 6, 7]
        col = [0, 1, 2, 3, 4, 5, 6, 7]
        print(*row)
        for b in range(board.board_size):
            print(col[b], *board.cells[b])

        where_you_can_put = list(set(self.manager.where_you_can_put(board=board, input_tile=input_tile)))
        
        if len(where_you_can_put) > 0:
            logger.info(f"置ける場所 {where_you_can_put}")
        else:
            logger.info(f"置ける場所がありません")