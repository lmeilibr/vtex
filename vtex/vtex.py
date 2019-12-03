"""
Code for the Vtex class, that wraps the APIs into a single client object.

Each vtex microservice have its dedicate module inside the api_collections package
"""
from collections import namedtuple

import requests

from .api_collections import (
    LogisticsApi,
    CatalogApi,
    GiftCardApi,
    PaymentsGatewayApi,
    OrderManagementApi,
    MasterDataApi,
)

DEFAULT_TIMEOUT = 60.0


class Vtex:
    """
    Client class for the Vtex apis endpoints
    """

    def __init__(
            self,
            account_name=None,
            environment=None,
            app_key=None,
            app_token=None,
            session=None,
            timeout=None,
    ):
        """
        Setup the parameters values and create attributes composing with the api_collections modules

        :param account_name: Your VTEX accountName
        :param environment: Vtex Environment, normally 'vtexcommercestable'
        :param app_key: Your VTEX appKey
        :param app_token: Your VTEX appToken
        :param session: a requests Session object, to reuse the TCP connection (Performance!)
        :param timeout: 60 seconds by default, after this the request will throw an Error
        """
        self.account_name = account_name
        self.environment = environment
        self.app_key = app_key
        self.app_token = app_token

        session = self._init_session(session)
        timeout = timeout or DEFAULT_TIMEOUT

        config = namedtuple(
            "config", ["account_name", "environment", "session", "timeout"]
        )

        cfg = config(account_name, environment, session, timeout)
        self.logistics = LogisticsApi(cfg)
        self.catalog = CatalogApi(cfg)
        self.gift_card = GiftCardApi(cfg)
        self.payments_gateway = PaymentsGatewayApi(cfg)
        self.order_management = OrderManagementApi(cfg)
        self.master_data = MasterDataApi(cfg)

    def _get_header(self):
        """
        Setup the request header

        :return: dict()
        """
        return {
            "Accept": "application/vnd.vtex.ds.v10+json",
            "Content-Type": "application/json",
            "X-VTEX-API-AppToken": f"{self.app_token}",
            "X-VTEX-API-AppKey": f"{self.app_key}",
        }

    def _init_session(self, session):
        """
        Initialize the session and its header

        :param session:
        :return: a requests Session object
        """
        if not session:
            session = requests.Session()

        headers = self._get_header()
        session.headers.update(headers)
        return session
