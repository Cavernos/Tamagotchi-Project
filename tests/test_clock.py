import unittest
import tamagotchi
import time

from clock import Clock
from config import DAY_DURATION


class TestClock(unittest.TestCase):
    def setUp(self):
        self.tamagotchis = tamagotchi.tamagotchis
        self.clock = Clock("test_clock")

    def test_clock_duration(self):
        self.clock.start()
        duration = DAY_DURATION
        while duration:
            print(self.tamagotchis[0]['hunger'])
            time.sleep(1)
            duration -= 1
        self.assertEqual(self.tamagotchis[0]['hunger'], 200 - 5 * DAY_DURATION)
