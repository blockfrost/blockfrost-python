import requests
from dataclasses import dataclass
from ..utils import request_wrapper, list_request_wrapper


@request_wrapper
def nutlink_address(self, address: str, **kwargs):
    """
    List metadata about specific address

    https://docs.blockfrost.io/#tag/Nut.link

    :param address: Address of a metadata oracle.
    :type address: str
    :param return_type: Optional. "object", "json" or "pandas". Default: "object".
    :type return_type: str
    :returns NutlinkAddressResponse object.
    :rtype NutlinkAddressResponse
    :raises ApiError: If API fails
    :raises Exception: If the API response is somehow malformed.
    """
    return requests.get(
        url=f"{self.url}/nutlink/{address}",
        headers=self.default_headers
    )


@list_request_wrapper
def nutlink_address_tickers(self, address: str, **kwargs):
    """
    List tickers for a specific metadata oracle

    https://docs.blockfrost.io/#tag/Nut.link/paths/~1nutlink~1{address}~1tickers/get

    :param address: Address of a metadata oracle.
    :type address: str
    :param return_type: Optional. "object", "json" or "pandas". Default: "object".
    :type return_type: str
    :param gather_pages: Optional. Default: 100. Will collect all pages into one return
    :type gather_pages: bool
    :param count: Optional. Default: 1. The number of results displayed on one page.
    :type count: int
    :param page: Optional. The page number for listing the results.
    :type page: int
    :param order: Optional. "asc" or "desc". Default: "asc".
    :type order: str
    :returns A list of NutlinkAddressTickersResponse objects.
    :rtype [NutlinkAddressTickersResponse]
    :raises ApiError: If API fails
    :raises Exception: If the API response is somehow malformed.
    """
    return requests.get(
        url=f"{self.url}/nutlink/{address}/tickers",
        params=self.query_parameters(kwargs),
        headers=self.default_headers
    )


@list_request_wrapper
def nutlink_address_ticker(self, address: str, ticker: str, **kwargs):
    """
    List of records of a specific ticker

    https://docs.blockfrost.io/#tag/Nut.link/paths/~1nutlink~1{address}~1tickers~1{ticker}/get

    :param address: Address of a metadata oracle.
    :type address: str
    :param ticker: Ticker for the pool record.
    :type ticker: str
    :param return_type: Optional. "object", "json" or "pandas". Default: "object".
    :type return_type: str
    :param gather_pages: Optional. Default: 100. Will collect all pages into one return
    :type gather_pages: bool
    :param count: Optional. Default: 1. The number of results displayed on one page.
    :type count: int
    :param page: Optional. The page number for listing the results.
    :type page: int
    :param order: Optional. "asc" or "desc". Default: "asc".
    :type order: str
    :returns A list of NutlinkAddressTickerResponse objects.
    :rtype [NutlinkAddressTickerResponse]
    :raises ApiError: If API fails
    :raises Exception: If the API response is somehow malformed.
    """
    return requests.get(
        url=f"{self.url}/nutlink/{address}/tickers/{ticker}",
        params=self.query_parameters(kwargs),
        headers=self.default_headers
    )


@list_request_wrapper
def nutlink_ticker(self, ticker: str, **kwargs):
    """
    List of records of a specific ticker

    https://docs.blockfrost.io/#tag/Nut.link/paths/~1nutlink~1tickers~1{ticker}/get

    :param ticker: Ticker for the pool record.
    :type ticker: str
    :param return_type: Optional. "object", "json" or "pandas". Default: "object".
    :type return_type: str
    :param gather_pages: Optional. Default: 100. Will collect all pages into one return
    :type gather_pages: bool
    :param count: Optional. Default: 1. The number of results displayed on one page.
    :type count: int
    :param page: Optional. The page number for listing the results.
    :type page: int
    :param order: Optional. "asc" or "desc". Default: "asc".
    :type order: str
    :returns A list of NutlinkTickerResponse objects.
    :rtype [NutlinkTickerResponse]
    :raises ApiError: If API fails
    :raises Exception: If the API response is somehow malformed.
    """
    return requests.get(
        url=f"{self.url}/nutlink/tickers/{ticker}",
        params=self.query_parameters(kwargs),
        headers=self.default_headers
    )
