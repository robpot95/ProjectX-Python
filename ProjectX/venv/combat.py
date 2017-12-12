#Här tar vi hand om all slagsmål som sker på spelet
from player import Player
from monster import Monster

def executeFight(player, monster):
    monster.onDeath(player)