from ..utils import object_request_wrapper, object_list_request_wrapper
import requests


@object_request_wrapper()
def nutlink(self, address: str) -> requests.Response:
    """
    List metadata about specific address

    https://docs.blockfrost.io/#tag/Nut.link
    """
    return requests.get(
        url=f"{self.url}/nutlink/{address}",
        headers=self.authentication_header
    )


@object_list_request_wrapper()
def nutlink_address_ticker(self, address: str, **kwargs) -> requests.Response:
    """
    List tickers for a specific metadata oracle

    https://docs.blockfrost.io/#tag/Nut.link/paths/~1nutlink~1{address}~1tickers/get
    """
    return requests.get(
        url=f"{self.url}/nutlink/{address}/tickers",
        params=self.query_parameters(kwargs),
        headers=self.authentication_header
    )


@object_list_request_wrapper()
def nutlink_tickers(self, address: str, **kwargs) -> requests.Response:
    """
    List tickers for a specific metadata oracle

    https://docs.blockfrost.io/#tag/Nut.link/paths/~1nutlink~1{address}~1tickers/get
    """
    return requests.get(
        url=f"{self.url}/nutlink/{address}/tickers",
        params=self.query_parameters(kwargs),
        headers=self.authentication_header
    )
