from tamagoatchi.lib.communication import Response, Request, ResponseType
from tamagoatchi.lib.controller import Controller
from tamagoatchi.lib.view import ConsoleView


class HomeController(Controller):
    """
    Class used to show home page and exit the game
    """
    @staticmethod
    def show_home(request: Request) -> Response:
        """
        Method used to show home on Console Version
        """
        view = ConsoleView('', {}, request.json)
        return Response(ResponseType.valid, view)

    @staticmethod
    def exit(request: Request) -> None:
        """
        Method used to exit program
        """
        exit(0)
