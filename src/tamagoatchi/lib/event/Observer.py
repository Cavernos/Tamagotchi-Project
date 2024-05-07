from abc import ABC

from tamagoatchi.lib.event import Event


class Observer(ABC):
    def __init__(self):
        pass

    def notify(self, event: Event):
        pass
