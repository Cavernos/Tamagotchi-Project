from lib.event.Event import *
from lib.event.Observer import *

__event_handler_instance = None


def get_event_handler() -> EventHandler:
    global __event_handler_instance
    if __event_handler_instance is None:
        __event_handler_instance = EventHandler()
    return __event_handler_instance
