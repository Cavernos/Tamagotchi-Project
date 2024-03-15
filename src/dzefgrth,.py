import threading
from random import randint
from time import sleep

player = {"Biscuit": 50}
tamagotchis = [{"Health": 200, "Hunger": 200, "Boredom": 200, "Tiredness": 200} for _ in range(5)]

#------------ Tamagotchi ------------#

# Tamagotchi day
def tamagotchi_timer(index_tamagotchi: int):
    global tamagotchis
    is_day = [True for _ in range(5)]
    night_duration = randint(30, 60)
    day_duration = 180 - night_duration
    
    while day_duration > 0:
        if not in_game():
            break
        is_day[index_tamagotchi] = True
        tamagotchis[index_tamagotchi]["Hunger"] -= 50
        tamagotchis[index_tamagotchi]["Boredom"] -= 3
        day_duration -= 1
        sleep(1)
    while night_duration > 0:
        if not in_game():
            break
        is_day[index_tamagotchi] = False
        tamagotchis[index_tamagotchi]["Health"] += 1
        tamagotchis[index_tamagotchi]["Boredom"] += 1
        tamagotchis[index_tamagotchi]["Tiredness"] -= 1
        night_duration -= 1
        sleep(1)
    
# Feed a tamagotchi
def feed(index_tamagotchi: int) -> None:
    global player
    global tamagotchis
    player["Biscuit"] -= 1
    tamagotchis[index_tamagotchi]["Hunger"] += 50

# Play with a tamagotchi
def play(index_tamagotchi: int) -> None:
    global tamagotchis
    tamagotchis[index_tamagotchi]["Boredom"] += 50
    tamagotchis[index_tamagotchi]["Tiredness"] -= 50

# Tamagotchi is alive ?
def is_alive(index_tamagotchi: int) -> bool:
    global tamagotchis
    if tamagotchis[index_tamagotchi].get("Hunger") <= 0 or tamagotchis[index_tamagotchi].get("Health") <= 0 or tamagotchis[index_tamagotchi].get("Tiredness") <= 0:
        return False
    else:
        return True


#------------ Interaction with the player ------------#

# Request for actions
def select_action():
    print("Actions :\n1 - Status\n2 - Play\n3 - Feed")
    action = int(input("Actions ? "))
    match action:
        case 1:
            status()
        case 2:
            tamagotchi = int(input("With which one ? "))
            play(tamagotchi)
        case 3:
            tamagotchi = int(input("Which one ? "))
            feed(tamagotchi)


#------------ Game ------------#

# Print tamagotchi status
def status():
    global tamagotchis
    status = f""
    for i in range(len(tamagotchis)):
        status += f"\nTamagotchi {i} :\nHealth : {tamagotchis[i]["Health"]}\nHunger : {tamagotchis[i]["Hunger"]}\nBoredom : {tamagotchis[i]["Boredom"]}\nTiredness : {tamagotchis[i]["Tiredness"]}\n"
    print(status)

# Is the game lose ?
def in_game():
    global tamagotchis
    for i in range(len(tamagotchis)):
        if not is_alive(i):
            return False
    return True

# Game
def game():
    #__ini__
    global tamagotchis

    t0 = threading.Thread(target=tamagotchi_timer, args=(0,))
    t1 = threading.Thread(target=tamagotchi_timer, args=(1,))
    t2 = threading.Thread(target=tamagotchi_timer, args=(2,))
    t3 = threading.Thread(target=tamagotchi_timer, args=(3,))
    t4 = threading.Thread(target=tamagotchi_timer, args=(4,))

    t0.start()
    t1.start()
    t2.start()
    t3.start()
    t4.start()

    # Routine
    while True:
        if not in_game():
            break
        select_action()
    
    # End
    t0.join()
    t1.join()
    t2.join()
    t3.join()
    t4.join()
    print("YOU KILLED THEM IDIOT!")


#------------ Dev start ------------#

def main() -> None:
    game()

if __name__ == '__main__':
    main()