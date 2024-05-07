import logging

from tamagoatchi.lib.event import Observer, Event, EventType


class Logger(Observer):
    def __init__(self) -> None:
        super().__init__()
        logging.basicConfig(filename='log.txt', filemode='a', format='%(asctime)s: %(levelname)s > %(message)s',
                            level=logging.DEBUG)

        def notify(self, event: Event):
            match  event.event_type:
                case EventType.info:
                    logging.info(event.message)
                case EventType.error:
                    logging.error(event.message)
                case EventType.warning:
                    logging.warning(event.message)