from tamagoatchi.lib.communication import Request
import tamagoatchi.app.controllers as controllers


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
        route_builder = self.routes[request.json["form_redirect"]]
        class_name, method_name = route_builder.controller.split(".")
        return controllers.call_controller(class_name, method_name, request)
