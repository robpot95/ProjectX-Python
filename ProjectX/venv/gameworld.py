import random
import sys

import combat
import config
import game
from player import Player
from monster import Monster

def sendGameWorld(player):
    # Vi fortsätter skicka vår gameWorld så länge spelaren exsisterar
    while True:
        # Healing system
        if player.getHealth() <= 0:
            healingInput = input("You are dead, please write heal.\n> ")
            if healingInput == "heal":
                player.addHealth(player.getMaxHealth())
                print("You are fully recovered.")
            else:
                continue

        option = input("###  Welcome " + player.getName() + " ###\nWhat would you like todo 1. Gamble 2. Hunting 3. Character 4. Exit\n> ")

        if not option.isdigit():
            continue

        if int(option) == 1:
            if player.getMoney() < 10:
                print("You need minium 10 gold coins to gamble.")
                continue

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
            # Generera en huntingList
            huntingList = {}
            for name, info in config.monsterList.items():
                level = int(info["baseLevel"])
                if level < 5:
                    huntingList.setdefault("easy", []).append(name)
                elif level < 10:
                    huntingList.setdefault("medium", []).append(name)
                else:
                    huntingList.setdefault("hard", []).append(name)

            chooseDifficulty = input("Choose difficulty between: easy, medium or hard.\n> ")
            while not chooseDifficulty in ["easy", "medium", "hard"]:
                chooseDifficulty = input("Choose difficulty between: easy, medium or hard.\n> ")

            chooseMonster = input("What monster would you like to fight? " + ", ".join(huntingList[chooseDifficulty]) + "?\n> ")
            if chooseMonster in huntingList[chooseDifficulty]:
                monster = Monster(chooseMonster.lower(), None)
                monster.adjustStatus()
                combat.executeFight(player, monster)
        elif int(option) == 3:
            game.sendTextMessage("#Loading character#\n")
            characterOption = input("1. Character Status\n2. Inventory\n3. Equipment\n> ")

            if int(characterOption) == 1:
                print("Name: {}, Level: {}\nHealth: {}/{}, Profession: {}\nAttack: {}, Defense: {}\nMoney: {}, Inventory: {}".format(player.getName(), player.getLevel(), player.getHealth(), player.getMaxHealth(), player.getProfession(), player.getAttack(), player.getDefense(), player.getMoney(), ", ".join(player.getInventory()) or "Empty"))
            elif int(characterOption) == 2:
                if len(player.getInventory()) == 0:
                    print("Your inventory is empty.")
                    return

                inventoryInput = input("You got these items in your inventory: " + ", ".join(player.getInventory()) + ". Would you like equip these items?\n> ")
                if inventoryInput.lower() == "yes":
                    itemInput = input("What item would you like to wear? " + ", ".join(player.getInventory()) + "\n> ")
                    player.wearItem(itemInput.lower())
            elif int(characterOption) == 3:
                print(player.getEquipment())
        elif int(option) == 4:
            # To-do spara spelarens framsteg
            game.savePlayer(player)
            game.sendTextMessage("Saving player... Logging out.")
            sys.exit()