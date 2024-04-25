import random
tamagotchi = {"faim": 200, "santé": 200, "ennui": 200, "soif": 200, "fatigue": 200, "dead": False, "sleep": False, "in_battle": False, "night_duration": random.randint(30 ,60)}

def eat(tamagotchi :dict) -> None:
    tamagotchi["faim"] += 50

def drink(tamagotchi :dict):
    tamagotchi["soif"] += 50

def play(tamagotchi :dict):
    tamagotchi["ennui"] += 50
    tamagotchi["fatigue"] -= 50

def die(tamagotchi :dict):
    if tamagotchi["santé"] <= 0:
        tamagotchi["dead"] = True
    tamagotchi["dead"] = False

def battle(tamagotchi: dict):
    if tamagotchi["ennui"] <= 0:
        tamagotchi["in_battle"] = True


def is_in_battle(tamagotchis: list[dict]):
    for tamagotchi in tamagotchis:
        if tamagotchi["in_battle"]:
            tamagotchis["santé"] -= 5
        tamagotchi["in_battle"] = False

def sleep_zzz(tamagotchi :dict):
    tamagotchi["santé"] += 1
    tamagotchi["fatigue"] += 1
    tamagotchi["ennui"] += 1

def awake(tamagotchi :dict):
    tamagotchi["ennui"] -= 3
    tamagotchi["faim"] -= 5
