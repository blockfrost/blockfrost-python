import requests
from dataclasses import dataclass
from ..utils import object_request_wrapper


@dataclass
class IPFSPinnedObject:
    ipfs_hash: str
    state: int


@object_request_wrapper(IPFSPinnedObject)
def pin(self, IPFS_path: str):
    """
    Pinned objects are counted in your user storage quota.

    https://docs.blockfrost.io/#tag/IPFS-Pins
    """
    return requests.post(
        url=f"{self.url}/ipfs/pin/add/{IPFS_path}",
        headers=self.default_headers,
    )
