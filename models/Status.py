class Status:
    """Model"""

    def __init__(self) -> None:
        self.turn: int = 0
        self.current_player: int = 0
    
    def change_player(self):
        if self.current_player == 0:
            self.current_player = 1
        elif self.current_player == 1:
            self.current_player = 0
    
    def show_whos_turn(self) -> str:
        if self.current_player == 0:
            return "黒"
        if self.current_player == 1:
            return "白"
