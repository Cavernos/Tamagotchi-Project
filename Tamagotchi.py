from Player import Player


class Tamagotchi:
    """
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
                 name: str,
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

    # getter
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
    
    # setter
    @health.setter
    def health(self, value: int) -> None:
        self._health = value

    @tiredness.setter
    def tiredness(self, value: int) -> None:
        self._tiredness = value

    @boredom.setter
    def boredom(self, value: int) -> None:
        self._boredom = value

    @hunger.setter
    def hunger(self, value: int) -> None:
        self._hunger = value

    # methods
    def play(self) -> None:
        self.boredom = self.boredom + 50
        self.tiredness = self.tiredness - 50

    def feed(self, player: Player) -> None:
        self.hunger = self.hunger - 50

    # methods
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
        player.biscuit = player.biscuit - 1

