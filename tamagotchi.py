class Tamagotchi:
    """
    Management of the Tamagotchi entity
    """
    
    def __init__(self, name: str, health: int = 200, boredom: int = 200, tiredness: int = 200, hunger: int = 200) -> None:
        self.name: str = name
        self.health: int = health
        self.tiredness: int = tiredness
        self.boredom: int = boredom
        self.hunger: int = hunger

    # getter
    @property
    def health(self) -> int:
        return self.health
    
    @property
    def tiredness(self) -> int:
        return self.tiredness
    
    @property
    def boredom(self) -> int:
        return self.boredom
    
    @property
    def hunger(self) -> int:
        return self.hunger
    
    # setter
    @health.setter
    def health(self, value: int) -> None:
        self.health = value
    
    @tiredness.setter
    def tiredness(self, value: int) -> None:
        self.tiredness = value
    
    @boredom.setter
    def boredom(self, value: int) -> None:
        self.boredom = value
    
    @hunger.setter
    def hunger(self, value: int) -> None:
        self.hunger = value

    # methods
    def play(self) -> None:
        self.boredom += 50
        self.tiredness -= 50

    def feed(self, player: Player) -> None:
        self.hunger += 50
        player.biscuit = player.biscuit - 1
