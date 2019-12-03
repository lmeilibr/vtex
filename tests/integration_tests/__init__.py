import os

import pytest

from vtex import Vtex

# HTTP Status Code
OK = 200


@pytest.fixture
def client() -> Vtex:
    account_name = os.environ.get('ACCOUNTNAME')
    environment = os.environ.get('ENVIRONMENT')
    app_key = os.environ.get('KEY')
    app_token = os.environ.get('TOKEN')
    return Vtex(account_name, environment, app_key, app_token)


@pytest.fixture
def customer_id():
    return os.environ.get('CUSTOMER_ID')


@pytest.fixture
def transaction_id():
    return os.environ.get("TRANSACTION_ID")

