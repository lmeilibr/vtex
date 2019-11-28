class BaseApi:

    def __init__(self, config):
        self.account_name = config.account_name
        self.environment = config.environment
        self.session = config.session
        self.timeout = config.timeout

    def get_result(self, url):
        response = self.session.get(url, timeout=self.timeout)
        return response.json()
