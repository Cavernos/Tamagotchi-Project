

class Tamagotchi:
    def __init__(self, name: str, health: int = 200, boredom: int = 200, tiredness: int = 200, hunger: int = 200) -> None:
        self.name: str = name
        self.health: int = health
        self.tiredness: int = tiredness
        self.boredom: int = boredom
        self.hunger: int = hunger

    # getter
    def getHealth(self) -> int:
        return self.health
    
    def getTiredness(self) -> int:
        return self.tiredness
    
    def getBoredom(self) -> int:
        return self.boredom
    
    def getHunger(self) -> int:
        return self.hunger
    
    # setter
    def setHealth(self, number: int) -> None:
        self.health += number
    
    def setTiredness(self, number: int) -> None:
        self.tiredness += number
    
    def setBoredom(self, number: int) -> None:
        self.boredom += number
    
    def setHunger(self, number: int) -> None:
        self.hunger += number

    # methods
    def play(self) -> None:
        self.boredom += 50
        self.tiredness -= 50

    def feed(self, player: Player) -> None:
        self.hunger += 50
        player.setBiscuit(player.getBiscuit() - 1)
