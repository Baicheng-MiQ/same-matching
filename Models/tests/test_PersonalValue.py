import unittest
from ..PersonalValue import PersonalValue

class TestPersonalValue(unittest.TestCase):

    def test_valid_input(self):
        # Test valid input
        pv1 = PersonalValue('a', 'a', 'a', 'a', 'a', 'a', ['a', 'b', 'c'], ['a', 'b', 'c', 'd', 'e'])
        pv2 = PersonalValue('b', 'b', 'b', 'b', 'b', 'b', ['a', 'b', 'c'], ['a', 'b', 'c', 'd', 'e'])
        self.assertEqual(pv1.score(pv2), 0)

    def test_invalid_input(self):
        # Test invalid input
        with self.assertRaises(ValueError):
            PersonalValue('z', 'a', 'a', 'a', 'a', 'a', ['a', 'b', 'c'], ['a', 'b', 'c', 'd', 'e'])
        with self.assertRaises(ValueError):
            PersonalValue('a', 'z', 'a', 'a', 'a', 'a', ['a', 'b', 'c'], ['a', 'b', 'c', 'd', 'e'])
        with self.assertRaises(ValueError):
            PersonalValue('a', 'a', 'z', 'a', 'a', 'a', ['a', 'b', 'c'], ['a', 'b', 'c', 'd', 'e'])
        with self.assertRaises(ValueError):
            PersonalValue('a', 'a', 'a', 'z', 'a', 'a', ['a', 'b', 'c'], ['a', 'b', 'c', 'd', 'e'])
        with self.assertRaises(ValueError):
            PersonalValue('a', 'a', 'a', 'a', 'z', 'a', ['a', 'b', 'c'], ['a', 'b', 'c', 'd', 'e'])
        with self.assertRaises(ValueError):
            PersonalValue('a', 'a', 'a', 'a', 'a', 'z', ['a', 'b', 'c'], ['a', 'b', 'c', 'd', 'e'])
        with self.assertRaises(ValueError):
            PersonalValue('a', 'a', 'a', 'a', 'a', 'a', ['z', 'b', 'c'], ['a', 'b', 'c', 'd', 'e'])
        with self.assertRaises(ValueError):
            PersonalValue('a', 'a', 'a', 'a', 'a', 'a', ['a', 'b', 'c'], ['a', 'b', 'c', 'd'])

    def test_score(self):
        # Test score calculation
        pv1 = PersonalValue('a', 'a', 'a', 'a', 'a', 'a', ['a', 'b', 'c'], ['a', 'b', 'c', 'd', 'e'])
        pv2 = PersonalValue('b', 'b', 'b', 'b', 'b', 'b', ['a', 'b', 'c'], ['a', 'b', 'c', 'd', 'e'])
        self.assertEqual(pv1.score(pv2), 0)
        pv3 = PersonalValue('a', 'a', 'a', 'a', 'a', 'a', ['a', 'b', 'c'], ['a', 'b', 'c', 'd', 'e'])
        pv4 = PersonalValue('a', 'a', 'a', 'a', 'a', 'a', ['a', 'b', 'c'], ['a', 'b', 'c', 'd', 'e'])
        self.assertEqual(pv3.score(pv4), 12)
        pv5 = PersonalValue('a', 'a', 'a', 'a', 'a', 'a', ['a', 'b', 'c'], ['a', 'b', 'c', 'd', 'e'])
        pv6 = PersonalValue('a', 'a', 'a', 'a', 'a', 'a', ['a', 'b', 'c'], ['a', 'b', 'c', 'd', 'f'])
        self.assertEqual(pv5.score(pv6), 12)

if __name__ == '__main__':
    unittest.main()