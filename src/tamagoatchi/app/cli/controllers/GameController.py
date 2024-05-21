from tamagoatchi.app.time import Clock
from tamagoatchi.lib.communication import Request, Response, ResponseType
from tamagoatchi.lib.controller import Controller
from tamagoatchi.lib.view import ConsoleView
from tamagoatchi.app.models import tamagotchi_file
from tamagoatchi.app.models import Player


class GameController(Controller):
    """
    A classed used to control the game and make the link
    between models and views in relation with the game.

    Attributes
    ----------
    clock: Clock
    The clock used to play the game
    """

    def __init__(self) -> None:
        """
        Initialize the clock used for the game
        """
        self.clock = Clock(name='game_clock')
        self.clock.start()

    def game(self, request: Request) -> Response:
        """
        Load the game and define if the player has lost the game

        Attributes
        __________
        request: Request
        All the information send by the player when he was redirected
        """
        if "ext" in request.inputs.keys():
            player: Player = Player.get_instance(request.inputs["ext"][0])
        else:
            player = Player()
        if not self.clock.is_alive():
            self.clock.join()
            return Response(ResponseType.error, ConsoleView('',
                                                     {"error": "Vous avez perdu ! Un des tamagotchis est mort"},
                                                     request.json))
        return Response(ResponseType.valid, ConsoleView('game',
                                                 {'tamagotchis': tamagotchi_file,
                                                  'player': player
                                                  },
                                                 request.json))

    def play(self, request: Request) -> Response:
        """
        Define play interaction

        Attributes
        __________
        request: Request
        All the information send by the player when he was redirected
        """
        name_of_tamagotchi = request.inputs['name']
        player = Player.get_instance(request.inputs['ext'][0])
        for tamagotchi in tamagotchi_file.tamagotchis:
            if tamagotchi['name'] == name_of_tamagotchi and self.clock.day_duration > tamagotchi['night_duration']:
                player.play_with(tamagotchi)
        request.json['form_redirect'] = 'game.load'
        return Response(ResponseType.valid, ConsoleView("game",
                                                 {'player': player, 'tamagotchis': tamagotchi_file},
                                                 request.json))

    def eat(self, request: Request) -> Response:
        """
        Define eat interaction

        Attributes
        __________
        request: Request
        All the information send by the player when he was redirected
        """
        name_of_tamagotchi = request.inputs['name']
        player = Player.get_instance(request.inputs['ext'][0])
        for tamagotchi in tamagotchi_file.tamagotchis:
            if tamagotchi['name'] == name_of_tamagotchi and self.clock.day_duration > tamagotchi['night_duration']:
                player.give_biscuit(tamagotchi)
        request.json['form_redirect'] = 'game.load'
        return Response(ResponseType.valid, ConsoleView("game",
                                                 {'player': player, 'tamagotchis': tamagotchi_file},
                                                 request.json))
