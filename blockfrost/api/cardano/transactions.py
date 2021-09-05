import requests
from dataclasses import dataclass
from blockfrost.utils import object_request_wrapper, object_list_request_wrapper


@dataclass
class Transaction:
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


@object_request_wrapper(Transaction)
def transaction(self, hash: str):
    """
    Return content of the requested transaction.

    https://docs.blockfrost.io/#tag/Cardano-Transactions/paths/~1txs~1{hash}/get
    """
    return requests.get(
        url=f"{self.url}/txs/{hash}",
        headers=self.default_headers
    )


@dataclass
class AccountAddressesUTXOS:
    @dataclass
    class Inputs:
        unit: str
        quantity: str

    @dataclass
    class Outputs:
        unit: str
        quantity: str

    hash: str
    inputs: [Inputs]
    outputs: [Outputs]

    def __init__(self, hash: str, inputs: [Inputs], outputs: [Outputs]) -> None:
        self.hash = hash
        self.inputs = [self.Inputs(**o) for o in inputs]
        self.outputs = [self.Outputs(**o) for o in outputs]


@object_request_wrapper(AccountAddressesUTXOS)
def transaction_utxos(self, hash: str):
    """
    Return the inputs and UTXOs of the specific transaction.

    https://docs.blockfrost.io/#tag/Cardano-Transactions/paths/~1txs~1{hash}~1utxos/get
    """
    return requests.get(
        url=f"{self.url}/txs/{hash}/utxos",
        headers=self.default_headers
    )


@dataclass
class Stake:
    cert_index: int
    hash: str
    registration: bool


@object_list_request_wrapper(Stake)
def transaction_stakes(self, hash: str):
    """
    Obtain information about (de)registration of stake addresses within a transaction.

    https://docs.blockfrost.io/#tag/Cardano-Transactions/paths/~1txs~1{hash}~1stakes/get
    """
    return requests.get(
        url=f"{self.url}/txs/{hash}/stakes",
        headers=self.default_headers
    )


@dataclass
class Delegations:
    cert_index: int
    hash: str
    pool_id: str
    active_epoch: int


@object_list_request_wrapper(Delegations)
def transaction_delegations(self, hash: str):
    """
    Obtain information about delegation certificates of a specific transaction.

    https://docs.blockfrost.io/#tag/Cardano-Transactions/paths/~1txs~1{hash}~1delegations/get
    """
    return requests.get(
        url=f"{self.url}/txs/{hash}/delegations",
        headers=self.default_headers
    )


@dataclass
class Withdrawal:
    address: str
    amount: str


@object_list_request_wrapper(Withdrawal)
def transaction_withdrawals(self, hash: str):
    """
    Obtain information about withdrawals of a specific transaction.

    https://docs.blockfrost.io/#tag/Cardano-Transactions/paths/~1txs~1{hash}~1withdrawals/get
    """
    return requests.get(
        url=f"{self.url}/txs/{hash}/withdrawals",
        headers=self.default_headers
    )


@dataclass
class MIR:
    pot: str
    cert_index: str
    address: str
    amount: str


@object_list_request_wrapper(MIR)
def transaction_mirs(self, hash: str):
    """
    Obtain information about Move Instantaneous Rewards (MIRs) of a specific transaction.

    https://docs.blockfrost.io/#tag/Cardano-Transactions/paths/~1txs~1{hash}~1mirs/get
    """
    return requests.get(
        url=f"{self.url}/txs/{hash}/mirs",
        headers=self.default_headers
    )


@dataclass
class PoolUpdate:
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


@object_list_request_wrapper(PoolUpdate)
def transaction_pool_updates(self, hash: str):
    """
    Obtain information about stake pool registration and update certificates of a specific transaction.

    https://docs.blockfrost.io/#tag/Cardano-Transactions/paths/~1txs~1{hash}~1pool_updates/get
    """
    return requests.get(
        url=f"{self.url}/txs/{hash}/pool_updates",
        headers=self.default_headers
    )


@dataclass
class PoolRetires:
    cert_index: int
    pool_id: str
    retiring_epoch: int


@object_list_request_wrapper(PoolRetires)
def transaction_pool_retires(self, hash: str):
    """
    Obtain information about stake pool retirements within a specific transaction.

    https://docs.blockfrost.io/#tag/Cardano-Transactions/paths/~1txs~1{hash}~1pool_retires/get
    """
    return requests.get(
        url=f"{self.url}/txs/{hash}/pool_retires",
        headers=self.default_headers
    )


@dataclass
class Metadata:
    label: str
    json_metadata: dict


@object_list_request_wrapper(Metadata)
def transaction_metadata(self, hash: str):
    """
    Obtain the transaction metadata.

    https://docs.blockfrost.io/#tag/Cardano-Transactions/paths/~1txs~1{hash}~1metadata/get
    """
    return requests.get(
        url=f"{self.url}/txs/{hash}/metadata",
        headers=self.default_headers
    )


@dataclass
class Metadata:
    label: str
    cbor_metadata: str


@object_list_request_wrapper(Metadata)
def transaction_metadata_cbor(self, hash: str):
    """
    Obtain the transaction metadata in CBOR.

    https://docs.blockfrost.io/#tag/Cardano-Transactions/paths/~1txs~1{hash}~1metadata~1cbor/get
    """
    return requests.get(
        url=f"{self.url}/txs/{hash}/metadata/cbor",
        headers=self.default_headers
    )


@object_request_wrapper(str)
def transaction_submit(self, file_path: str):
    """
    Submit an already serialized transaction to the network.

    https://docs.blockfrost.io/#tag/Cardano-Transactions/paths/~1tx~1submit/post
    """
    with open(file_path, 'rb') as file:
        return requests.post(
            url=f"{self.url}/tx/submit",
            headers=self.default_headers,
            data=file,
        )
