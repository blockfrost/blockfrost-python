import requests
from dataclasses import dataclass
from blockfrost.utils import object_request_wrapper, object_list_request_wrapper


@dataclass
class Epoch:
    epoch: int
    start_time: int
    end_time: int
    first_block_time: int
    last_block_time: int
    block_count: int
    tx_count: int
    output: str
    fees: str
    active_stake: str


@object_request_wrapper(Epoch)
def epoch_latest(self):
    """
    Return the information about the latest, therefore current, epoch.

    https://docs.blockfrost.io/#tag/Cardano-Epochs/paths/~1epochs~1latest/get
    """
    return requests.get(
        url=f"{self.url}/epochs/latest",
        headers=self.default_headers
    )


@dataclass
class EpochParameters:
    epoch: int
    min_fee_a: int
    min_fee_b: int
    max_block_size: int
    max_tx_size: int
    max_block_header_size: int
    key_deposit: str
    pool_deposit: str
    e_max: int
    n_opt: int
    a0: float
    rho: float
    tau: float
    decentralisation_param: float
    extra_entropy: dict
    protocol_major_ver: int
    protocol_minor_ver: int
    min_utxo: str
    min_pool_cost: str
    nonce: str


@object_request_wrapper(EpochParameters)
def epoch_latest_parameters(self):
    """
    Return the protocol parameters for the latest epoch.

    https://docs.blockfrost.io/#tag/Cardano-Epochs/paths/~1epochs~1latest~1parameters/get
    """
    return requests.get(
        url=f"{self.url}/epochs/latest/parameters",
        headers=self.default_headers
    )


@object_request_wrapper(Epoch)
def epoch(self, number: int):
    """
    Return the content of the requested epoch.

    https://docs.blockfrost.io/#tag/Cardano-Epochs/paths/~1epochs~1{number}/get
    """
    return requests.get(
        url=f"{self.url}/epochs/{number}",
        headers=self.default_headers
    )


@object_list_request_wrapper(Epoch)
def epochs_next(self, number: int):
    """
    Return the list of epochs following a specific epoch.

    https://docs.blockfrost.io/#tag/Cardano-Epochs/paths/~1epochs~1{number}~1next/get
    """
    return requests.get(
        url=f"{self.url}/epochs/{number}/next",
        headers=self.default_headers
    )


@object_list_request_wrapper(Epoch)
def epochs_previous(self, number: int):
    """
    Return the list of epochs preceding a specific epoch.

    https://docs.blockfrost.io/#tag/Cardano-Epochs/paths/~1epochs~1{number}~1previous/get
    """
    return requests.get(
        url=f"{self.url}/epochs/{number}/previous",
        headers=self.default_headers
    )


@dataclass
class Stake:
    stake_address: str
    pool_id: str
    amount: str


@object_list_request_wrapper(Stake)
def epoch_stakes(self, number: int):
    """
    Return the active stake distribution for the specified epoch.

    https://docs.blockfrost.io/#tag/Cardano-Epochs/paths/~1epochs~1{number}~1stakes/get
    """
    return requests.get(
        url=f"{self.url}/epochs/{number}/stakes",
        headers=self.default_headers
    )


@dataclass
class StakeByPool:
    stake_address: str
    amount: str


@object_list_request_wrapper(StakeByPool)
def epoch_pool_stakes(self, number: int, pool_id: str):
    """
    Return the active stake distribution for the epoch specified by stake pool.

    https://docs.blockfrost.io/#tag/Cardano-Epochs/paths/~1epochs~1{number}~1stakes~1{pool_id}/get
    """
    return requests.get(
        url=f"{self.url}/epochs/{number}/stakes/{pool_id}",
        headers=self.default_headers
    )


@object_list_request_wrapper(str)
def epoch_blocks(self, number: int):
    """
    Return the blocks minted for the epoch specified.

    https://docs.blockfrost.io/#tag/Cardano-Epochs/paths/~1epochs~1{number}~1blocks/get
    """
    return requests.get(
        url=f"{self.url}/epochs/{number}/blocks",
        headers=self.default_headers
    )


@object_list_request_wrapper(str)
def epoch_pool_blocks(self, number: int, pool_id: str):
    """
    Return the block minted for the epoch specified by stake pool.

    https://docs.blockfrost.io/#tag/Cardano-Epochs/paths/~1epochs~1{number}~1blocks~1{pool_id}/get
    """
    return requests.get(
        url=f"{self.url}/epochs/{number}/stakes/{pool_id}/blocks",
        headers=self.default_headers
    )


@object_request_wrapper(EpochParameters)
def epoch_latest_parameters(self, number: int):
    """
    Return the protocol parameters for the epoch specified.

    https://docs.blockfrost.io/#tag/Cardano-Epochs/paths/~1epochs~1{number}~1parameters/get
    """
    return requests.get(
        url=f"{self.url}/epochs/{number}/parameters",
        headers=self.default_headers
    )
