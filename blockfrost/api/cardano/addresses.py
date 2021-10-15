import requests
from dataclasses import dataclass
from blockfrost.utils import object_request_wrapper, object_list_request_wrapper


@dataclass
class AddressResponse:
    @dataclass
    class Amount:
        unit: str
        quantity: str

    address: str
    amount: [Amount]
    stake_address: str
    type: str
    script: bool

    def __init__(self, address: str, amount: [Amount], stake_address: str, type: str, script: bool) -> None:
        self.address = address
        self.amount = [self.Amount(**o) for o in amount]
        self.stake_address = stake_address
        self.type = type
        self.script = script


@object_request_wrapper(AddressResponse)
def address(self, address: str, **kwargs):
    """
    Obtain information about a specific address.

    https://docs.blockfrost.io/#tag/Cardano-Addresses/paths/~1addresses~1{address}/get

    :param address: Bech32 address.
    :type address: str
    :param return_type: Optional. "object", "json" or "pandas". Default: "object".
    :type return_type: str
    :returns AddressResponse object.
    :rtype AddressResponse
    :raises ApiError: If API fails
    :raises Exception: If the API response is somehow malformed.
    """
    return requests.get(
        url=f"{self.url}/addresses/{address}",
        headers=self.default_headers
    )


@dataclass
class AddressesTotalResponse:
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


@object_request_wrapper(AddressesTotalResponse)
def address_total(self, address: str, **kwargs):
    """
    Obtain details about an address.

    https://docs.blockfrost.io/#tag/Cardano-Addresses/paths/~1addresses~1{address}~1total/get

    :param address: Bech32 address.
    :type address: str
    :param return_type: Optional. "object", "json" or "pandas". Default: "object".
    :type return_type: str
    :returns AddressesTotalResponse object.
    :rtype AddressesTotalResponse
    :raises ApiError: If API fails
    :raises Exception: If the API response is somehow malformed.
    """
    return requests.get(
        url=f"{self.url}/addresses/{address}/total",
        headers=self.default_headers
    )


@dataclass
class AddressesUTXOSResponse:
    @dataclass
    class Amount:
        unit: str
        quantity: str

    tx_hash: str
    output_index: int
    amount: [Amount]
    block: str
    data_hash: str

    def __init__(self, tx_hash: str, output_index: int, amount: [Amount], block: str, data_hash: str) -> None:
        self.tx_hash = tx_hash
        self.output_index = output_index
        self.amount = [self.Amount(**o) for o in amount]
        self.block = block
        self.data_hash = data_hash


@object_list_request_wrapper(AddressesUTXOSResponse)
def address_utxos(self, address: str, **kwargs):
    """
    UTXOs of the address.

    https://docs.blockfrost.io/#tag/Cardano-Addresses/paths/~1addresses~1{address}~1utxos/get

    :param address: Bech32 address.
    :type address: str
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
    :returns A list of AddressesUTXOSResponse objects.
    :rtype [AddressesUTXOSResponse]
    :raises ApiError: If API fails
    :raises Exception: If the API response is somehow malformed.
    """
    return requests.get(
        url=f"{self.url}/addresses/{address}/utxos",
        params=self.query_parameters(kwargs),
        headers=self.default_headers
    )


@dataclass
class AddressesUTXOSAssetResponse:
    @dataclass
    class Amount:
        unit: str
        quantity: str

    tx_hash: str
    output_index: int
    amount: [Amount]
    block: str
    data_hash: str

    def __init__(self, tx_hash: str, output_index: int, amount: [Amount], block: str, data_hash: str) -> None:
        self.tx_hash = tx_hash
        self.output_index = output_index
        self.amount = [self.Amount(**o) for o in amount]
        self.block = block
        self.data_hash = data_hash


@object_list_request_wrapper(AddressesUTXOSAssetResponse)
def address_utxos_asset(self, address: str, asset: str, **kwargs):
    """
    UTXOs of the address.

    https://docs.blockfrost.io/#tag/Cardano-Addresses/paths/~1addresses~1{address}~1utxos~1{asset}/get

    :param address: Bech32 address.
    :type address: str
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
    :returns A list of AddressesUTXOSAssetResponse objects.
    :rtype [AddressesUTXOSAssetResponse]
    :raises ApiError: If API fails
    :raises Exception: If the API response is somehow malformed.
    """
    return requests.get(
        url=f"{self.url}/addresses/{address}/utxos/{asset}",
        params=self.query_parameters(kwargs),
        headers=self.default_headers
    )


@dataclass
class AddressesTransactionResponse:
    tx_hash: str
    tx_index: int
    block_height: int


@object_list_request_wrapper(AddressesTransactionResponse)
def address_transactions(self, address: str, from_block: str = None, to_block: str = None,
                         **kwargs):
    """
    Transactions on the address.

    https://docs.blockfrost.io/#tag/Cardano-Addresses/paths/~1addresses~1{address}~1transactions/get

    :param address: Bech32 address.
    :type address: str
    :param from: The block number and optionally also index from which (inclusive) to start search for results, concatenated using colon. Has to be lower than or equal to to parameter.
    :type from: str
    :param to: The block number and optionally also index where (inclusive) to end the search for results, concatenated using colon. Has to be higher than or equal to from parameter.
    :type to: str
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
    :returns A list of AddressesUTXOSResponse objects.
    :rtype [AddressesUTXOSResponse]
    :raises ApiError: If API fails
    :raises Exception: If the API response is somehow malformed.
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
