import requests
from dataclasses import dataclass
from blockfrost.utils import object_request_wrapper, object_list_request_wrapper


@dataclass
class Genesis:
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


@object_request_wrapper(Genesis)
def genesis(self):
    """
    Return the information about blockchain genesis.

    https://docs.blockfrost.io/#tag/Cardano-Ledger/paths/~1genesis/get
    """
    return requests.get(
        url=f"{self.url}/genesis",
        headers=self.default_headers
    )
