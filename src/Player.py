#--------------- Player ---------------#

class Player:
    """
    A classed used to represent a Player
    ...

    Attributes
    ----------
    name : str
        the name of the Player
    biscuits : int
        The number of biscuit in player inventory
    """

    def __init___(self,
                  name: str= "Player",
                  biscuits: int= 50) -> None:
        """
        Parameters
        ----------
        name : str
            The name of the Player
        biscuits : int
            The number of biscuit got by the Player
        """
        self.name: str = name
        self.biscuits: int = biscuits
        return None

    @property
    def biscuits(self) -> int:
        """
        Biscuit Property equivalent of getter
        """
        return self._biscuits

    @biscuits.setter
    def biscuits(self, value) -> None:
        """
        Biscuit Setter
        """
        self._biscuits = value
        return None

    @property
    def name(self) -> str:
        """
        Name Property equivalent of getter
        """
        return self._name

    @name.setter
    def name(self, value) -> None:
        """
        Name Setter
        """
        self._name = value
        return None

    # Methods
    def give_biscuit(self) -> None:
        """
        The Player feed the Tamagotchi
        """
        self._biscuits -= 1
        eat()
        return None

    def play_with(self) -> None:
        """
        The Player feed the Tamagotchi
        """
        play()
        return None

#--------------- Test ---------------#

if __name__ == "__main__":
    ...
