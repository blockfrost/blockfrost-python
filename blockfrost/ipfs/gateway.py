import requests
from ..utils import simple_request_wrapper


@simple_request_wrapper
def gateway(self, IPFS_path: str, **kwargs):
    """
    Retrieve an object from the IFPS gateway (useful if you do not want to rely on a public gateway, such as ipfs.blockfrost.dev).

    https://docs.blockfrost.io/#tag/IPFS-Gateway

    :param IPFS_path: Path to the IPFS object.
    :type IPFS_path: str
    :returns file text.
    :rtype data
    :raises ApiError: If API fails
    :raises Exception: If the API response is somehow malformed.
    """

    response = requests.get(
        url=f"{self.url}/ipfs/gateway/{IPFS_path}",
        headers=self.default_headers,
    )
    return response
