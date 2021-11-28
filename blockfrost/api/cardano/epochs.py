import requests
from dataclasses import dataclass, field
from blockfrost.utils import request_wrapper, list_request_wrapper


@request_wrapper
def epoch_latest(self, **kwargs):
    """
    Return the information about the latest, therefore current, epoch.

    https://docs.blockfrost.io/#tag/Cardano-Epochs/paths/~1epochs~1latest/get

    :param return_type: Optional. "object", "json" or "pandas". Default: "object".
    :type return_type: str
    :returns object.
    :rtype: Namespace
    :raises ApiError: If API fails
    :raises Exception: If the API response is somehow malformed.
    """
    return requests.get(
        url=f"{self.url}/epochs/latest",
        headers=self.default_headers
    )


@request_wrapper
def epoch_latest_parameters(self, **kwargs):
    """
    Return the protocol parameters for the latest epoch.

    https://docs.blockfrost.io/#tag/Cardano-Epochs/paths/~1epochs~1latest~1parameters/get

    :param return_type: Optional. "object", "json" or "pandas". Default: "object".
    :type return_type: str
    :returns object.
    :rtype: Namespace
    :raises ApiError: If API fails
    :raises Exception: If the API response is somehow malformed.
    """
    return requests.get(
        url=f"{self.url}/epochs/latest/parameters",
        headers=self.default_headers
    )


@request_wrapper
def epoch(self, number: int, **kwargs):
    """
    Return the content of the requested epoch.

    https://docs.blockfrost.io/#tag/Cardano-Epochs/paths/~1epochs~1{number}/get

    :param number: Number of the epoch.
    :type number: int
    :param return_type: Optional. "object", "json" or "pandas". Default: "object".
    :type return_type: str
    :returns object.
    :rtype: Namespace
    :raises ApiError: If API fails
    :raises Exception: If the API response is somehow malformed.
    """
    return requests.get(
        url=f"{self.url}/epochs/{number}",
        headers=self.default_headers
    )


@list_request_wrapper
def epochs_next(self, number: int, **kwargs):
    """
    Return the list of epochs following a specific epoch.

    https://docs.blockfrost.io/#tag/Cardano-Epochs/paths/~1epochs~1{number}~1next/get

    :param number: Number of the epoch.
    :type number: int
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
        url=f"{self.url}/epochs/{number}/next",
        params=self.query_parameters(kwargs),
        headers=self.default_headers
    )


@list_request_wrapper
def epochs_previous(self, number: int, **kwargs):
    """
    Return the list of epochs preceding a specific epoch.

    https://docs.blockfrost.io/#tag/Cardano-Epochs/paths/~1epochs~1{number}~1previous/get

    :param number: Number of the epoch.
    :type number: int
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
        url=f"{self.url}/epochs/{number}/previous",
        params=self.query_parameters(kwargs),
        headers=self.default_headers
    )


@list_request_wrapper
def epoch_stakes(self, number: int, **kwargs):
    """
    Return the active stake distribution for the specified epoch.

    https://docs.blockfrost.io/#tag/Cardano-Epochs/paths/~1epochs~1{number}~1stakes/get

    :param number: Number of the epoch.
    :type number: int
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
        url=f"{self.url}/epochs/{number}/stakes",
        params=self.query_parameters(kwargs),
        headers=self.default_headers
    )


@list_request_wrapper
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
        url=f"{self.url}/epochs/{number}/stakes/{pool_id}",
        params=self.query_parameters(kwargs),
        headers=self.default_headers
    )


@list_request_wrapper
def epoch_blocks(self, number: int, **kwargs):
    """
    Return the blocks minted for the epoch specified.

    https://docs.blockfrost.io/#tag/Cardano-Epochs/paths/~1epochs~1{number}~1blocks/get

    :param number: Number of the epoch.
    :type number: int
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
        url=f"{self.url}/epochs/{number}/blocks",
        params=self.query_parameters(kwargs),
        headers=self.default_headers
    )


@list_request_wrapper
def epoch_pool_blocks(self, number: int, pool_id: str, **kwargs):
    """
    Return the block minted for the epoch specified by stake pool.

    https://docs.blockfrost.io/#tag/Cardano-Epochs/paths/~1epochs~1{number}~1blocks~1{pool_id}/get

    :param number: Number of the epoch.
    :type number: int
    :param pool_id: Stake pool ID to filter.
    :type pool_id: int
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
        url=f"{self.url}/epochs/{number}/blocks/{pool_id}",
        params=self.query_parameters(kwargs),
        headers=self.default_headers
    )


@request_wrapper
def epoch_latest_parameters(self, number: int, **kwargs):
    """
    Return the protocol parameters for the epoch specified.

    https://docs.blockfrost.io/#tag/Cardano-Epochs/paths/~1epochs~1{number}~1parameters/get

    :param number: Number of the epoch.
    :type number: int
    :param return_type: Optional. "object", "json" or "pandas". Default: "object".
    :type return_type: str
    :returns object.
    :rtype: Namespace
    :raises ApiError: If API fails
    :raises Exception: If the API response is somehow malformed.
    """
    return requests.get(
        url=f"{self.url}/epochs/{number}/parameters",
        headers=self.default_headers
    )
