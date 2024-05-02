# dev Cavernos
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
        self.assertEqual(self.saver.save(tamagotchis), json.dumps({"tamagotchis": tamagotchis}))
    
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
        self.assertEqual(self.saver.save(tamagotchis, player, clock.game_time), json.dumps({'tamagotchis': tamagotchis, 'player': dict(player), 'game_time': clock.game_time}))
    
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
        self.assetEqual(self.saver.load(tamagotchis), tamagotchis)
    
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
        saver_tamagotchis, saver_clock, saver_player = self.saver.load_all()
        self.assertEqual(saver_clock, clock.game_time)
        self.assertEqualt(saver_player, player)
        self.assertEqual(saver_tamagotchis, tamagotchis)
    
    def test_save_in_file(self):
        file = self.saver.file_to_saves
        self.saver.save_in_file()
        with open(file) as file:
            data = file.read()
        self.assertIsFile(file)
        self.assertEqual(self.saver.save_all(), data)
        