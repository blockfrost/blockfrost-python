import requests
from dataclasses import dataclass
from blockfrost.utils import object_request_wrapper, object_list_request_wrapper


@dataclass
class Account:
    stake_address: str
    active: bool
    active_epoch: int
    controlled_amount: str
    rewards_sum: str
    withdrawals_sum: str
    reserves_sum: str
    treasury_sum: str
    withdrawable_amount: str
    pool_id: str


@object_request_wrapper(Account)
def accounts(self, stake_address: str):
    """
    Obtain information about a specific networkStake account.

    https://docs.blockfrost.io/#tag/Cardano-Accounts/paths/~1accounts~1{stake_address}/get
    """
    return requests.get(
        url=f"{self.url}/accounts/{stake_address}",
        headers=self.authentication_header
    )


@dataclass
class AccountReward:
    epoch: int
    amount: str
    pool_id: str


@object_list_request_wrapper(AccountReward)
def account_rewards(self, stake_address: str, **kwargs):
    """
    Obtain information about the history of a specific account.

    https://docs.blockfrost.io/#tag/Cardano-Accounts/paths/~1accounts~1{stake_address}~1rewards/get
    """
    return requests.get(
        url=f"{self.url}/accounts/{stake_address}/rewards",
        params=self.query_parameters(kwargs),
        headers=self.authentication_header
    )


@dataclass
class AccountHistory:
    active_epoch: int
    amount: str
    pool_id: str


@object_list_request_wrapper(AccountHistory)
def account_history(self, stake_address: str, **kwargs):
    """
    Obtain information about the history of a specific account.

    https://docs.blockfrost.io/#tag/Cardano-Accounts/paths/~1accounts~1{stake_address}~1history/get
    """
    return requests.get(
        url=f"{self.url}/accounts/{stake_address}/history",
        params=self.query_parameters(kwargs),
        headers=self.authentication_header
    )


@dataclass
class AccountDelegation:
    active_epoch: int
    tx_hash: str
    amount: str
    pool_id: str


@object_list_request_wrapper(AccountDelegation)
def account_delegations(self, stake_address: str, **kwargs):
    """
    Obtain information about the delegation of a specific account.

    https://docs.blockfrost.io/#tag/Cardano-Accounts/paths/~1accounts~1{stake_address}~1delegations/get
    """
    return requests.get(
        url=f"{self.url}/accounts/{stake_address}/delegations",
        params=self.query_parameters(kwargs),
        headers=self.authentication_header
    )


@dataclass
class AccountRegistration:
    tx_hash: str
    action: str


@object_list_request_wrapper(AccountRegistration)
def account_registrations(self, stake_address: str, **kwargs):
    """
    Obtain information about the registrations and deregistrations of a specific account.

    https://docs.blockfrost.io/#tag/Cardano-Accounts/paths/~1accounts~1{stake_address}~1registrations/get
    """
    return requests.get(
        url=f"{self.url}/accounts/{stake_address}/registrations",
        params=self.query_parameters(kwargs),
        headers=self.authentication_header
    )


@dataclass
class AccountWithdrawals:
    tx_hash: str
    amount: str


@object_list_request_wrapper(AccountWithdrawals)
def account_withdrawals(self, stake_address: str, **kwargs):
    """
    Obtain information about the withdrawals of a specific account.

    https://docs.blockfrost.io/#tag/Cardano-Accounts/paths/~1accounts~1{stake_address}~1withdrawals/get
    """
    return requests.get(
        url=f"{self.url}/accounts/{stake_address}/withdrawals",
        params=self.query_parameters(kwargs),
        headers=self.authentication_header
    )


@dataclass
class AccountMIRS:
    tx_hash: str
    amount: str


@object_list_request_wrapper(AccountMIRS)
def account_mirs(self, stake_address: str, **kwargs):
    """
    Obtain information about the MIRs of a specific account.

    https://docs.blockfrost.io/#tag/Cardano-Accounts/paths/~1accounts~1{stake_address}~1mirs/get
    """
    return requests.get(
        url=f"{self.url}/accounts/{stake_address}/mirs",
        params=self.query_parameters(kwargs),
        headers=self.authentication_header
    )


@dataclass
class AccountAddress:
    address: str


@object_list_request_wrapper(AccountAddress)
def account_addresses(self, stake_address: str, **kwargs):
    """
    Obtain information about the addresses of a specific account.

    https://docs.blockfrost.io/#tag/Cardano-Accounts/paths/~1accounts~1{stake_address}~1addresses/get
    """
    return requests.get(
        url=f"{self.url}/accounts/{stake_address}/addresses",
        params=self.query_parameters(kwargs),
        headers=self.authentication_header
    )


@dataclass
class AccountAddressesAsset:
    unit: str
    quantity: str


@object_list_request_wrapper(AccountAddressesAsset)
def account_addresses_assets(self, stake_address: str, **kwargs):
    """
    Obtain information about assets associated with addresses of a specific account.

    Be careful, as an account could be part of a mangled address and does not necessarily mean the addresses are owned by user as the account.

    https://docs.blockfrost.io/#tag/Cardano-Accounts/paths/~1accounts~1{stake_address}~1addresses~1assets/get
    """
    return requests.get(
        url=f"{self.url}/accounts/{stake_address}/addresses/assets",
        params=self.query_parameters(kwargs),
        headers=self.authentication_header
    )
