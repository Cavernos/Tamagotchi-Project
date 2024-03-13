from Player import Player


class Tamagotchi:
    """
    Dev : Nicolas Clement
    A classed used to represent a Tamagotchi
    ...

    Attributes
    ----------
    name : str
        The name of the Tamagotchi
    health : int
        The number of health point
    boredom : int
        The number of boredom point
    tiredness : int
        The number of tiredness point
    hunger : int
        The number of hunger point
    """
    def __init__(self,
                 name: str = "Tamagotchi",
                 health: int = 200,
                 boredom: int = 200,
                 tiredness: int = 200,
                 hunger: int = 200
                 ) -> None:
        """
        Parameters
        ----------
        name : str
            The name of the Tamagotchi
        health : int
            The number of health point
        boredom : int
            The number of boredom point
        tiredness : int
            The number of tiredness point
        hunger : int
            The number of hunger point
        """
        self._name: str = name
        self._health: int = health
        self._tiredness: int = tiredness
        self._boredom: int = boredom
        self._hunger: int = hunger

    # Getters
    @property
    def name(self) -> str:
        """
        Name Property equivalent of getter
        """
        return self._name
    
    @property
    def health(self) -> int:
        """
        Health Property equivalent of getter
        """
        return self._health

    @property
    def tiredness(self)-> int:
        """
        Tiredness Property equivalent of getter
        """
        return self._tiredness

    @property
    def boredom(self) -> int:
        """
        Boredum Property equivalent of getter
        """
        return self._boredom

    @property
    def hunger(self) -> int:
        """
        Hunger Property equivalent of getter
        """
        return self._hunger
    
    # Setters
    @health.setter
    def health(self, value: int) -> None:
        """
        Health Setter
        """
        self._health = value

    @tiredness.setter
    def tiredness(self, value: int) -> None:
        """
        Tiredness Setter
        """
        self._tiredness = value

    @boredom.setter
    def boredom(self, value: int) -> None:
        """
        Boredom Setter
        """
        self._boredom = value

    @hunger.setter
    def hunger(self, value: int) -> None:
        """
        Hunger Setter
        """
        self._hunger = value

    # Methods
    def play(self) -> None:
        """
        Play with the Tamagotchi
        """
        self.boredom += 50
        self.tiredness -= 50

    def feed(self, player: Player) -> None:
        """
        Feed the Tamagotchi
        """
        self.hunger += 50
        player.give_biscuit()

    def __str__(self) -> str:
        return f"\n{self.name}\nHealth : {self.health}\nHunger : {self.hunger}\nBoredom : {self.boredom}\nTiredness : {self.tiredness}"


if __name__ == '__main__':
    player = Player("Master")
    tamagotchi = Tamagotchi(name="Slave")
    tamagotchi.feed(player)
    print(tamagotchi)
