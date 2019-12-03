from .base_api import BaseApi
from datetime import datetime, timedelta
from collections import namedtuple

res = namedtuple('result', ["json", "total_pages", "status_code"])


class OrderManagementApi(BaseApi):

    def _build_url(self, endpoint):
        url = self.base_url + f'/api/oms/pvt/orders'
        return url + endpoint

    def get_order(self, order_id):
        endpoint = f'/{order_id}'
        url = self._build_url(endpoint)
        return self.get_result(url)

    def get_list_orders(self, initial_date: datetime = datetime(2000, 1, 1), page: int = 1):
        end_dt = datetime.today()
        url = self._build_url(
            f'?f_creationDate=creationDate:[{initial_date.date()}T00:00:00.000Z TO {end_dt.date()}T23:59:59.999Z]')
        params = {"page": f'{page}', "orderBy": "creationDate,asc"}
        result = self.session.get(url, params=params, timeout=self.timeout)
        if result.status_code == 200:
            js = result.json()
            total_pages = js['paging']['pages']
            return res(js, total_pages, result.status_code)
        else:
            return res(None, None, result.status_code)

    def get_conversation(self, order_id):
        url = self._build_url(f'/{order_id}/conversation-message')
        return self.get_result(url)

    def get_payment_transaction(self, order_id):
        url = self._build_url(f'/{order_id}/payment-transaction')
        return self.get_result(url)
