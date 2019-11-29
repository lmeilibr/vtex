# Integration Tests
from tests.integration_tests import OK, client
from vtex import Vtex
import pytest


@pytest.fixture
def product_id():
    return 1697


@pytest.fixture
def sku_id():
    return 14362


@pytest.fixture
def sales_channel_id():
    return 1


@pytest.fixture
def seller_id():
    return 1


def test_get_category(client: Vtex):
    result = client.catalog.get_category(2)
    assert result.status_code == OK


def test_get_category_tree(client: Vtex):
    result = client.catalog.get_category_tree()
    assert result.status_code == OK


def test_get_brand(client: Vtex):
    result = client.catalog.get_brand(2000000)
    assert result.status_code == OK


def test_get_product_specification(client: Vtex, product_id):
    result = client.catalog.get_product_specification(product_id)
    assert result.status_code == OK


def test_get_product(client: Vtex, product_id):
    result = client.catalog.get_product(product_id)
    assert result.status_code == OK


def test_get_product_review_rate(client: Vtex, product_id):
    result = client.catalog.get_product_review_rate(product_id)
    assert result.status_code == OK


def test_get_list_all_skus(client: Vtex):
    result = client.catalog.get_list_all_skus()
    assert result.status_code == OK


def test_get_sku(client: Vtex, sku_id):
    result = client.catalog.get_sku(sku_id)
    assert result.status_code == OK


def test_get_sales_channel(client: Vtex):
    result = client.catalog.get_sales_channel()
    assert result.status_code == OK


def test_get_sales_channel_by_id(client: Vtex, sales_channel_id):
    result = client.catalog.get_sales_channel_by_id(sales_channel_id)
    assert result.status_code == OK


def test_get_seller_by_id(client: Vtex, seller_id):
    result = client.catalog.get_seller_by_id(seller_id)
    assert result.status_code == OK
