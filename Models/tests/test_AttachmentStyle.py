import unittest
from ..AttachmentStyle import AttachmentStyle

class TestAttachmentStyle(unittest.TestCase):
    def test_valid_style(self):
        style = AttachmentStyle("secure")
        self.assertEqual(style.style, "secure")

    def test_invalid_style(self):
        with self.assertRaises(ValueError):
            AttachmentStyle("invalid-style")

    def test_score(self):
        style1 = AttachmentStyle("secure")
        style2 = AttachmentStyle("preoccupied")
        self.assertEqual(style1.score(style2), 0.5)

    def test_incompatible_score(self):
        with self.assertRaises(ValueError):
            style1 = AttachmentStyle("secure")
            style2 = AttachmentStyle("invalid-style")
            style1.score(style2)

if __name__ == '__main__':
    unittest.main()