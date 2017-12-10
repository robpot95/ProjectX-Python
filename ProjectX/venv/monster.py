from creature import Creature

import config

class Monster(Creature):
    def __init__(self, name, level):
        super(Monster, self).__init__(name, level or config.monsterList[name]["baseLevel"])

    def onDeath(self, killer):
        killer.addExperience(config.monsterList[self._name]["experience"] * self._level, True)

    def getBaseLevel(self):
        return config.monsterList[self._name]["baseLevel"]

    def getBaseExperience(self):
        return config.monsterList[self._name]["experience"]

    def isMonster(self):
        return True

    def getType(self):
        return "Monster"