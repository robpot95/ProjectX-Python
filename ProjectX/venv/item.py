items = {
    "iron sword": {
        "attack": 5,
        "defense": 4,
        "description": "One sword slays hundreds of creatures.",
        "slot": "weapon",
    },
    "giant sword": {
        "attack": 10,
        "defense": 5,
        "description": "This sword was smith by the gods.",
        "slot": "weapon",
        "type": "two-handed"
    },
    "iron helmet": {
        "defense": 5,
        "description": "This helmet was smith by the gods.",
        "slot": "head",
    },
    "rusty shield": {
        "defense": 5,
        "description": "This shield was smith by the gods.",
        "slot": "shield",
    },
}

def getInfo(item):
    if item in items:
        return items[str(item)]
    else:
        return None