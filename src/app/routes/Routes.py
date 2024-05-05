class RouteBuilder:
    def __init__(self, controller: str) -> None:
        self.controller = controller


def get_routes() -> dict:
    return {
            '': RouteBuilder(controller='GameController.show_home'),
            'game': RouteBuilder(controller='GameController.new_game'),
            'game.load': RouteBuilder(controller='GameController.load_game'),
            'game.quit': RouteBuilder(controller='GameController.quit_game')
    }
