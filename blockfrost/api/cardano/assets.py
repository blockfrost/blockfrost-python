import requests
from dataclasses import dataclass
from blockfrost.utils import object_request_wrapper, object_list_request_wrapper


@dataclass
class AssetsResponse:
    asset: str
    quantity: str


@object_list_request_wrapper(AssetsResponse)
def assets(self, **kwargs):
    """
    List of assets.

    https://docs.blockfrost.io/#tag/Cardano-Assets/paths/~1assets/get

    :param return_type: Optional. "object", "json" or "pandas". Default: "object".
    :type return_type: str
    :param gather_pages: Optional. Default: 100. Will collect all pages into one return
    :type gather_pages: bool
    :param count: Optional. Default: 1. The number of results displayed on one page.
    :type count: int
    :param page: Optional. The page number for listing the results.
    :type page: int
    :param order: Optional. "asc" or "desc". Default: "asc".
    :type order: str
    :returns A list of AssetResponse objects.
    :rtype [AssetResponse]
    :raises ApiError: If API fails
    :raises Exception: If the API response is somehow malformed.
    """
    return requests.get(
        url=f"{self.url}/assets",
        params=self.query_parameters(kwargs),
        headers=self.default_headers
    )


@dataclass
class AssetResponse:
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


@object_request_wrapper(AssetResponse)
def asset(self, asset: str, **kwargs):
    """
    Information about a specific asset

    https://docs.blockfrost.io/#tag/Cardano-Assets/paths/~1assets~1{asset}/get

    :param asset: Concatenation of the policy_id and hex-encoded asset_name.
    :type asset: str
    :param return_type: Optional. "object", "json" or "pandas". Default: "object".
    :type return_type: str
    :returns AssetResponse object.
    :rtype AssetResponse
    :raises ApiError: If API fails
    :raises Exception: If the API response is somehow malformed.
    """
    return requests.get(
        url=f"{self.url}/assets/{asset}",
        headers=self.default_headers
    )


@dataclass
class AssetHistoryResponse:
    tx_hash: str
    action: str
    amount: str


@object_list_request_wrapper(AssetHistoryResponse)
def asset_history(self, asset: str, **kwargs):
    """
    History of a specific asset

    https://docs.blockfrost.io/#tag/Cardano-Assets/paths/~1assets~1{asset}~1history/get

    :param asset: Concatenation of the policy_id and hex-encoded asset_name.
    :type asset: str
    :param return_type: Optional. "object", "json" or "pandas". Default: "object".
    :type return_type: str
    :param gather_pages: Optional. Default: 100. Will collect all pages into one return
    :type gather_pages: bool
    :param count: Optional. Default: 1. The number of results displayed on one page.
    :type count: int
    :param page: Optional. The page number for listing the results.
    :type page: int
    :param order: Optional. "asc" or "desc". Default: "asc".
    :type order: str
    :returns A list of AssetHistoryResponse objects.
    :rtype [AssetHistoryResponse]
    :raises ApiError: If API fails
    :raises Exception: If the API response is somehow malformed.
    """
    return requests.get(
        url=f"{self.url}/assets/{asset}/history",
        params=self.query_parameters(kwargs),
        headers=self.default_headers
    )


@dataclass
class AssetTransactionResponse:
    tx_hash: str
    tx_index: int
    block_height: int


@object_list_request_wrapper(AssetTransactionResponse)
def asset_transactions(self, asset: str, **kwargs):
    """
    List of a specific asset transactions

    https://docs.blockfrost.io/#tag/Cardano-Assets/paths/~1assets~1{asset}~1transactions/get

    :param asset: Concatenation of the policy_id and hex-encoded asset_name.
    :type asset: str
    :param return_type: Optional. "object", "json" or "pandas". Default: "object".
    :type return_type: str
    :param gather_pages: Optional. Default: 100. Will collect all pages into one return
    :type gather_pages: bool
    :param count: Optional. Default: 1. The number of results displayed on one page.
    :type count: int
    :param page: Optional. The page number for listing the results.
    :type page: int
    :param order: Optional. "asc" or "desc". Default: "asc".
    :type order: str
    :returns A list of AssetTransactionResponse objects.
    :rtype [AssetTransactionResponse]
    :raises ApiError: If API fails
    :raises Exception: If the API response is somehow malformed.
    """
    return requests.get(
        url=f"{self.url}/assets/{asset}/transactions",
        params=self.query_parameters(kwargs),
        headers=self.default_headers
    )


@dataclass
class AssetAddressResponse:
    address: str
    quantity: str


@object_list_request_wrapper(AssetAddressResponse)
def asset_addresses(self, asset: str, **kwargs):
    """
    List of a addresses containing a specific asset

    https://docs.blockfrost.io/#tag/Cardano-Assets/paths/~1assets~1{asset}~1addresses/get

    :param asset: Concatenation of the policy_id and hex-encoded asset_name.
    :type asset: str
    :param return_type: Optional. "object", "json" or "pandas". Default: "object".
    :type return_type: str
    :param gather_pages: Optional. Default: 100. Will collect all pages into one return
    :type gather_pages: bool
    :param count: Optional. Default: 1. The number of results displayed on one page.
    :type count: int
    :param page: Optional. The page number for listing the results.
    :type page: int
    :param order: Optional. "asc" or "desc". Default: "asc".
    :type order: str
    :returns A list of AssetAddressResponse objects.
    :rtype [AssetAddressResponse]
    :raises ApiError: If API fails
    :raises Exception: If the API response is somehow malformed.
    """
    return requests.get(
        url=f"{self.url}/assets/{asset}/addresses",
        params=self.query_parameters(kwargs),
        headers=self.default_headers
    )


@dataclass
class AssetPolicyResponse:
    asset: str
    quantity: str


@object_list_request_wrapper(AssetPolicyResponse)
def assets_policy(self, policy_id: str, **kwargs):
    """
    List of asset minted under a specific policy

    https://docs.blockfrost.io/#tag/Cardano-Assets/paths/~1assets~1policy~1{policy_id}/get

    :param policy_id: Specific policy_id.
    :type policy_id: str
    :param return_type: Optional. "object", "json" or "pandas". Default: "object".
    :type return_type: str
    :param gather_pages: Optional. Default: 100. Will collect all pages into one return
    :type gather_pages: bool
    :param count: Optional. Default: 1. The number of results displayed on one page.
    :type count: int
    :param page: Optional. The page number for listing the results.
    :type page: int
    :param order: Optional. "asc" or "desc". Default: "asc".
    :type order: str
    :returns A list of PolicyAssetResponse objects.
    :rtype [PolicyAssetResponse]
    :raises ApiError: If API fails
    :raises Exception: If the API response is somehow malformed.
    """
    return requests.get(
        url=f"{self.url}/assets/policy/{policy_id}",
        params=self.query_parameters(kwargs),
        headers=self.default_headers
    )
