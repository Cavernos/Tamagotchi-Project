# dev Nicolas

import tamagoatchi.app.models.tamagotchi_file as tamagotchi_file
from tamagoatchi.lib.model import Model


# --------------- Player ---------------#
class Player(Model):
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

    def __init__(self,
                 name: str = "Player",
                 biscuits: int = 50) -> None:
        """
        Parameters
        ----------
        name : str
            The name of the Player
        biscuits : int
            The number of biscuit got by the Player
        """
        self._name: str = name
        self._biscuits: int = biscuits
        return

    # property & setter

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
        return

    # Methods

    def give_biscuit(self, tama) -> None:
        """
        The Player feed the tamagotchi
        """
        self.biscuits = self.biscuits - 1
        tamagotchi_file.eat(tama)
        return

    def play_with(self, tama) -> None:
        """
        The Player play with the tamagotchi
        """
        tamagotchi_file.play(tama)
        return


# --------------- Test ---------------#
if __name__ == "__main__":
    ...
