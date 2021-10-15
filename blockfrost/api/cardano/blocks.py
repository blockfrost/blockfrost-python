import requests
from dataclasses import dataclass
from blockfrost.utils import object_request_wrapper, object_list_request_wrapper


@dataclass
class BlockResponse:
    time: int
    height: int
    hash: str
    slot: int
    epoch: int
    epoch_slot: int
    slot_leader: str
    size: int
    tx_count: int
    output: str
    fees: str
    block_vrf: str
    previous_block: str
    next_block: str
    confirmations: int


@object_request_wrapper(BlockResponse)
def block_latest(self, **kwargs):
    """
    Return the latest block available to the backends, also known as the tip of the blockchain.

    https://docs.blockfrost.io/#tag/Cardano-Blocks/paths/~1blocks~1latest/get

    :param return_type: Optional. "object", "json" or "pandas". Default: "object".
    :type return_type: str
    :returns BlockResponse object.
    :rtype BlockResponse
    :raises ApiError: If API fails
    :raises Exception: If the API response is somehow malformed.
    """
    return requests.get(
        url=f"{self.url}/blocks/latest",
        headers=self.default_headers
    )


@object_list_request_wrapper()
def block_latest_transactions(self, **kwargs):
    """
    Return the transactions within the latest block.

    https://docs.blockfrost.io/#tag/Cardano-Blocks/paths/~1blocks~1latest~1txs/get

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
        url=f"{self.url}/blocks/latest/txs",
        params=self.query_parameters(kwargs),
        headers=self.default_headers
    )


@object_request_wrapper(BlockResponse)
def block(self, hash_or_number: str, **kwargs):
    """
    Return the content of a requested block.

    https://docs.blockfrost.io/#tag/Cardano-Blocks/paths/~1blocks~1{hash_or_number}/get

    :param hash_or_number: Hash or number of the requested block.
    :type hash_or_number: str
    :param return_type: Optional. "object", "json" or "pandas". Default: "object".
    :type return_type: str
    :returns BlockResponse object.
    :rtype BlockResponse
    :raises ApiError: If API fails
    :raises Exception: If the API response is somehow malformed.
    """
    return requests.get(
        url=f"{self.url}/blocks/{hash_or_number}",
        headers=self.default_headers
    )


@object_request_wrapper(BlockResponse)
def block_slot(self, slot_number: int, **kwargs):
    """
    Return the content of a requested block for a specific slot.

    https://docs.blockfrost.io/#tag/Cardano-Blocks/paths/~1blocks~1slot~1{slot_number}/get

    :param slot_number: Slot position for requested block.
    :type slot_number: int
    :param return_type: Optional. "object", "json" or "pandas". Default: "object".
    :type return_type: str
    :returns BlockResponse object.
    :rtype BlockResponse
    :raises ApiError: If API fails
    :raises Exception: If the API response is somehow malformed.
    """
    return requests.get(
        url=f"{self.url}/blocks/slot/{slot_number}",
        headers=self.default_headers
    )


@object_request_wrapper(BlockResponse)
def block_epoch_slot(self, epoch_number: int, slot_number: int, **kwargs):
    """
    Return the content of a requested block for a specific slot in an epoch.

    https://docs.blockfrost.io/#tag/Cardano-Blocks/paths/~1blocks~1epoch~1{epoch_number}~1slot~1{slot_number}/get

    :param epoch_number: Epoch for specific epoch slot.
    :type epoch_number: int
    :param slot_number: Slot position for requested block.
    :type slot_number: int
    :param return_type: Optional. "object", "json" or "pandas". Default: "object".
    :type return_type: str
    :returns BlockResponse object.
    :rtype BlockResponse
    :raises ApiError: If API fails
    :raises Exception: If the API response is somehow malformed.
    """
    return requests.get(
        url=f"{self.url}/blocks/epoch/{epoch_number}/slot/{slot_number}",
        headers=self.default_headers
    )


@object_list_request_wrapper(BlockResponse)
def blocks_next(self, hash_or_number: str, **kwargs):
    """
    Return the list of blocks following a specific block.

    https://docs.blockfrost.io/#tag/Cardano-Blocks/paths/~1blocks~1{hash_or_number}~1next/get

    :param hash_or_number: Hash or number of the requested block.
    :type hash_or_number: str
    :param return_type: Optional. "object", "json" or "pandas". Default: "object".
    :type return_type: str
    :param count: Optional. Default: 1. The number of results displayed on one page.
    :type count: int
    :param page: Optional. The page number for listing the results.
    :type page: int
    :returns A list of BlockResponse objects.
    :rtype [BlockResponse]
    :raises ApiError: If API fails
    :raises Exception: If the API response is somehow malformed.
    """
    return requests.get(
        url=f"{self.url}/blocks/{hash_or_number}/next",
        params=self.query_parameters(kwargs),
        headers=self.default_headers
    )


@object_list_request_wrapper(BlockResponse)
def blocks_previous(self, hash_or_number: str, **kwargs):
    """
    Return the list of blocks preceding a specific block.

    https://docs.blockfrost.io/#tag/Cardano-Blocks/paths/~1blocks~1{hash_or_number}~1previous/get

    :param hash_or_number: Hash or number of the requested block.
    :type hash_or_number: str
    :param return_type: Optional. "object", "json" or "pandas". Default: "object".
    :type return_type: str
    :param count: Optional. Default: 1. The number of results displayed on one page.
    :type count: int
    :param page: Optional. The page number for listing the results.
    :type page: int
    :returns A list of BlockResponse objects.
    :rtype [BlockResponse]
    :raises ApiError: If API fails
    :raises Exception: If the API response is somehow malformed.
    """
    return requests.get(
        url=f"{self.url}/blocks/{hash_or_number}/previous",
        params=self.query_parameters(kwargs),
        headers=self.default_headers
    )


@object_list_request_wrapper()
def block_transactions(self, hash_or_number: str, **kwargs):
    """
    Return the transactions within the block.

    https://docs.blockfrost.io/#tag/Cardano-Blocks/paths/~1blocks~1{hash_or_number}~1txs/get

    :param hash_or_number: Hash or number of the requested block.
    :type hash_or_number: str
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
        url=f"{self.url}/blocks/{hash_or_number}/txs",
        params=self.query_parameters(kwargs),
        headers=self.default_headers
    )
