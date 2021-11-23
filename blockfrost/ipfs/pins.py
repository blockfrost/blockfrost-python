import requests
from dataclasses import dataclass
from ..utils import request_wrapper, list_request_wrapper


@request_wrapper
def pin_object(self, IPFS_path: str, **kwargs):
    """
    Pinned objects are counted in your user storage quota.

    https://docs.blockfrost.io/#tag/IPFS-Pins

    :param IPFS_path: Path to the IPFS object.
    :type IPFS_path: str
    :param return_type: Optional. "object", "json" or "pandas". Default: "object".
    :type return_type: str
    :returns object.
    :rtype: Namespace
    :raises ApiError: If API fails
    :raises Exception: If the API response is somehow malformed.
    """
    return requests.post(
        url=f"{self.url}/ipfs/pin/add/{IPFS_path}",
        headers=self.default_headers,
    )


@list_request_wrapper
def pined_list(self, **kwargs):
    """
    List objects pinned to local storage

    https://docs.blockfrost.io/#tag/IPFS-Pins/paths/~1ipfs~1pin~1list~1/get

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
        url=f"{self.url}/ipfs/pin/list",
        params=self.query_parameters(kwargs),
        headers=self.default_headers,
    )


@request_wrapper
def pined_object(self, IPFS_path: str, **kwargs):
    """
    List objects pinned to local storage

    https://docs.blockfrost.io/#tag/IPFS-Pins/paths/~1ipfs~1pin~1list~1{IPFS_path}/get

    :param IPFS_path: Path to the IPFS object.
    :type IPFS_path: str
    :param return_type: Optional. "object", "json" or "pandas". Default: "object".
    :type return_type: str
    :returns object.
    :rtype: Namespace
    :raises ApiError: If API fails
    :raises Exception: If the API response is somehow malformed.
    """
    return requests.get(
        url=f"{self.url}/ipfs/pin/list/{IPFS_path}",
        headers=self.default_headers,
    )


@request_wrapper
def pined_object_remove(self, IPFS_path: str, **kwargs):
    """
    Remove pinned objects from local storage

    https://docs.blockfrost.io/#tag/IPFS-Pins/paths/~1ipfs~1pin~1remove~1{IPFS_path}/post

    :param IPFS_path: Path to the IPFS object.
    :type IPFS_path: str
    :param return_type: Optional. "object", "json" or "pandas". Default: "object".
    :type return_type: str
    :returns object.
    :rtype: Namespace
    :raises ApiError: If API fails
    :raises Exception: If the API response is somehow malformed.
    """
    return requests.post(
        url=f"{self.url}/ipfs/pin/remove/{IPFS_path}",
        headers=self.default_headers,
    )
