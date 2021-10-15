import requests
from dataclasses import dataclass
from blockfrost.utils import object_request_wrapper, object_list_request_wrapper


@dataclass
class TransactionResponse:
    @dataclass
    class Amount:
        unit: str
        quantity: str

    hash: str
    block: str
    block_height: int
    slot: int
    index: int
    output_amount: [Amount]
    fees: str
    deposit: str
    size: int
    invalid_before: str
    invalid_hereafter: str
    utxo_count: int
    withdrawal_count: int
    mir_cert_count: int
    delegation_count: int
    stake_cert_count: int
    pool_update_count: int
    pool_retire_count: int
    asset_mint_or_burn_count: int
    redeemer_count: int
    valid_contract: bool

    def __init__(self,
                 hash: str,
                 block: str,
                 block_height: int,
                 slot: int,
                 index: int,
                 output_amount: [Amount],
                 fees: str,
                 deposit: str,
                 size: int,
                 invalid_before: str,
                 invalid_hereafter: str,
                 utxo_count: int,
                 withdrawal_count: int,
                 mir_cert_count: int,
                 delegation_count: int,
                 stake_cert_count: int,
                 pool_update_count: int,
                 pool_retire_count: int,
                 asset_mint_or_burn_count: int,
                 redeemer_count: int,
                 valid_contract: bool,
                 ) -> None:
        self.hash = hash
        self.block = block
        self.block_height = block_height
        self.slot = slot
        self.index = index
        self.output_amount = [self.Amount(**o) for o in output_amount]
        self.fees = fees
        self.deposit = deposit
        self.size = size
        self.invalid_before = invalid_before
        self.invalid_hereafter = invalid_hereafter
        self.utxo_count = utxo_count
        self.withdrawal_count = withdrawal_count
        self.mir_cert_count = mir_cert_count
        self.delegation_count = delegation_count
        self.stake_cert_count = stake_cert_count
        self.pool_update_count = pool_update_count
        self.pool_retire_count = pool_retire_count
        self.asset_mint_or_burn_count = asset_mint_or_burn_count
        self.redeemer_count = redeemer_count
        self.valid_contract = valid_contract


@object_request_wrapper(TransactionResponse)
def transaction(self, hash: str, **kwargs):
    """
    Return content of the requested transaction.

    https://docs.blockfrost.io/#tag/Cardano-Transactions/paths/~1txs~1{hash}/get

    :param hash: Hash of the requested transaction.
    :type hash: str
    :param return_type: Optional. "object", "json" or "pandas". Default: "object".
    :type return_type: str
    :returns TransactionResponse object.
    :rtype TransactionResponse
    :raises ApiError: If API fails
    :raises Exception: If the API response is somehow malformed.
    """
    return requests.get(
        url=f"{self.url}/txs/{hash}",
        headers=self.default_headers
    )


@dataclass
class TransactionAddressUTXOSResponse:
    @dataclass
    class Inputs:
        @dataclass
        class Amount:
            unit: str
            quantity: str

        address: str
        amount: [Amount]
        tx_hash: str
        output_index: int
        data_hash: str
        collateral: bool

        def __init_(self, address, amount: [Amount], tx_hash, output_index, data_hash, collateral) -> None:
            self.address = address
            self.amount = [self.Amount(**o) for o in amount]
            self.tx_hash = tx_hash
            self.output_index = output_index
            self.data_hash = data_hash
            self.collateral = collateral

    @dataclass
    class Outputs:
        @dataclass
        class Amount:
            unit: str
            quantity: str

        address: str
        amount: [Amount]
        output_index: int
        data_hash: str

        def __init_(self, address, amount: [Amount], output_index, data_hash) -> None:
            self.address = address
            self.amount = [self.Amount(**o) for o in amount]
            self.output_index = output_index
            self.data_hash = data_hash

    hash: str
    inputs: [Inputs]
    outputs: [Outputs]

    def __init__(self, hash: str, inputs: [Inputs], outputs: [Outputs]) -> None:
        self.hash = hash
        self.inputs = [self.Inputs(**o) for o in inputs]
        self.outputs = [self.Outputs(**o) for o in outputs]


@object_request_wrapper(TransactionAddressUTXOSResponse)
def transaction_utxos(self, hash: str, **kwargs):
    """
    Return the inputs and UTXOs of the specific transaction.

    https://docs.blockfrost.io/#tag/Cardano-Transactions/paths/~1txs~1{hash}~1utxos/get

    :param hash: Hash of the requested transaction.
    :type hash: str
    :param return_type: Optional. "object", "json" or "pandas". Default: "object".
    :type return_type: str
    :returns TransactionAddressUTXOSResponse object.
    :rtype TransactionAddressUTXOSResponse
    :raises ApiError: If API fails
    :raises Exception: If the API response is somehow malformed.
    """
    return requests.get(
        url=f"{self.url}/txs/{hash}/utxos",
        headers=self.default_headers
    )


