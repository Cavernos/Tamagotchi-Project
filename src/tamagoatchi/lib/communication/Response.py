import enum

from tamagoatchi.lib.view import View


class ResponseType(enum.Enum):
    """
    Enumerate all response type
    """
    valid = 0
    error = 1


class Response:
    """
    Class used to materialize a response

    Attributes
    ----------
    response_type: ResponseType
    Type of response [valid or error]

    view: View
    A view
    """
    def __init__(self, response_type: ResponseType, view: View) -> None:
        self.response_type = response_type
        self.view = view
