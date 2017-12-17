#Inbyggda
import json
import os
import sys
import textwrap
import time

#Custom class
import config
import gameworld
from player import Player

def setupCharacter():
    validName = False
    while (validName != True):
        try:
            nameInput = input(sendTextMessage("What would you like your name to be? \n> ")).capitalize()
        except SyntaxError:
            nameInput = ""

        if nameInput == "" or nameInput.isspace():
            print("Invalid name.")
        elif len(nameInput) < 3:
            print("Sorry, name is to short.")
        elif nameInput in ["Fuck", "Bitch"]:
            print("This kind of language is not acceptable.")
        else:
            validName = True

    sendTextMessage(nameInput + ", what a lovely name.\n")

    professionValid = False
    while (professionValid != True):
        professionInput = input(sendTextMessage("What profession would you like to be? " + ", ".join(config.professionList.keys()) + "?\n> ")).capitalize()

        if professionInput in config.professionList:
            professionDescription = input(sendTextMessage(config.professionList.get(professionInput)["description"] + " Are you sure?\n> "))
            if (professionDescription.capitalize() == "Yes"):
                professionValid = True


    sendTextMessage("A new character has been created. Your name will be: {} and your profession is: {}\n".format(nameInput, professionInput))
    newPlayer = Player(nameInput, 1, professionInput)

    time.sleep(1)
    clear = lambda: os.system('cls')
    clear()
    gameworld.sendGameWorld(newPlayer)

def sendTextMessage(message):
    for text in str(message):
        sys.stdout.write(text)
        sys.stdout.flush()
        time.sleep(0.05)
    return ""

def savePlayer(player):
    with open('data.txt', 'w') as outputFile:
        data = {
            "name": player.getName(),
            "level": player.getLevel(),
            "profession": player.getProfession(),
            "health": player.getHealth(),
            "maxHealth": player.getMaxHealth(),
            "experience": player.getExperience(),
            "money": player.getMoney(),
            "inventory": player.getInventory()
        }
        outputFile.write(json.dumps(data, default = lambda o: o.__dict__, sort_keys = False, indent = 4))

def loadPlayer():
    try:
        data = json.load(open('data.txt'))
    except:
        data = False

    return data

def init():
    playerInfo = loadPlayer()
    if playerInfo:
        option = input(sendTextMessage("Would you like to 1. New Game or 2. Continue Game.\n> "))
        if not option.isdigit():
            sys.exit()

        if int(option) == 1:
            open('data.txt', 'w').close()
            setupCharacter()
        elif int(option) == 2:
            pass
        else:
            sys.exit()

        player = Player(playerInfo["name"], 1, playerInfo["profession"])
        player.setHealth(playerInfo["health"])
        player.setMaxHealth(playerInfo["maxHealth"])
        player.addExperience(playerInfo["experience"], False)
        player.addMoney(playerInfo["money"])
        player.setInventory(playerInfo["inventory"])
        gameworld.sendGameWorld(player)
    else:
        setupCharacter()