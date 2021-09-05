import requests
from dataclasses import dataclass
from blockfrost.utils import object_request_wrapper, object_list_request_wrapper


@dataclass
class AccountAddressesAsset:
    @dataclass
    class Amount:
        unit: str
        quantity: str

    address: str
    amount: [Amount]
    stake_address: str
    type: str

    def __init__(self, address: str, amount: [Amount], stake_address: str, type: str) -> None:
        self.address = address
        self.amount = [self.Amount(**o) for o in amount]
        self.stake_address = stake_address
        self.type = type


@object_request_wrapper(AccountAddressesAsset)
def address(self, address: str):
    """
    Obtain information about a specific address.

    https://docs.blockfrost.io/#tag/Cardano-Addresses/paths/~1addresses~1{address}/get
    """
    return requests.get(
        url=f"{self.url}/addresses/{address}",
        headers=self.default_headers
    )


@dataclass
class AccountAddressesTotal:
    @dataclass
    class Sum:
        unit: str
        quantity: str

    address: str
    received_sum: [Sum]
    sent_sum: [Sum]
    tx_count: int

    def __init__(self, address: str, received_sum: [Sum], sent_sum: [Sum], tx_count: int) -> None:
        self.address = address
        self.received_sum = [self.Sum(**o) for o in received_sum]
        self.sent_sum = [self.Sum(**o) for o in sent_sum]
        self.tx_count = tx_count


@object_request_wrapper(AccountAddressesTotal)
def address_total(self, address: str):
    """
    Obtain details about an address.

    https://docs.blockfrost.io/#tag/Cardano-Addresses/paths/~1addresses~1{address}~1total/get
    """
    return requests.get(
        url=f"{self.url}/addresses/{address}/total",
        headers=self.default_headers
    )


@dataclass
class AccountAddressesUTXOS:
    @dataclass
    class Amount:
        unit: str
        quantity: str

    tx_hash: str
    output_index: int
    amount: [Amount]
    block: str

    def __init__(self, tx_hash: str, output_index: int, amount: [Amount], block: str) -> None:
        self.tx_hash = tx_hash
        self.output_index = output_index
        self.amount = [self.Amount(**o) for o in amount]
        self.block = block


@object_list_request_wrapper(AccountAddressesUTXOS)
def address_utxos(self, address: str, **kwargs):
    """
    UTXOs of the address.

    https://docs.blockfrost.io/#tag/Cardano-Addresses/paths/~1addresses~1{address}~1utxos/get
    """
    return requests.get(
        url=f"{self.url}/addresses/{address}/utxos",
        params=self.query_parameters(kwargs),
        headers=self.default_headers
    )


@dataclass
class AccountAddressesTransaction:
    tx_hash: str
    tx_index: int
    block_height: int


@object_list_request_wrapper(AccountAddressesTransaction)
def address_transactions(self, address: str, from_block: str = None, to_block: str = None,
                         **kwargs):
    """
    Transactions on the address.

    from
    string
    Example: from=8929261
    The block number and optionally also index from which (inclusive) to start search for results, concatenated using colon. Has to be lower than or equal to to parameter.

    to
    string
    Example: to=9999269:10
    The block number and optionally also index where (inclusive) to end the search for results, concatenated using colon. Has to be higher than or equal to from parameter.

    https://docs.blockfrost.io/#tag/Cardano-Addresses/paths/~1addresses~1{address}~1transactions/get
    """
    return requests.get(
        url=f"{self.url}/addresses/{address}/transactions",
        params={
            'from': from_block,
            'to': to_block,
            **self.query_parameters(kwargs)
        },
        headers=self.default_headers
    )
