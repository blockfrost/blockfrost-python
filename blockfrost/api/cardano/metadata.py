import requests
from dataclasses import dataclass
from blockfrost.utils import object_request_wrapper, object_list_request_wrapper


@dataclass
class MetadataLabelResponse:
    label: str
    cip10: str
    count: str


@object_list_request_wrapper(MetadataLabelResponse)
def metadata_labels(self, **kwargs):
    """
    List of all used transaction metadata labels.

    https://docs.blockfrost.io/#tag/Cardano-Metadata/paths/~1metadata~1txs~1labels/get

    :param return_type: Optional. "object", "json" or "pandas". Default: "object".
    :type return_type: str
    :param gather_pages: Optional. Default: 100. Will collect all pages into one return
    :type gather_pages: bool
    :param count: Optional. Default: 1. The number of results displayed on one page.
    :type count: int
    :param page: Optional. The page number for listing the results.
    :type page: int
    :param order: Optional. "asc" or "desc". Default: "asc".
    :type order: str
    :returns A list of MetadataLabelResponse objects.
    :rtype [MetadataLabelResponse]
    :raises ApiError: If API fails
    :raises Exception: If the API response is somehow malformed.
    """
    return requests.get(
        url=f"{self.url}/metadata/txs/labels",
        params=self.query_parameters(kwargs),
        headers=self.default_headers
    )


@dataclass
class MetadataLabelJsonResponse:
    tx_hash: str
    json_metadata: dict


@object_list_request_wrapper(MetadataLabelJsonResponse)
def metadata_label_json(self, label: str, **kwargs):
    """
    Transaction metadata per label.

    https://docs.blockfrost.io/#tag/Cardano-Metadata/paths/~1metadata~1txs~1labels~1{label}/get

    :param label: Metadata label
    :type label: str
    :param return_type: Optional. "object", "json" or "pandas". Default: "object".
    :type return_type: str
    :param gather_pages: Optional. Default: 100. Will collect all pages into one return
    :type gather_pages: bool
    :param count: Optional. Default: 1. The number of results displayed on one page.
    :type count: int
    :param page: Optional. The page number for listing the results.
    :type page: int
    :param order: Optional. "asc" or "desc". Default: "asc".
    :type order: str
    :returns A list of MetadataLabelJsonResponse objects.
    :rtype [MetadataLabelJsonResponse]
    :raises ApiError: If API fails
    :raises Exception: If the API response is somehow malformed.
    """
    return requests.get(
        url=f"{self.url}/metadata/txs/labels/{label}",
        params=self.query_parameters(kwargs),
        headers=self.default_headers
    )


@dataclass
class MetadataLabelCBORResponse:
    tx_hash: str
    cbor_metadata: str


@object_list_request_wrapper(MetadataLabelCBORResponse)
def metadata_label_cbor(self, label: str, **kwargs):
    """
    Transaction metadata per label.

    https://docs.blockfrost.io/#tag/Cardano-Metadata/paths/~1metadata~1txs~1labels~1{label}~1cbor/get

    :param label: Metadata label
    :type label: str
    :param return_type: Optional. "object", "json" or "pandas". Default: "object".
    :type return_type: str
    :param gather_pages: Optional. Default: 100. Will collect all pages into one return
    :type gather_pages: bool
    :param count: Optional. Default: 1. The number of results displayed on one page.
    :type count: int
    :param page: Optional. The page number for listing the results.
    :type page: int
    :param order: Optional. "asc" or "desc". Default: "asc".
    :type order: str
    :returns A list of MetadataLabelCBORResponse objects.
    :rtype [MetadataLabelCBORResponse]
    :raises ApiError: If API fails
    :raises Exception: If the API response is somehow malformed.
    """
    return requests.get(
        url=f"{self.url}/metadata/txs/labels/{label}/cbor",
        params=self.query_parameters(kwargs),
        headers=self.default_headers
    )
