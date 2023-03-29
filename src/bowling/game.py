from typing import List

from frame import Frame


MAX_FRAMES = 10 

class BowlingGame:
    def __init__(self, frames: List[Frame] = [], bonus: Frame = None) -> None:
        self.frames = frames
        self.bonus = bonus

    def add_frame(self, frame: Frame):
        """ Add a frame to the game """
        if frame.valid_throw():
            if len(self.frames) < MAX_FRAMES:
                self.frames.append(frame)
            else:
                raise ValueError("Limit of frames achived.")
        else:
            raise ValueError("Invalid frame.")

    def set_bonus(self, first_throw: int, second_throw: int):
        """ The the bonus throw """
        if self.is_next_frame_bonus():
            if self.frames[-1].is_strike():
                self.bonus = Frame(first_throw, second_throw)
            elif self.frames[-1].is_spare():
                self.bonus = Frame(first_throw)
            else:
                raise ValueError("Bonus not needed.")
        else:
            raise ValueError("Not allowed to set bonus yet")

    def score(self) -> int:
        """ Get the score from the game """
        score = 0
        for i, frame in enumerate(self.frames):
            score += frame.score()

            if frame.is_strike():
                if len(self.frames) > i:
                    score += self.frames[i+1].score()
                    if self.frames[i+1].is_strike():
                        if len(self.frames) > i + 1:
                            score +=  self.frames[i+2].first_throw
                        else:
                            score += self.bonus.first_throw
                else:
                    score += self.bonus.score()

                    

            if frame.is_spare():
                if len(self.frames) > i:
                    score += self.frames[i+1].first_throw
                else:
                    score += self.bonus.first_throw
            
        return score


    def is_next_frame_bonus(self) -> bool:
        """ Get if the next frame is bonus """
        return len(self.frames) == MAX_FRAMES and (self.frames[-1].is_strike() or self.frames[-1].is_spare())
