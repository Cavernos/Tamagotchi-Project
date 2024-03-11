class Player:
    """

    """
    def __init__(self, biscuit=50, name="PLayer"):
        self._name = name
        self._biscuit = biscuit

    @property
    def biscuit(self):
        return self._biscuit

    @biscuit.setter
    def biscuit(self, value):
        self._biscuit = value

