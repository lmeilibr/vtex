from collections import namedtuple

result = namedtuple('result', ['json', 'status_code'])

class BaseApi:



    def __init__(self, config):
        self.account_name = config.account_name
        self.environment = config.environment
        self.session = config.session
        self.timeout = config.timeout
        self.base_url = f'https://{self.account_name}.{self.environment}.com.br'

    def get_result(self, url):
        response = self.session.get(url, timeout=self.timeout)
        return result(response.json(), response.status_code)
