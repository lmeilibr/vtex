from collections import namedtuple

result = namedtuple('result', ['json', 'status_code'])


class BaseApi:

    def __init__(self, config):
        self.account_name = config.account_name
        self.environment = config.environment
        self.session = config.session
        self.timeout = config.timeout
        self.base_url = f'https://{self.account_name}.{self.environment}.com.br'

    def _call_api(self, endpoint):
        url = self._build_url(endpoint)
        return self.get_result(url)

    def get_result(self, url):
        response = self.session.get(url, timeout=self.timeout)
        if response.status_code == 200:
            js = response.json()
        else:
            js = None
        res = result(js, response.status_code)
        return res
