import unittest
from Player import Player


class TestPlayer(unittest.TestCase):
    def setUp(self) -> None:
        self.player = Player()

    def test_is_instance_of_player(self) -> None:
        self.assertIsInstance(self.player, Player)

    def test_biscuit_is_greater_than_zero(self) -> None:
        self.assertGreater(self.player.biscuit, 0)


if __name__ == '__main__':
    unittest.main()
