from secrets import randbelow
from time import sleep, time

class dice():
    def __init__(self, freq):
        self.freq=freq # YOU MUST COLLECT AT LEAST 6*4*5*300 TIMES
        # freq[6上面][4前面][5可能的面骰到的比例]
    def roll(self, side, strength) -> int:
        # type(side)==int
        # type(strength)==float
        throwing_time=(randbelow(100)+1)/100*strength
        time1=time()
        time2=time()
        while time2-time1<=throwing_time:
            pass