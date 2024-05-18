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


class EventHandler:
    targets: dict = {}

    @staticmethod
    def register(type):
        def decorator(fn: callable):
            EventHandler.targets.setdefault(type, []).append(fn)
        return decorator

    @staticmethod
    def notify(view_instance, event):
        fnl = EventHandler.targets[event.type] if event.type in EventHandler.targets else []
        for fn in fnl:
            if len(view_instance.buttons):
                for button in view_instance.buttons:
                    fn(button, event)
            else:
                fn(view_instance, event)

    @staticmethod
    def unregister(type):
        if type in EventHandler.targets:
            del EventHandler.targets[type]
