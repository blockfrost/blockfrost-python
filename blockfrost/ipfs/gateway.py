import requests
from dataclasses import dataclass
from ..utils import simple_request_wrapper


# @dataclass
# class IPFSObject:
#     name: str
#     size: int
#     ipfs_hash: str


@simple_request_wrapper
def gateway(self, IPFS_path: str):
    """
    Retrieve an object from the IFPS gateway (useful if you do not want to rely on a public gateway, such as ipfs.blockfrost.dev).

    https://docs.blockfrost.io/#tag/IPFS-Gateway
    """

    response = requests.get(
        url=f"{self.url}/ipfs/gateway/{IPFS_path}",
        headers=self.default_headers,
    )
    return response.text
