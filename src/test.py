from threading import Thread
from time import sleep
from random import randint


#------------ Tamagotchi ------------#

# Tamagotchi Thread
def clock():
    global tamagotchis
    day_duration = 180
    
    while True:
        for tamagotchi in tamagotchis:
            tamagotchi["sleep_duration"] = randint(30, 60)
        
        while day_duration:
            if not in_game(tamagotchis):
                break
            
            for tamagotchi in tamagotchis:
                if day_duration <= tamagotchi["sleep_duration"]:
                    tamagotchi["awake"] = False
                else:
                    tamagotchi["awake"] = True
                
                if not tamagotchi["awake"]:
                    tamagotchi["Hunger"] -= 50
                    tamagotchi["Boredom"] -= 3
                else:
                    tamagotchi["Health"] += 1
                    tamagotchi["Boredom"] += 1
                    tamagotchi["Tiredness"] += 1
            
            day_duration -= 1
            sleep(1)
            

#------------ Game ------------#

# Print tamagotchi status
def tamagotchis_status(tamagotchis: list[dict]) -> str:
    status = f""
    for i in range(len(tamagotchis)):
        status += f"\nTamagotchi {i} :\nHealth : {tamagotchis[i]["Health"]}\nHunger : {tamagotchis[i]["Hunger"]}\nBoredom : {tamagotchis[i]["Boredom"]}\nTiredness : {tamagotchis[i]["Tiredness"]}\n"
    print(status)

# Tamagotchi is alive ?
def alive(tamagotchis: list[dict], index_tamagotchi: int) -> bool:
    if (tamagotchis[index_tamagotchi].get("Hunger") or tamagotchis[index_tamagotchi].get("Health") or tamagotchis[index_tamagotchi].get("Tiredness")) <= 0:
        return False
    else:
        return True

# Is the game lose ?
def in_game(tamagotchis: list[dict]) -> bool:
    for i in range(len(tamagotchis)):
        if not alive(tamagotchis, i):
            return False
    return True

# Game
def game() -> None:
    #__ini__
    player = {"Biscuit": 50}
    global tamagotchis
    tamagotchis = [{"Health": 200, "Hunger": 200, "Boredom": 200, "Tiredness": 200} for _ in range(5)]

    t0 = Thread(target=clock)
    t1 = Thread(target=clock)
    t2 = Thread(target=clock)
    t3 = Thread(target=clock)
    t4 = Thread(target=clock)

    t0.start()
    t1.start()
    t2.start()
    t3.start()
    t4.start()

    # Routine
    while True:
        if not in_game(tamagotchis):
            break
        
        # Actions
        print("Actions :\n1 - Status\n2 - Play\n3 - Feed")
        action = int(input("Actions ? "))
        match action:

            case 1:
                tamagotchis_status(tamagotchis)
            
            # Play 
            case 2:
                tamagotchi_id = int(input("With which one ? "))
                tamagotchis[tamagotchi_id]["Boredom"] += 50
                tamagotchis[tamagotchi_id]["Tiredness"] -= 50
            
            # Eat
            case 3:
                tamagotchi_id = int(input("Which one ? "))
                tamagotchis[tamagotchi_id]["Hunger"] += 50
                player["Biscuit"] -= 1

    # End
    t0.join()
    t1.join()
    t2.join()
    t3.join()
    t4.join()
    print("YOU KILLED THEM IDIOT!")


#------------ Dev test ------------#

def test() -> None:
    game()

if __name__ == '__main__':
    test()
