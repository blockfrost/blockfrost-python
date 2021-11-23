import requests
from blockfrost.utils import request_wrapper


@request_wrapper
def genesis(self, **kwargs):
    """
    Return the information about blockchain genesis.

    https://docs.blockfrost.io/#tag/Cardano-Ledger/paths/~1genesis/get

    :param return_type: Optional. "object", "json" or "pandas". Default: "object".
    :type return_type: str
    :returns object.
    :rtype: Namespace
    :raises ApiError: If API fails
    :raises Exception: If the API response is somehow malformed.
    """
    return requests.get(
        url=f"{self.url}/genesis",
        headers=self.default_headers
    )
