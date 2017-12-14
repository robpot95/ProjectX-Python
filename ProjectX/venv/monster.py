from creature import Creature

import config
import random

class Monster(Creature):
    def __init__(self, name, level):
        info = config.monsterList[name]
        self._attackValue = info["attack"]
        self._defenseValue = info["defense"]
        self._health = info["health"]
        self._healthMax = info["health"]
        super(Monster, self).__init__(name, level or info["baseLevel"])

    def onDeath(self, killer):
        killer.addExperience(config.monsterList[self._name]["experience"] * self._level, True)

        # Droppa loot
        for loot in config.monsterList[self._name]["loot"]:
            randomValue = random.randint(0, 100)
            if randomValue < loot[1]:
                count = randomValue % loot[2] + 1
                print("You have looted {} {}.".format(count, loot[0]))

                if loot[0] == "gold coins":
                    killer.addMoney(count)
                else:
                    killer.addInventoryItem(loot[0])

    def getBaseLevel(self):
        return config.monsterList[self._name]["baseLevel"]

    def getBaseExperience(self):
        return config.monsterList[self._name]["experience"]

    def isMonster(self):
        return True

    def getType(self):
        return "Monster"