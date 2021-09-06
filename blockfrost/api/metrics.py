import requests
from dataclasses import dataclass
from ..utils import object_list_request_wrapper


@dataclass
class UsageMetric:
    time: int
    calls: int


@object_list_request_wrapper(UsageMetric)
def metrics(self):
    """
    History of your Blockfrost usage metrics in the past 30 days.

    https://docs.blockfrost.io/#tag/Metrics/paths/~1metrics~1/get
    """
    return requests.get(
        url=f"{self.url}/metrics",
        headers=self.default_headers
    )


@dataclass
class UsageMetricEndpoint:
    time: int
    calls: int
    endpoint: str


@object_list_request_wrapper(UsageMetricEndpoint)
def metrics_endpoints(self):
    """
    History of your Blockfrost usage metrics per endpoint in the past 30 days.

    https://docs.blockfrost.io/#tag/Metrics/paths/~1metrics~1endpoints/get
    """
    return requests.get(
        url=f"{self.url}/metrics/endpoints",
        headers=self.default_headers
    )
