from collections import defaultdict
from operator import attrgetter

from pygame.event import Event

from tamagoatchi import logger
from tamagoatchi.lib.event import EventHandler


class EventManager:
    _managers = {}

    def __init__(self, name):
        self.name = name
        self.handlers: dict[int, list[EventHandler]] = defaultdict(list)

    def notify(self, event: Event, selector=attrgetter('type')):
        for handler in self.handlers[selector(event)]:
            handler(event)

    def register(self, event_type: int, handler: EventHandler):
        logger.info(f"{self.name} registered {event_type}")
        self.handlers[event_type].append(handler)

    def deregister(self, event_type: int, handler: EventHandler):
        if handler in self.handlers[event_type]:
            logger.info(f"{self.name} deregistered {event_type}")
            self.handlers[event_type].remove(handler)

    @classmethod
    def from_id(cls, _id: str):
        if _id not in cls._managers:
            cls._managers[_id] = EventManager(_id)
        return cls._managers[_id]
