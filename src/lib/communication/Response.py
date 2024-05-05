import enum

from lib.views.View import View


class ResponseType(enum.Enum):
    valid = 0
    error = 1


class Response:
    def __init__(self, response_type: ResponseType, view: View) -> None:
        self.response_type = response_type
        self.view = view
