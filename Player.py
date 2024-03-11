class Player:
    """
<<<<<<< HEAD
    Management of the Player
    """
    def __init__(self, biscuit: int = 50, name: str = "PLayer") -> None:
=======
    A classed used to represent a Player
    ...

    Attributes
    ----------
    name : str
        the name of the Player
    biscuit : int
        The number of biscuit in player inventory
    """
    def __init__(self, name="PLayer", biscuit=50) -> None:
        """
        Parameters
        ----------
        name : str
            The name of the Player
        biscuit : int
            The number of biscuit got by the Player
        """
>>>>>>> 7c3609611401bcf3410429071bf2d72efdec8f0c
        self._name: str = name
        self._biscuit: int = biscuit

    @property
    def biscuit(self) -> int:
<<<<<<< HEAD
        return self._biscuit

    @biscuit.setter
    def biscuit(self, value: int) -> None:
        self._biscuit = value
=======
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


>>>>>>> 7c3609611401bcf3410429071bf2d72efdec8f0c
