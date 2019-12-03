# Integration Tests
from tests.integration_tests import OK, client, transaction_id, customer_id
from vtex import Vtex
import pytest
import os


@pytest.fixture
def gift_card_provider_id():
    return 'VtexGiftCard'


@pytest.fixture
def gift_card_id():
    return os.environ.get("GIFT_CARD_ID")


def test_gift_card_imports(gift_card_id, transaction_id):
    assert gift_card_id and transaction_id


@pytest.mark.skip(reason="endpoint returning 500")
def test_get_gift_card_by_id(client: Vtex):
    result = client.gift_card.get_gift_card_by_id(gift_card_id)
    assert result.status_code == OK


def test_get_list_gift_card(client: Vtex, customer_id):
    result = client.gift_card.get_list_gift_card(customer_id)
    assert result.status_code == OK


def test_get_list_all_gift_card_providers(client: Vtex):
    result = client.gift_card.get_list_all_gift_card_providers()
    assert result.status_code == OK


def test_get_list_all_gift_card_transactions(client: Vtex, gift_card_provider_id, gift_card_id):
    result = client.gift_card.get_list_all_gift_card_transactions(gift_card_provider_id, gift_card_id)
    assert result.status_code == OK


def test_get_gift_card_transaction_by_id(client: Vtex, gift_card_provider_id, gift_card_id, transaction_id):
    result = client.gift_card.get_gift_card_transaction_by_id(gift_card_provider_id,
                                                              gift_card_id,
                                                              transaction_id)
    assert result.status_code == OK


def test_get_gift_card_authorization_transaction(client: Vtex, gift_card_provider_id, gift_card_id, transaction_id):
    result = client.gift_card.get_gift_card_authorization_transaction(gift_card_provider_id,
                                                                      gift_card_id,
                                                                      transaction_id)
    assert result.status_code == OK


def test_get_list_all_gift_card_settlement_transactions(client: Vtex, gift_card_provider_id, gift_card_id,
                                                        transaction_id):
    result = client.gift_card.get_list_all_gift_card_settlement_transactions(gift_card_provider_id, gift_card_id,
                                                                             transaction_id)
    assert result.status_code == OK


def test_get_list_all_gift_card_cancellation_transactions(client: Vtex, gift_card_provider_id, gift_card_id,
                                                          transaction_id):
    result = client.gift_card.get_list_all_gift_card_cancellation_transactions(gift_card_provider_id, gift_card_id,
                                                                               transaction_id)
    assert result.status_code == OK
