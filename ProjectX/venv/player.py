import config
from creature import Creature
import item

class Player(Creature):
    __profession = None
    __experience = 0
    __money = 0
    __inventory = []
    __equipment = {
        "weapon": None,
        "shield": None,
        "head": None,
        "armor": None,
        "legs": None,
        "boots": None
    }

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
            self._health += config.getHealthGain(self.__profession)
            self._healthMax += config.getHealthGain(self.__profession)
            self._attackValue += config.getAttackGain(self.__profession)
            self._defenseValue += config.getDefenseGain(self.__profession)

            if self._level >= config.maxLevel:
                break

        if self._level != previousLevel:
            if sendText:
                print("You advanced from Level {} to Level {}.".format(previousLevel, self._level))

    def wearItem(self, _item):
        info = item.getInfo(_item)
        if info == None:
            print(_item + " does not exsist.")
            return

        slot = self.__equipment[info["slot"]]
        if not slot == None:
            # Om slot är tagen, gör en exchange
            exchangeInput = input("Would you like to switch your {} to {}?\n> ".format(slot, _item))
            if exchangeInput.lower() == "yes":
                self.__inventory.append(slot)
                print("Now you wearing {} and your {} has been moved to your inventory.".format(_item, slot))
            else:
                return

        self.__inventory.remove(_item)
        self.__equipment[info["slot"]] = _item

    # Getters & Setters
    def getEquipment(self):
        return self.__equipment

    def addEquipment(self, eq):
        self.__equipment = eq

    def getInventory(self):
        return self.__inventory

    def setInventory(self, inventory):
        self.__inventory = inventory

    def addInventoryItem(self, itemName):
        self.__inventory.append(itemName)

    def removeInvetoryItem(self, itemName):
        self.__inventory.remove(itemName)

    def addMoney(self, count):
        self.__money += count

    def getMoney(self):
        return self.__money

    def setProfession(self, profession):
        self.__profession = profession

    def getProfession(self):
        return self.__profession

    def setExperience(self, value):
        self.__experience = value

    def getExperience(self):
        return self.__experience

    def isPlayer(self):
        return True

    def getType(self):
        return "Player"