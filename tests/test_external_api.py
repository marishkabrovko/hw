import unittest
from unittest.mock import patch

from src.external_api import convert_to_rub


class TestConvertToRub(unittest.TestCase):

    @patch("src.external_api.requests.get")
    def test_convert_to_rub_success(self, mock_get):
        mock_response = {"result": 740.0}
        mock_get.return_value.json.return_value = mock_response
        transaction = {"amount": 10, "currency": "USD"}
        result = convert_to_rub(transaction)
        self.assertEqual(result, 740.0)

    @patch("src.external_api.requests.get")
    def test_convert_to_rub_rub_currency(self, mock_get):
        transaction = {"amount": 10, "currency": "RUB"}
        result = convert_to_rub(transaction)
        self.assertEqual(result, 10.0)

    @patch("src.external_api.requests.get")
    def test_convert_to_rub_no_amount(self, mock_get):
        mock_response = {"result": 0.0}
        mock_get.return_value.json.return_value = mock_response
        transaction = {"currency": "USD"}
        result = convert_to_rub(transaction)
        self.assertEqual(result, 0.0)


if __name__ == "__main__":
    unittest.main()
