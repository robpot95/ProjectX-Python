#Inbyggda
import os
import sys
import textwrap
import time

#Custom class
import const
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
        professionInput = input(sendTextMessage("What profession would you like to be? " + ", ".join(const.professionList.keys()) + "?\n> ")).capitalize()

        if professionInput in const.professionList:
            professionDescription = input(sendTextMessage(const.professionList.get(professionInput) + " Are you sure?\n> "))
            if (professionDescription.capitalize() == "Yes"):
                professionValid = True


    sendTextMessage("A new character has been created. Your name will be: {} and your profession is: {}\n".format(nameInput, professionInput))
    newPlayer = Player(nameInput, 1, 100, 100, professionInput)

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

def init():
    setupCharacter()