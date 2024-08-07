import unittest

from src.utils import read_transactions


class TestUtils(unittest.TestCase):

    def test_read_transactions_success(self):
        result = read_transactions("data/operations.json")
        self.assertIsInstance(result, list)

    def test_read_transactions_file_not_found(self):
        result = read_transactions("data/non_existing_file.json")
        self.assertEqual(result, [])

    def test_read_transactions_empty_file(self):
        result = read_transactions("data/empty.json")
        self.assertEqual(result, [])

    def test_read_transactions_not_a_list(self):
        result = read_transactions("data/not_a_list.json")
        self.assertEqual(result, [])


if __name__ == "__main__":
    unittest.main()
