class RouteBuilder:
    def __init__(self, controller: str) -> None:
        self.controller = controller


def get_routes() -> dict:
    return {
            '': RouteBuilder(controller='HomeController.show_home'),
            'home.exit': RouteBuilder(controller='HomeController.exit'),

            'game': RouteBuilder(controller='GameController.new_game'),
            'game.load': RouteBuilder(controller='GameController.load_game')
    }
