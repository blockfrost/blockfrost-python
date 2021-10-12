import requests
from dataclasses import dataclass
from blockfrost.utils import object_request_wrapper, object_list_request_wrapper


@dataclass
class ScriptsResponse:
    script_hash: str


@object_list_request_wrapper(ScriptsResponse)
def scripts(self):
    """
    List of scripts.

    https://docs.blockfrost.io/#tag/Cardano-Scripts/paths/~1scripts/get

    :returns A list of ScriptsResponse objects.
    :rtype [ScriptsResponse]
    :raises ApiError: If API fails
    :raises Exception: If the API response is somehow malformed.
    """
    return requests.get(
        url=f"{self.url}/scripts",
        headers=self.default_headers
    )


@dataclass
class ScriptResponse:
    script_hash: str
    type: str
    serialised_size: int


@object_request_wrapper(ScriptResponse)
def script(self, script_hash: str):
    """
    Information about a specific script.

    https://docs.blockfrost.io/#tag/Cardano-Scripts/paths/~1scripts~1{script_hash}/get

    :param script_hash: Hash of the script.
    :type script_hash: str
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
class ScriptRedeemersResponse:
    tx_hash: str
    tx_index: int
    purpose: str
    unit_mem: str
    unit_steps: str
    fee: str


@object_list_request_wrapper(ScriptRedeemersResponse)
def script_redeemers(self, script_hash: str):
    """
    List of redeemers of a specific script.

    https://docs.blockfrost.io/#tag/Cardano-Scripts/paths/~1scripts~1{script_hash}~1redeemers/get

    :param script_hash: Hash of the script.
    :type script_hash: str
    :returns A list of ScriptRedeemersResponse objects.
    :rtype [ScriptRedeemersResponse]
    :raises ApiError: If API fails
    :raises Exception: If the API response is somehow malformed.
    """
    return requests.get(
        url=f"{self.url}/scripts/{script_hash}/redeemers",
        headers=self.default_headers
    )
