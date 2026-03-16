import requests
from blockfrost.utils import request_wrapper, list_request_wrapper


@list_request_wrapper
def pools(self, **kwargs):
    """
    List of registered stake pools.

    https://docs.blockfrost.io/#tag/cardano--pools/GET/pools

    :param gather_pages: Optional. Default: false. Will collect all pages into one return
    :type gather_pages: bool
    :param count: Optional. Default: 100. The number of results displayed on one page.
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


@list_request_wrapper
def pools_extended(self, **kwargs):
    """
    List of registered stake pools with additional information.

    https://docs.blockfrost.io/#tag/cardano--pools/GET/pools/extended

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
        url=f"{self.url}/pools/extended",
        params=self.query_parameters(kwargs),
        headers=self.default_headers
    )


@list_request_wrapper
def pools_retired(self, **kwargs):
    """
    List of already retired pools.

    https://docs.blockfrost.io/#tag/cardano--pools/GET/pools/retired

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
        url=f"{self.url}/pools/retired",
        params=self.query_parameters(kwargs),
        headers=self.default_headers
    )


@list_request_wrapper
def pools_retiring(self, **kwargs):
    """
    List of stake pools retiring in the upcoming epochs

    https://docs.blockfrost.io/#tag/cardano--pools/GET/pools/retiring

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
        url=f"{self.url}/pools/retiring",
        params=self.query_parameters(kwargs),
        headers=self.default_headers
    )


@request_wrapper
def pool(self, pool_id: str, **kwargs):
    """
    Pool information.

    https://docs.blockfrost.io/#tag/cardano--pools/GET/pools/{pool_id}

    :param pool_id: Bech32 or hexadecimal pool ID.
    :type pool_id: str
    :returns object.
    :rtype: Namespace
    :raises ApiError: If API fails
    :raises Exception: If the API response is somehow malformed.
    """
    return requests.get(
        url=f"{self.url}/pools/{pool_id}",
        headers=self.default_headers
    )


@list_request_wrapper
def pool_history(self, pool_id: str, **kwargs):
    """
    History of stake pool parameters over epochs.

    https://docs.blockfrost.io/#tag/cardano--pools/GET/pools/{pool_id}/history

    :param pool_id: Bech32 or hexadecimal pool ID.
    :type pool_id: str
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
        url=f"{self.url}/pools/{pool_id}/history",
        params=self.query_parameters(kwargs),
        headers=self.default_headers
    )


@request_wrapper
def pool_metadata(self, pool_id: str, **kwargs):
    """
    Stake pool registration metadata.

    https://docs.blockfrost.io/#tag/cardano--pools/GET/pools/{pool_id}/metadata

    :param pool_id: Bech32 or hexadecimal pool ID.
    :type pool_id: str
    :returns object.
    :rtype: Namespace
    :raises ApiError: If API fails
    :raises Exception: If the API response is somehow malformed.
    """
    return requests.get(
        url=f"{self.url}/pools/{pool_id}/metadata",
        headers=self.default_headers
    )


@request_wrapper
def pool_relays(self, pool_id: str, **kwargs):
    """
    Relays of a stake pool.

    https://docs.blockfrost.io/#tag/cardano--pools/GET/pools/{pool_id}/relays

    :param pool_id: Bech32 or hexadecimal pool ID.
    :type pool_id: str
    :returns A list of objects.
    :rtype [Namespace]
    :raises ApiError: If API fails
    :raises Exception: If the API response is somehow malformed.
    """
    return requests.get(
        url=f"{self.url}/pools/{pool_id}/relays",
        headers=self.default_headers
    )


@list_request_wrapper
def pool_delegators(self, pool_id: str, **kwargs):
    """
    List of current stake pools delegators.

    https://docs.blockfrost.io/#tag/cardano--pools/GET/pools/{pool_id}/delegators

    :param pool_id: Bech32 or hexadecimal pool ID.
    :type pool_id: str
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
        url=f"{self.url}/pools/{pool_id}/delegators",
        params=self.query_parameters(kwargs),
        headers=self.default_headers
    )


@list_request_wrapper
def pool_blocks(self, pool_id: str, **kwargs):
    """
    List of stake pools blocks.

    https://docs.blockfrost.io/#tag/cardano--pools/GET/pools/{pool_id}/blocks

    :param pool_id: Bech32 or hexadecimal pool ID.
    :type pool_id: str
    :param gather_pages: Optional. Default: false. Will collect all pages into one return
    :type gather_pages: bool
    :param count: Optional. Default: 100. The number of results displayed on one page.
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


@list_request_wrapper
def pool_updates(self, pool_id: str, **kwargs):
    """
    List of certificate updates to the stake pool.

    https://docs.blockfrost.io/#tag/cardano--pools/GET/pools/{pool_id}/updates

    :param pool_id: Bech32 or hexadecimal pool ID.
    :type pool_id: str
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
        url=f"{self.url}/pools/{pool_id}/updates",
        params=self.query_parameters(kwargs),
        headers=self.default_headers
    )


@list_request_wrapper
def pool_votes(self, pool_id: str, **kwargs):
    """
    History of stake pool votes.

    https://docs.blockfrost.io/#tag/cardano--pools/GET/pools/{pool_id}/votes

    :param pool_id: Bech32 or hexadecimal pool ID.
    :type pool_id: str
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
        url=f"{self.url}/pools/{pool_id}/votes",
        params=self.query_parameters(kwargs),
        headers=self.default_headers
    )
