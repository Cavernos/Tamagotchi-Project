import unittest
import tamagotchi

from clock import Clock


class TestClock(unittest.TestCase):
    def setUp(self):
        self.tamagotchis = tamagotchi.tamagotchis
        self.clock = Clock("test_clock")
