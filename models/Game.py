import Player

class Game:
    """Model"""

    def __init__(self):
        self.player = Player()

    def get_input(self):
        return self.player.player_input()

    @property
    def not_done(self):
        done = 0
        return done == 0
