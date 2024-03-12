import unittest

from Player import Player
from Tamagotchi import Tamagotchi


class TestTamagotchi(unittest.TestCase):
    """
    Dev : Nicolas Clement
    """
    # Attributes
    def setUp(self) -> None:
        self.tamagotchi = Tamagotchi()

    def test_name_attribute(self) -> None:
        self.assertTrue(hasattr(self.tamagotchi, 'name'))

    def test_hunger_attribute(self) -> None:
        self.assertTrue(hasattr(self.tamagotchi, 'hunger'))

    def test_boredom_attribute(self) -> None:
        self.assertTrue(hasattr(self.tamagotchi, 'boredom'))

    def test_tiredness_attribute(self) -> None:
        self.assertTrue(hasattr(self.tamagotchi, 'tiredness'))

    def test_health_attribute(self) -> None:
        self.assertTrue(hasattr(self.tamagotchi, 'health'))

    # Methods
    def test_play(self) -> None:
        initial_boredom = self.tamagotchi.boredom
        initial_tiredness = self.tamagotchi.tiredness
        self.tamagotchi.play()
        self.assertEqual(self.tamagotchi.tiredness, initial_tiredness - 50)
        self.assertEqual(self.tamagotchi.boredom, initial_boredom + 50)

    def test_feed(self) -> None:
        initial_hunger = self.tamagotchi.hunger
        p = Player()
        self.tamagotchi.feed(p)
        self.assertEqual(self.tamagotchi.hunger, initial_hunger + 50)


if __name__ == '__main__':
    unittest.main()
