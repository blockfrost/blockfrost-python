import requests
from dataclasses import dataclass
from blockfrost.utils import object_request_wrapper, object_list_request_wrapper


@dataclass
class Network:
    @dataclass
    class Supply:
        max: str
        total: str
        circulating: str

    @dataclass
    class Stake:
        live: str
        active: str

    supply: Supply
    stake: Stake

    def __init__(self, supply: Supply, stake: Stake) -> None:
        self.supply = self.Supply(**supply) if supply is not None else None
        self.stake = self.Stake(**stake) if stake is not None else None


@object_request_wrapper(Network)
def network(self):
    """
    Return detailed network information.

    https://docs.blockfrost.io/#tag/Cardano-Network/paths/~1network/get
    """
    return requests.get(
        url=f"{self.url}/network",
        headers=self.default_headers
    )
