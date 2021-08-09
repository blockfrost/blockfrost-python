from ..utils import object_request_wrapper
import requests


@object_request_wrapper
def metrics(self) -> requests.Response:
    """
    History of your Blockfrost usage metrics in the past 30 days.

    https://docs.blockfrost.io/#tag/Metrics/paths/~1metrics~1/get
    """
    return requests.get(
        url=f"{self.url}/metrics",
        headers=self.authentication_header
    )


@object_request_wrapper
def metrics_endpoints(self) -> requests.Response:
    """
    History of your Blockfrost usage metrics per endpoint in the past 30 days.

    https://docs.blockfrost.io/#tag/Metrics/paths/~1metrics~1endpoints/get
    """
    return requests.get(
        url=f"{self.url}/metrics/endpoints",
        headers=self.authentication_header
    )
