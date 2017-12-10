import random
import sys

from player import Player

def sendGameWorld(player):
    option = input("###  Welcome " + player.getName() + " ###\nWhat would you like todo 1. Gamble 2. Hunting 3. Exit\n> ")

    if not option.isdigit():
        sendGameWorld(player)

    if int(option) == 1:
        rolledDice = False
        while (rolledDice != True):
            chooseNumberInput = input("Choose a number between 1-6\n> ")
            if not chooseNumberInput.isdigit() or int(chooseNumberInput) < 1 or int(chooseNumberInput) > 6:
                continue

            dice = random.randint(1, 6)
            if dice == int(chooseNumberInput):
                print("\nWooo you won.\n")
                sendGameWorld(player)
            else:
                print("\nYou rolled number : " + str(dice) + ", you lost.\n")
                sendGameWorld(player)

            rolledDice = True
    elif int(option) == 2:
        huntingList = {
            "1": ["Orc", "Minotaur"],
            "2": ["Dragon", "Demon"]
        }

        chooseDifficulty = input("Choose a number between 1-" + str(len(huntingList)) +"\n> ")
    elif int(option) == 3:
        print("Exiting the game.")
        sys.exit()
    else:
        sendGameWorld(player)