import requests
from blockfrost.utils import list_request_wrapper


@list_request_wrapper
def metadata_labels(self, **kwargs):
    """
    List of all used transaction metadata labels.

    https://docs.blockfrost.io/#tag/cardano--metadata/GET/metadata/txs/labels

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
        url=f"{self.url}/metadata/txs/labels",
        params=self.query_parameters(kwargs),
        headers=self.default_headers
    )


@list_request_wrapper
def metadata_label_json(self, label: str, **kwargs):
    """
    Transaction metadata per label.

    https://docs.blockfrost.io/#tag/cardano--metadata/GET/metadata/txs/labels/{label}

    :param label: Metadata label
    :type label: str
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
        url=f"{self.url}/metadata/txs/labels/{label}",
        params=self.query_parameters(kwargs),
        headers=self.default_headers
    )


@list_request_wrapper
def metadata_label_cbor(self, label: str, **kwargs):
    """
    Transaction metadata per label.

    https://docs.blockfrost.io/#tag/cardano--metadata/GET/metadata/txs/labels/{label}/cbor

    :param label: Metadata label
    :type label: str
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
        url=f"{self.url}/metadata/txs/labels/{label}/cbor",
        params=self.query_parameters(kwargs),
        headers=self.default_headers
    )