@dataclass
class TransactionStakeResponse:
    cert_index: int
    address: str
    registration: bool


@object_list_request_wrapper(TransactionStakeResponse)
def transaction_stakes(self, hash: str, **kwargs):
    """
    Obtain information about (de)registration of stake addresses within a transaction.

    https://docs.blockfrost.io/#tag/Cardano-Transactions/paths/~1txs~1{hash}~1stakes/get

    :param hash: Hash of the requested transaction.
    :type hash: str
    :param return_type: Optional. "object", "json" or "pandas". Default: "object".
    :type return_type: str
    :returns A list of TransactionStakeResponse objects.
    :rtype [TransactionStakeResponse]
    :raises ApiError: If API fails
    :raises Exception: If the API response is somehow malformed.
    """
    return requests.get(
        url=f"{self.url}/txs/{hash}/stakes",
        headers=self.default_headers
    )


@dataclass
class TransactionDelegationResponse:
    index: int
    cert_index: int
    address: str
    pool_id: str
    active_epoch: int


@object_list_request_wrapper(TransactionDelegationResponse)
def transaction_delegations(self, hash: str, **kwargs):
    """
    Obtain information about delegation certificates of a specific transaction.

    https://docs.blockfrost.io/#tag/Cardano-Transactions/paths/~1txs~1{hash}~1delegations/get

    :param hash: Hash of the requested transaction.
    :type hash: str
    :param return_type: Optional. "object", "json" or "pandas". Default: "object".
    :type return_type: str
    :returns A list of TransactionDelegationResponse objects.
    :rtype [TransactionDelegationResponse]
    :raises ApiError: If API fails
    :raises Exception: If the API response is somehow malformed.
    """
    return requests.get(
        url=f"{self.url}/txs/{hash}/delegations",
        headers=self.default_headers
    )


@dataclass
class TransactionWithdrawalResponse:
    address: str
    amount: str


@object_list_request_wrapper(TransactionWithdrawalResponse)
def transaction_withdrawals(self, hash: str, **kwargs):
    """
    Obtain information about withdrawals of a specific transaction.

    https://docs.blockfrost.io/#tag/Cardano-Transactions/paths/~1txs~1{hash}~1withdrawals/get

    :param hash: Hash of the requested transaction.
    :type hash: str
    :param return_type: Optional. "object", "json" or "pandas". Default: "object".
    :type return_type: str
    :returns A list of TransactionWithdrawalResponse objects.
    :rtype [TransactionWithdrawalResponse]
    :raises ApiError: If API fails
    :raises Exception: If the API response is somehow malformed.
    """
    return requests.get(
        url=f"{self.url}/txs/{hash}/withdrawals",
        headers=self.default_headers
    )


@dataclass
class TransactionMIRResponse:
    pot: str
    cert_index: str
    address: str
    amount: str


@object_list_request_wrapper(TransactionMIRResponse)
def transaction_mirs(self, hash: str, **kwargs):
    """
    Obtain information about Move Instantaneous Rewards (MIRs) of a specific transaction.

    https://docs.blockfrost.io/#tag/Cardano-Transactions/paths/~1txs~1{hash}~1mirs/get

    :param hash: Hash of the requested transaction.
    :type hash: str
    :param return_type: Optional. "object", "json" or "pandas". Default: "object".
    :type return_type: str
    :returns A list of TransactionMIRResponse objects.
    :rtype [TransactionMIRResponse]
    :raises ApiError: If API fails
    :raises Exception: If the API response is somehow malformed.
    """
    return requests.get(
        url=f"{self.url}/txs/{hash}/mirs",
        headers=self.default_headers
    )


@dataclass
class TransactionPoolUpdateResponse:
    @dataclass
    class PoolMetadata:
        url: str
        hash: str
        ticker: str
        name: str
        description: str
        homepage: str

    @dataclass
    class PoolRelay:
        ipv4: str
        ipv6: str
        dns: str
        dns_srv: str
        port: int

    cert_index: int
    pool_id: str
    vrf_key: str
    pledge: str
    margin_cost: float
    fixed_cost: str
    reward_account: str
    owners: [str]
    metadata: PoolMetadata
    relays: [PoolRelay]
    active_epoch: int

    def __init__(self,
                 cert_index: int,
                 pool_id: str,
                 vrf_key: str,
                 pledge: str,
                 margin_cost: float,
                 fixed_cost: str,
                 reward_account: str,
                 owners: [str],
                 metadata: PoolMetadata,
                 relays: [PoolRelay],
                 active_epoch: int) -> None:
        self.cert_index = cert_index
        self.pool_id = pool_id
        self.vrf_key = vrf_key
        self.pledge = pledge
        self.margin_cost = margin_cost
        self.fixed_cost = fixed_cost
        self.reward_account = reward_account
        self.owners = owners
        self.metadata = self.PoolMetadata(**metadata) if metadata is not None else None
        self.relays = [self.PoolRelay(**o) for o in relays]
        self.active_epoch = active_epoch


