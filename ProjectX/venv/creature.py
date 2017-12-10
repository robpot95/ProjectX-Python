'''
Detta är vår basklass för alla slags varelser från Monsters, Npcs (Non Playing Character) & Players
På detta sätt kan vi dela samma logik mellan alla varelser och har små skiljningar som player har professions
'''

class Creature:
    _name = ""
    _level = 1
    _health = 100
    _healthMax = 100
    _attackValue = 1
    _defenseValue = 1

    def __init__(self, name, level):
        self._name = name
        self._level = level

    # Methods
    def doAttacking(self, target):
        print(self._name, target.getName())

    def onDeath(self, killer):
        pass

    # Getters & Setters
    def setName(self, name):
        self._name = name

    def getName(self):
        return self._name.capitalize()

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

    def getAttackValue(self):
        return self._attackValue

    def getDefenseValue(self):
        return self._defenseValue

    def isPlayer(self):
        return False

    def isMonster(self):
        return False

    def isCreature(self):
        return True

    def getType(self):
        return "Creature"