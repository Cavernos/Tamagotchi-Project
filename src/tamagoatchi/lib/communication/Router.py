from tamagoatchi.lib.communication import Request
import tamagoatchi.app.cli.controllers as controllers_cli
import tamagoatchi.app.gui.controllers as controllers_gui


class Router:
    """
    This class used to represent a router

    Attributes
    ----------
    routes: dict
    routes used by the router
    """
    def __init__(self, routes: dict) -> None:
        self.routes = routes

    def send_request(self, request: Request):
        """
        Function used to send a request from models to controller

        Attributes
        ----------
        request: Request
        request to send
        """
        route_builder = self.routes[request.json["form_redirect"]]
        class_name, method_name = route_builder.controller.split(".")
        return controllers_gui.call_controller(class_name, method_name, request)
