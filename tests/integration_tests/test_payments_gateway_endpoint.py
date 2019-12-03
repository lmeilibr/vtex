# Integration Tests
from tests.integration_tests import OK, client
from vtex import Vtex
import pytest
import os


@pytest.fixture
def transaction_id():
    return os.environ.get('PAY_TRANSACTION_ID')


@pytest.fixture
def payment_id():
    return os.environ.get('PAYMENT_ID')


def test_get_transaction_details(client: Vtex, transaction_id):
    result = client.payments_gateway.get_transaction_details(transaction_id)
    assert result.status_code == OK


def test_get_payments_by_transaction(client: Vtex, transaction_id):
    result = client.payments_gateway.get_payments_by_transaction(transaction_id)
    assert result.status_code == OK


def test_get_payment_details(client: Vtex, transaction_id, payment_id):
    result = client.payments_gateway.get_payment_details(transaction_id, payment_id)
    assert result.status_code == OK


def test_get_transaction_settlement_details(client: Vtex, transaction_id):
    result = client.payments_gateway.get_transaction_settlement_details(transaction_id)
    assert result.status_code == OK
