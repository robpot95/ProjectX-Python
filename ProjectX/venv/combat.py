#Här tar vi hand om all slagsmål som sker på spelet, vi använder turn-based combat
import time

from player import Player
from monster import Monster

def executeFight(player, monster):
    attacker = None
    target = None
    lastTurn = "Monster"
    while (True):
        if lastTurn == "Player":
            attacker = monster
            target = player
            lastTurn = "Monster"
        elif lastTurn == "Monster":
            attacker = player
            target = monster
            lastTurn = "Player"

        if attacker != None and target != None:
            target.drainHealth(attacker.getAttack())

            if target.getHealth() <= 0:
                target.onDeath(attacker)
                break

        time.sleep(1.5)