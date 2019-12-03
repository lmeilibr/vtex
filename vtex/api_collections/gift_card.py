"""Module for the Gift Card Microservice, official docs on:
https://documenter.getpostman.com/view/18468/vtex-giftcard-system-api/6YtyvrM?version=latest
https://documenter.getpostman.com/view/18468/RVfqmDgC?version=latest
https://documenter.getpostman.com/view/18468/7TRdAJy?version=latest
"""

from .base_api import BaseApi


class GiftCardApi(BaseApi):
    """
    Gift Card get functions for different endpoints
    """

    def _build_url(self, endpoint):
        midpoint = "/api/giftcardproviders"
        return self.base_url + midpoint + endpoint

    def get_gift_card_by_id(self, gift_card_id: str) -> dict:
        """
        Given a gift_card_id returns the information details in a dictionary

        :param gift_card_id: an UUID for gift_card
        :return: a json dict
        """
        url = f"https://api.vtexcommerce.com.br/{self.account_name}/giftcards/{gift_card_id}"
        return self.get_result(url)

    def get_list_gift_card(self, customer_id) -> dict:
        """
        Given a customer_id returns the information details in a dictionary

        :param customer_id:
        :return: a json dict
        """
        url = (self.base_url
               + f"/api/gift-card-system/pvt/giftCards?customerId={customer_id}")
        return self.get_result(url)

    def get_list_all_gift_card_providers(self) -> dict:
        """
        Return a dictionary with a list of the gift card providers
        :return:
        """
        url = self.base_url + f"/api/giftcardproviders"
        return self.get_result(url)

    def get_list_all_gift_card_transactions(self, gift_card_provider_id, gift_card_id):
        """
        Given a gift_card_provider_id and a gift_card_id, returns the transaction details

        :param gift_card_provider_id: a regular camelCase String(!?)
        :param gift_card_id: an UUID value
        :return:
        """
        endpoint = f"/{gift_card_provider_id}/giftcards/{gift_card_id}/transactions"
        return self._call_api(endpoint)

    def get_gift_card_transaction_by_id(self, gift_card_provider_id, gift_card_id, transaction_id):
        """
        Given a gift_card_provider_id, gift_card_id and a transaction_id,
        get the information into a dictionary format

        :param gift_card_provider_id: String
        :param gift_card_id: UUDI
        :param transaction_id: UUID
        :return: json dict
        """
        endpoint = _build_midpoint(gift_card_id, gift_card_provider_id, transaction_id)
        return self._call_api(endpoint)

    def get_gift_card_authorization_transaction(self, gift_card_provider_id,
                                                gift_card_id, transaction_id):
        """

        :param gift_card_provider_id:
        :param gift_card_id:
        :param transaction_id:
        :return:
        """
        endpoint = (_build_midpoint(gift_card_id, gift_card_provider_id, transaction_id)
                    + "/authorization")
        return self._call_api(endpoint)

    def get_list_all_gift_card_settlement_transactions(self, gift_card_provider_id,
                                                       gift_card_id, transaction_id):
        """
        Get settlement information in a json-dict format
        :param gift_card_provider_id: String
        :param gift_card_id: UUID
        :param transaction_id: UUID
        :return:
        """
        endpoint = (_build_midpoint(gift_card_id, gift_card_provider_id, transaction_id)
                    + "/settlements")
        return self._call_api(endpoint)

    def get_list_all_gift_card_cancellation_transactions(
            self, gift_card_provider_id, gift_card_id, transaction_id
    ):
        """
        Get cancellation information in a json-dict format
        :param gift_card_provider_id: String
        :param gift_card_id: UUID
        :param transaction_id: UUID
        :return:
        """
        endpoint = (_build_midpoint(gift_card_id, gift_card_provider_id, transaction_id)
                    + "/cancellations")
        return self._call_api(endpoint)


def _build_midpoint(gift_card_id, gift_card_provider_id, transaction_id):
    endpoint = f"/{gift_card_provider_id}/giftcards/{gift_card_id}/transactions/{transaction_id}"
    return endpoint
