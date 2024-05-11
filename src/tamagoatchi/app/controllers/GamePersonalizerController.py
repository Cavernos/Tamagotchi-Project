from tamagoatchi.app.models import Player
from tamagoatchi.lib.communication import Response, Request, ResponseType
from tamagoatchi.lib.view import View
from tamagoatchi.app.models import tamagotchis, print_status
from tamagoatchi.app.definitions import NUMBER_OF_TAMAGOTCHI


class GamePersonalizerController:
    def __init__(self):
        self.player = Player()

    @staticmethod
    def show_personalization(request: Request) -> Response:
        view = View('personalization',
                    {"player": Player(), "tamagotchi_status": print_status(), "tamagotchis": tamagotchis
                     }, request.json)
        return Response(ResponseType.valid, view)

    def new_player(self, request: Request) -> Response:
        player_name = request.json['inputs']['playername']
        self.player.name = player_name
        view = View('personalization',
                    {'player': self.player,
                     "tamagotchi_status": print_status(),
                     "tamagotchis": tamagotchis}, request.json)
        return Response(ResponseType.valid, view)

    def new_tamagotchis(self, request: Request) -> Response:
        tamagotchi_names = request.json['inputs']['tamaname']
        if len(tamagotchi_names) != NUMBER_OF_TAMAGOTCHI:
            return Response(ResponseType.error,
                            View('personalization', {
                                'error': "Il n'y a pas assez de noms pour les tamagotchis",
                                'player': self.player, 'tamagotchi_status': print_status(),
                                'tamagotchis': tamagotchis
                            },
                                 request.json)
                            )
        for tamagotchi in tamagotchis:
            tamagotchi["name"] = tamagotchi_names[tamagotchis.index(tamagotchi)]
        return Response(ResponseType.valid, View('personalization', {'player': self.player,
                                                                     'tamagotchi_status': print_status(),
                                                                     'tamagotchis': tamagotchis}, request.json))
