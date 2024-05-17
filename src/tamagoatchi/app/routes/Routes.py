class RouteBuilder:
    """
    A class used to create some Routes
    """
    def __init__(self, controller: str) -> None:
        """
        Controller.method
        """
        self.controller = controller


def get_routes() -> dict:
    """
    Return the different route use for our app
    """
    return {
            '': RouteBuilder(controller='HomeController.show_home'),
            'home.exit': RouteBuilder(controller='HomeController.exit'),

            'game.load': RouteBuilder(controller='GameController.game'),
            'game.play': RouteBuilder(controller='GameController.play'),
            'game.eat': RouteBuilder(controller='GameController.eat'),

            'personalization': RouteBuilder(controller='GamePersonalizeController.show_personalization'),
            'personalization.player': RouteBuilder(controller='GamePersonalizeController.new_player'),
            'personalization.tamagotchi': RouteBuilder(controller='GamePersonalizeController.new_tamagotchis')
    }
