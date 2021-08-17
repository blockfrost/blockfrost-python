import os
import requests

from ..utils import Api, ApiUrls, object_request_wrapper
from .health import \
    health, \
    clock
from .metrics import \
    metrics, \
    metrics_endpoints
from .nutlink import \
    nutlink, \
    nutlink_tickers
from .cardano import \
    accounts, \
    account_rewards, \
    account_history, \
    account_delegations, \
    account_registrations, \
    account_withdrawals, \
    account_mirs, \
    account_addresses, \
    account_addresses_assets, \
    address, \
    address_total, \
    address_utxos, \
    address_transactions


class BlockFrostApi(Api):

    def __init__(self, project_id: str = None, base_url: str = None, api_version: str = None):
        super().__init__(
            project_id=project_id,
            base_url=base_url if base_url else os.environ.get('BLOCKFROST_API_URL', default=ApiUrls.mainnet.value),
            api_version=api_version)

    @object_request_wrapper()
    def root(self) -> requests.Response:
        """https://cardano-mainnet.blockfrost.io/api/v0/"""
        return requests.get(
            url=f"{self.url}/",
            headers=self.authentication_header
        )

    # misc
    health = health
    clock = clock
    nutlink = nutlink
    nutlink_tickers = nutlink_tickers
    # metrics
    metrics = metrics
    metrics_endpoints = metrics_endpoints
    # account
    accounts = accounts
    account_rewards = account_rewards
    account_history = account_history
    account_delegations = account_delegations
    account_registrations = account_registrations
    account_withdrawals = account_withdrawals
    account_mirs = account_mirs
    account_addresses = account_addresses
    account_addresses_assets = account_addresses_assets
    # address
    address = address
    address_total = address_total
    address_utxos = address_utxos
    address_transactions = address_transactions
