import requests
from collections import namedtuple

from .api_collections import LogisticsApi
from .api_collections import CatalogApi
from .api_collections import GiftCardApi

DEFAULT_TIMEOUT = 60.0


class Vtex:

    def __init__(self, account_name=None, environment=None,
                 app_key=None, app_token=None,
                 session=None, timeout=None):
        self.account_name = account_name
        self.environment = environment
        self.app_key = app_key
        self.app_token = app_token

        session = self._init_session(session)
        timeout = timeout or DEFAULT_TIMEOUT

        config = namedtuple("config", ["account_name",
                                       "environment",
                                       "session",
                                       "timeout"])

        cfg = config(account_name, environment, session, timeout)
        self.logistics = LogisticsApi(cfg)
        self.catalog = CatalogApi(cfg)
        self.gift_card = GiftCardApi(cfg)

    def _get_header(self):
        return {'Accept': 'application/vnd.vtex.ds.v10+json',
                'Content-Type': 'application/json',
                'X-VTEX-API-AppToken': f'{self.app_token}',
                'X-VTEX-API-AppKey': f'{self.app_key}'
                }

    def _init_session(self, session):
        if not session:
            session = requests.Session()

        headers = self._get_header()
        session.headers.update(headers)
        return session
