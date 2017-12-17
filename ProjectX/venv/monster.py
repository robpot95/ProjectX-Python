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
        super(Monster, self).__init__(name, level or random.randint(info["baseLevel"], info["baseLevel"] + 3))

    def adjustStatus(self):
        level = self._level
        self._attackValue *= level
        self._defenseValue *= level
        self._health *= level
        self._healthMax *= level

    def onDeath(self, killer):
        killer.addExperience(config.monsterList[self._name]["experience"] * self._level, True)

        # Droppa loot
        if len(killer.getInventory()) <= config.maxInventorySize:
            try:
                for loot in config.monsterList[self._name]["loot"]:
                    randomValue = random.randint(0, 100)
                    if randomValue < loot[1]:
                        count = randomValue % loot[2] + 1
                        print("You have looted {} {}.".format(count, loot[0]))

                        if loot[0] == "gold coins":
                            killer.addMoney(count)
                        else:
                            killer.addInventoryItem(loot[0])
            except KeyError:
                print("Loot was empty.")
        else:
            print("You inventory is full.")

        super(Monster, self).onDeath(killer)

    def getBaseLevel(self):
        return config.monsterList[self._name]["baseLevel"]

    def getBaseExperience(self):
        return config.monsterList[self._name]["experience"]

    def isMonster(self):
        return True

    def getType(self):
        return "Monster"