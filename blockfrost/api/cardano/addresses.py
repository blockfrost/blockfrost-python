import requests
from blockfrost.utils import request_wrapper, list_request_wrapper


@request_wrapper
def address(self, address: str, **kwargs):
    """
    Obtain information about a specific address.

    https://docs.blockfrost.io/#tag/Cardano-Addresses/paths/~1addresses~1{address}/get

    :param address: Bech32 address.
    :type address: str
    :param return_type: Optional. "object", "json" or "pandas". Default: "object".
    :type return_type: str
    :returns object.
    :rtype: Namespace
    :raises ApiError: If API fails
    :raises Exception: If the API response is somehow malformed.
    """
    return requests.get(
        url=f"{self.url}/addresses/{address}",
        headers=self.default_headers
    )


@request_wrapper
def address_extended(self, address: str, **kwargs):
    """
    Obtain information about a specific address.

    https://docs.blockfrost.io/#tag/Cardano-Addresses/paths/~1addresses~1{address}~1extended/get

    :param address: Bech32 address.
    :type address: str
    :param return_type: Optional. "object", "json" or "pandas". Default: "object".
    :type return_type: str
    :returns object.
    :rtype: Namespace
    :raises ApiError: If API fails
    :raises Exception: If the API response is somehow malformed.
    """
    return requests.get(
        url=f"{self.url}/addresses/{address}/extended",
        headers=self.default_headers
    )


@request_wrapper
def address_total(self, address: str, **kwargs):
    """
    Obtain details about an address.

    https://docs.blockfrost.io/#tag/Cardano-Addresses/paths/~1addresses~1{address}~1total/get

    :param address: Bech32 address.
    :type address: str
    :param return_type: Optional. "object", "json" or "pandas". Default: "object".
    :type return_type: str
    :returns object.
    :rtype: Namespace
    :raises ApiError: If API fails
    :raises Exception: If the API response is somehow malformed.
    """
    return requests.get(
        url=f"{self.url}/addresses/{address}/total",
        headers=self.default_headers
    )


@list_request_wrapper
def address_utxos(self, address: str, **kwargs):
    """
    UTXOs of the address.

    https://docs.blockfrost.io/#tag/Cardano-Addresses/paths/~1addresses~1{address}~1utxos/get

    :param address: Bech32 address.
    :type address: str
    :param return_type: Optional. "object", "json" or "pandas". Default: "object".
    :type return_type: str
    :param gather_pages: Optional. Default: false. Will collect all pages into one return
    :type gather_pages: bool
    :param count: Optional. Default: 100. The number of results displayed on one page.
    :type count: int
    :param page: Optional. The page number for listing the results.
    :type page: int
    :param order: Optional. "asc" or "desc". Default: "asc".
    :type order: str
    :returns A list of objects.
    :rtype [Namespace]
    :raises ApiError: If API fails
    :raises Exception: If the API response is somehow malformed.
    """
    return requests.get(
        url=f"{self.url}/addresses/{address}/utxos",
        params=self.query_parameters(kwargs),
        headers=self.default_headers
    )


@list_request_wrapper
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
    :param gather_pages: Optional. Default: false. Will collect all pages into one return
    :type gather_pages: bool
    :param count: Optional. Default: 100. The number of results displayed on one page.
    :type count: int
    :param page: Optional. The page number for listing the results.
    :type page: int
    :param order: Optional. "asc" or "desc". Default: "asc".
    :type order: str
    :returns A list of objects.
    :rtype [Namespace]
    :raises ApiError: If API fails
    :raises Exception: If the API response is somehow malformed.
    """
    return requests.get(
        url=f"{self.url}/addresses/{address}/utxos/{asset}",
        params=self.query_parameters(kwargs),
        headers=self.default_headers
    )


@list_request_wrapper
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
    :param gather_pages: Optional. Default: false. Will collect all pages into one return
    :type gather_pages: bool
    :param count: Optional. Default: 100. The number of results displayed on one page.
    :type count: int
    :param page: Optional. The page number for listing the results.
    :type page: int
    :param order: Optional. "asc" or "desc". Default: "asc".
    :type order: str
    :returns A list of objects.
    :rtype [Namespace]
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
