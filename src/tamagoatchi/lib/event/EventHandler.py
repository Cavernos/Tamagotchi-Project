from typing import Callable

from pygame.event import Event

EventHandler = Callable[[Event], None]
