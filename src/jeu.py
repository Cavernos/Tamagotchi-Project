import random
import time
from threading import Thread


def verif_mort(tamagotchis):
    for tamagotchi in tamagotchis:
        if tamagotchi["santé"] <= 0 or tamagotchi["faim"] <= 0 or tamagotchi["fatigue"] <= 0:
            tamagotchi["dead"] = True
    return tamagotchis


def clock(duration, tamagotchis, player):
    while True:
        for tamagotchi in tamagotchis:
            tamagotchi["night_time"] = random.randint(30, 60)
        player["biscuit"] = 50
        while duration:
            tamagotchis = verif_mort(tamagotchis)
            time.sleep(1)
            for tamagotchi in tamagotchis:
                if tamagotchi["dead"]:
                    return
                if duration <= tamagotchi["night_time"]:
                    tamagotchi["sleep"] = True
                else:
                    tamagotchi["sleep"] = False
                if not tamagotchi["sleep"]:
                    tamagotchi["faim"] -= 5
                    tamagotchi["ennui"] -= 3
                if tamagotchi["sleep"]:
                    tamagotchi["santé"] += 1
                    tamagotchi["ennui"] += 1
                    tamagotchi["fatigue"] += 1
            duration -= 1


def action(tamagotchis, player):
    for tamagotchi in tamagotchis:
        if tamagotchi["dead"]:
            return
        print(tamagotchi)
    a = int(input("Action ?"))
    match a:
        case 1:
            id = int(input("id:"))
            if tamagotchis[id - 1]["sleep"]:
                action(tamagotchis, player)
            tamagotchis[id - 1]["faim"] += 50
            player["biscuit"] -= 1
            action(tamagotchis, player)
        case 2:
            id = int(input("id:"))
            if tamagotchis[id - 1]["sleep"]:
                action(tamagotchis, player)
            tamagotchis[id - 1]["ennui"] += 50
            tamagotchis[id - 1]["fatigue"] -= 50
            action(tamagotchis, player)
        case _:
            action(tamagotchis, player)


def lancement_du_jeu():
    tamagotchis = []
    player = {"biscuit": 50}
    for i in range(5):
        tamagotchis.append(
            {"faim": 200, "santé": 200, "ennui": 200, "fatigue": 200, "dead": False, "sleep": False}
        )
    Thread(target=clock, args=[180, tamagotchis, player]).start()
    return tamagotchis, player


t, p = lancement_du_jeu()
action(t, p)

