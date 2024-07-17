import pytest
from src.processing import filter_by_state, sort_by_date


def test_filter_by_state(transactions):
    assert len(filter_by_state(transactions)) == 2
    assert len(filter_by_state(transactions, 'CANCELED')) == 2
    assert len(filter_by_state(transactions, 'PENDING')) == 0


def test_sort_by_date(transactions):
    sorted_transactions = sort_by_date(transactions)
    assert sorted_transactions[0]['id'] == 41428829
    assert sorted_transactions[-1]['id'] == 939719570

    sorted_transactions_asc = sort_by_date(transactions, descending=False)
    assert sorted_transactions_asc[0]['id'] == 939719570
    assert sorted_transactions_asc[-1]['id'] == 41428829
