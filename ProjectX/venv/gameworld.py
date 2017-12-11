import random
import sys

import config
import game
from player import Player
from monster import Monster

def sendGameWorld(player):
    # Vi fortsätter skicka vår gameWorld så länge spelaren exsisterar
    while True:
        option = input("###  Welcome " + player.getName() + " ###\nWhat would you like todo 1. Gamble 2. Hunting 3. Status 4. Exit\n> ")

        if not option.isdigit():
            continue

        if int(option) == 1:
            rolledDice = False
            while (rolledDice != True):
                betAmountInput = input("How much would you like to bet\n>")
                if not betAmountInput.isdigit():
                    continue

                if int(betAmountInput) > player.getMoney():
                    print("You dont have enough money.")
                    continue
                elif int(betAmountInput) < 10:
                    print("You cannot bet less than 10 gold coins.")
                    continue

                chooseNumberInput = input("Choose a number between 1-6\n> ")
                if not chooseNumberInput.isdigit() or int(chooseNumberInput) < 1 or int(chooseNumberInput) > 6:
                    continue

                dice = random.randint(1, 6)
                if dice == int(chooseNumberInput):
                    print("\nWooo you won " + str(int(betAmountInput) * 2) + ".\n")
                    player.addMoney(int(betAmountInput) * 2)
                else:
                    print("\nYou rolled number : " + str(dice) + ", you lost.\n")
                    player.addMoney(-int(betAmountInput))

                rolledDice = True
        elif int(option) == 2:
            huntingList = {
                "easy": ["orc", "troll"],
                "medium": ["vampire", "cyclops"],
                "hard": ["demon", "dragon"]
            }

            chooseDifficulty = input("Choose difficulty between: easy, medium or hard.\n> ")
            while not chooseDifficulty in ["easy", "medium", "hard"]:
                chooseDifficulty = input("Choose difficulty between: easy, medium or hard.\n> ")

            chooseMonster = input("What monster would you like to fight? " + str(huntingList[chooseDifficulty]) + "?\n>")
            if chooseMonster in huntingList[chooseDifficulty]:
                monster = Monster(chooseMonster.lower(), None)
                monster.onDeath(player)
        elif int(option) == 3:
            game.sendTextMessage("#Loading character status#\n")
            print("Name: {}, Level: {}\nHealth: {}/{}, Profession: {}\nAttack: {}, Defense: {}\nMoney: {}, Inventory: {}".format(player.getName(), player.getLevel(), player.getHealth(), player.getMaxHealth(), player.getProfession(), player.getAttack(), player.getDefense(), player.getMoney(), player.getInventory()))
        elif int(option) == 4:
            # To-do spara spelarens framsteg
            print("Logging out.")
            sys.exit()