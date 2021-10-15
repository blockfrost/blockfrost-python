import requests
from dataclasses import dataclass
from blockfrost.utils import object_request_wrapper, object_list_request_wrapper


@object_list_request_wrapper()
def pools(self, **kwargs):
    """
    List of registered stake pools.

    https://docs.blockfrost.io/#tag/Cardano-Pools/paths/~1pools/get

    :param gather_pages: Optional. Default: 100. Will collect all pages into one return
    :type gather_pages: bool
    :param count: Optional. Default: 1. The number of results displayed on one page.
    :type count: int
    :param page: Optional. The page number for listing the results.
    :type page: int
    :param order: Optional. "asc" or "desc". Default: "asc".
    :type order: str
    :returns A list of str objects.
    :rtype [str]
    :raises ApiError: If API fails
    :raises Exception: If the API response is somehow malformed.
    """
    return requests.get(
        url=f"{self.url}/pools",
        params=self.query_parameters(kwargs),
        headers=self.default_headers
    )


@dataclass
class PoolListResponse:
    pool_id: str
    epoch: str


@object_list_request_wrapper(PoolListResponse)
def pools_retired(self, **kwargs):
    """
    List of already retired pools.

    https://docs.blockfrost.io/#tag/Cardano-Pools/paths/~1pools~1retired/get

    :param gather_pages: Optional. Default: 100. Will collect all pages into one return
    :type gather_pages: bool
    :param count: Optional. Default: 1. The number of results displayed on one page.
    :type count: int
    :param page: Optional. The page number for listing the results.
    :type page: int
    :param order: Optional. "asc" or "desc". Default: "asc".
    :type order: str
    :returns A list of PoolListResponse objects.
    :rtype [PoolListResponse]
    :raises ApiError: If API fails
    :raises Exception: If the API response is somehow malformed.
    """
    return requests.get(
        url=f"{self.url}/pools/retired",
        params=self.query_parameters(kwargs),
        headers=self.default_headers
    )


@object_list_request_wrapper(PoolListResponse)
def pools_retiring(self, **kwargs):
    """
    List of stake pools retiring in the upcoming epochs

    https://docs.blockfrost.io/#tag/Cardano-Pools/paths/~1pools~1retiring/get

    :param gather_pages: Optional. Default: 100. Will collect all pages into one return
    :type gather_pages: bool
    :param count: Optional. Default: 1. The number of results displayed on one page.
    :type count: int
    :param page: Optional. The page number for listing the results.
    :type page: int
    :param order: Optional. "asc" or "desc". Default: "asc".
    :type order: str
    :returns A list of PoolListResponse objects.
    :rtype [PoolListResponse]
    :raises ApiError: If API fails
    :raises Exception: If the API response is somehow malformed.
    """
    return requests.get(
        url=f"{self.url}/pools/retiring",
        params=self.query_parameters(kwargs),
        headers=self.default_headers
    )


@dataclass
class PoolResponse:
    pool_id: str
    hex: str
    vrf_key: str
    blocks_minted: int
    live_stake: str
    live_size: float
    live_saturation: float
    live_delegators: float
    active_stake: str
    active_size: float
    declared_pledge: str
    live_pledge: str
    margin_cost: float
    fixed_cost: str
    reward_account: str
    owners: [str]
    registration: [str]
    retirement: [str]


@object_request_wrapper(PoolResponse)
def pool(self, pool_id: str, **kwargs):
    """
    Pool information.

    https://docs.blockfrost.io/#tag/Cardano-Pools/paths/~1pools~1{pool_id}/get

    :param pool_id: Bech32 or hexadecimal pool ID.
    :type pool_id: str
    :returns PoolResponse object.
    :rtype PoolResponse
    :raises ApiError: If API fails
    :raises Exception: If the API response is somehow malformed.
    """
    return requests.get(
        url=f"{self.url}/pools/{pool_id}",
        headers=self.default_headers
    )


@dataclass
class PoolHistoryResponse:
    epoch: int
    blocks: int
    active_stake: str
    active_size: float
    delegators_count: int
    rewards: str
    fees: str


@object_list_request_wrapper(PoolHistoryResponse)
def pool_history(self, pool_id: str, **kwargs):
    """
    History of stake pool parameters over epochs.

    https://docs.blockfrost.io/#tag/Cardano-Pools/paths/~1pools~1{pool_id}~1history/get

    :param pool_id: Bech32 or hexadecimal pool ID.
    :type pool_id: str
    :param gather_pages: Optional. Default: 100. Will collect all pages into one return
    :type gather_pages: bool
    :param count: Optional. Default: 1. The number of results displayed on one page.
    :type count: int
    :param page: Optional. The page number for listing the results.
    :type page: int
    :param order: Optional. "asc" or "desc". Default: "asc".
    :type order: str
    :returns A list of PoolHistoryResponse objects.
    :rtype [PoolHistoryResponse]
    :raises ApiError: If API fails
    :raises Exception: If the API response is somehow malformed.
    """
    return requests.get(
        url=f"{self.url}/pools/{pool_id}/history",
        params=self.query_parameters(kwargs),
        headers=self.default_headers
    )


