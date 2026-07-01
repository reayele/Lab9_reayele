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

    player1.toss_coin()
    player2.toss_coin()

    side1 = player1.get_coin_side()
    side2 = player2.get_coin_side()

    print(player1.get_name(), "tossed", side1)
    print(player2.get_name(), "tossed", side2)

    if side1 == side2:
        print("...Match! Player 1 wins a coin.")
        player1.win_coin()
        player2.lose_coin()

    else:
        print("...No Match! Player 2 wins a coin.")
        player1.lose_coin()
        player2.win_coin()

    print(player1.get_name(), "has", player1.get_wallet(), "coins.")
    print(player2.get_name(), "has", player2.get_wallet(), "coins.")

    coins = input("Do you want to toss the coins? (y/n): ")

    while coins == "n":
     print("--- Final Score ---")
    print(player1.get_name(), ":", player1.get_wallet())
    print(player2.get_name(), ":", player2.get_wallet())

    if player1.get_wallet() == player2.get_wallet():
        print("It's a draw!")

    elif player1.get_wallet() > player2.get_wallet():
        print(player1.get_name(), "wins!")

    else:
     print(player2.get_name(), "wins!")



if __name__ == "__main__":
    main()