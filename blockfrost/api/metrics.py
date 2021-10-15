import requests
from dataclasses import dataclass
from ..utils import object_list_request_wrapper


@dataclass
class UsageMetricResponse:
    time: int
    calls: int


@object_list_request_wrapper(UsageMetricResponse)
def metrics(self, **kwargs):
    """
    History of your Blockfrost usage metrics in the past 30 days.

    https://docs.blockfrost.io/#tag/Metrics/paths/~1metrics~1/get

    :param return_type: Optional. "object", "json" or "pandas". Default: "object".
    :type return_type: str
    :returns UsageMetricResponse object.
    :rtype UsageMetricResponse
    :raises ApiError: If API fails
    :raises Exception: If the API response is somehow malformed.
    """
    return requests.get(
        url=f"{self.url}/metrics",
        headers=self.default_headers
    )


@dataclass
class UsageMetricEndpointResponse:
    time: int
    calls: int
    endpoint: str


@object_list_request_wrapper(UsageMetricEndpointResponse)
def metrics_endpoints(self, **kwargs):
    """
    History of your Blockfrost usage metrics per endpoint in the past 30 days.

    https://docs.blockfrost.io/#tag/Metrics/paths/~1metrics~1endpoints/get

    :param return_type: Optional. "object", "json" or "pandas". Default: "object".
    :type return_type: str
    :returns UsageMetricEndpointResponse object.
    :rtype UsageMetricEndpointResponse
    :raises ApiError: If API fails
    :raises Exception: If the API response is somehow malformed.
    """
    return requests.get(
        url=f"{self.url}/metrics/endpoints",
        headers=self.default_headers
    )
