import requests
from blockfrost.utils import list_request_wrapper


@list_request_wrapper
def mempool(self, **kwargs):
    """
    Obtains transactions that are currently stored in Blockfrost mempool, waiting to be included in a newly minted block.
    Returns only transactions submitted via Blockfrost.io.

    https://docs.blockfrost.io/#tag/Cardano-Mempool/paths/~1mempool/get

    :param return_type: Optional. "object", "json" or "pandas". Default: "object".
    :type return_type: str
    :param gather_pages: Optional. Default: false. Will collect all pages into one return
    :type gather_pages: bool
    :param count: Optional. Default: 100. The number of results displayed on one page.
    :type count: int
    :param page: Optional. The page number for listing the results.
    :type page: int
    :returns A list of objects.
    :rtype [Namespace]
    :raises ApiError: If API fails
    :raises Exception: If the API response is somehow malformed.
    """
    return requests.get(
        url=f"{self.url}/mempool",
        params=self.query_parameters(kwargs),
        headers=self.default_headers
    )

@list_request_wrapper
def mempool_tx(self, hash: str, **kwargs):
    """
    Obtains mempool transaction

    https://docs.blockfrost.io/#tag/Cardano-Mempool/paths/~1mempool~1%7Bhash%7D/get

    :param hash: Hash of the requested transaction.
    :type hash: str
    :param return_type: Optional. "object", "json" or "pandas". Default: "object".
    :type return_type: str
    :param gather_pages: Optional. Default: false. Will collect all pages into one return
    :type gather_pages: bool
    :param count: Optional. Default: 100. The number of results displayed on one page.
    :type count: int
    :param page: Optional. The page number for listing the results.
    :type page: int
    :returns A list of objects.
    :rtype [Namespace]
    :raises ApiError: If API fails
    :raises Exception: If the API response is somehow malformed.
    """
    return requests.get(
        url=f"{self.url}/mempool/{hash}",
        params=self.query_parameters(kwargs),
        headers=self.default_headers
    )

@list_request_wrapper
def mempool_address(self, address: str, **kwargs):
    """
    Obtains list of mempool transactions where at least one of the transaction inputs or outputs belongs to the address (paginated).
    Shows only transactions submitted via Blockfrost.io.

    https://docs.blockfrost.io/#tag/Cardano-Mempool/paths/~1mempool~1addresses~1%7Baddress%7D/get

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
    :returns A list of objects.
    :rtype [Namespace]
    :raises ApiError: If API fails
    :raises Exception: If the API response is somehow malformed.
    """
    return requests.get(
        url=f"{self.url}/mempool/addresses/{address}",
        params=self.query_parameters(kwargs),
        headers=self.default_headers
    )

