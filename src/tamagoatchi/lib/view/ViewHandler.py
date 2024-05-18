import pygame

from tamagoatchi.lib.communication import Request, Response, get_router
from tamagoatchi.lib.event import EventHandler
from tamagoatchi.lib.view import View


class ViewHandler:
    """
    Class used to handle views
    """
    def __init__(self, init_link: str = '') -> None:
        """
        Attribute the first view
        """
        header = {'form_redirect': init_link}
        self.current_view = self.get_response_view(header)

    def update(self):
        """
        Update the view when there is redirection
        """
        header = self.current_view.header
        self.current_view = self.get_response_view(header)

    @staticmethod
    def get_response_view(header: dict) -> View:
        """
        Get the header in function of the header
        """
        request: Request = Request(header)
        response: Response = get_router().send_request(request)
        return response.view

    def render(self):
        """
        Rendering the view
        """
        self.current_view.render()
