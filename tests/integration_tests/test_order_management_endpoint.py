# Integration Tests
from tests.integration_tests import OK, client
from vtex import Vtex
import pytest
import os
from datetime import datetime


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


def test_get_orders_list_by_page(client: Vtex):
    page = 4
    result = client.order_management.get_list_orders_by_page(page)
    assert result.status_code == OK


def test_get_order_list_by_date(client: Vtex):
    dt = datetime(2018, 3, 2)
    result = client.order_management.get_list_orders_per_day(dt)
    assert result.status_code == OK


def test_get_order_list_by_date_hour(client: Vtex):
    dt = datetime(2019, 11, 29)
    hour = 23
    result = client.order_management.get_list_orders_per_hour_of_day(dt, hour)
    assert result.status_code == OK


def test_get_order_list_by_date_hour_minute(client: Vtex):
    dt = datetime(2019, 11, 29)
    hour = 23
    minute = 1
    result = client.order_management \
        .get_list_orders_per_hour_minute_of_day(dt, hour, minute)
    assert result.status_code == OK
