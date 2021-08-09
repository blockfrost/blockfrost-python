from ..utils import object_request_wrapper
import requests


@object_request_wrapper
def health(self) -> requests.Response:
    """
    Return backend status as a boolean. Your application should handle situations when backend for the given chain is unavailable.

    https://docs.blockfrost.io/#tag/Health/paths/~1health/get
    """
    return requests.get(
        url=f"{self.url}/health",
        headers=self.authentication_header
    )


@object_request_wrapper
def clock(self) -> requests.Response:
    """
    This endpoint provides the current UNIX time. Your application might use this to verify if the client clock is not out of sync.

    https://cardano-mainnet.blockfrost.io/api/v0/health
    """
    return requests.get(
        url=f"{self.url}/health/clock",
        headers=self.authentication_header
    )
