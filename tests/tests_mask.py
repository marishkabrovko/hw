import unittest

from src.masks import get_mask_account
from src.masks import get_mask_card_number
from src.widget import get_date
from src.widget import mask_account_card


class TestMasks(unittest.TestCase):

    def test_get_mask_card_number(self):
        self.assertEqual(get_mask_card_number(7000792289606361), "7000 79** **** 6361")

    def test_get_mask_account(self):
        self.assertEqual(get_mask_account(73654108430135874305), "**4305")


class TestWidget(unittest.TestCase):

    def test_mask_account_card(self):
        self.assertEqual(mask_account_card("Visa Platinum 7000792289606361"), "Visa Platinum 7000 79** **** 6361")
        self.assertEqual(mask_account_card("Счет 73654108430135874305"), "Счет **4305")

    def test_get_date(self):
        self.assertEqual(get_date("2024-03-11T02:26:18.671407"), "11.03.2024")


if __name__ == "__main__":
    unittest.main()
