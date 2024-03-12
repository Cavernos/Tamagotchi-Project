import unittest
from Player import Player
from Tamagotchi import Tamagotchi


class TestPlayer(unittest.TestCase):
    def setUp(self) -> None:
        self.player = Player()
    
    def test_is_instance_of_player(self) -> None:
        self.assertIsInstance(self.player, Player)

    def test_biscuit_is_greater_than_zero(self) -> None:
        self.assertGreater(self.player.biscuit, 0)

    def test_player_feed_tamagotchi(self) -> None:
        tamagotchi = Tamagotchi()
        tamagotchi.feed(self.player)


if __name__ == '__main__':
    unittest.main()
