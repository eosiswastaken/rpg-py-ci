import unittest
import character


class TestRpg(unittest.TestCase):

    def test_has_ten_hp(self):
        bobasis = character.Character()
        self.assertEqual(10, bobasis.get_hp())

    def test_ten_attacks_kill(self):
        bobasis = character.Character()
        for i in range(10):
            bobasis.recieve_damage()
        self.assertEqual(0, bobasis.get_hp())

    def test_nine_attacks_dont_kill(self):
        bobasis = character.Character()
        for i in range(9):
            self.assertLess(0, bobasis.get_hp())


if __name__ == '__main__':
    unittest.main()
