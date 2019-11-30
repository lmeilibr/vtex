from .base_api import BaseApi


class GiftCardApi(BaseApi):

    def _build_url(self, endpoint):
        midpoint = '/api/giftcardproviders'
        return self.base_url + midpoint + endpoint

    def get_gift_card_by_id(self, gift_card_id):
        url = f'https://api.vtexcommerce.com.br/{self.account_name}/giftcards/{gift_card_id}'
        return self.get_result(url)

    def get_list_gift_card(self, customer_id):
        url = self.base_url + f'/api/gift-card-system/pvt/giftCards?customerId={customer_id}'
        return self.get_result(url)

    def get_list_all_gift_card_providers(self):
        url = self.base_url + f'/api/giftcardproviders'
        return self.get_result(url)

    def get_list_all_gift_card_transactions(self, gift_card_provider_id, gift_card_id):
        endpoint = f'/{gift_card_provider_id}/giftcards/{gift_card_id}/transactions'
        return self._call_api(endpoint)

    def get_gift_card_transaction_by_id(self, gift_card_provider_id, gift_card_id, transaction_id):
        endpoint = _build_midpoint(gift_card_id, gift_card_provider_id, transaction_id)
        return self._call_api(endpoint)

    def get_gift_card_authorization_transaction(self, gift_card_provider_id, gift_card_id, transaction_id):
        endpoint = _build_midpoint(gift_card_id, gift_card_provider_id, transaction_id) + '/authorization'
        return self._call_api(endpoint)

    def get_list_all_gift_card_settlement_transactions(self, gift_card_provider_id, gift_card_id, transaction_id):
        endpoint = _build_midpoint(gift_card_id, gift_card_provider_id, transaction_id) + '/settlements'
        return self._call_api(endpoint)

    def get_list_all_gift_card_cancellation_transactions(self, gift_card_provider_id, gift_card_id, transaction_id):
        endpoint = _build_midpoint(gift_card_id, gift_card_provider_id, transaction_id) + '/cancellations'
        return self._call_api(endpoint)


def _build_midpoint(gift_card_id, gift_card_provider_id, transaction_id):
    endpoint = f'/{gift_card_provider_id}/giftcards/{gift_card_id}/transactions/{transaction_id}'
    return endpoint
