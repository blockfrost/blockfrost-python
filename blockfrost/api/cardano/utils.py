import requests
from blockfrost.utils import request_wrapper, list_request_wrapper


@list_request_wrapper
def utils_addresses_xpub(self, xpub: str, role: int, index: int, **kwargs):
    """
    Derive Shelley address from an xpub

    https://docs.blockfrost.io/#tag/Cardano-Utilities/paths/~1utils~1addresses~1xpub~1{xpub}~1{role}~1{index}/get

    :param xpub: Hex xpub.
    :type xpub: str
    :param role: Account role.
    :type role: int
    :param index: Address index.
    :type index: int
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
        url=f"{self.url}/utils/addresses/xpub/{xpub}/{role}/{index}",
        params=self.query_parameters(kwargs),
        headers=self.default_headers
    )
