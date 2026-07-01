"""
Program name: The Player Class 
Author: Rediet Ayele
Purpose: This class represents a player. A player has a name, has a wallet of coins, and has a Coin object to toss.
Date: 06/27/26
"""

from coin import Coin

class Player:
        def __init__(self, name):
            self.__name = name
            self.__wallet = 20
            self.__coin = Coin()
       
        def get_name(self):
            return self.__name
        def get_wallet(self):
            return self.__wallet
        def win_coin(self):
            self.__wallet += 1
        def lose_coin(self):
             self.__wallet -= 1
        def toss_coin(self):
             self.__coin.toss()
        def get_coin_side(self):
           return self.__coin.get_sideup()
