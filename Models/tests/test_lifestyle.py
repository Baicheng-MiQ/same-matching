import unittest
from ..Lifestyle import Lifestyle

class TestLifestyle(unittest.TestCase):
    def test_same_lifestyle(self):
        # Test when both lifestyles are the same
        lifestyle1 = Lifestyle('Night Owl', True, True, True)
        lifestyle2 = Lifestyle('Night Owl', True, True, True)
        self.assertEqual(lifestyle1.score(lifestyle2), 4)

    def test_different_routine(self):
        # Test when the routines are different
        lifestyle1 = Lifestyle('Night Owl', True, True, True)
        lifestyle2 = Lifestyle('Early bird', True, True, True)
        self.assertEqual(lifestyle1.score(lifestyle2), 2)

    def test_different_habits(self):
        # Test when some habits are different
        lifestyle1 = Lifestyle('Night Owl', True, True, True)
        lifestyle2 = Lifestyle('Night Owl', False, False, False)
        self.assertEqual(lifestyle1.score(lifestyle2), -2)

    def test_all_different(self):
        # Test when all habits are different
        lifestyle1 = Lifestyle('Night Owl', True, True, True)
        lifestyle2 = Lifestyle('Early bird', False, False, False)
        self.assertEqual(lifestyle1.score(lifestyle2), -4)

if __name__ == '__main__':
    unittest.main()