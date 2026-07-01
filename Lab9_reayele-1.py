"""
Program name: The Main Game Logic
Author: Rediet Ayele
Purpose: This file runs the game. It creates the Player objects and manages the game loop and rules.
Date: 06/27/26
"""

from player import Player

def main():
    print("--- Coin Match Game ---")

    player1 = Player("Player 1")
    player2 = Player("Player 2")

    print(player1.get_name(), "has", player1.get_wallet(), "coins.")
    print(player2.get_name(), "has", player2.get_wallet(), "coins.")

    coins = input("Do you want to toss the coins? (y/n): ")

    while coins == "y":
        print("Tossing...")

    

        coins = input("Do you want to toss the coins? (y/n): ")
if __name__ == "__main__":
    main()