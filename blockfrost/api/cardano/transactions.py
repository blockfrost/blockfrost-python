import requests
from blockfrost.utils import request_wrapper, list_request_wrapper


@request_wrapper
def transaction(self, hash: str, **kwargs):
    """
    Return content of the requested transaction.

    https://docs.blockfrost.io/#tag/Cardano-Transactions/paths/~1txs~1{hash}/get

    :param hash: Hash of the requested transaction.
    :type hash: str
    :param return_type: Optional. "object", "json" or "pandas". Default: "object".
    :type return_type: str
    :returns object.
    :rtype: Namespace
    :raises ApiError: If API fails
    :raises Exception: If the API response is somehow malformed.
    """
    return requests.get(
        url=f"{self.url}/txs/{hash}",
        headers=self.default_headers
    )


@request_wrapper
def transaction_utxos(self, hash: str, **kwargs):
    """
    Return the inputs and UTXOs of the specific transaction.

    https://docs.blockfrost.io/#tag/Cardano-Transactions/paths/~1txs~1{hash}~1utxos/get

    :param hash: Hash of the requested transaction.
    :type hash: str
    :param return_type: Optional. "object", "json" or "pandas". Default: "object".
    :type return_type: str
    :returns object.
    :rtype: Namespace
    :raises ApiError: If API fails
    :raises Exception: If the API response is somehow malformed.
    """
    return requests.get(
        url=f"{self.url}/txs/{hash}/utxos",
        headers=self.default_headers
    )


@list_request_wrapper
def transaction_stakes(self, hash: str, **kwargs):
    """
    Obtain information about (de)registration of stake addresses within a transaction.

    https://docs.blockfrost.io/#tag/Cardano-Transactions/paths/~1txs~1{hash}~1stakes/get

    :param hash: Hash of the requested transaction.
    :type hash: str
    :param return_type: Optional. "object", "json" or "pandas". Default: "object".
    :type return_type: str
    :returns A list of objects.
    :rtype [Namespace]
    :raises ApiError: If API fails
    :raises Exception: If the API response is somehow malformed.
    """
    return requests.get(
        url=f"{self.url}/txs/{hash}/stakes",
        headers=self.default_headers
    )


@list_request_wrapper
def transaction_delegations(self, hash: str, **kwargs):
    """
    Obtain information about delegation certificates of a specific transaction.

    https://docs.blockfrost.io/#tag/Cardano-Transactions/paths/~1txs~1{hash}~1delegations/get

    :param hash: Hash of the requested transaction.
    :type hash: str
    :param return_type: Optional. "object", "json" or "pandas". Default: "object".
    :type return_type: str
    :returns A list of objects.
    :rtype [Namespace]
    :raises ApiError: If API fails
    :raises Exception: If the API response is somehow malformed.
    """
    return requests.get(
        url=f"{self.url}/txs/{hash}/delegations",
        headers=self.default_headers
    )


@list_request_wrapper
def transaction_withdrawals(self, hash: str, **kwargs):
    """
    Obtain information about withdrawals of a specific transaction.

    https://docs.blockfrost.io/#tag/Cardano-Transactions/paths/~1txs~1{hash}~1withdrawals/get

    :param hash: Hash of the requested transaction.
    :type hash: str
    :param return_type: Optional. "object", "json" or "pandas". Default: "object".
    :type return_type: str
    :returns A list of objects.
    :rtype [Namespace]
    :raises ApiError: If API fails
    :raises Exception: If the API response is somehow malformed.
    """
    return requests.get(
        url=f"{self.url}/txs/{hash}/withdrawals",
        headers=self.default_headers
    )


@list_request_wrapper
def transaction_mirs(self, hash: str, **kwargs):
    """
    Obtain information about Move Instantaneous Rewards (MIRs) of a specific transaction.

    https://docs.blockfrost.io/#tag/Cardano-Transactions/paths/~1txs~1{hash}~1mirs/get

    :param hash: Hash of the requested transaction.
    :type hash: str
    :param return_type: Optional. "object", "json" or "pandas". Default: "object".
    :type return_type: str
    :returns A list of objects.
    :rtype [Namespace]
    :raises ApiError: If API fails
    :raises Exception: If the API response is somehow malformed.
    """
    return requests.get(
        url=f"{self.url}/txs/{hash}/mirs",
        headers=self.default_headers
    )


