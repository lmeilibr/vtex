from .base_api import BaseApi


class PaymentsGatewayApi(BaseApi):
    def _build_url_with_endpoint(self, transaction_id, endpoint=""):
        url = f"https://{self.account_name}.vtexpayments.com.br/api/pvt/transactions/{transaction_id}"
        return url + endpoint

    def get_transaction_details(self, transaction_id):
        url = self._build_url_with_endpoint(transaction_id)
        return self.get_result(url)

    def get_payments_by_transaction(self, transaction_id):
        url = self._build_url_with_endpoint(transaction_id, "/payments")
        return self.get_result(url)

    def get_payment_details(self, transaction_id, payment_id):
        url = self._build_url_with_endpoint(transaction_id, f"/payments/{payment_id}")
        return self.get_result(url)

    def get_transaction_settlement_details(self, transaction_id):
        url = self._build_url_with_endpoint(transaction_id, "/settlements")
        return self.get_result(url)
