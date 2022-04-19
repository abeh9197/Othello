from models.Game import Game
from models.Board import Board
from utils.log import logger


def game_start():
    """Model"""
    logger.info("----- game start -----")
    game = Game()
    init_board = Board(cells=None)
    game.draw(init_board)
    while game.not_done:
        logger.info(game.log_whos_turn())
        row, col = game.get_input()
        """validation"""
        if game.input_validation(row, col, init_board):
            board = init_board
            board_not_flipped = board.get_from_input(row=row, col=col, input_color=game.status.current_player)
            board_tiles_flipped = game.flip_tiles(board_not_flipped, row=row, col=col)
            game.status.change_player()
            game.draw(board_tiles_flipped)
        else:
            logger.info("そこには置けません")