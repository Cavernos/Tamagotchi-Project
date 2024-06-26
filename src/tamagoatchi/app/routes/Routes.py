from tamagoatchi.app.definitions import GUI_EXECUTION


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
    if GUI_EXECUTION:
        return {
            '': RouteBuilder(controller='HomeController.show_home'),
            'home': RouteBuilder(controller='GameController.start_game'),
            'game.tamagotchi': RouteBuilder(controller='GameController.view_tamagotchi')
        }
    return {
        '': RouteBuilder(controller='HomeController.show_home'),
        'home.exit': RouteBuilder(controller='HomeController.exit'),

        'game.start': RouteBuilder(controller='GameController.game'),
        'game.load': RouteBuilder(controller='GameController.load'),
        'game.play': RouteBuilder(controller='GameController.play'),
        'game.eat': RouteBuilder(controller='GameController.eat'),
        'game.save': RouteBuilder(controller='GameController.save'),

        'personalization': RouteBuilder(controller='GamePersonalizeController.show_personalization'),
        'personalization.player': RouteBuilder(controller='GamePersonalizeController.new_player'),
        'personalization.tamagotchi': RouteBuilder(controller='GamePersonalizeController.new_tamagotchis'),

        'save': RouteBuilder(controller='SaveController.save'),
    }
