import unittest
import character


class TestRpg(unittest.TestCase):

    def test_has_ten_hp(self):
        bobasis = character.Character()
        self.assertEqual(10, bobasis.get_hp())


if __name__ == '__main__':
    unittest.main()
