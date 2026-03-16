import os
import requests
from dataclasses import dataclass

from blockfrost.config import DEFAULT_API_VERSION

from ..utils import Api, ApiUrls, request_wrapper


class BlockFrostApi(Api):

    def __init__(self, project_id: str = None, base_url: str = None, api_version: str = None):
        super().__init__(
            project_id=project_id,
            base_url=base_url if base_url else os.environ.get(
                'BLOCKFROST_API_URL', default=ApiUrls.mainnet.value),
            # if custom base_url is specified then also use specified api_version
            api_version=api_version if base_url else os.environ.get('BLOCKFROST_API_VERSION',
                                                                    default=DEFAULT_API_VERSION))

    @request_wrapper
    def root(self, **kwargs):
        """
        Root endpoint has no other function than to point end users to documentation.

        https://docs.blockfrost.io/#tag/health/GET/
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
        account_addresses_assets, \
        account_addresses_total, \
        account_utxos, \
        account_transactions
    from .cardano.addresses import \
        address, \
        address_extended, \
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
        block_latest_transactions_cbor, \
        block, \
        block_slot, \
        block_epoch_slot, \
        blocks_next, \
        blocks_previous, \
        block_transactions, \
        block_transactions_cbor, \
        blocks_addresses
    from .cardano.epochs import \
        epoch_latest, \
        epoch_latest_parameters, \
        epoch, \
        epochs_next, \
        epochs_previous, \
        epoch_stakes, \
        epoch_pool_stakes, \
        epoch_blocks, \
        epoch_pool_blocks, \
        epoch_protocol_parameters
    from .cardano.ledger import \
        genesis
    from .cardano.mempool import \
        mempool, \
        mempool_address, \
        mempool_tx
    from .cardano.metadata import \
        metadata_labels, \
        metadata_label_json, \
        metadata_label_cbor
    from .cardano.network import \
        network, \
        network_eras
    from .cardano.pools import \
        pools, \
        pools_extended, \
        pools_retired, \
        pools_retiring, \
        pool, \
        pool_history, \
        pool_metadata, \
        pool_relays, \
        pool_delegators, \
        pool_blocks, \
        pool_updates, \
        pool_votes
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
        transaction_submit_cbor, \
        transaction_redeemers, \
        transaction_required_signers, \
        transaction_cbor, \
        transaction_evaluate, \
        transaction_evaluate_cbor, \
        transaction_evaluate_utxos
    from .cardano.scripts import \
        scripts, \
        script, \
        script_json, \
        script_cbor, \
        script_redeemers, \
        script_datum, \
        script_datum_cbor
    from .cardano.governance import \
        governance_dreps, \
        governance_drep, \
        governance_drep_delegators, \
        governance_drep_metadata, \
        governance_drep_updates, \
        governance_drep_votes, \
        governance_proposals, \
        governance_proposal, \
        governance_proposal_parameters, \
        governance_proposal_withdrawals, \
        governance_proposal_votes, \
        governance_proposal_metadata, \
        governance_proposal_by_gov_action_id, \
        governance_proposal_parameters_by_gov_action_id, \
        governance_proposal_withdrawals_by_gov_action_id, \
        governance_proposal_votes_by_gov_action_id, \
        governance_proposal_metadata_by_gov_action_id
    from .cardano.utils import \
        utils_addresses_xpub
