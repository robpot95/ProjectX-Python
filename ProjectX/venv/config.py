maxInventorySize = 20
maxLevel = 100

professionList = {
    "Archer": {
        "description": "Archers are masters of distance weapons.",
        "attackGain": 25,
        "defenseGain": 22,
        "healthGain": 20
    },
    "Mage": {
        "description": "Mages are masters of offensive and aggressive magic.",
        "attackGain": 15,
        "defenseGain": 10,
        "healthGain": 15
    },
    "Warrior": {
        "description": "Warriors are masters of weapons, shielding and hand-to-hand combat.",
        "attackGain": 30,
        "defenseGain": 30,
        "healthGain": 30
    }
}

def getHealthGain(profession):
    return professionList[profession]["healthGain"]

def getAttackGain(profession):
    return professionList[profession]["attackGain"]

def getDefenseGain(profession):
    return professionList[profession]["defenseGain"]

def getDescription(profession):
    return professionList[profession]["description"]

monsterList = {
    "orc": {
        "baseLevel": 1,
        "experience": 50,
        "health": 5,
        "attack": 3,
        "defense": 3,
        "loot": [
            ("iron sword", 5, 1),
            ("iron helmet", 10, 1),
            ("gold coins", 100, 50)
        ]
    },
    "troll": {
        "baseLevel": 1,
        "experience": 45,
        "health": 5,
        "attack": 3,
        "defense": 2
    },
    "vampire": {
        "baseLevel": 5,
        "experience": 100,
        "health": 7,
        "attack": 5,
        "defense": 4
    },
    "cyclops": {
        "baseLevel": 7,
        "experience": 120,
        "health": 6,
        "attack": 7,
        "defense": 5
    },
    "demon": {
        "baseLevel": 12,
        "experience": 200,
        "health": 10,
        "attack": 12,
        "defense": 10
    },
    "dragon": {
        "baseLevel": 10,
        "experience": 150,
        "health": 8,
        "attack": 9,
        "defense": 9
    }
}

def getExpForLevel(level):
    level -= 1
    return (50 * level * level) - (75 * level) + (125 * level)
