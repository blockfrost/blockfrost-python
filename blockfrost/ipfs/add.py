from ..utils import object_request_wrapper
import requests


@object_request_wrapper()
def add(self, file_path: str) -> requests.Response:
    """
    Add a file or directory to IPFS

    You need to `/ipfs/pin/add` an object to avoid it being garbage collected.
    This usage is being counted in your user account quota.

    https://docs.blockfrost.io/#tag/IPFS-Add/paths/~1ipfs~1add/post
    """
    with open(file_path, 'rb') as file:
        return requests.post(
            url=f"{self.url}/ipfs/add",
            headers=self.default_headers,
            files={'file': file},
        )
