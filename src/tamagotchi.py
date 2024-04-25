import random
tamagotchi = {"name": "Michel","hunger": 200, "health": 200, "boredom": 200, "thirsty": 200, "tireness": 200, "dead": False, "sleep": False, "in_battle": False, "night_duration": random.randint(30 ,60)}

def eat(tamagotchi :dict) -> None:
    tamagotchi["hunger"] += 50

def drink(tamagotchi :dict):
    tamagotchi["thirsty"] += 50

def play(tamagotchi :dict):
    tamagotchi["boredom"] += 50
    tamagotchi["tireness"] -= 50

def die(tamagotchi :dict):
    if tamagotchi["health"] <= 0:
        tamagotchi["dead"] = True
    tamagotchi["dead"] = False

def battle(tamagotchi: dict):
    if tamagotchi["boredom"] <= 0:
        tamagotchi["in_battle"] = True


def is_in_battle(tamagotchis: list[dict]):
    for tamagotchi in tamagotchis:
        if tamagotchi["in_battle"]:
            tamagotchis["health"] -= 5
        tamagotchi["in_battle"] = False

def sleep_zzz(tamagotchi :dict):
    tamagotchi["health"] += 1
    tamagotchi["tireness"] += 1
    tamagotchi["boredom"] += 1

def awake(tamagotchi :dict):
    tamagotchi["boredom"] -= 3
    tamagotchi["hunger"] -= 5
