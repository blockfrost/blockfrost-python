import requests
from dataclasses import dataclass, field
from blockfrost.utils import object_request_wrapper, object_list_request_wrapper


@dataclass
class EpochResponse:
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


@object_request_wrapper(EpochResponse)
def epoch_latest(self, **kwargs):
    """
    Return the information about the latest, therefore current, epoch.

    https://docs.blockfrost.io/#tag/Cardano-Epochs/paths/~1epochs~1latest/get

    :param return_type: Optional. "object", "json" or "pandas". Default: "object".
    :type return_type: str
    :returns EpochResponse object.
    :rtype EpochResponse
    :raises ApiError: If API fails
    :raises Exception: If the API response is somehow malformed.
    """
    return requests.get(
        url=f"{self.url}/epochs/latest",
        headers=self.default_headers
    )


@dataclass
class EpochParameterResponse:
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
    price_mem: float
    price_step: float
    max_tx_ex_mem: str
    max_tx_ex_steps: str
    max_block_ex_mem: str
    max_block_ex_steps: str
    max_val_size: str
    collateral_percent: int
    max_collateral_inputs: int
    coins_per_utxo_word: str


@object_request_wrapper(EpochParameterResponse)
def epoch_latest_parameters(self, **kwargs):
    """
    Return the protocol parameters for the latest epoch.

    https://docs.blockfrost.io/#tag/Cardano-Epochs/paths/~1epochs~1latest~1parameters/get

    :param return_type: Optional. "object", "json" or "pandas". Default: "object".
    :type return_type: str
    :returns EpochParameterResponse object.
    :rtype EpochParameterResponse
    :raises ApiError: If API fails
    :raises Exception: If the API response is somehow malformed.
    """
    return requests.get(
        url=f"{self.url}/epochs/latest/parameters",
        headers=self.default_headers
    )


@object_request_wrapper(EpochResponse)
def epoch(self, number: int, **kwargs):
    """
    Return the content of the requested epoch.

    https://docs.blockfrost.io/#tag/Cardano-Epochs/paths/~1epochs~1{number}/get

    :param number: Number of the epoch.
    :type number: int
    :param return_type: Optional. "object", "json" or "pandas". Default: "object".
    :type return_type: str
    :returns EpochResponse object.
    :rtype EpochResponse
    :raises ApiError: If API fails
    :raises Exception: If the API response is somehow malformed.
    """
    return requests.get(
        url=f"{self.url}/epochs/{number}",
        headers=self.default_headers
    )


@object_list_request_wrapper(EpochResponse)
def epochs_next(self, number: int, **kwargs):
    """
    Return the list of epochs following a specific epoch.

    https://docs.blockfrost.io/#tag/Cardano-Epochs/paths/~1epochs~1{number}~1next/get

    :param number: Number of the epoch.
    :type number: int
    :param return_type: Optional. "object", "json" or "pandas". Default: "object".
    :type return_type: str
    :param count: Optional. Default: 1. The number of results displayed on one page.
    :type count: int
    :param page: Optional. The page number for listing the results.
    :type page: int
    :returns A list of EpochResponse objects.
    :rtype [EpochResponse]
    :raises ApiError: If API fails
    :raises Exception: If the API response is somehow malformed.
    """
    return requests.get(
        url=f"{self.url}/epochs/{number}/next",
        params=self.query_parameters(kwargs),
        headers=self.default_headers
    )


@object_list_request_wrapper(EpochResponse)
def epochs_previous(self, number: int, **kwargs):
    """
    Return the list of epochs preceding a specific epoch.

    https://docs.blockfrost.io/#tag/Cardano-Epochs/paths/~1epochs~1{number}~1previous/get

    :param number: Number of the epoch.
    :type number: int
    :param return_type: Optional. "object", "json" or "pandas". Default: "object".
    :type return_type: str
    :param count: Optional. Default: 1. The number of results displayed on one page.
    :type count: int
    :param page: Optional. The page number for listing the results.
    :type page: int
    :returns A list of EpochResponse objects.
    :rtype [EpochResponse]
    :raises ApiError: If API fails
    :raises Exception: If the API response is somehow malformed.
    """
    return requests.get(
        url=f"{self.url}/epochs/{number}/previous",
        params=self.query_parameters(kwargs),
        headers=self.default_headers
    )


