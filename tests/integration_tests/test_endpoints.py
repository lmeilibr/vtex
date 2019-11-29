# Integration Tests
import pytest
import os
from vtex import Vtex

# HTTP Status Code
OK = 200


@pytest.fixture
def client():
    account_name = os.environ.get('ACCOUNTNAME')
    environment = os.environ.get('ENVIRONMENT')
    app_key = os.environ.get('KEY')
    app_token = os.environ.get('TOKEN')
    return Vtex(account_name, environment, app_key, app_token)


def test_get_category_tree(client: Vtex):
    result = client.catalog.get_category_tree()
    assert result.status_code == OK


def test_get_sales_channel(client: Vtex):
    result = client.catalog.get_sales_channel()
    assert result.status_code == OK
