# dev Cavernos

import random
import unittest
import models.tamagotchi_file as tamagotchi_file
from config import CARACTERISTICS_INITIAL_VALUE


class TestTamagotchi(unittest.TestCase):
    def setUp(self) -> None:
        self.tamagotchis = tamagotchi_file.tamagotchis

    def test_tamagotchi_dictionary(self) -> None:
        """
        Test of tamagotchi's dict structure
        """
        test_tamagotchi = self.tamagotchis[0]
        result = False
        if (
                "name" and
                "hunger" and
                "health" and
                "boredom" and
                "thirsty" and
                "tireness" and
                "dead" and
                "sleep" and
                "in_battle"
                and "night_duration"
                in test_tamagotchi.keys()):
            result = True
        self.assertTrue(result)

    def test_eat(self) -> None:
        """
        Test of eat tamagotchi's function
        """
        test_tamagotchi = {
            "hunger": CARACTERISTICS_INITIAL_VALUE - 50,
        }
        tamagotchi_file.eat(test_tamagotchi)
        self.assertEqual(test_tamagotchi['hunger'], 200)

    def test_drink(self) -> None:
        """
        Test of drink tamagotchi's function
        """
        test_tamagotchi = {
            "thirsty": CARACTERISTICS_INITIAL_VALUE - 50,
        }
        tamagotchi_file.drink(test_tamagotchi)
        self.assertEqual(test_tamagotchi['thirsty'], 200)

    def test_play(self) -> None:
        """
        Test of play tamagotchi's function
        """
        test_tamagotchi = {
            "boredom": CARACTERISTICS_INITIAL_VALUE - 50,
            "tireness": CARACTERISTICS_INITIAL_VALUE,
        }
        tamagotchi_file.play(test_tamagotchi)
        self.assertEqual(test_tamagotchi['boredom'], 200)
        self.assertEqual(test_tamagotchi["tireness"], 150)

    def test_die(self) -> None:
        """
        Test of die tamagotchi's function
        """
        test_tamagotchi = {
            "health": CARACTERISTICS_INITIAL_VALUE
        }
        test_tamagotchi['health'] -= (CARACTERISTICS_INITIAL_VALUE + 1)
        self.assertTrue(tamagotchi_file.die(test_tamagotchi))

    def test_battle(self) -> None:
        """
        Test of battle tamagotchi's function
        """
        test_tamagotchi = {
            "boredom": CARACTERISTICS_INITIAL_VALUE,
        }
        test_tamagotchi['boredom'] -= (CARACTERISTICS_INITIAL_VALUE + 1)
        self.assertTrue(tamagotchi_file.battle(test_tamagotchi))

    def test_is_in_battle(self):
        """
        Test of is_in_battle tamagotchi's function
        """
        test_tamagotchis = [
            {
                "health": CARACTERISTICS_INITIAL_VALUE,
                "boredom": CARACTERISTICS_INITIAL_VALUE,
            }
            for i in range(5)
        ]
        test_tamagotchis[0]['boredom'] = 0
        tamagotchi_file.is_in_battle(test_tamagotchis)
        assert_result = [195 for i in range(5)]
        result = [test_tamagotchis[i]['health'] for i in range(5)]
        self.assertEqual(result, assert_result)

    def test_night_duration(self) -> None:
        """
        Test of night_duration tamagotchi's function
        """
        test_tamagotchi = {
            "night_duration": random.randint(30, 60)
        }
        self.assertGreaterEqual(test_tamagotchi["night_duration"], 30)
        self.assertLessEqual(test_tamagotchi["night_duration"], 60)

    def test_sleep_zzz(self) -> None:
        """
        Test of sleep_zzz tamagotchi's function
        """
        test_tamagotchi = {
            "health": CARACTERISTICS_INITIAL_VALUE - 1,
            "tireness": CARACTERISTICS_INITIAL_VALUE - 1,
            "boredom": CARACTERISTICS_INITIAL_VALUE - 1
        }
        tamagotchi_file.sleep_zzz(test_tamagotchi)
        assertion_result = [200 for i in range(3)]
        result = [test_tamagotchi["health"], test_tamagotchi["tireness"], test_tamagotchi["boredom"]]
        self.assertEqual(result, assertion_result)

    def test_awake(self) -> None:
        """
        Test of awake tamagotchi's function
        """
        test_tamagotchi = {
            "hunger": CARACTERISTICS_INITIAL_VALUE,
            "boredom": CARACTERISTICS_INITIAL_VALUE
        }
        tamagotchi_file.awake(test_tamagotchi)
        assertion_result = [195, 197]
        result = [test_tamagotchi["hunger"], test_tamagotchi["boredom"]]
        self.assertEqual(result, assertion_result)

    def test_status(self) -> None:
        """
        Test of get_status tamagotchi's function
        """
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
        self.assertEqual(tamagotchi_file.get_status(self.tamagotchis), result)

    def test_print_status(self) -> None:
        self.assertIsNone(tamagotchi_file.print_status(tamagotchi_file.get_status(self.tamagotchis)))


if __name__ == '__main__':
    unittest.main()
