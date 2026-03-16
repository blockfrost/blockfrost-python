import requests
from typing import Union
from blockfrost.utils import request_wrapper


@request_wrapper
def transaction(self, hash: str, **kwargs):
    """
    Return content of the requested transaction.

    https://docs.blockfrost.io/#tag/cardano--transactions/GET/txs/{hash}

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

    https://docs.blockfrost.io/#tag/cardano--transactions/GET/txs/{hash}/utxos

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


@request_wrapper
def transaction_stakes(self, hash: str, **kwargs):
    """
    Obtain information about (de)registration of stake addresses within a transaction.

    https://docs.blockfrost.io/#tag/cardano--transactions/GET/txs/{hash}/stakes

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


@request_wrapper
def transaction_delegations(self, hash: str, **kwargs):
    """
    Obtain information about delegation certificates of a specific transaction.

    https://docs.blockfrost.io/#tag/cardano--transactions/GET/txs/{hash}/delegations

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


@request_wrapper
def transaction_withdrawals(self, hash: str, **kwargs):
    """
    Obtain information about withdrawals of a specific transaction.

    https://docs.blockfrost.io/#tag/cardano--transactions/GET/txs/{hash}/withdrawals

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


@request_wrapper
def transaction_mirs(self, hash: str, **kwargs):
    """
    Obtain information about Move Instantaneous Rewards (MIRs) of a specific transaction.

    https://docs.blockfrost.io/#tag/cardano--transactions/GET/txs/{hash}/mirs

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


@request_wrapper
def transaction_pool_updates(self, hash: str, **kwargs):
    """
    Obtain information about stake pool registration and update certificates of a specific transaction.

    https://docs.blockfrost.io/#tag/cardano--transactions/GET/txs/{hash}/pool_updates

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


@request_wrapper
def transaction_pool_retires(self, hash: str, **kwargs):
    """
    Obtain information about stake pool retirements within a specific transaction.

    https://docs.blockfrost.io/#tag/cardano--transactions/GET/txs/{hash}/pool_retires

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


@request_wrapper
def transaction_metadata(self, hash: str, **kwargs):
    """
    Obtain the transaction metadata.

    https://docs.blockfrost.io/#tag/cardano--transactions/GET/txs/{hash}/metadata

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


@request_wrapper
def transaction_metadata_cbor(self, hash: str, **kwargs):
    """
    Obtain the transaction metadata in CBOR.

    https://docs.blockfrost.io/#tag/cardano--transactions/GET/txs/{hash}/metadata/cbor

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


@request_wrapper
def transaction_redeemers(self, hash: str, **kwargs):
    """
    Obtain the transaction redeemers.

    https://docs.blockfrost.io/#tag/cardano--transactions/GET/txs/{hash}/redeemers

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
def transaction_required_signers(self, hash: str, **kwargs):
    """
    Obtain the required signers of a specific transaction.

    https://docs.blockfrost.io/#tag/cardano--transactions/GET/txs/{hash}/required_signers

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
        url=f"{self.url}/txs/{hash}/required_signers",
        headers=self.default_headers
    )


@request_wrapper
def transaction_cbor(self, hash: str, **kwargs):
    """
    Obtain the transaction in CBOR format.

    https://docs.blockfrost.io/#tag/cardano--transactions/GET/txs/{hash}/cbor

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
        url=f"{self.url}/txs/{hash}/cbor",
        headers=self.default_headers
    )


@request_wrapper
def transaction_submit(self, file_path: str, **kwargs):
    """
    Submit an already serialized transaction to the network.

    https://docs.blockfrost.io/#tag/cardano--transactions/POST/tx/submit

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


@request_wrapper
def transaction_submit_cbor(self, tx_cbor: Union[bytes, str], **kwargs):
    """
    Submit an already serialized transaction to the network.

    https://docs.blockfrost.io/#tag/cardano--transactions/POST/tx/submit

    :param tx_cbor: Transaction in CBOR format, either as a hex-encoded string or as bytes.
    :type tx_cbor: Union[str, bytes]
    :returns str object.
    :rtype str
    :raises ApiError: If API fails
    :raises Exception: If the API response is somehow malformed.
    """

    # Convert to bytes
    if isinstance(tx_cbor, str):
        data = bytes.fromhex(tx_cbor)
    else:
        data = tx_cbor

    header = self.default_headers
    header['Content-Type'] = 'application/cbor'
    return requests.post(
        url=f"{self.url}/tx/submit",
        headers=header,
        data=data,
    )


@request_wrapper
def transaction_evaluate(self, file_path: str, **kwargs):
    """
    Submit an already serialized transaction to evaluate how much execution units it requires.

    https://docs.blockfrost.io/#tag/cardano--utilities/POST/utils/txs/evaluate

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
            url=f"{self.url}/utils/txs/evaluate",
            headers=header,
            data=file,
        )


@request_wrapper
def transaction_evaluate_cbor(self, tx_cbor: Union[bytes, str], **kwargs):
    """
    Submit an already serialized transaction to evaluate how much execution units it requires.

    https://docs.blockfrost.io/#tag/cardano--utilities/POST/utils/txs/evaluate

    :param tx_cbor: Transaction in CBOR format, either as a hex-encoded string or as bytes.
    :type tx_cbor: Union[str, bytes]
    :returns str object.
    :rtype str
    :raises ApiError: If API fails
    :raises Exception: If the API response is somehow malformed.
    """
    header = self.default_headers
    header['Content-Type'] = 'application/cbor'

    # Convert bytes to hex
    if isinstance(tx_cbor, bytes):
        data = tx_cbor.hex()
    else:
        data = tx_cbor

    return requests.post(
        url=f"{self.url}/utils/txs/evaluate",
        headers=header,
        data=data,
    )


@request_wrapper
def transaction_evaluate_utxos(self, tx_cbor: Union[bytes, str], additional_utxo_set: list, **kwargs):
    """
    Submits a transaction CBOR and additional utxo set to evaluate how much execution units it requires.

    https://docs.blockfrost.io/#tag/cardano--utilities/POST/utils/txs/evaluate/utxos
    https://ogmios.dev/mini-protocols/local-tx-submission/#evaluatetx

    :param tx_cbor: Transaction in CBOR format, either as a hex-encoded string or as bytes.
    :type tx_cbor: Union[bytes, str]
    :param additional_utxo_set: Additional UTXO as an array of tuples [TxIn, TxOut] https://ogmios.dev/mini-protocols/local-tx-submission/#additional-utxo-set.
    :type additional_utxo_set: list
    :returns: Result of Ogmios EvaluateTx
    :rtype dict
    :raises ApiError: If API fails
    :raises Exception: If the API response is somehow malformed.
    """

    # Convert bytes to hex
    if isinstance(tx_cbor, bytes):
        data = tx_cbor.hex()
    else:
        data = tx_cbor

    headers = {
        'Content-type': 'application/json',
        **self.default_headers
    }

    payload = {
        'cbor': data,
        'additionalUtxoSet': additional_utxo_set
    }

    return requests.post(
        url=f"{self.url}/utils/txs/evaluate/utxos",
        headers=headers,
        json=payload
    )
