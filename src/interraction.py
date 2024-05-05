from clock import Clock
from models.player import Player


class Interraction:
    def __init__(self, name: str = "", text_to_print: str = "", key_cap: str = "", action: callable = ()) -> None:
        self.clock = Clock("hello")
        self.player = Player()
        self.choices = {
            "s": self.save(),
            "q": self.quit(),
            "n": self.feed(),
            "j": self.play(),

        }

    def action(self) -> None:


