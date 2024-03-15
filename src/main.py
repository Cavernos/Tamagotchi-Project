from threading import Thread
from time import sleep
from random import randint


def alive(tamagotchis):
    for tamagotchi in tamagotchis:
        if tamagotchi["santé"] <= 0 or tamagotchi["faim"] <= 0 or tamagotchi["fatigue"] <= 0:
            tamagotchi["dead"] = True
    return tamagotchis

def clock(duration, tamagotchis):
    for tamagotchi in tamagotchis:
        tamagotchi["night_time"] = randint(30, 60)
    
    while True:
        while duration:
            tamagotchis = alive(tamagotchis)
            sleep(1)
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
       
def action(tamagotchis, player, thread):
    for tamagotchi in tamagotchis:
        if tamagotchi["dead"]:
            return
        print(tamagotchi)
    a = int(input("Action ?"))
    match a:
        case 1:
            id = int(input("id:"))
            if tamagotchis[id - 1]["sleep"]:
                action(tamagotchis, player, thread)
            tamagotchis[id - 1]["faim"] += 50
            player["biscuit"] -= 1
            action(tamagotchis, player, thread)
        case 2:
            id = int(input("id:"))
            if tamagotchis[id - 1]["sleep"]:
                action(tamagotchis, player, thread)
            tamagotchis[id - 1]["ennui"] += 50
            tamagotchis[id - 1]["fatigue"] -= 50
            action(tamagotchis, player, thread)

        case _:
            action(tamagotchis, player, thread)


#--------------- Game ---------------#

def lancement_du_jeu():
    tamagotchis = [{"faim": 200, "santé": 200, "ennui": 200, "fatigue": 200,
             "sleep": False,
             "dead": False} for _ in range(5)]
    player = {"biscuit": 50}
    
    thread = Thread(target=clock, args=[180, tamagotchis])
    thread.start()
    
    return tamagotchis, player, thread


#----------------- Start -----------------#

def main():
    tamagotchis, player, thread = lancement_du_jeu()
    action(tamagotchis, player, thread)

if __name__ == '__main__':
    main()
