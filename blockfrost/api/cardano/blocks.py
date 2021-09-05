import requests
from dataclasses import dataclass
from blockfrost.utils import object_request_wrapper, object_list_request_wrapper


@dataclass
class Block:
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


@object_request_wrapper(Block)
def block_latest(self):
    """
    Return the latest block available to the backends, also known as the tip of the blockchain.

    https://docs.blockfrost.io/#tag/Cardano-Blocks/paths/~1blocks~1latest/get
    """
    return requests.get(
        url=f"{self.url}/blocks/latest",
        headers=self.default_headers
    )


@object_list_request_wrapper(str)
def block_latest_transactions(self):
    """
    Return the transactions within the latest block.

    https://docs.blockfrost.io/#tag/Cardano-Blocks/paths/~1blocks~1latest~1txs/get
    """
    return requests.get(
        url=f"{self.url}/blocks/latest/txs",
        headers=self.default_headers
    )


@object_request_wrapper(Block)
def block(self, hash_or_number: str):
    """
    Return the content of a requested block.

    https://docs.blockfrost.io/#tag/Cardano-Blocks/paths/~1blocks~1{hash_or_number}/get
    """
    return requests.get(
        url=f"{self.url}/blocks/{hash_or_number}",
        headers=self.default_headers
    )


@object_request_wrapper(Block)
def block_slot(self, slot_number: int):
    """
    Return the content of a requested block for a specific slot.

    https://docs.blockfrost.io/#tag/Cardano-Blocks/paths/~1blocks~1slot~1{slot_number}/get
    """
    return requests.get(
        url=f"{self.url}/blocks/slot/{slot_number}",
        headers=self.default_headers
    )


@object_request_wrapper(Block)
def block_epoch_slot(self, epoch_number: int, slot_number: int):
    """
    Return the content of a requested block for a specific slot in an epoch.

    https://docs.blockfrost.io/#tag/Cardano-Blocks/paths/~1blocks~1epoch~1{epoch_number}~1slot~1{slot_number}/get
    """
    return requests.get(
        url=f"{self.url}/blocks/epoch/{epoch_number}/slot/{slot_number}",
        headers=self.default_headers
    )


@object_list_request_wrapper(Block)
def blocks_next(self, hash_or_number: str):
    """
    Return the list of blocks following a specific block.

    https://docs.blockfrost.io/#tag/Cardano-Blocks/paths/~1blocks~1{hash_or_number}~1next/get
    """
    return requests.get(
        url=f"{self.url}/blocks/{hash_or_number}/next",
        headers=self.default_headers
    )


@object_list_request_wrapper(Block)
def blocks_previous(self, hash_or_number: str):
    """
    Return the list of blocks preceding a specific block.

    https://docs.blockfrost.io/#tag/Cardano-Blocks/paths/~1blocks~1{hash_or_number}~1previous/get
    """
    return requests.get(
        url=f"{self.url}/blocks/{hash_or_number}/previous",
        headers=self.default_headers
    )

@object_list_request_wrapper(str)
def block_transactions(self, hash_or_number: str):
    """
    Return the transactions within the block.

    https://docs.blockfrost.io/#tag/Cardano-Blocks/paths/~1blocks~1{hash_or_number}~1txs/get
    """
    return requests.get(
        url=f"{self.url}/blocks/{hash_or_number}/txs",
        headers=self.default_headers
    )