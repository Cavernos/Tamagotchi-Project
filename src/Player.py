# dev Cavernos


class Player():
    """
    A classed used to represent a Player
    ...

    Attributes
    ----------
    name : str
        the name of the Player
    biscuit : int
        The number of biscuit in player inventory
    """

    def __init__(self, name: str = "PLayer", biscuit: int = 50) -> None:
        """
        Parameters
        ----------
        name : str
            The name of the Player
        biscuit : int
            The number of biscuit got by the Player
        """
        self._name: str = name
        self._biscuit: int = biscuit

    @property
    def biscuit(self) -> int:
        """
        Biscuit Property equivalent of getter
        """
        return self._biscuit

    @biscuit.setter
    def biscuit(self, value) -> None:
        """
        Biscuit Setter
        """
        self._biscuit = value

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

    @property
    def instance(self):
        return self

    def give_biscuit(self):
        self.biscuit = self.biscuit - 1
