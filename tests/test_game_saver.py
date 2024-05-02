# dev Cavernos
from unittest.mock import mock_open, patch

from Player import Player
from clock import Clock
from config import CARACTERISTICS_INITIAL_VALUE
from game_saver import GameSaver
import unittest
import json


class TestGameSaver(unittest.TestCase):

    def setUp(self):
        self.saver = GameSaver("test.json")

    def test_save_one(self):
        tamagotchis = [{
            "name": "Michel",
            "hunger": CARACTERISTICS_INITIAL_VALUE,
            "health": CARACTERISTICS_INITIAL_VALUE,
            "boredom": CARACTERISTICS_INITIAL_VALUE,
            "thirsty": CARACTERISTICS_INITIAL_VALUE,
            "tireness": CARACTERISTICS_INITIAL_VALUE,
            "sleep": False,
            "night_duration": 32
        }]
        self.assertEqual(self.saver.save(tamagotchis=tamagotchis), json.dumps({"tamagotchis": tamagotchis}))

    def test_save_all(self):
        tamagotchis = [{
            "name": "Michel",
            "hunger": CARACTERISTICS_INITIAL_VALUE,
            "health": CARACTERISTICS_INITIAL_VALUE,
            "boredom": CARACTERISTICS_INITIAL_VALUE,
            "thirsty": CARACTERISTICS_INITIAL_VALUE,
            "tireness": CARACTERISTICS_INITIAL_VALUE,
            "sleep": False,
            "night_duration": 32
        }]
        clock = Clock()
        player = Player()
        self.assertEqual(self.saver.save(tamagotchis=tamagotchis, player=player.__dict__, game_time=clock.game_time),
                         json.dumps(
                             {'tamagotchis': tamagotchis,
                              'player': player.__dict__,
                              'game_time': clock.game_time}
                         )
                         )

    def test_load(self):
        tamagotchis = [{
            "name": "Michel",
            "hunger": CARACTERISTICS_INITIAL_VALUE,
            "health": CARACTERISTICS_INITIAL_VALUE,
            "boredom": CARACTERISTICS_INITIAL_VALUE,
            "thirsty": CARACTERISTICS_INITIAL_VALUE,
            "tireness": CARACTERISTICS_INITIAL_VALUE,
            "sleep": False,
            "night_duration": 32
        }]
        self.saver.save(tamagotchis=tamagotchis)
        self.assertEqual(self.saver.load("tamagotchis"), tamagotchis)

    def test_load_all(self):
        tamagotchis = [{
            "name": "Michel",
            "hunger": CARACTERISTICS_INITIAL_VALUE,
            "health": CARACTERISTICS_INITIAL_VALUE,
            "boredom": CARACTERISTICS_INITIAL_VALUE,
            "thirsty": CARACTERISTICS_INITIAL_VALUE,
            "tireness": CARACTERISTICS_INITIAL_VALUE,
            "sleep": False,
            "night_duration": 32
        }]
        clock = Clock()
        player = Player()
        self.saver.save(tamagotchis=tamagotchis, player=player.__dict__, game_time=clock.game_time)
        saver_tamagotchis, saver_clock, saver_player = self.saver.load()
        self.assertEqual(saver_clock, clock.game_time)
        self.assertTrue(isinstance(saver_player, Player))
        self.assertEqual(saver_tamagotchis, tamagotchis)