@dataclass
class PoolMetadataResponse:
    pool_id: str
    hex: str
    url: str
    hash: str
    ticker: str
    name: str
    description: str
    homepage: str


@object_request_wrapper(PoolMetadataResponse)
def pool_metadata(self, pool_id: str, **kwargs):
    """
    Stake pool registration metadata.

    https://docs.blockfrost.io/#tag/Cardano-Pools/paths/~1pools~1{pool_id}~1metadata/get

    :param pool_id: Bech32 or hexadecimal pool ID.
    :type pool_id: str
    :returns PoolMetadataResponse object.
    :rtype PoolMetadataResponse
    :raises ApiError: If API fails
    :raises Exception: If the API response is somehow malformed.
    """
    return requests.get(
        url=f"{self.url}/pools/{pool_id}/metadata",
        headers=self.default_headers
    )


@dataclass
class PoolRelayResponse:
    ipv4: str
    ipv6: str
    dns: str
    dns_srv: str
    port: int


@object_list_request_wrapper(PoolRelayResponse)
def pool_relays(self, pool_id: str, **kwargs):
    """
    Relays of a stake pool.

    https://docs.blockfrost.io/#tag/Cardano-Pools/paths/~1pools~1{pool_id}~1relays/get

    :param pool_id: Bech32 or hexadecimal pool ID.
    :type pool_id: str
    :returns A list of PoolRelayResponse objects.
    :rtype [PoolRelayResponse]
    :raises ApiError: If API fails
    :raises Exception: If the API response is somehow malformed.
    """
    return requests.get(
        url=f"{self.url}/pools/{pool_id}/relays",
        headers=self.default_headers
    )


@dataclass
class PoolDelegatorResponse:
    address: str
    live_stake: str


@object_list_request_wrapper(PoolDelegatorResponse)
def pool_delegators(self, pool_id: str, **kwargs):
    """
    List of current stake pools delegators.

    https://docs.blockfrost.io/#tag/Cardano-Pools/paths/~1pools~1{pool_id}~1delegators/get

    :param pool_id: Bech32 or hexadecimal pool ID.
    :type pool_id: str
    :param gather_pages: Optional. Default: 100. Will collect all pages into one return
    :type gather_pages: bool
    :param count: Optional. Default: 1. The number of results displayed on one page.
    :type count: int
    :param page: Optional. The page number for listing the results.
    :type page: int
    :param order: Optional. "asc" or "desc". Default: "asc".
    :type order: str
    :returns A list of PoolDelegatorResponse objects.
    :rtype [PoolDelegatorResponse]
    :raises ApiError: If API fails
    :raises Exception: If the API response is somehow malformed.
    """
    return requests.get(
        url=f"{self.url}/pools/{pool_id}/delegators",
        params=self.query_parameters(kwargs),
        headers=self.default_headers
    )


@object_list_request_wrapper()
def pool_blocks(self, pool_id: str, **kwargs):
    """
    List of stake pools blocks.

    https://docs.blockfrost.io/#tag/Cardano-Pools/paths/~1pools~1{pool_id}~1blocks/get

    :param pool_id: Bech32 or hexadecimal pool ID.
    :type pool_id: str
    :param gather_pages: Optional. Default: 100. Will collect all pages into one return
    :type gather_pages: bool
    :param count: Optional. Default: 1. The number of results displayed on one page.
    :type count: int
    :param page: Optional. The page number for listing the results.
    :type page: int
    :param order: Optional. "asc" or "desc". Default: "asc".
    :type order: str
    :returns A list of str objects.
    :rtype [str]
    :raises ApiError: If API fails
    :raises Exception: If the API response is somehow malformed.
    """
    return requests.get(
        url=f"{self.url}/pools/{pool_id}/blocks",
        params=self.query_parameters(kwargs),
        headers=self.default_headers
    )


@dataclass
class PoolUpdateResponse:
    tx_hash: str
    cert_index: int
    action: str


@object_list_request_wrapper(PoolUpdateResponse)
def pool_updates(self, pool_id: str, **kwargs):
    """
    List of certificate updates to the stake pool.

    https://docs.blockfrost.io/#tag/Cardano-Pools/paths/~1pools~1{pool_id}~1updates/get

    :param pool_id: Bech32 or hexadecimal pool ID.
    :type pool_id: str
    :param gather_pages: Optional. Default: 100. Will collect all pages into one return
    :type gather_pages: bool
    :param count: Optional. Default: 1. The number of results displayed on one page.
    :type count: int
    :param page: Optional. The page number for listing the results.
    :type page: int
    :param order: Optional. "asc" or "desc". Default: "asc".
    :type order: str
    :returns A list of PoolUpdateResponse objects.
    :rtype [PoolUpdateResponse]
    :raises ApiError: If API fails
    :raises Exception: If the API response is somehow malformed.
    """
    return requests.get(
        url=f"{self.url}/pools/{pool_id}/updates",
        params=self.query_parameters(kwargs),
        headers=self.default_headers
    )
