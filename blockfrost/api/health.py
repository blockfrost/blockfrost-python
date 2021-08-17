import requests
from dataclasses import dataclass

from ..utils import object_request_wrapper


@dataclass
class Health:
    is_healthy: bool


@object_request_wrapper(Health)
def health(self):
    """
    Return backend status as a boolean. Your application should handle situations when backend for the given chain is unavailable.

    https://docs.blockfrost.io/#tag/Health/paths/~1health/get
    """
    return requests.get(
        url=f"{self.url}/health",
        headers=self.authentication_header
    )


@dataclass
class Clock:
    server_time: int


@object_request_wrapper(Clock)
def clock(self):
    """
    This endpoint provides the current UNIX time. Your application might use this to verify if the client clock is not out of sync.

    https://cardano-mainnet.blockfrost.io/api/v0/health
    """
    return requests.get(
        url=f"{self.url}/health/clock",
        headers=self.authentication_header
    )
