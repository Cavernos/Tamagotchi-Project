from tamagoatchi.app.models import Player
from tamagoatchi.lib.communication import Response, Request, ResponseType
from tamagoatchi.lib.view import ConsoleView
from tamagoatchi.app.models import tamagotchis, print_status
from tamagoatchi.app.definitions import NUMBER_OF_TAMAGOTCHI


class GamePersonalizeController:
    """
    A class used to personalize our player and tamagoatchis

    Attributes
    __________
    player: Player
    instance of player
    """
    def __init__(self):
        """
        Make a new instance of player
        """
        self.player = Player()

    @staticmethod
    def show_personalization(request: Request) -> Response:
        """
        Method to show personalization page

        Attributes
        __________
        request: Request
        All the information send by the player when he was redirected
        """
        view = ConsoleView('personalization',
                    {"player": Player(), "tamagotchi_status": print_status(), "tamagotchis": tamagotchis
                     }, request.json)
        return Response(ResponseType.valid, view)

    def new_player(self, request: Request) -> Response:
        """
        Method that create the player

        Attributes
        __________
        request: Request
        All the information send by the player when he was redirected
        """
        player_name = request.json['inputs']['playername']
        self.player.name = player_name
        view = ConsoleView('personalization',
                    {'player': self.player,
                     "tamagotchi_status": print_status(),
                     "tamagotchis": tamagotchis}, request.json)
        return Response(ResponseType.valid, view)

    def new_tamagotchis(self, request: Request) -> Response:
        """
        Method that rename tamagotchis

        Attributes
        __________
        request: Request
        All the information send by the player when he was redirected
        """
        tamagotchi_names = request.json['inputs']['tamaname']
        if len(tamagotchi_names) != NUMBER_OF_TAMAGOTCHI:
            return Response(ResponseType.error,
                            ConsoleView('personalization', {
                                'error': "Il n'y a pas assez de noms pour les tamagotchis",
                                'player': self.player, 'tamagotchi_status': print_status(),
                                'tamagotchis': tamagotchis
                            },
                                 request.json)
                            )
        for tamagotchi in tamagotchis:
            tamagotchi["name"] = tamagotchi_names[tamagotchis.index(tamagotchi)]
        return Response(ResponseType.valid, ConsoleView('personalization', {'player': self.player,
                                                                     'tamagotchi_status': print_status(),
                                                                     'tamagotchis': tamagotchis}, request.json))
