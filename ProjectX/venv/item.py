items = {
    "iron sword": {
        "attack": 5,
        "defense": 4,
        "description": "One sword slays hundreds of creatures.",
        "slot": "hand"
    },
    "iron helmet": {
        "defense": 5,
        "description": "This helmet was smith by the gods.",
        "slot": "head"
    }
}

def getInfo(item):
    return items[str(item)]