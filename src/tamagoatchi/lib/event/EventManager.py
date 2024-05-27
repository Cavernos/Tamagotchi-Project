from collections import defaultdict
from operator import attrgetter

from pygame.event import Event

from tamagoatchi import logger
from tamagoatchi.lib.event import EventHandler


class EventManager:
    """
    Class used to manage event
    """
    _managers = {}

    def __init__(self, name):
        """
        Initialize value  for event and handlers for this event
        """
        self.name = name
        self.handlers: dict[int, list[EventHandler]] = defaultdict(list)

    def notify(self, event: Event, selector=attrgetter('type')):
        """
        Method used to appeal method when an event interfere
        """
        for handler in self.handlers[selector(event)]:
            handler(event)

    def register(self, event_type: int, handler: EventHandler):
        """
        Add new event in manager event list
        """
        logger.info(f"{self.name} registered {event_type}")
        self.handlers[event_type].append(handler)

    def deregister(self, event_type: int, handler: EventHandler):
        """
        Remove event from manager event list
        """
        if handler in self.handlers[event_type]:
            logger.info(f"{self.name} deregistered {event_type}")
            del self.handlers[event_type]

    @classmethod
    def from_id(cls, _id: str):
        """
        Get Manager from an id
        """
        if _id not in cls._managers:
            cls._managers[_id] = EventManager(_id)
        return cls._managers[_id]
