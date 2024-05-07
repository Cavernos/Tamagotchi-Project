from tamagoatchi.lib.communication import Request, Response, get_router
from tamagoatchi.lib.view import View


class ViewHandler:
    def __init__(self, init_link: str = '') -> None:
        header = {'form_redirect': init_link}
        self.current_view = self.get_response_view(header)

    def update(self):
        header = self.current_view.header
        self.current_view = self.get_response_view(header)

    @staticmethod
    def get_response_view(header: dict) -> View:
        request: Request = Request(header)
        response: Response = get_router().send_request(request)
        return response.view

    def render(self):
        self.current_view.render()
