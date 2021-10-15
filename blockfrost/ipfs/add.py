import requests
from dataclasses import dataclass
from ..utils import object_request_wrapper


@dataclass
class IPFSObjectResponse:
    name: str
    ipfs_hash: str
    size: int


@object_request_wrapper(IPFSObjectResponse)
def add(self, file_path: str, **kwargs):
    """
    Add a file or directory to IPFS

    You need to `/ipfs/pin/add` an object to avoid it being garbage collected.
    This usage is being counted in your user account quota.

    https://docs.blockfrost.io/#tag/IPFS-Add/paths/~1ipfs~1add/post

    :param file_path: Path to file.
    :type file_path: str
    :param return_type: Optional. "object", "json" or "pandas". Default: "object".
    :type return_type: str
    :returns IPFSObject object.
    :rtype IPFSObject
    :raises ApiError: If API fails
    :raises Exception: If the API response is somehow malformed.
    """
    with open(file_path, 'rb') as file:
        return requests.post(
            url=f"{self.url}/ipfs/add",
            headers=self.default_headers,
            files={'file': file},
        )