@list_request_wrapper
def transaction_pool_updates(self, hash: str, **kwargs):
    """
    Obtain information about stake pool registration and update certificates of a specific transaction.

    https://docs.blockfrost.io/#tag/Cardano-Transactions/paths/~1txs~1{hash}~1pool_updates/get

    :param hash: Hash of the requested transaction.
    :type hash: str
    :param return_type: Optional. "object", "json" or "pandas". Default: "object".
    :type return_type: str
    :returns A list of objects.
    :rtype [Namespace]
    :raises ApiError: If API fails
    :raises Exception: If the API response is somehow malformed.
    """
    return requests.get(
        url=f"{self.url}/txs/{hash}/pool_updates",
        headers=self.default_headers
    )


@list_request_wrapper
def transaction_pool_retires(self, hash: str, **kwargs):
    """
    Obtain information about stake pool retirements within a specific transaction.

    https://docs.blockfrost.io/#tag/Cardano-Transactions/paths/~1txs~1{hash}~1pool_retires/get

    :param hash: Hash of the requested transaction.
    :type hash: str
    :param return_type: Optional. "object", "json" or "pandas". Default: "object".
    :type return_type: str
    :returns A list of objects.
    :rtype [Namespace]
    :raises ApiError: If API fails
    :raises Exception: If the API response is somehow malformed.
    """
    return requests.get(
        url=f"{self.url}/txs/{hash}/pool_retires",
        headers=self.default_headers
    )


@list_request_wrapper
def transaction_metadata(self, hash: str, **kwargs):
    """
    Obtain the transaction metadata.

    https://docs.blockfrost.io/#tag/Cardano-Transactions/paths/~1txs~1{hash}~1metadata/get

    :param hash: Hash of the requested transaction.
    :type hash: str
    :param return_type: Optional. "object", "json" or "pandas". Default: "object".
    :type return_type: str
    :returns A list of objects.
    :rtype [Namespace]
    :raises ApiError: If API fails
    :raises Exception: If the API response is somehow malformed.
    """
    return requests.get(
        url=f"{self.url}/txs/{hash}/metadata",
        headers=self.default_headers
    )


@list_request_wrapper
def transaction_metadata_cbor(self, hash: str, **kwargs):
    """
    Obtain the transaction metadata in CBOR.

    https://docs.blockfrost.io/#tag/Cardano-Transactions/paths/~1txs~1{hash}~1metadata~1cbor/get

    :param hash: Hash of the requested transaction.
    :type hash: str
    :param return_type: Optional. "object", "json" or "pandas". Default: "object".
    :type return_type: str
    :returns A list of objects.
    :rtype [Namespace]
    :raises ApiError: If API fails
    :raises Exception: If the API response is somehow malformed.
    """
    return requests.get(
        url=f"{self.url}/txs/{hash}/metadata/cbor",
        headers=self.default_headers
    )


@list_request_wrapper
def transaction_redeemers(self, hash: str, **kwargs):
    """
    Obtain the transaction redeemers.

    https://docs.blockfrost.io/#tag/Cardano-Transactions/paths/~1txs~1{hash}~1redeemers/get

    :param hash: Hash of the requested transaction.
    :type hash: str
    :param return_type: Optional. "object", "json" or "pandas". Default: "object".
    :type return_type: str
    :returns A list of objects.
    :rtype [Namespace]
    :raises ApiError: If API fails
    :raises Exception: If the API response is somehow malformed.
    """
    return requests.get(
        url=f"{self.url}/txs/{hash}/redeemers",
        headers=self.default_headers
    )


@request_wrapper
def transaction_submit(self, file_path: str, **kwargs):
    """
    Submit an already serialized transaction to the network.

    https://docs.blockfrost.io/#tag/Cardano-Transactions/paths/~1tx~1submit/post

    :param file_path: Path to file.
    :type file_path: str
    :returns str object.
    :rtype str
    :raises ApiError: If API fails
    :raises Exception: If the API response is somehow malformed.
    """
    header = self.default_headers
    header['Content-Type'] = 'application/cbor'
    with open(file_path, 'rb') as file:
        return requests.post(
            url=f"{self.url}/tx/submit",
            headers=header,
            data=file,
        )
