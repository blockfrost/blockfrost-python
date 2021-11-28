import requests
from dataclasses import dataclass
from ..utils import list_request_wrapper


@list_request_wrapper
def metrics(self, **kwargs):
    """
    History of your Blockfrost usage metrics in the past 30 days.

    https://docs.blockfrost.io/#tag/Metrics/paths/~1metrics~1/get

    :param return_type: Optional. "object", "json" or "pandas". Default: "object".
    :type return_type: str
    :returns A list of objects.
    :rtype [Namespace]
    :raises ApiError: If API fails
    :raises Exception: If the API response is somehow malformed.
    """
    return requests.get(
        url=f"{self.url}/metrics",
        headers=self.default_headers
    )


@list_request_wrapper
def metrics_endpoints(self, **kwargs):
    """
    History of your Blockfrost usage metrics per endpoint in the past 30 days.

    https://docs.blockfrost.io/#tag/Metrics/paths/~1metrics~1endpoints/get

    :param return_type: Optional. "object", "json" or "pandas". Default: "object".
    :type return_type: str
    :returns A list of objects.
    :rtype [Namespace]
    :raises ApiError: If API fails
    :raises Exception: If the API response is somehow malformed.
    """
    return requests.get(
        url=f"{self.url}/metrics/endpoints",
        headers=self.default_headers
    )
