import requests
from dataclasses import dataclass

from ..utils import object_request_wrapper


@dataclass
class HealthResponse:
    is_healthy: bool


@object_request_wrapper(HealthResponse)
def health(self, **kwargs):
    """
    Return backend status as a boolean. Your application should handle situations when backend for the given chain is unavailable.

    https://docs.blockfrost.io/#tag/Health/paths/~1health/get

    :returns HealthResponse object.
    :rtype HealthResponse
    :raises ApiError: If API fails
    :raises Exception: If the API response is somehow malformed.
    """
    return requests.get(
        url=f"{self.url}/health",
        headers=self.default_headers
    )


@dataclass
class ClockResponse:
    server_time: int


@object_request_wrapper(ClockResponse)
def clock(self, **kwargs):
    """
    This endpoint provides the current UNIX time. Your application might use this to verify if the client clock is not out of sync.

    https://docs.blockfrost.io/#tag/Health/paths/~1health~1clock/get

    :param return_type: Optional. "object", "json" or "pandas". Default: "object".
    :type return_type: str
    :returns ClockResponse object.
    :rtype ClockResponse
    :raises ApiError: If API fails
    :raises Exception: If the API response is somehow malformed.
    """
    return requests.get(
        url=f"{self.url}/health/clock",
        headers=self.default_headers
    )
