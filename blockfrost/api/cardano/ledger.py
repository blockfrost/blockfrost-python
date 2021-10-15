import requests
from dataclasses import dataclass
from blockfrost.utils import object_request_wrapper, object_list_request_wrapper


@dataclass
class GenesisResponse:
    active_slots_coefficient: float
    update_quorum: int
    max_lovelace_supply: str
    network_magic: int
    epoch_length: int
    system_start: int
    slots_per_kes_period: int
    slot_length: int
    max_kes_evolutions: int
    security_param: int


@object_request_wrapper(GenesisResponse)
def genesis(self, **kwargs):
    """
    Return the information about blockchain genesis.

    https://docs.blockfrost.io/#tag/Cardano-Ledger/paths/~1genesis/get

    :param return_type: Optional. "object", "json" or "pandas". Default: "object".
    :type return_type: str
    :returns GenesisResponse object.
    :rtype GenesisResponse
    :raises ApiError: If API fails
    :raises Exception: If the API response is somehow malformed.
    """
    return requests.get(
        url=f"{self.url}/genesis",
        headers=self.default_headers
    )
