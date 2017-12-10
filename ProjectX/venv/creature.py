'''
Detta är vår basklass för alla slags varelser från Monsters, Npcs (Non Playing Character) & Players
På detta sätt kan vi dela samma logik mellan alla varelser och har små skiljningar som player har professions
'''

class Creature:
    _name = ""
    _level = 1
    _health = 100
    _healthMax = 100

    def __init__(self, name, level, health, healthMax):
        self._name = name
        self._level = level
        self._health = health
        self._healthMax = healthMax

    def setName(self, name):
        self._name = name

    def getName(self):
        return self._name

    def setLevel(self, level):
        self._level = level

    def getLevel(self):
        return self._level

    def setHealth(self, health):
        self._health = health

    def getHealth(self):
        return self._health

    def setMaxHealth(self, maxHealth):
        self._healthMax = maxHealth

    def getMaxHealth(self):
        return self._healthMax

    def getType(self):
        print("Creature")