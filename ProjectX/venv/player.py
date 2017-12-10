import config
from creature import Creature

class Player(Creature):
    __profession = 0
    __experience = 0

    def __init__(self, name, level, profession):
        self.__profession = profession
        super(Player, self).__init__(name, level)

    # Methods
    def addExperience(self, exp, sendText = False):
        if exp <= 0 or self._level >= config.maxLevel:
            return

        self.__experience += exp

        if sendText:
            print("You gained {} {}".format(exp, "experience points." if exp != 1 else "experience point."))

        previousLevel = self._level
        while self.__experience >= config.getExpForLevel(self._level + 1):
            self._level += 1

            if self._level >= config.maxLevel:
                break

        if self._level != previousLevel:
            print("You advanced from Level {} to Level {}.".format(previousLevel, self._level))

    # Getters & Setters
    def setProfession(self, profession):
        self.__profession = profession

    def getProfession(self):
        return self.__profession

    def isPlayer(self):
        return True

    def getType(self):
        return "Player"