from os import listdir
from os.path import join, isfile

from tamagoatchi.app.time import Clock
from tamagoatchi.lib.communication import Request, Response, ResponseType
from tamagoatchi.lib.controller import Controller
from tamagoatchi.lib.handlers import SaveHandler
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
        self.started = False

    def load(self, request: Request) -> Response:
        files_list = [
            f.split('.json')[0] for f in listdir(SaveHandler.save_dir) if isfile(join(SaveHandler.save_dir, f))
        ]
        if 'filename' in request.inputs.keys():
            SaveHandler.add_file_path(request.inputs['filename'])
            try:
                datas = SaveHandler.load(SaveHandler())
            except FileNotFoundError:
                return Response(ResponseType.valid, ConsoleView('game.load',
                                                                {'error': "Le Fichier est introuvable",
                                                                 "files_in_save_dir": files_list}, request.json))
            if datas is not None:
                tamagotchi_file.tamagotchis = datas['tamagotchis']
                self.clock.day_duration = datas['game_duration']
                self.clock.tamagotchis = datas['tamagotchis']
                request.json['form_redirect'] = 'game.start'
                return Response(ResponseType.valid, ConsoleView('game',
                                                                {'player': Player.get_instance(datas['player']),
                                                                 "tamagotchis": tamagotchi_file},
                                                                request.json))
        return Response(ResponseType.valid, ConsoleView('game.load', {'files_in_save_dir': files_list}, request.json))

    def game(self, request: Request) -> Response:
        """
        Start the game and define if the player has lost the game

        Attributes
        __________
        request: Request
        All the information send by the player when he was redirected
        """
        if 'ext' in request.inputs.keys():
            player: Player = Player.get_instance(request.inputs["ext"][0])
            if not self.clock.is_alive() and not self.started:
                self.clock.start()
                self.started = True
        if not self.clock.is_alive():
            self.clock.join()
            return Response(ResponseType.error, ConsoleView('',
                                                            {"error": "Vous avez perdu ! Un des tamagotchis est mort"},
                                                            request.json))

        return Response(ResponseType.valid, ConsoleView('game',
                                                        {'tamagotchis': tamagotchi_file,
                                                         'player': player,
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
            elif not self.clock.day_duration > tamagotchi['night_duration']:
                request.json['form_redirect'] = 'game.start'
                return Response(ResponseType.error, ConsoleView("game",
                                                        {'player': player, 'tamagotchis': tamagotchi_file,
                                                         "error": "Le tamagotchi dort"},
                                                        request.json))
        request.json['form_redirect'] = 'game.start'
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
            elif not self.clock.day_duration > tamagotchi['night_duration']:
                request.json['form_redirect'] = 'game.start'
                return Response(ResponseType.error, ConsoleView("game",
                                                        {'player': player, 'tamagotchis': tamagotchi_file,
                                                         "error": "Le tamagotchi dort"},
                                                        request.json))
        request.json['form_redirect'] = 'game.start'
        return Response(ResponseType.valid, ConsoleView("game",
                                                        {'player': player, 'tamagotchis': tamagotchi_file},
                                                        request.json))

    def save(self, request: Request) -> Response:
        day_duration = self.clock.stop()
        player = request.inputs['ext'][0]
        tamagotchis = request.inputs['ext'][1]
        request.json['form_redirect'] = 'save'
        return Response(ResponseType.valid, ConsoleView('save', {'tamagotchis': tamagotchis,
                                                                 'player': player,
                                                                 'game_duration': day_duration}, request.json))
