# dev Cavernos

from threading import Event
import time
import unittest
import random
import logging
from unittest.mock import patch
from clock import Clock
from config import NUMBER_OF_TAMAGOTCHI, CARACTERISTICS_INITIAL_VALUE, DAY_DURATION


class TestClock(unittest.TestCase):

    def setUp(self):
        self.clock = Clock("test_clock", Event())

    @patch("time.sleep", return_value=None)
    def test_clock_time(self, patched_time_sleep) -> None:
        """
            Test clock duration
        """
        self.clock.start()
        time.sleep(DAY_DURATION)
        self.assertEqual(self.clock.day_duration, 0)
        self.clock.join()

    @patch("time.sleep", return_value=None)
    def test_night_routine(self, patched_time_sleep) -> None:
        """
        Test caracteristics increase in night
        """
        self.clock.day_duration = 2
        tamagotchis = [
            {
                "name": "Michel",
                "hunger": CARACTERISTICS_INITIAL_VALUE,
                "health": CARACTERISTICS_INITIAL_VALUE - 2,
                "boredom": CARACTERISTICS_INITIAL_VALUE -2,
                "thirsty": CARACTERISTICS_INITIAL_VALUE,
                "tireness": CARACTERISTICS_INITIAL_VALUE -2,
                "sleep": False,
                "night_duration": random.randint(30, 60)
            }
            for i in range(NUMBER_OF_TAMAGOTCHI)
        ]
        self.clock.tamagotchis = tamagotchis
        self.clock.start()
        time.sleep(2)
        result = [
            [tamagotchis[i]["boredom"] for i in range(len(tamagotchis))],
            [tamagotchis[i]["health"] for i in range(len(tamagotchis))],
            [tamagotchis[i]["tireness"] for i in range(len(tamagotchis))]
        ]
        self.assertEqual(result, [
            [CARACTERISTICS_INITIAL_VALUE for i in range(len(tamagotchis))] for i in range(3)
        ]
                         )
        self.clock.join()

    @patch("time.sleep", return_value=None)
    def test_die(self, patched_time_sleep) -> None:
        """
        Test of die
        """
        tamagotchi_ = {
            "name": "Michel",
            "hunger": CARACTERISTICS_INITIAL_VALUE,
            "health": CARACTERISTICS_INITIAL_VALUE,
            "boredom": CARACTERISTICS_INITIAL_VALUE,
            "thirsty": CARACTERISTICS_INITIAL_VALUE,
            "tireness": CARACTERISTICS_INITIAL_VALUE,
            "sleep": False,
            "night_duration": random.randint(30, 60)
        }
        self.clock.tamagotchis = [tamagotchi_]
        self.clock.start()
        time.sleep(180)
        self.assertFalse(self.clock.is_alive())

    @patch("time.sleep", return_value=None)
    def test_battle(self, patched_time_sleep) -> None:
        """
        Test of battle function
        """
        tamagotchi_ = {
            "name": "Michel",
            "hunger": CARACTERISTICS_INITIAL_VALUE,
            "health": CARACTERISTICS_INITIAL_VALUE,
            "boredom": 0,
            "thirsty": CARACTERISTICS_INITIAL_VALUE,
            "tireness": CARACTERISTICS_INITIAL_VALUE,
            "sleep": False,
            "night_duration": 0
        }
        self.clock.tamagotchis = [tamagotchi_]
        self.clock.day_duration = 1
        self.clock.start()
        time.sleep(1)
        self.assertEqual(self.clock.tamagotchis[0]['health'], 195)

    @patch("time.sleep", return_value=None)
    def test_recalculate_night_time(self, patched_time_sleep) -> None:
        """
        Test of nigth_duration recalculation function
        """
        tamagotchi_ = {
            "name": "Michel",
            "hunger": CARACTERISTICS_INITIAL_VALUE,
            "health": CARACTERISTICS_INITIAL_VALUE,
            "boredom": CARACTERISTICS_INITIAL_VALUE,
            "thirsty": CARACTERISTICS_INITIAL_VALUE,
            "tireness": CARACTERISTICS_INITIAL_VALUE,
            "sleep": False,
            "night_duration": random.randint(30, 60)
        }
        initial_night_duration = tamagotchi_['night_duration']
        self.clock.tamagotchis = [tamagotchi_]
        self.clock.day_duration = 1
        self.clock.start()
        time.sleep(2)
        self.assertNotEqual(self.clock.tamagotchis[0]["night_duration"], initial_night_duration)


