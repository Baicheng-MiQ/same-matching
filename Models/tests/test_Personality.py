import unittest
from ..Personality import Personality


class TestPersonality(unittest.TestCase):

    def setUp(self):
        self.personality1 = Personality(5, 7, 3, 8, 4)
        self.personality2 = Personality(4, 6, 2, 7, 5)
        self.personality3 = Personality(1, 1, 1, 1, 1)

    def test_score(self):
        self.assertEqual(self.personality1.score(self.personality2), 3)
        self.assertEqual(self.personality2.score(self.personality1), 3)
        self.assertEqual(self.personality1.score(self.personality3), -5)
        self.assertEqual(self.personality3.score(self.personality1), -5)
        self.assertEqual(self.personality2.score(self.personality3), -5)
        self.assertEqual(self.personality3.score(self.personality2), -5)

if __name__ == '__main__':
    unittest.main()