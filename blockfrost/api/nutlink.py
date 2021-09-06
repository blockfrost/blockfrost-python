import requests
from dataclasses import dataclass
from ..utils import object_request_wrapper, object_list_request_wrapper


@dataclass
class NutlinkAddressResponse:
    address: str
    metadata_url: str
    metadata_hash: str
    metadata: dict


@object_request_wrapper(NutlinkAddressResponse)
def nutlink_address(self, address: str):
    """
    List metadata about specific address

    https://docs.blockfrost.io/#tag/Nut.link
    """
    return requests.get(
        url=f"{self.url}/nutlink/{address}",
        headers=self.default_headers
    )


@dataclass
class NutlinkAddressTickersResponse:
    name: str
    count: int
    latest_block: int


@object_list_request_wrapper(NutlinkAddressTickersResponse)
def nutlink_address_tickers(self, address: str) -> requests.Response:
    """
    List tickers for a specific metadata oracle

    https://docs.blockfrost.io/#tag/Nut.link/paths/~1nutlink~1{address}~1tickers/get
    """
    return requests.get(
        url=f"{self.url}/nutlink/{address}/tickers",
        headers=self.default_headers
    )


@dataclass
class NutlinkAddressTickerResponse:
    tx_hash: str
    block_height: int
    tx_index: int
    payload = dict


@object_list_request_wrapper(NutlinkAddressTickerResponse)
def nutlink_address_ticker(self, address: str, ticker: str) -> requests.Response:
    """
    List of records of a specific ticker

    https://docs.blockfrost.io/#tag/Nut.link/paths/~1nutlink~1{address}~1tickers~1{ticker}/get
    """
    return requests.get(
        url=f"{self.url}/nutlink/{address}/tickers/{ticker}",
        headers=self.default_headers
    )


@dataclass
class NutlinkTickerResponse:
    address: str
    tx_hash: str
    block_height: int
    tx_index: int
    payload = dict


@object_list_request_wrapper(NutlinkTickerResponse)
def nutlink_ticker(self, ticker: str) -> requests.Response:
    """
    List of records of a specific ticker

    https://docs.blockfrost.io/#tag/Nut.link/paths/~1nutlink~1tickers~1{ticker}/get
    """
    return requests.get(
        url=f"{self.url}/nutlink/tickers/{ticker}",
        headers=self.default_headers
    )
