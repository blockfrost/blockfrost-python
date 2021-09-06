import os
import requests
from dataclasses import dataclass

from ..utils import Api, ApiUrls, object_request_wrapper
from .health import \
    health, \
    clock
from .metrics import \
    metrics, \
    metrics_endpoints
from .nutlink import \
    nutlink_address, \
    nutlink_address_tickers, \
    nutlink_address_ticker, \
    nutlink_ticker
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
    address_transactions, \
    assets, \
    asset, \
    asset_history, \
    asset_transactions, \
    asset_addresses, \
    policy_assets, \
    block_latest, \
    block_latest_transactions, \
    block, \
    block_slot, \
    block_epoch_slot, \
    blocks_next, \
    blocks_previous, \
    block_transactions, \
    epoch_latest, \
    epoch_latest_parameters, \
    epoch, \
    epochs_next, \
    epochs_previous, \
    epoch_stakes, \
    epoch_pool_stakes, \
    epoch_blocks, \
    epoch_pool_blocks, \
    genesis, \
    metadata_labels, \
    metadata_label_json, \
    metadata_label_cbor, \
    network, \
    pools, \
    pools_retired, \
    pools_retiring, \
    pool, \
    pool_history, \
    pool_metadata, \
    pool_relays, \
    pool_delegators, \
    pool_blocks, \
    pool_updates, \
    transaction, \
    transaction_utxos, \
    transaction_stakes, \
    transaction_delegations, \
    transaction_withdrawals, \
    transaction_mirs, \
    transaction_pool_updates, \
    transaction_pool_retires, \
    transaction_metadata, \
    transaction_metadata_cbor, \
    transaction_submit


class BlockFrostApi(Api):

    def __init__(self, project_id: str = None, base_url: str = None, api_version: str = None):
        super().__init__(
            project_id=project_id,
            base_url=base_url if base_url else os.environ.get('BLOCKFROST_API_URL', default=ApiUrls.mainnet.value),
            api_version=api_version)

    @dataclass
    class RootResponse:
        url: str
        version: str

    @object_request_wrapper(RootResponse)
    def root(self) -> requests.Response:
        """https://cardano-mainnet.blockfrost.io/api/v0/"""
        return requests.get(
            url=f"{self.url}/",
            headers=self.authentication_header
        )

    # misc
    health = health
    clock = clock
    nutlink_address = nutlink_address
    nutlink_address_tickers = nutlink_address_tickers
    nutlink_address_ticker = nutlink_address_ticker
    nutlink_ticker = nutlink_ticker
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
    # assets
    assets = assets
    asset = asset
    asset_history = asset_history
    asset_transactions = asset_transactions
    asset_addresses = asset_addresses
    policy_assets = policy_assets
    # blocks
    block_latest = block_latest
    block_latest_transactions = block_latest_transactions
    block = block
    block_slot = block_slot
    block_epoch_slot = block_epoch_slot
    blocks_next = blocks_next
    blocks_previous = blocks_previous
    block_transactions = block_transactions
    # epochs
    epoch_latest = epoch_latest
    epoch_latest_parameters = epoch_latest_parameters
    epoch = epoch
    epochs_next = epochs_next
    epochs_previous = epochs_previous
    epoch_stakes = epoch_stakes
    epoch_pool_stakes = epoch_pool_stakes
    epoch_blocks = epoch_blocks
    epoch_pool_blocks = epoch_pool_blocks
    # ledger
    genesis = genesis
    # metadata
    metadata_labels = metadata_labels
    metadata_label_json = metadata_label_json
    metadata_label_cbor = metadata_label_cbor
    # network
    network = network
    # pools
    pools = pools
    pools_retired = pools_retired
    pools_retiring = pools_retiring
    pool = pool
    pool_history = pool_history
    pool_metadata = pool_metadata
    pool_relays = pool_relays
    pool_delegators = pool_delegators
    pool_blocks = pool_blocks
    pool_updates = pool_updates
    # transactions
    transaction = transaction
    transaction_utxos = transaction_utxos
    transaction_stakes = transaction_stakes
    transaction_delegations = transaction_delegations
    transaction_withdrawals = transaction_withdrawals
    transaction_mirs = transaction_mirs
    transaction_pool_updates = transaction_pool_updates
    transaction_pool_retires = transaction_pool_retires
    transaction_metadata = transaction_metadata
    transaction_metadata_cbor = transaction_metadata_cbor
    transaction_submit = transaction_submit
