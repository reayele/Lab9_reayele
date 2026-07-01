"""
Program name: The Coin Class
Author: Rediet Ayele
Purpose: This class represents a single, tossable coin. It only knows about its own state (heads or tails).
Date: 06/27/26
"""

import random

class Coin:
    def __init__(self):
        self.__sideup = "Heads"

    def toss(self):
        random_number = random.randint(0, 1)

        if random_number == 0:
            self.__sideup = "Heads"
        else:
            self.__sideup = "Tails"
    def get_sideup(self):
        return self.__sideup