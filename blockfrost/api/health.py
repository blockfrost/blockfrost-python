from blockfrost.utils import api_request_wrapper
import requests
from requests import Response

@api_request_wrapper
def health(self) -> Response:
    """https://cardano-mainnet.blockfrost.io/api/v0/health"""
    return requests.get(
        url=f"{self.url}/health",
        headers=self.authentication_header
    )


@api_request_wrapper
def clock(self) -> Response:
    """https://cardano-mainnet.blockfrost.io/api/v0/health"""
    return requests.get(
        url=f"{self.url}/health/clock",
        headers=self.authentication_header
    )
