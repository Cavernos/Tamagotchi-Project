import unittest
import tamagotchi


class TestTamagotchi(unittest.TestCase):
    def setUp(self) -> None:
        self.tamagotchis = tamagotchi.tamagotchis

    def test_status(self) -> None:
        result = [
            ['Name', 'Michel', 'Michel', 'Michel', 'Michel', 'Michel'],
            ['Hunger', 200, 200, 200, 200, 200],
            ['Health', 200, 200, 200, 200, 200],
            ['Boredom', 200, 200, 200, 200, 200],
            ['Thirsty', 200, 200, 200, 200, 200],
            ['Tireness', 200, 200, 200, 200, 200]
        ]
        self.assertEqual(tamagotchi.get_status(), result)

    def test_print_status(self) -> None:
        self.assertIsNone(tamagotchi.print_status())

if __name__ == '__main__':
    unittest.main()
