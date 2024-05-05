from lib.logger.Logger import Logger
from lib.event import *

logger = Logger()
get_event_handler().add_to_subscription(logger)