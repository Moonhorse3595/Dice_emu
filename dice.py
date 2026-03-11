import secrets
from time import sleep

class dice():
    def __init__(self, freq):
        self.freq=freq # YOU MUST COLLECT AT LEAST 6*4*5*300 TIMES
        # freq[6][4][5]
    def roll(self, side, strength) -> int:
        # type(side)==int
        # type(strength)==float
        pass