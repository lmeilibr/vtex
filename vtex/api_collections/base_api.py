"""Basic setup for the other modules requests"""

from collections import namedtuple

Result = namedtuple("result", ["json", "status_code", "token"])


class BaseApi:
    """
    Base Class for all the other api_collections modules
    """

    def __init__(self, config):
        self.account_name = config.account_name
        self.environment = config.environment
        self.session = config.session
        self.timeout = config.timeout
        self.base_url = f"https://{self.account_name}.{self.environment}.com.br"

    def _call_api(self, endpoint):
        url = self._build_url(endpoint)
        return self.get_result(url)

    def _build_url(self, endpoint):
        raise NotImplementedError

    def get_result(self, url) -> Result:
        """
        Given a url, fetch the json result, its status code, and a token (scroll-only)

        :param url: the vtex endpoint
        :return: a namedtuple
        """
        response = self.session.get(url, timeout=self.timeout)
        if response.status_code == 200:
            json_response = response.json()
            token = response.headers.get("x-vtex-md-token", None)
        else:
            json_response = None
            token = None
        output = Result(json_response, response.status_code, token)
        return output
