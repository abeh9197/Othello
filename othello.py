import random
from models.Game import Game
from models.Board import Board
from models.Tile import Tile
from utils.log import logger


def game_start(autoplay: bool):
    """Model"""
    logger.info("----- game start -----")
    logger.info("auto-play : %s", autoplay)
    game = Game()
    init_board = Board(cells=None)
    game.draw(init_board)
    while game.not_done:
        board = init_board
        if not game.no_position_to_put(board=board):
            logger.info(game.log_whos_turn())

            # autoplay
            if autoplay:
                row, col = random.choice(game.manager.where_you_can_put(board=board, input_tile=Tile.from_number(game.status.current_player)))
            else:
                row, col = game.get_input()
            """validation"""
            if game.input_validation(row, col, init_board):
                board_not_flipped = board.get_from_input(
                    row=row, col=col, input_color=game.status.current_player
                )
                board_tiles_flipped = game.flip_tiles(
                    board_not_flipped, row=row, col=col
                )
                game.status.change_player()
                game.draw(board_tiles_flipped)
            else:
                logger.info("そこには置けません")
        elif game.end(board=board):
            logger.info("----- game end -----")
            game.show_result(board=board)
            break
        else:
            logger.info("置ける場所がありません")
            logger.info("パス！")
            game.status.change_player()
