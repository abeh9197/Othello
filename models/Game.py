from models.Manager import Manager
from models.Player import Player
from view.Drawboard import DrawBoard
from models.Status import Status
from models.Tile import Tile
from models.Board import Board

class Game:
    """Model"""

    def __init__(self):
        self.player = Player()
        self.drawboard = DrawBoard()
        self.status = Status()
        self.manager = Manager()

    @property
    def not_done(self):
        done = 0
        return done == 0
    
    @property
    def input_tile(self):
        return Tile.from_number(self.status.current_player)

    def log_whos_turn(self) -> str:
        return f"{self.status.show_whos_turn()}の番"

    def get_input(self):
        return self.player.player_input()

    def input_validation(self, row, col, board) -> bool:
        positions_you_can_put = self.manager.where_you_can_put(board=board, input_tile=self.input_tile)
        return (row, col) in positions_you_can_put
    
    def draw(self, board):
        return self.drawboard.draw(board=board, input_tile=self.input_tile)

    def flip_tiles(self, board: Board, row: int, col: int) -> Board:
        return self.manager.flip_tiles(board, row, col, input_tile=self.input_tile)
    
    def no_position_to_put(self, board: Board) -> bool:
        return len(self.manager.where_you_can_put(board=board, input_tile=self.input_tile)) == 0

    def end(self, board: Board) -> bool:
        pass
