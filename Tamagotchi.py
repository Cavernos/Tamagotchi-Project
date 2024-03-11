from Player import Player


class Tamagotchi:
    def __init__(self,
                 name: str,
                 health: int = 200,
                 boredom: int = 200,
                 tiredness: int = 200,
                 hunger: int = 200
                 ) -> None:
        self._name: str = name
        self._health: int = health
        self._tiredness: int = tiredness
        self._boredom: int = boredom
        self._hunger: int = hunger

    # getter
    @property
    def health(self) -> int:
        return self._health

    @property
    def name(self) -> str:
        return self._name

    @property
    def tiredness(self)-> int:
        return self._tiredness

    @property
    def boredom(self) -> int:
        """
        Boredum getter
        """
        return self._boredom

    @property
    def hunger(self) -> int:
        return self._hunger
    
    # setter
    @health.setter
    def health(self, number: int) -> None:
        self.health += number

    @tiredness.setter
    def tiredness(self, number: int) -> None:
        self.tiredness += number

    @boredom.setter
    def boredom(self, number: int) -> None:
        self.boredom += number

    @hunger.setter
    def hunger(self, number: int) -> None:
        self.hunger += number

    # methods
    def play(self) -> None:
        self.boredom += 50
        self.tiredness -= 50

    def feed(self, player: Player) -> None:
        self.hunger += 50
        player.biscuit = player.biscuit - 1
