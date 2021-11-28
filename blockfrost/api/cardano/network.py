import requests
from blockfrost.utils import request_wrapper


@request_wrapper
def network(self, **kwargs):
    """
    Return detailed network information.

    https://docs.blockfrost.io/#tag/Cardano-Network/paths/~1network/get

    :param return_type: Optional. "object", "json" or "pandas". Default: "object".
    :type return_type: str
    :returns object.
    :rtype: Namespace
    :raises ApiError: If API fails
    :raises Exception: If the API response is somehow malformed.
    """
    return requests.get(
        url=f"{self.url}/network",
        headers=self.default_headers
    )
