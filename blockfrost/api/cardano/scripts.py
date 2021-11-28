import requests
from blockfrost.utils import request_wrapper, list_request_wrapper


@list_request_wrapper
def scripts(self, **kwargs):
    """
    List of scripts.

    https://docs.blockfrost.io/#tag/Cardano-Scripts/paths/~1scripts/get

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
        url=f"{self.url}/scripts",
        params=self.query_parameters(kwargs),
        headers=self.default_headers
    )


@request_wrapper
def script(self, script_hash: str, **kwargs):
    """
    Information about a specific script.

    https://docs.blockfrost.io/#tag/Cardano-Scripts/paths/~1scripts~1{script_hash}/get

    :param script_hash: Hash of the script.
    :type script_hash: str
    :param return_type: Optional. "object", "json" or "pandas". Default: "object".
    :type return_type: str
    :returns object.
    :rtype: Namespace
    :raises ApiError: If API fails
    :raises Exception: If the API response is somehow malformed.
    """
    return requests.get(
        url=f"{self.url}/scripts/{script_hash}",
        headers=self.default_headers
    )


@request_wrapper
def script_json(self, script_hash: str, **kwargs):
    """
    JSON representation of a timelock script.

    https://docs.blockfrost.io/#tag/Cardano-Scripts/paths/~1scripts~1{script_hash}~1json/get

    :param script_hash: Hash of the script.
    :type script_hash: str
    :param return_type: Optional. "object", "json" or "pandas". Default: "object".
    :type return_type: str
    :returns object.
    :rtype: Namespace
    :raises ApiError: If API fails
    :raises Exception: If the API response is somehow malformed.
    """
    return requests.get(
        url=f"{self.url}/scripts/{script_hash}/json",
        headers=self.default_headers
    )


@request_wrapper
def script_cbor(self, script_hash: str, **kwargs):
    """
    CBOR representation of a plutus script

    https://docs.blockfrost.io/#tag/Cardano-Scripts/paths/~1scripts~1{script_hash}~1cbor/get

    :param script_hash: Hash of the script.
    :type script_hash: str
    :param return_type: Optional. "object", "json" or "pandas". Default: "object".
    :type return_type: str
    :returns object.
    :rtype: Namespace
    :raises ApiError: If API fails
    :raises Exception: If the API response is somehow malformed.
    """
    return requests.get(
        url=f"{self.url}/scripts/{script_hash}/cbor",
        headers=self.default_headers
    )


@list_request_wrapper
def script_redeemers(self, script_hash: str, **kwargs):
    """
    List of redeemers of a specific script.

    https://docs.blockfrost.io/#tag/Cardano-Scripts/paths/~1scripts~1{script_hash}~1redeemers/get

    :param script_hash: Hash of the script.
    :type script_hash: str
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
        url=f"{self.url}/scripts/{script_hash}/redeemers",
        params=self.query_parameters(kwargs),
        headers=self.default_headers
    )


@request_wrapper
def script_datum(self, datum_hash: str, **kwargs):
    """
    Query JSON value of a datum by its hash.

    https://docs.blockfrost.io/#tag/Cardano-Scripts/paths/~1scripts~1datum~1{datum_hash}/get

    :param datum_hash: Hash of the datum.
    :type datum_hash: str
    :param return_type: Optional. "object", "json" or "pandas". Default: "object".
    :type return_type: str
    :returns object.
    :rtype: Namespace
    :raises ApiError: If API fails
    :raises Exception: If the API response is somehow malformed.
    """
    return requests.get(
        url=f"{self.url}/scripts/datum/{datum_hash}",
        headers=self.default_headers
    )
