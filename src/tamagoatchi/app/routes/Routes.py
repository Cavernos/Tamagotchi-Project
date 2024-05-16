class RouteBuilder:
    def __init__(self, controller: str) -> None:
        self.controller = controller


def get_routes() -> dict:
    return {
            '': RouteBuilder(controller='HomeController.show_home'),
            'home.exit': RouteBuilder(controller='HomeController.exit'),

            'game': RouteBuilder(controller='GameController.new_game'),
            'game.load': RouteBuilder(controller='GameController.load_game'),
            'game.play': RouteBuilder(controller='GameController.play'),
            'game.eat': RouteBuilder(controller='GameController.eat'),

            'personalization': RouteBuilder(controller='GamePersonalizerController.show_personalization'),
            'personalization.player': RouteBuilder(controller='GamePersonalizerController.new_player'),
            'personalization.tamagotchi': RouteBuilder(controller='GamePersonalizerController.new_tamagotchis')
    }
