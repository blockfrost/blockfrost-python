import os
import requests
from dataclasses import dataclass

from ..utils import Api, ApiUrls, object_request_wrapper


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
    def root(self, **kwargs):
        """
        Root endpoint has no other function than to point end users to documentation.

        https://docs.blockfrost.io/#tag/Health/paths/~1/get
        :param return_type: Optional. "object", "json" or "pandas". Default: "object".
        :type return_type: str
        :returns RootResponse object.
        :rtype RootResponse
        :raises ApiError: If API fails
        :raises Exception: If the API response is somehow malformed.
        """
        return requests.get(
            url=f"{self.url}/",
            headers=self.authentication_header
        )

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
    from .cardano.accounts import \
        accounts, \
        account_rewards, \
        account_history, \
        account_delegations, \
        account_registrations, \
        account_withdrawals, \
        account_mirs, \
        account_addresses, \
        account_addresses_assets
    from .cardano.addresses import \
        address, \
        address_total, \
        address_utxos, \
        address_utxos_asset, \
        address_transactions
    from .cardano.assets import \
        assets, \
        asset, \
        asset_history, \
        asset_transactions, \
        asset_addresses, \
        assets_policy
    from .cardano.blocks import \
        block_latest, \
        block_latest_transactions, \
        block, \
        block_slot, \
        block_epoch_slot, \
        blocks_next, \
        blocks_previous, \
        block_transactions
    from .cardano.epochs import \
        epoch_latest, \
        epoch_latest_parameters, \
        epoch, \
        epochs_next, \
        epochs_previous, \
        epoch_stakes, \
        epoch_pool_stakes, \
        epoch_blocks, \
        epoch_pool_blocks
    from .cardano.ledger import \
        genesis
    from .cardano.metadata import \
        metadata_labels, \
        metadata_label_json, \
        metadata_label_cbor
    from .cardano.network import \
        network
    from .cardano.pools import \
        pools, \
        pools_retired, \
        pools_retiring, \
        pool, \
        pool_history, \
        pool_metadata, \
        pool_relays, \
        pool_delegators, \
        pool_blocks, \
        pool_updates
    from .cardano.transactions import \
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
        transaction_submit, \
        transaction_redeemers
    from .cardano.scripts import \
        scripts, \
        script, \
        script_json, \
        script_cbor, \
        script_redeemers, \
        script_datum
