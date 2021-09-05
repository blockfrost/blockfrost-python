import requests
from dataclasses import dataclass
from blockfrost.utils import object_request_wrapper, object_list_request_wrapper


@dataclass
class Assets:
    asset: str
    quantity: str


@object_list_request_wrapper(Assets)
def assets(self):
    """
    List of assets.

    https://docs.blockfrost.io/#tag/Cardano-Assets/paths/~1assets/get
    """
    return requests.get(
        url=f"{self.url}/assets",
        headers=self.default_headers
    )


@dataclass
class Asset:
    @dataclass
    class OnchainMetadata:
        name: str
        image: str
        additional_properties: dict

        def __init__(self, name: str, image: str, **kwargs) -> None:
            self.name = name
            self.image = image
            self.additional_properties = kwargs

    @dataclass
    class Metadata:
        name: str
        description: str
        ticker: str
        url: str
        logo: str
        decimals: int

    asset: str
    policy_id: str
    asset_name: str
    fingerprint: str
    quantity: str
    initial_mint_tx_hash: str
    mint_or_burn_count: int
    onchain_metadata: OnchainMetadata
    metadata: Metadata

    def __init__(self, asset: str, policy_id: str, asset_name: str, fingerprint: str, quantity: str,
                 initial_mint_tx_hash: str, mint_or_burn_count: int, onchain_metadata: OnchainMetadata,
                 metadata: Metadata = None) -> None:
        self.asset = asset
        self.policy_id = policy_id
        self.asset_name = asset_name
        self.fingerprint = fingerprint
        self.quantity = quantity
        self.initial_mint_tx_hash = initial_mint_tx_hash
        self.mint_or_burn_count = mint_or_burn_count
        self.onchain_metadata = self.OnchainMetadata(**onchain_metadata) if onchain_metadata is not None else None
        self.metadata = self.Metadata(**metadata) if metadata is not None else None


@object_request_wrapper(Asset)
def asset(self, asset: str):
    """
    Information about a specific asset

    https://docs.blockfrost.io/#tag/Cardano-Assets/paths/~1assets~1{asset}/get
    """
    return requests.get(
        url=f"{self.url}/assets/{asset}",
        headers=self.default_headers
    )


@dataclass
class AssetHistory:
    tx_hash: str
    action: str
    amount: str


@object_request_wrapper(AssetHistory)
def asset_history(self, asset: str):
    """
    History of a specific asset

    https://docs.blockfrost.io/#tag/Cardano-Assets/paths/~1assets~1{asset}~1history/get
    """
    return requests.get(
        url=f"{self.url}/assets/{asset}/history",
        headers=self.default_headers
    )


@dataclass
class AssetTransactions:
    tx_hash: str
    tx_index: int
    block_height: int


@object_request_wrapper(AssetTransactions)
def asset_transactions(self, asset: str):
    """
    List of a specific asset transactions

    https://docs.blockfrost.io/#tag/Cardano-Assets/paths/~1assets~1{asset}~1transactions/get
    """
    return requests.get(
        url=f"{self.url}/assets/{asset}/transactions",
        headers=self.default_headers
    )


@dataclass
class AssetAddresses:
    address: str
    quantity: str


@object_request_wrapper(AssetAddresses)
def asset_addresses(self, asset: str):
    """
    List of a addresses containing a specific asset

    https://docs.blockfrost.io/#tag/Cardano-Assets/paths/~1assets~1{asset}~1addresses/get
    """
    return requests.get(
        url=f"{self.url}/assets/{asset}/addresses",
        headers=self.default_headers
    )


@dataclass
class PolicyAsset:
    address: str
    quantity: str


@object_request_wrapper(PolicyAsset)
def policy_assets(self, policy_id: str):
    """
    List of asset minted under a specific policy

    https://docs.blockfrost.io/#tag/Cardano-Assets/paths/~1assets~1policy~1{policy_id}/get
    """
    return requests.get(
        url=f"{self.url}/assets/{policy_id}",
        headers=self.default_headers
    )
