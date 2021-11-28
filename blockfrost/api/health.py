import requests
from ..utils import request_wrapper


@request_wrapper
def health(self, **kwargs):
    """
    Return backend status as a boolean. Your application should handle situations when backend for the given chain is unavailable.

    https://docs.blockfrost.io/#tag/Health/paths/~1health/get

    :param return_type: Optional. "object", "json" or "pandas". Default: "object".
    :type return_type: str
    :returns HealthResponse object.
    :rtype HealthResponse
    :raises ApiError: If API fails
    :raises Exception: If the API response is somehow malformed.
    """
    return requests.get(
        url=f"{self.url}/health",
        headers=self.default_headers
    )


@request_wrapper
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
