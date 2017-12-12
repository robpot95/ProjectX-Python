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
        "loot": [
            ("iron sword", 5, 1),
            ("iron helmet", 10, 1),
            ("gold coins", 100, 50)
        ]
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

def getExpForLevel(level):
    level -= 1
    return (50 * level * level) - (75 * level) + (125 * level)
