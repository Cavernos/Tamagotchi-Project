import unittest
import tamagotchi


class TestTamagotchi(unittest.TestCase):
    def setUp(self) -> None:
        self.tamagotchis = tamagotchi.tamagotchis

    def test_status(self) -> None:
        tamagotchis_name = [self.tamagotchis[i]['name'] for i in range(len(self.tamagotchis))]
        tamagotchis_hunger = [self.tamagotchis[i]['hunger'] for i in range(len(self.tamagotchis))]
        tamagotchis_health = [self.tamagotchis[i]['health'] for i in range(len(self.tamagotchis))]
        tamagotchis_boredom = [self.tamagotchis[i]['boredom'] for i in range(len(self.tamagotchis))]
        tamagotchis_thirsty = [self.tamagotchis[i]['thirsty'] for i in range(len(self.tamagotchis))]
        tamagotchis_tireness = [self.tamagotchis[i]['tireness'] for i in range(len(self.tamagotchis))]
        result = [
            ['Name'] + tamagotchis_name,
            ['Hunger'] + tamagotchis_hunger,
            ['Health'] + tamagotchis_health,
            ['Boredom'] + tamagotchis_boredom,
            ['Thirsty'] + tamagotchis_thirsty,
            ['Tireness'] + tamagotchis_tireness
        ]
        self.assertEqual(tamagotchi.get_status(), result)

    def test_print_status(self) -> None:
        self.assertIsNone(tamagotchi.print_status())

if __name__ == '__main__':
    unittest.main()
