class Player:
    """
    Management of the Player
    """
    def __init__(self, biscuit: int = 50, name: str = "PLayer") -> None:
        self._name: str = name
        self._biscuit: int = biscuit

    @property
    def biscuit(self) -> int:
        return self._biscuit

    @biscuit.setter
    def biscuit(self, value: int) -> None:
        self._biscuit = value
