import os
import json
from enum import Enum

from blockfrost.utils import ApiError, api_request_wrapper
from blockfrost.api.health import health, clock
import requests


class ApiUrls(Enum):
    mainnet = 'https://cardano-mainnet.blockfrost.io/api'
    testnet = 'https://cardano-testnet.blockfrost.io/api'
    ipfs = 'https://ipfs.blockfrost.io/api'


DEFAULT_API_VERSION = 'v0'
DEFAULT_ORDER = 'asc'
DEFAULT_PAGINATION_PAGE_COUNT = 1
DEFAULT_PAGINATION_PAGE_ITEMS_COUNT = 100

ADDRESS_GAP_LIMIT = 20


class Api:

    def __init__(
            self,
            project_id: str = None,
            base_url: str = None,
            api_version: str = None,
    ):
        self.project_id = project_id if project_id else os.environ.get('BLOCKFROST_PROJECT_ID')
        self.base_url = base_url if base_url else os.environ.get('BLOCKFROST_API_URL', default=ApiUrls.mainnet.value)
        self.api_version = api_version if api_version else os.environ.get('BLOCKFROST_API_VERSION',
                                                                          default=DEFAULT_API_VERSION)

    @property
    def url(self):
        return f"{self.base_url}/{self.api_version}"

    @property
    def authentication_header(self):
        return {
            'project_id': self.project_id
        }


class BlockFrostApi(Api):
    @api_request_wrapper
    def root(self) -> json:
        """https://cardano-mainnet.blockfrost.io/api/v0/"""
        return requests.get(
            url=f"{self.url}/",
            headers=self.authentication_header
        )

    health = health
    clock = clock
