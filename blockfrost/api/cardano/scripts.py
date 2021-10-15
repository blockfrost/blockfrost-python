import requests
from dataclasses import dataclass
from blockfrost.utils import object_request_wrapper, object_list_request_wrapper


@dataclass
class ScriptsResponse:
    script_hash: str


@object_list_request_wrapper(ScriptsResponse)
def scripts(self, **kwargs):
    """
    List of scripts.

    https://docs.blockfrost.io/#tag/Cardano-Scripts/paths/~1scripts/get

    :param return_type: Optional. "object", "json" or "pandas". Default: "object".
    :type return_type: str
    :returns A list of ScriptsResponse objects.
    :rtype [ScriptsResponse]
    :raises ApiError: If API fails
    :raises Exception: If the API response is somehow malformed.
    """
    return requests.get(
        url=f"{self.url}/scripts",
        params=self.query_parameters(kwargs),
        headers=self.default_headers
    )


@dataclass
class ScriptResponse:
    script_hash: str
    type: str
    serialised_size: int


@object_request_wrapper(ScriptResponse)
def script(self, script_hash: str, **kwargs):
    """
    Information about a specific script.

    https://docs.blockfrost.io/#tag/Cardano-Scripts/paths/~1scripts~1{script_hash}/get

    :param script_hash: Hash of the script.
    :type script_hash: str
    :param return_type: Optional. "object", "json" or "pandas". Default: "object".
    :type return_type: str
    :returns A list of ScriptResponse objects.
    :rtype [ScriptResponse]
    :raises ApiError: If API fails
    :raises Exception: If the API response is somehow malformed.
    """
    return requests.get(
        url=f"{self.url}/scripts/{script_hash}",
        headers=self.default_headers
    )


@dataclass
class ScriptJsonResponse:
    json: dict

    def __init__(self, **kwargs) -> None:
        self.json = kwargs


@object_request_wrapper(ScriptJsonResponse)
def script_json(self, script_hash: str, **kwargs):
    """
    JSON representation of a timelock script.

    https://docs.blockfrost.io/#tag/Cardano-Scripts/paths/~1scripts~1{script_hash}~1json/get

    :param script_hash: Hash of the script.
    :type script_hash: str
    :param return_type: Optional. "object", "json" or "pandas". Default: "object".
    :type return_type: str
    :returns A list of ScriptJsonResponse objects.
    :rtype [ScriptJsonResponse]
    :raises ApiError: If API fails
    :raises Exception: If the API response is somehow malformed.
    """
    return requests.get(
        url=f"{self.url}/scripts/{script_hash}/json",
        headers=self.default_headers
    )


@dataclass
class ScriptCBORResponse:
    cbor: str


@object_request_wrapper(ScriptCBORResponse)
def script_cbor(self, script_hash: str, **kwargs):
    """
    CBOR representation of a plutus script

    https://docs.blockfrost.io/#tag/Cardano-Scripts/paths/~1scripts~1{script_hash}~1cbor/get

    :param script_hash: Hash of the script.
    :type script_hash: str
    :param return_type: Optional. "object", "json" or "pandas". Default: "object".
    :type return_type: str
    :returns A list of ScriptCborResponse objects.
    :rtype [ScriptCborResponse]
    :raises ApiError: If API fails
    :raises Exception: If the API response is somehow malformed.
    """
    return requests.get(
        url=f"{self.url}/scripts/{script_hash}/cbor",
        headers=self.default_headers
    )


@dataclass
class ScriptRedeemersResponse:
    tx_hash: str
    tx_index: int
    purpose: str
    unit_mem: str
    unit_steps: str
    fee: str


@object_list_request_wrapper(ScriptRedeemersResponse)
def script_redeemers(self, script_hash: str, **kwargs):
    """
    List of redeemers of a specific script.

    https://docs.blockfrost.io/#tag/Cardano-Scripts/paths/~1scripts~1{script_hash}~1redeemers/get

    :param script_hash: Hash of the script.
    :type script_hash: str
    :param return_type: Optional. "object", "json" or "pandas". Default: "object".
    :type return_type: str
    :returns A list of ScriptRedeemersResponse objects.
    :rtype [ScriptRedeemersResponse]
    :raises ApiError: If API fails
    :raises Exception: If the API response is somehow malformed.
    """
    return requests.get(
        url=f"{self.url}/scripts/{script_hash}/redeemers",
        params=self.query_parameters(kwargs),
        headers=self.default_headers
    )


@dataclass
class ScriptDatumResponse:
    json_value: dict


@object_request_wrapper(ScriptDatumResponse)
def script_datum(self, datum_hash: str, **kwargs):
    """
    Query JSON value of a datum by its hash.

    https://docs.blockfrost.io/#tag/Cardano-Scripts/paths/~1scripts~1datum~1{datum_hash}/get

    :param datum_hash: Hash of the datum.
    :type datum_hash: str
    :param return_type: Optional. "object", "json" or "pandas". Default: "object".
    :type return_type: str
    :returns A list of ScriptDatumResponse objects.
    :rtype [ScriptDatumResponse]
    :raises ApiError: If API fails
    :raises Exception: If the API response is somehow malformed.
    """
    return requests.get(
        url=f"{self.url}/scripts/datum/{datum_hash}",
        headers=self.default_headers
    )
