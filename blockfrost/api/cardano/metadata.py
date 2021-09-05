import requests
from dataclasses import dataclass
from blockfrost.utils import object_request_wrapper, object_list_request_wrapper


@dataclass
class Label:
    label: str
    cipl0: str
    count: str


@object_list_request_wrapper(Label)
def metadata_labels(self):
    """
    List of all used transaction metadata labels.

    https://docs.blockfrost.io/#tag/Cardano-Metadata/paths/~1metadata~1txs~1labels/get
    """
    return requests.get(
        url=f"{self.url}/metadata/txs/labels",
        headers=self.default_headers
    )


@dataclass
class LabelJson:
    tx_hash: str
    json_metadata: dict


@object_list_request_wrapper(LabelJson)
def metadata_label_json(self, label: str):
    """
    Transaction metadata per label.

    https://docs.blockfrost.io/#tag/Cardano-Metadata/paths/~1metadata~1txs~1labels~1{label}/get
    """
    return requests.get(
        url=f"{self.url}/metadata/txs/labels/{label}",
        headers=self.default_headers
    )

@dataclass
class LabelCBOR:
    tx_hash: str
    cbor_metadata: str


@object_list_request_wrapper(LabelCBOR)
def metadata_label_cbor(self, label: str):
    """
    Transaction metadata per label.

    https://docs.blockfrost.io/#tag/Cardano-Metadata/paths/~1metadata~1txs~1labels~1{label}~1cbor/get
    """
    return requests.get(
        url=f"{self.url}/metadata/txs/labels/{label}/cbor",
        headers=self.default_headers
    )