@object_list_request_wrapper(TransactionPoolUpdateResponse)
def transaction_pool_updates(self, hash: str, **kwargs):
    """
    Obtain information about stake pool registration and update certificates of a specific transaction.

    https://docs.blockfrost.io/#tag/Cardano-Transactions/paths/~1txs~1{hash}~1pool_updates/get

    :param hash: Hash of the requested transaction.
    :type hash: str
    :param return_type: Optional. "object", "json" or "pandas". Default: "object".
    :type return_type: str
    :returns A list of TransactionPoolUpdateResponse objects.
    :rtype [TransactionPoolUpdateResponse]
    :raises ApiError: If API fails
    :raises Exception: If the API response is somehow malformed.
    """
    return requests.get(
        url=f"{self.url}/txs/{hash}/pool_updates",
        headers=self.default_headers
    )


@dataclass
class TransactionPoolRetiresResponse:
    cert_index: int
    pool_id: str
    retiring_epoch: int


@object_list_request_wrapper(TransactionPoolRetiresResponse)
def transaction_pool_retires(self, hash: str, **kwargs):
    """
    Obtain information about stake pool retirements within a specific transaction.

    https://docs.blockfrost.io/#tag/Cardano-Transactions/paths/~1txs~1{hash}~1pool_retires/get

    :param hash: Hash of the requested transaction.
    :type hash: str
    :param return_type: Optional. "object", "json" or "pandas". Default: "object".
    :type return_type: str
    :returns A list of TransactionPoolRetiresResponse objects.
    :rtype [TransactionPoolRetiresResponse]
    :raises ApiError: If API fails
    :raises Exception: If the API response is somehow malformed.
    """
    return requests.get(
        url=f"{self.url}/txs/{hash}/pool_retires",
        headers=self.default_headers
    )


@dataclass
class TransactionMetadataResponse:
    label: str
    json_metadata: dict


@object_list_request_wrapper(TransactionMetadataResponse)
def transaction_metadata(self, hash: str, **kwargs):
    """
    Obtain the transaction metadata.

    https://docs.blockfrost.io/#tag/Cardano-Transactions/paths/~1txs~1{hash}~1metadata/get

    :param hash: Hash of the requested transaction.
    :type hash: str
    :param return_type: Optional. "object", "json" or "pandas". Default: "object".
    :type return_type: str
    :returns A list of TransactionMetadataResponse objects.
    :rtype [TransactionMetadataResponse]
    :raises ApiError: If API fails
    :raises Exception: If the API response is somehow malformed.
    """
    return requests.get(
        url=f"{self.url}/txs/{hash}/metadata",
        headers=self.default_headers
    )


@dataclass
class TransactionMetadataCBORResponse:
    label: str
    cbor_metadata: str
    metadata: str


@object_list_request_wrapper(TransactionMetadataCBORResponse)
def transaction_metadata_cbor(self, hash: str, **kwargs):
    """
    Obtain the transaction metadata in CBOR.

    https://docs.blockfrost.io/#tag/Cardano-Transactions/paths/~1txs~1{hash}~1metadata~1cbor/get

    :param hash: Hash of the requested transaction.
    :type hash: str
    :param return_type: Optional. "object", "json" or "pandas". Default: "object".
    :type return_type: str
    :returns A list of TransactionMetadataCBORResponse objects.
    :rtype [TransactionMetadataCBORResponse]
    :raises ApiError: If API fails
    :raises Exception: If the API response is somehow malformed.
    """
    return requests.get(
        url=f"{self.url}/txs/{hash}/metadata/cbor",
        headers=self.default_headers
    )


@dataclass
class TransactionRedeemersResponse:
    tx_index: int
    purpose: str
    script_hash: str
    datum_hash: str
    unit_mem: str
    unit_steps: str
    fee: str


@object_list_request_wrapper(TransactionRedeemersResponse)
def transaction_redeemers(self, hash: str, **kwargs):
    """
    Obtain the transaction redeemers.

    https://docs.blockfrost.io/#tag/Cardano-Transactions/paths/~1txs~1{hash}~1redeemers/get

    :param hash: Hash of the requested transaction.
    :type hash: str
    :param return_type: Optional. "object", "json" or "pandas". Default: "object".
    :type return_type: str
    :returns A list of TransactionRedeemersResponse objects.
    :rtype [TransactionRedeemersResponse]
    :raises ApiError: If API fails
    :raises Exception: If the API response is somehow malformed.
    """
    return requests.get(
        url=f"{self.url}/txs/{hash}/redeemers",
        headers=self.default_headers
    )


@object_request_wrapper()
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
