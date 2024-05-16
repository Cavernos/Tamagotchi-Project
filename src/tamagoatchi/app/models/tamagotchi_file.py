# dev Cavernos
# A file to manage tamagotchis actions

import random
from tamagoatchi.app.definitions import NUMBER_OF_TAMAGOTCHI, NOT_PRINTABLE_KEYS, CARACTERISTICS_INITIAL_VALUE, \
    DAY_DURATION

# Lists of Tamagotchis
tamagotchis = [
    {
        "name": "Michel",
        "hunger": CARACTERISTICS_INITIAL_VALUE,
        "health": CARACTERISTICS_INITIAL_VALUE,
        "boredom": CARACTERISTICS_INITIAL_VALUE,
        "thirsty": CARACTERISTICS_INITIAL_VALUE,
        "tireness": CARACTERISTICS_INITIAL_VALUE,
        "night_duration": random.randint(30, 60)
    }
    for i in range(NUMBER_OF_TAMAGOTCHI)
]


def eat(tamagotchi: dict) -> None:
    """
    This function feeding the tamagotchi
    Parameter
    ---------
    tamagotchi : dict
        One tamagotchi
    """
    tamagotchi["hunger"] += 50 if tamagotchi["hunger"] < CARACTERISTICS_INITIAL_VALUE else 0


def drink(tamagotchi: dict):
    """
        This function drinking the tamagotchi
        Parameter
        ---------
        tamagotchi : dict
            One tamagotchi
    """
    tamagotchi["thirsty"] += 50 if tamagotchi["thirsty"] < CARACTERISTICS_INITIAL_VALUE else 0


def play(tamagotchi: dict):
    """
        This function make the tamagotchi played
        Parameter
        ---------
        tamagotchi : dict
            One tamagotchi
    """
    tamagotchi["boredom"] += 50 if tamagotchi["boredom"] < CARACTERISTICS_INITIAL_VALUE else 0
    if tamagotchi["tireness"] > 0:
        tamagotchi["tireness"] -= 50


def die(tamagotchi: dict):
    """
        This function verify if the tamagotchi is dead
        Parameter
        ---------
        tamagotchi : dict
            One tamagotchi
    """
    return True if tamagotchi["health"] <= 0 else False


def battle(tamagotchi: dict):
    """
        This function verify if the tamagotchi is in battle
        Parameter
        ---------
        tamagotchi : dict
            One tamagotchi
    """
    return True if tamagotchi["boredom"] <= 0 else False


def is_in_battle(tamagotchis: list[dict]) -> None:
    """
        This function damaged all tamagotchis if one of these is in battle
        Parameter
        ---------
        tamagotchis : list[dict]
            All tamagotchis
    """
    for element in tamagotchis:
        if battle(element):
            for e in tamagotchis:
                e["health"] -= 5


def night_duration(tamagotchi: dict) -> None:
    """
        This function calculate tamagotchi's night_duration
        Parameter
        ---------
        tamagotchi : dict
            One tamagotchi
    """
    tamagotchi["night_duration"] = random.randint(DAY_DURATION // 6, DAY_DURATION // 3)


def sleep_zzz(tamagotchi: dict) -> None:
    """
        This function represent the tamagotchi night routine
        Parameter
        ---------
        tamagotchi : dict
            One tamagotchi
    """
    if (tamagotchi["health"] or tamagotchi["tireness"] or tamagotchi["boredom"]) < CARACTERISTICS_INITIAL_VALUE:
        tamagotchi["health"] += 1
        tamagotchi["tireness"] += 1
        tamagotchi["boredom"] += 1


def awake(tamagotchi: dict) -> None:
    """
           This function represent the tamagotchi day routine
           Parameter
           ---------
           tamagotchi : dict
               One tamagotchi
    """
    tamagotchi["boredom"] -= 3 if tamagotchi["boredom"] > 0 else 0
    tamagotchi["hunger"] -= 5 if tamagotchi["hunger"] > 0 else 0


def get_status(tamagotchis: list[dict]) -> list:
    """
           This function get a list of the tamagotchi status
           Parameter
           ---------
           tamagotchis : list[dict]
               All tamagotchis
    """
    tamagotchis_status = [[] for i in range(len(tamagotchis[0].keys()) - NOT_PRINTABLE_KEYS)]
    for i in range(len(tamagotchis[0].keys()) - NOT_PRINTABLE_KEYS):
        tamagotchis_status[i].insert(0, list(tamagotchis[0])[i].capitalize())
    for i in range(len(tamagotchis)):
        for j in range(len(tamagotchis[0].keys()) - NOT_PRINTABLE_KEYS):
            tamagotchis_status[j].append(tamagotchis[i][list(tamagotchis[i])[j]])
    return tamagotchis_status


def print_status() -> str:
    """
        This function print the tamagotchi status
    """
    tamagotchis_status: list[list] = get_status(tamagotchis)
    return_str = ""
    for i in range(len(tamagotchis[0].keys()) - NOT_PRINTABLE_KEYS):
        return_str += "\n"
        for j in range(len(tamagotchis) + 1):
            return_str += format(str(tamagotchis_status[i][j]), "<15")
    return return_str
