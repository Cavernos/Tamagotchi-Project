import unittest

from Player import Player
from Tamagotchi import Tamagotchi


class TestTamagotchi(unittest.TestCase):
    def setUp(self):
        self.tamagotchi = Tamagotchi("")

    def test_name_attribute(self):
        self.assertEqual(hasattr(self.tamagotchi, 'name'), True)  # add assertion here

    def test_hunger_attribute(self):
        self.assertEqual(hasattr(self.tamagotchi, 'hunger'), True)

    def test_boredom_attribute(self):
        self.assertEqual(hasattr(self.tamagotchi, 'boredom'), True)

    def test_tiredness_attribute(self):
        self.assertEqual(hasattr(self.tamagotchi, 'tiredness'), True)

    def test_health_attribute(self):
        self.assertEqual(hasattr(self.tamagotchi, 'health'), True)

    def test_play(self):
        initial_boredom, initial_tiredness = self.tamagotchi.boredom, self.tamagotchi.tiredness
        self.tamagotchi.play()
        self.assertEqual(self.tamagotchi.tiredness, initial_tiredness - 50)
        self.assertEqual(self.tamagotchi.boredom, initial_boredom + 50)

    def test_feed(self):
        initial_hunger = self.tamagotchi.hunger
        p = Player()
        self.tamagotchi.feed(p)
        self.assertEqual(self.tamagotchi.hunger, initial_hunger - 50)


if __name__ == '__main__':
    unittest.main()
