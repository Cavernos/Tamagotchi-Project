import enum
from typing import List


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
    __observers: List[Observer]

    def __init__(self) -> None:
        self.__observers = []

    def dispatch(self, event: Event) -> None:
        for observer in self.__observers:
            observer.notify(event)

    def add_to_subscription(self, observer: Observer) -> None:
        self.__observers.append(observer)

    def cancel_subscription(self, observer: Observer) -> None:
        self.__observers.remove(observer)