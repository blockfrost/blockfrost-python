from blockfrost.utils import object_request_wrapper, object_list_request_wrapper
import requests


@object_request_wrapper()
def address(self, address: str) -> requests.Response:
    """
    Obtain information about a specific address.

    https://docs.blockfrost.io/#tag/Cardano-Addresses/paths/~1addresses~1{address}/get
    """
    return requests.get(
        url=f"{self.url}/addresses/{address}",
        headers=self.authentication_header
    )


@object_request_wrapper()
def address_total(self, address: str) -> requests.Response:
    """
    Obtain details about an address.

    https://docs.blockfrost.io/#tag/Cardano-Addresses/paths/~1addresses~1{address}~1total/get
    """
    return requests.get(
        url=f"{self.url}/addresses/{address}/total",
        headers=self.authentication_header
    )


@object_list_request_wrapper()
def address_utxos(self, address: str, **kwargs) -> requests.Response:
    """
    UTXOs of the address.

    https://docs.blockfrost.io/#tag/Cardano-Addresses/paths/~1addresses~1{address}~1utxos/get
    """
    return requests.get(
        url=f"{self.url}/addresses/{address}/utxos",
        params=self.query_parameters(kwargs),
        headers=self.authentication_header
    )


@object_list_request_wrapper()
def address_transactions(self, address: str, from_block: str = None, to_block: str = None,
                         **kwargs) -> requests.Response:
    """
    Transactions on the address.

    from
    string
    Example: from=8929261
    The block number and optionally also index from which (inclusive) to start search for results, concatenated using colon. Has to be lower than or equal to to parameter.

    to
    string
    Example: to=9999269:10
    The block number and optionally also index where (inclusive) to end the search for results, concatenated using colon. Has to be higher than or equal to from parameter.

    https://docs.blockfrost.io/#tag/Cardano-Addresses/paths/~1addresses~1{address}~1transactions/get
    """
    return requests.get(
        url=f"{self.url}/addresses/{address}/transactions",
        params={
            'from': from_block,
            'to': to_block,
            **self.query_parameters(kwargs)
        },
        headers=self.authentication_header
    )
