import enum
from inspect import signature


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
