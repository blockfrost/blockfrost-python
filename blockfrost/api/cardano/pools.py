import requests
from dataclasses import dataclass
from blockfrost.utils import object_request_wrapper, object_list_request_wrapper


@object_list_request_wrapper(str)
def pools(self):
    """
    List of registered stake pools.

    https://docs.blockfrost.io/#tag/Cardano-Pools/paths/~1pools/get
    """
    return requests.get(
        url=f"{self.url}/pools",
        headers=self.default_headers
    )


@dataclass
class PoolList:
    pool_id: str
    epoch: str


@object_list_request_wrapper(PoolList)
def pools_retired(self):
    """
    List of already retired pools.

    https://docs.blockfrost.io/#tag/Cardano-Pools/paths/~1pools~1retired/get
    """
    return requests.get(
        url=f"{self.url}/pools/retired",
        headers=self.default_headers
    )


@object_list_request_wrapper(PoolList)
def pools_retiring(self):
    """
    List of stake pools retiring in the upcoming epochs

    https://docs.blockfrost.io/#tag/Cardano-Pools/paths/~1pools~1retiring/get
    """
    return requests.get(
        url=f"{self.url}/pools/retiring",
        headers=self.default_headers
    )


@dataclass
class Pool:
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


@object_request_wrapper(Pool)
def pool(self, pool_id: str):
    """
    Pool information.

    https://docs.blockfrost.io/#tag/Cardano-Pools/paths/~1pools~1{pool_id}/get
    """
    return requests.get(
        url=f"{self.url}/pools/{pool_id}",
        headers=self.default_headers
    )


@dataclass
class PoolHistory:
    epoch: int
    blocks: int
    active_stake: str
    active_size: float
    delegators_count: int
    rewards: str
    fees: str


@object_list_request_wrapper(PoolHistory)
def pool_history(self, pool_id: str):
    """
    History of stake pool parameters over epochs.

    https://docs.blockfrost.io/#tag/Cardano-Pools/paths/~1pools~1{pool_id}~1history/get
    """
    return requests.get(
        url=f"{self.url}/pools/{pool_id}/history",
        headers=self.default_headers
    )


@dataclass
class PoolMetadata:
    pool_id: str
    hex: str
    url: str
    hash: str
    ticker: str
    name: str
    description: str
    homepage: str


@object_request_wrapper(PoolMetadata)
def pool_metadata(self, pool_id: str):
    """
    Stake pool registration metadata.

    https://docs.blockfrost.io/#tag/Cardano-Pools/paths/~1pools~1{pool_id}~1metadata/get
    """
    return requests.get(
        url=f"{self.url}/pools/{pool_id}/metadata",
        headers=self.default_headers
    )


@dataclass
class PoolRelay:
    ipv4: str
    ipv6: str
    dns: str
    dns_srv: str
    port: int


@object_list_request_wrapper(PoolRelay)
def pool_relays(self, pool_id: str):
    """
    Relays of a stake pool.

    https://docs.blockfrost.io/#tag/Cardano-Pools/paths/~1pools~1{pool_id}~1relays/get
    """
    return requests.get(
        url=f"{self.url}/pools/{pool_id}/relays",
        headers=self.default_headers
    )


@dataclass
class PoolDelegators:
    address: str
    live_stake: str


@object_list_request_wrapper(PoolDelegators)
def pool_delegators(self, pool_id: str):
    """
    List of current stake pools delegators.

    https://docs.blockfrost.io/#tag/Cardano-Pools/paths/~1pools~1{pool_id}~1delegators/get
    """
    return requests.get(
        url=f"{self.url}/pools/{pool_id}/delegators",
        headers=self.default_headers
    )


@object_list_request_wrapper(str)
def pool_blocks(self, pool_id: str):
    """
    List of stake pools blocks.

    https://docs.blockfrost.io/#tag/Cardano-Pools/paths/~1pools~1{pool_id}~1blocks/get
    """
    return requests.get(
        url=f"{self.url}/pools/{pool_id}/blocks",
        headers=self.default_headers
    )


@dataclass
class PoolUpdate:
    tx_hash: str
    cert_index: int
    action: str


@object_list_request_wrapper(PoolUpdate)
def pool_updates(self, pool_id: str):
    """
    List of certificate updates to the stake pool.

    https://docs.blockfrost.io/#tag/Cardano-Pools/paths/~1pools~1{pool_id}~1updates/get
    """
    return requests.get(
        url=f"{self.url}/pools/{pool_id}/updates",
        headers=self.default_headers
    )
