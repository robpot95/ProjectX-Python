#Här tar vi hand om all slagsmål som sker på spelet
import time

from player import Player
from monster import Monster

def executeFight(player, monster):
    while (True):
        if monster.getHealth() > 0:
            monster.drainHealth(player.getAttack())
        else:
            monster.onDeath(player)
            break

        if player.getHealth() > 0:
            player.drainHealth(monster.getAttack())
            pass
        else:
            print("You lost the fight.")

        # Vi skadar varandra varje 1.5 sekunder
        time.sleep(1.5)