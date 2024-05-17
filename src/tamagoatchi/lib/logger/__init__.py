from tamagoatchi.lib.logger.Logger import Logger
from tamagoatchi.lib.event import *

logger = Logger()
get_event_handler().add_to_subscription(logger)
