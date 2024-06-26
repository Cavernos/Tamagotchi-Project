# dev Cavernos
# A file to manage tamagotchis actions

import random

from tamagoatchi import logger
from tamagoatchi.app.definitions import NUMBER_OF_TAMAGOTCHI, NOT_PRINTABLE_KEYS, CARACTERISTICS_INITIAL_VALUE, \
    DAY_DURATION, MAP_SIZE

# Lists of Tamagotchis
tamagotchis = [
    {
        "name": f"Michel {i + 1}",
        "hunger": CARACTERISTICS_INITIAL_VALUE,
        "health": CARACTERISTICS_INITIAL_VALUE,
        "boredom": CARACTERISTICS_INITIAL_VALUE,
        "thirsty": CARACTERISTICS_INITIAL_VALUE,
        "tireness": CARACTERISTICS_INITIAL_VALUE,
        "night_duration": random.randint(30, 60)
    }
    for i in range(NUMBER_OF_TAMAGOTCHI)
]
tamagotchis[0]['position'] = (48, 48)
tamagotchis[1]['position'] = (48, 112)
tamagotchis[2]['position'] = (144, 112)
tamagotchis[3]['position'] = (192, 96)
tamagotchis[4]['position'] = (208, 48)


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
    if tamagotchi["tireness"] >= 50:
        tamagotchi["tireness"] -= 50


def die(tamagotchi: dict):
    """
        This function verify if the tamagotchi is dead
        Parameter
        ---------
        tamagotchi : dict
            One tamagotchi
    """
    if tamagotchi["health"] <= 0:
        logger.info("%s is dead", tamagotchi['name'])
        return True
    return False


def battle(tamagotchi: dict):
    """
        This function verify if the tamagotchi is in battle
        Parameter
        ---------
        tamagotchi : dict
            One tamagotchi
    """
    if tamagotchi["boredom"] <= 0:
        logger.info('%s has started a battle', tamagotchi['name'])
        return True
    return False


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
    logger.debug('%s has set this new night duration : %i', tamagotchi['name'], tamagotchi['night_duration'])


def sleep_zzz(tamagotchi: dict) -> None:
    """
        This function represent the tamagotchi night routine
        Parameter
        ---------
        tamagotchi : dict
            One tamagotchi
    """
    logger.info('%s is sleep', tamagotchi['name'])
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
    logger.info('%s is awake', tamagotchi['name'])
    tamagotchi["boredom"] -= 3 if tamagotchi["boredom"] >= 3 else 0
    tamagotchi["hunger"] -= 5 if tamagotchi["hunger"] >= 5 else 0


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
    logger.debug('%s', tamagotchis_status)
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
