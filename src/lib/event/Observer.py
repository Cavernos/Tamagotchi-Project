from abc import ABC

from lib.event import Event


class Observer(ABC):
    def __init__(self):
        pass

    def notify(self, event: Event):
        raise NotImplementedError
