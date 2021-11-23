import requests
from blockfrost.utils import request_wrapper, list_request_wrapper


@list_request_wrapper
def assets(self, **kwargs):
    """
    List of assets.

    https://docs.blockfrost.io/#tag/Cardano-Assets/paths/~1assets/get

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
        url=f"{self.url}/assets",
        params=self.query_parameters(kwargs),
        headers=self.default_headers
    )


@request_wrapper
def asset(self, asset: str, **kwargs):
    """
    Information about a specific asset

    https://docs.blockfrost.io/#tag/Cardano-Assets/paths/~1assets~1{asset}/get

    :param asset: Concatenation of the policy_id and hex-encoded asset_name.
    :type asset: str
    :param return_type: Optional. "object", "json" or "pandas". Default: "object".
    :type return_type: str
    :returns object.
    :rtype: Namespace
    :raises ApiError: If API fails
    :raises Exception: If the API response is somehow malformed.
    """
    return requests.get(
        url=f"{self.url}/assets/{asset}",
        headers=self.default_headers
    )


@list_request_wrapper
def asset_history(self, asset: str, **kwargs):
    """
    History of a specific asset

    https://docs.blockfrost.io/#tag/Cardano-Assets/paths/~1assets~1{asset}~1history/get

    :param asset: Concatenation of the policy_id and hex-encoded asset_name.
    :type asset: str
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
        url=f"{self.url}/assets/{asset}/history",
        params=self.query_parameters(kwargs),
        headers=self.default_headers
    )


@list_request_wrapper
def asset_transactions(self, asset: str, **kwargs):
    """
    List of a specific asset transactions

    https://docs.blockfrost.io/#tag/Cardano-Assets/paths/~1assets~1{asset}~1transactions/get

    :param asset: Concatenation of the policy_id and hex-encoded asset_name.
    :type asset: str
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
        url=f"{self.url}/assets/{asset}/transactions",
        params=self.query_parameters(kwargs),
        headers=self.default_headers
    )


@list_request_wrapper
def asset_addresses(self, asset: str, **kwargs):
    """
    List of a addresses containing a specific asset

    https://docs.blockfrost.io/#tag/Cardano-Assets/paths/~1assets~1{asset}~1addresses/get

    :param asset: Concatenation of the policy_id and hex-encoded asset_name.
    :type asset: str
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
        url=f"{self.url}/assets/{asset}/addresses",
        params=self.query_parameters(kwargs),
        headers=self.default_headers
    )


@list_request_wrapper
def assets_policy(self, policy_id: str, **kwargs):
    """
    List of asset minted under a specific policy

    https://docs.blockfrost.io/#tag/Cardano-Assets/paths/~1assets~1policy~1{policy_id}/get

    :param policy_id: Specific policy_id.
    :type policy_id: str
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
        url=f"{self.url}/assets/policy/{policy_id}",
        params=self.query_parameters(kwargs),
        headers=self.default_headers
    )
