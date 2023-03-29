class Frame:
    def __init__(self, first_throw: int = 0, second_throw: int = 0) -> None:
        self.first_throw = first_throw
        self.second_throw = second_throw

    def valid_throw(self) -> bool:
        if not 0 <= self.first_throw <= 10 or not 0 <= self.second_throw <= 10:
            return False
        if self.first_throw == 10 and self.second_throw != 0:
            return False
        if self.first_throw + self.second_throw > 10:
            return False
        return True
    
    def score(self) -> int:
        """ The score of a single frame """
        if not self.valid_throw():
            raise ValueError("Invalid throw")
        return self.first_throw + self.second_throw

    def is_strike(self) -> bool:
        """ Return whether the frame is a strike or not """
        return self.valid_throw() and self.first_throw == 10

    def is_spare(self) -> bool:
        """ Return whether the frame is a spare or not """
        return self.valid_throw() and self.first_throw + self.second_throw == 10

    # def is_last_frame(self) -> bool:
    #     """ Return whether the frame is a last frame of the game """

    # def bonus(self) -> int:
    #     """ Bonus throw """
