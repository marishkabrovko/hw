import unittest
from src.masks import get_mask_card_number, get_mask_account

class TestMasks(unittest.TestCase):

    def test_get_mask_card_number(self):
        self.assertEqual(get_mask_card_number(7000792289606361), "7000 79** **** 6361")

    def test_get_mask_account(self):
        self.assertEqual(get_mask_account(73654108430135874305), "**4305")

if __name__ == '__main__':
    unittest.main()
