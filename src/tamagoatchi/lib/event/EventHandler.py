from typing import Callable

from pygame.event import Event

# Define Our eventHandler
EventHandler = Callable[[Event], None]
