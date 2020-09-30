# Integration Tests
from tests.integration_tests import OK, client
from vtex import Vtex
import pytest
import os


@pytest.fixture
def order_id():
    return os.environ.get("ORDER_ID")


@pytest.fixture
def email():
    return os.environ.get("VTEX_EMAIL")


@pytest.fixture
def user_profile_id():
    return os.environ.get("CUSTOMER_ID")


@pytest.fixture
def acronym():
    return "CL"


# @pytest.mark.skip("working for now")
def test_get_profile_by_email(client: Vtex, email):
    result = client.master_data.get_profile_by_email(email)
    assert result.status_code == OK


@pytest.mark.skip("working for now")
def test_get_profile_by_user_profile_id(client: Vtex, user_profile_id):
    result = client.master_data.get_profile_by_user_profile_id(user_profile_id)
    assert result.status_code == OK


def test_get_clients_scroll(client: Vtex):
    result = client.master_data.get_clients_scroll()
    assert result.status_code == OK


# @pytest.mark.skip("working for now")
def test_get_clients_next_scroll(client: Vtex):
    initial = client.master_data.get_clients_scroll()
    result = client.master_data.get_clients_next_scroll(initial.token)
    assert result.status_code == OK


def test_data_entity_scroll(client: Vtex, acronym):
    result = client.master_data.get_data_entity_scroll(acronym)
    assert result.status_code == OK


def test_get_data_entity_next_scroll(client: Vtex, acronym):
    initial = client.master_data.get_data_entity_scroll(acronym)
    result = client.master_data.get_data_entity_next_scroll(initial.token)
    assert result.status_code == OK


def test_get_data_entities_list(client: Vtex):
    result = client.master_data.get_data_entities_list()
    assert result.status_code == OK


def test_get_data_entity_schema(client: Vtex, acronym):
    result = client.master_data.get_data_entity_schema(acronym)
    assert result.status_code == OK