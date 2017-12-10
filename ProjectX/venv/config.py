maxLevel = 100

professionList = {
    "Archer": "Archers are masters of distance weapons.",
    "Mage": "Mages are masters of offensive and aggressive magic.",
    "Warrior": "Warriors are masters of weapons, shielding and hand-to-hand combat.",
}

monsterList = {
    "orc": {
        "baseLevel": 5,
        "experience": 50,
        "health": 10,
        "attack": 5,
        "defense": 5,
    },
    "troll": {
        "baseLevel": 5,
        "experience": 45,
        "health": 8,
        "attack": 4,
        "defense": 6
    },
    "vampire": {
        "baseLevel": 10,
        "experience": 100,
        "health": 15,
        "attack": 10,
        "defense": 12
    },
    "cyclops": {
        "baseLevel": 12,
        "experience": 120,
        "health": 12,
        "attack": 15,
        "defense": 10
    },
    "demon": {
        "baseLevel": 20,
        "experience": 200,
        "health": 20,
        "attack": 30,
        "defense": 20
    },
    "dragon": {
        "baseLevel": 15,
        "experience": 150,
        "health": 15,
        "attack": 20,
        "defense": 18
    }
}

expTable = {
    1: 0,
    2: 100,
    3: 200,
    4: 400,
    5: 600,
    6: 900,
    7: 1200,
    8: 1500,
    9: 1700,
    10: 2000

}

def getExpForLevel(level):
    return expTable[level]