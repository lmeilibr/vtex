# Integration Tests
from tests.integration_tests import OK, client
from vtex import Vtex
import pytest
import os


@pytest.fixture
def order_id():
    return os.environ.get("ORDER_ID")


def test_get_order(client: Vtex, order_id):
    result = client.order_management.get_order(order_id)
    assert result.status_code == OK


@pytest.mark.skip("too long to run")
def test_get_order_list(client: Vtex):
    result = client.order_management.get_list_orders()
    assert result.status_code == OK


def test_get_conversation(client: Vtex, order_id):
    result = client.order_management.get_conversation(order_id)
    assert result.status_code == OK


def test_get_payment_transaction(client: Vtex, order_id):
    result = client.order_management.get_payment_transaction(order_id)
    assert result.status_code == OK
