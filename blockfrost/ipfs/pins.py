import requests
from dataclasses import dataclass
from ..utils import object_request_wrapper, object_list_request_wrapper


@dataclass
class IPFSPinnedObjectResponse:
    ipfs_hash: str
    state: str


@object_request_wrapper(IPFSPinnedObjectResponse)
def pin_object(self, IPFS_path: str, **kwargs):
    """
    Pinned objects are counted in your user storage quota.

    https://docs.blockfrost.io/#tag/IPFS-Pins

    :param IPFS_path: Path to the IPFS object.
    :type IPFS_path: str
    :param return_type: Optional. "object", "json" or "pandas". Default: "object".
    :type return_type: str
    :returns IPFSPinnedObjectResponse object.
    :rtype IPFSPinnedObjectResponse
    :raises ApiError: If API fails
    :raises Exception: If the API response is somehow malformed.
    """
    return requests.post(
        url=f"{self.url}/ipfs/pin/add/{IPFS_path}",
        headers=self.default_headers,
    )


@dataclass
class IPFSPinnedListObjectResponse:
    time_created: int
    time_pinned: int
    ipfs_hash: str
    size: int
    state: str


@object_list_request_wrapper(IPFSPinnedListObjectResponse)
def pined_list(self, **kwargs):
    """
    List objects pinned to local storage

    https://docs.blockfrost.io/#tag/IPFS-Pins/paths/~1ipfs~1pin~1list~1/get

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
    :returns A list of IPFSPinnedListObjectResponse objects.
    :rtype [IPFSPinnedListObjectResponse]
    :raises ApiError: If API fails
    :raises Exception: If the API response is somehow malformed.
    """
    return requests.get(
        url=f"{self.url}/ipfs/pin/list",
        params=self.query_parameters(kwargs),
        headers=self.default_headers,
    )


@object_request_wrapper(IPFSPinnedListObjectResponse)
def pined_object(self, IPFS_path: str, **kwargs):
    """
    List objects pinned to local storage

    https://docs.blockfrost.io/#tag/IPFS-Pins/paths/~1ipfs~1pin~1list~1{IPFS_path}/get

    :param IPFS_path: Path to the IPFS object.
    :type IPFS_path: str
    :param return_type: Optional. "object", "json" or "pandas". Default: "object".
    :type return_type: str
    :returns IPFSPinnedListObjectResponse object.
    :rtype IPFSPinnedListObjectResponse
    :raises ApiError: If API fails
    :raises Exception: If the API response is somehow malformed.
    """
    return requests.get(
        url=f"{self.url}/ipfs/pin/list/{IPFS_path}",
        headers=self.default_headers,
    )


@object_request_wrapper(IPFSPinnedObjectResponse)
def pined_object_remove(self, IPFS_path: str, **kwargs):
    """
    Remove pinned objects from local storage

    https://docs.blockfrost.io/#tag/IPFS-Pins/paths/~1ipfs~1pin~1remove~1{IPFS_path}/post

    :param IPFS_path: Path to the IPFS object.
    :type IPFS_path: str
    :param return_type: Optional. "object", "json" or "pandas". Default: "object".
    :type return_type: str
    :returns IPFSPinnedObjectResponse object.
    :rtype IPFSPinnedObjectResponse
    :raises ApiError: If API fails
    :raises Exception: If the API response is somehow malformed.
    """
    return requests.post(
        url=f"{self.url}/ipfs/pin/remove/{IPFS_path}",
        headers=self.default_headers,
    )
