from lib.communication.Request import Request
import app.controllers as controllers


class Router:
    def __init__(self, routes: dict) -> None:
        self.routes = routes

    def send_request(self, request: Request):
        route_builder = self.routes[request.json["form_redirect"]]
        class_name, method_name = route_builder.controller.split(".")
        return controllers.call_controller(class_name, method_name, request)
