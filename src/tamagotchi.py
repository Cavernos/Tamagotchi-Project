import random
from config import NUMBER_OF_TAMAGOTCHI, NOT_PRINTABLE_KEYS

# {"name": "Michel", "hunger": 200, "health": 200, "boredom": 200, "thirsty": 200, "tireness": 200,
#             "dead": False, "sleep": False, "in_battle": False, "night_duration": random.randint(30, 60)}
tamagotchis = [
    {
        "name": "Michel",
        "hunger": 200,
        "health": 200,
        "boredom": 200,
        "thirsty": 200,
        "tireness": 200,
        "dead": False,
        "sleep": False,
        "in_battle": False,
        "night_duration": random.randint(30, 60)
    }
    for i in range(NUMBER_OF_TAMAGOTCHI)
]


def eat(tamagotchi: dict) -> None:
    tamagotchi["hunger"] += 50


def drink(tamagotchi: dict):
    tamagotchi["thirsty"] += 50


def play(tamagotchi: dict):
    tamagotchi["boredom"] += 50
    tamagotchi["tireness"] -= 50


def die(tamagotchi: dict):
    if tamagotchi["health"] <= 0:
        tamagotchi["dead"] = True
    tamagotchi["dead"] = False


def battle(tamagotchi: dict):
    if tamagotchi["boredom"] <= 0:
        tamagotchi["in_battle"] = True
    tamagotchi["in_battle"] = False


def is_in_battle(tamagotchis: list[dict]):
    for element in tamagotchis:
        if element["in_battle"]:
            tamagotchis[tamagotchis.index(element)]["health"] -= 5


def night_duration(tamagotchi: dict):
    tamagotchi["night_duration"] = random.randint(30, 60)


def sleep_zzz(tamagotchi: dict):
    tamagotchi["health"] += 1
    tamagotchi["tireness"] += 1
    tamagotchi["boredom"] += 1


def awake(tamagotchi: dict):
    tamagotchi["boredom"] -= 3
    tamagotchi["hunger"] -= 5


def get_status() -> list:
    tamagotchis_status = [[] for i in range(len(tamagotchis[0].keys()) - NOT_PRINTABLE_KEYS)]
    for i in range(len(tamagotchis[0].keys()) - NOT_PRINTABLE_KEYS):
        tamagotchis_status[i].insert(0, list(tamagotchis[0])[i].capitalize())
    for i in range(len(tamagotchis)):
        for j in range(len(tamagotchis[0].keys()) - NOT_PRINTABLE_KEYS):
            tamagotchis_status[j].append(tamagotchis[i][list(tamagotchis[i])[j]])
    return tamagotchis_status


def print_status() -> None:
    tamagotchis_status = get_status()
    for i in range(len(tamagotchis[0].keys()) - NOT_PRINTABLE_KEYS):
        print("")
        for j in range(len(tamagotchis) + 1):
            print(format(str(tamagotchis_status[i][j]), "<15"), end="")

print_status()