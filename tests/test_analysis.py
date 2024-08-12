import pytest
from src.analysis import search_transactions_by_description, count_transactions_by_category


@pytest.fixture
def sample_transactions():
    return [
        {"description": "Payment to John", "amount": 100, "currency": "USD", "status": "EXECUTED"},
        {"description": "Refund from Alice", "amount": 50, "currency": "RUB", "status": "CANCELED"},
        {"description": "Payment to Alice", "amount": 200, "currency": "RUB", "status": "EXECUTED"},
    ]


def test_search_transactions_by_description(sample_transactions):
    result = search_transactions_by_description(sample_transactions, "Alice")
    assert len(result) == 2
    assert all("Alice" in transaction["description"] for transaction in result)


def test_count_transactions_by_category(sample_transactions):
    categories = ["Payment", "Refund"]
    result = count_transactions_by_category(sample_transactions, categories)
    assert result == {"Payment": 2, "Refund": 1}
