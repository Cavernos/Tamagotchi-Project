import enum
from typing import List

from tamagoatchi.lib.event import Observer


class EventType(enum.Enum):
    info = 0
    warning = 1
    error = 2


class Event:
    def __init__(self, event_type: EventType = EventType.info, message: str = '') -> None:
        self.event_type = event_type
        self.message = message

    def __str__(self) -> str:
        return 'Event Type: ' + self.event_type.name + ', Message: ' + self.message


class EventHandler:
    targets: dict = {}

    @staticmethod
    def register(type):
        def decorator(fn):
            EventHandler.targets.setdefault(type, []).append(fn)

        return decorator

    @staticmethod
    def notify(event):
        fnl = EventHandler.targets[event.type] if event.type in EventHandler.targets else []
        for fn in fnl:
            fn(event)