@dataclass
class EpochStakeResponse:
    stake_address: str
    pool_id: str
    amount: str


@object_list_request_wrapper(EpochStakeResponse)
def epoch_stakes(self, number: int, **kwargs):
    """
    Return the active stake distribution for the specified epoch.

    https://docs.blockfrost.io/#tag/Cardano-Epochs/paths/~1epochs~1{number}~1stakes/get

    :param number: Number of the epoch.
    :type number: int
    :param return_type: Optional. "object", "json" or "pandas". Default: "object".
    :type return_type: str
    :param count: Optional. Default: 1. The number of results displayed on one page.
    :type count: int
    :param page: Optional. The page number for listing the results.
    :type page: int
    :returns A list of EpochStakeResponse objects.
    :rtype [EpochStakeResponse]
    :raises ApiError: If API fails
    :raises Exception: If the API response is somehow malformed.
    """
    return requests.get(
        url=f"{self.url}/epochs/{number}/stakes",
        params=self.query_parameters(kwargs),
        headers=self.default_headers
    )


@dataclass
class EpochStakePoolResponse:
    stake_address: str
    amount: str


@object_list_request_wrapper(EpochStakePoolResponse)
def epoch_pool_stakes(self, number: int, pool_id: str, **kwargs):
    """
    Return the active stake distribution for the epoch specified by stake pool.

    https://docs.blockfrost.io/#tag/Cardano-Epochs/paths/~1epochs~1{number}~1stakes~1{pool_id}/get

    :param number: Number of the epoch.
    :type number: int
    :param pool_id: Stake pool ID to filter.
    :type pool_id: int
    :param return_type: Optional. "object", "json" or "pandas". Default: "object".
    :type return_type: str
    :param count: Optional. Default: 1. The number of results displayed on one page.
    :type count: int
    :param page: Optional. The page number for listing the results.
    :type page: int
    :returns A list of EpochStakePoolResponse objects.
    :rtype [EpochStakePoolResponse]
    :raises ApiError: If API fails
    :raises Exception: If the API response is somehow malformed.
    """
    return requests.get(
        url=f"{self.url}/epochs/{number}/stakes/{pool_id}",
        params=self.query_parameters(kwargs),
        headers=self.default_headers
    )


@object_list_request_wrapper()
def epoch_blocks(self, number: int, **kwargs):
    """
    Return the blocks minted for the epoch specified.

    https://docs.blockfrost.io/#tag/Cardano-Epochs/paths/~1epochs~1{number}~1blocks/get

    :param number: Number of the epoch.
    :type number: int
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
        url=f"{self.url}/epochs/{number}/blocks",
        params=self.query_parameters(kwargs),
        headers=self.default_headers
    )


@object_list_request_wrapper()
def epoch_pool_blocks(self, number: int, pool_id: str, **kwargs):
    """
    Return the block minted for the epoch specified by stake pool.

    https://docs.blockfrost.io/#tag/Cardano-Epochs/paths/~1epochs~1{number}~1blocks~1{pool_id}/get

    :param number: Number of the epoch.
    :type number: int
    :param pool_id: Stake pool ID to filter.
    :type pool_id: int
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
        url=f"{self.url}/epochs/{number}/stakes/{pool_id}/blocks",
        params=self.query_parameters(kwargs),
        headers=self.default_headers
    )


@object_request_wrapper(EpochParameterResponse)
def epoch_latest_parameters(self, number: int, **kwargs):
    """
    Return the protocol parameters for the epoch specified.

    https://docs.blockfrost.io/#tag/Cardano-Epochs/paths/~1epochs~1{number}~1parameters/get

    :param number: Number of the epoch.
    :type number: int
    :param return_type: Optional. "object", "json" or "pandas". Default: "object".
    :type return_type: str
    :returns EpochParameterResponse object.
    :rtype EpochParameterResponse
    :raises ApiError: If API fails
    :raises Exception: If the API response is somehow malformed.
    """
    return requests.get(
        url=f"{self.url}/epochs/{number}/parameters",
        headers=self.default_headers
    )
