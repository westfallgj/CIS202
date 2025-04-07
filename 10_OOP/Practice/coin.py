import random

class Coin:

    """Represents a coin that can be tossed to land on heads or tails.

    Attributes:
        sideup (str): The current side facing up ('Heads' or 'Tails'). Defaults to 'Heads'.

    Methods:
        toss(): Randomly flips the coin, updating the 'sideup' attribute.
        get_sideup(): Returns the current side facing up.
    """
   
    def __init__(self):
        self.__sideup = 'Heads'

    def toss(self):
        if random.randint(0, 1) == 0:
            self.sideup = 'Heads'
        else:
            self.sideup = 'Tails'

    def get_sideup(self):
        return self.sideup

    def __str__(self):
        return(self.sideup)