from creature import Creature

class Player(Creature):
    __profession = 0

    def __init__(self, name, level, health, healthMax, profession):
        self.__profession = profession
        super(Player, self).__init__(name, level, health, healthMax)

    def setProfession(self, profession):
        self.__profession = profession

    def getProfession(self):
        return self.__profession

    def getType(self):
        print("Player")