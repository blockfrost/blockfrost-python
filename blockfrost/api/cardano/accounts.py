import requests
from dataclasses import dataclass
from blockfrost.utils import object_request_wrapper, object_list_request_wrapper


@dataclass
class AccountResponse:
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


@object_request_wrapper(AccountResponse)
def accounts(self, stake_address: str, **kwargs):
    """
    Obtain information about a specific networkStake account.

    https://docs.blockfrost.io/#tag/Cardano-Accounts/paths/~1accounts~1{stake_address}/get

    :param stake_address: Bech32 stake address.
    :type stake_address: str
    :param return_type: Optional. "object", "json" or "pandas". Default: "object".
    :type return_type: str
    :returns AccountResponse object.
    :rtype: AccountResponse
    :raises ApiError: If API fails
    :raises Exception: If the API response is somehow malformed.
    """
    return requests.get(
        url=f"{self.url}/accounts/{stake_address}",
        headers=self.default_headers
    )


@dataclass
class AccountRewardResponse:
    epoch: int
    amount: str
    pool_id: str


@object_list_request_wrapper(AccountRewardResponse)
def account_rewards(self, stake_address: str, **kwargs):
    """
    Obtain information about the history of a specific account.

    https://docs.blockfrost.io/#tag/Cardano-Accounts/paths/~1accounts~1{stake_address}~1rewards/get

    :param stake_address: Bech32 stake address.
    :type stake_address: str
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
    :returns A list of AccountRewardResponse objects.
    :rtype: [AccountRewardResponse]
    :raises ApiError: If API fails
    :raises Exception: If the API response is somehow malformed.
    """
    return requests.get(
        url=f"{self.url}/accounts/{stake_address}/rewards",
        params=self.query_parameters(kwargs),
        headers=self.default_headers
    )


@dataclass
class AccountHistoryResponse:
    active_epoch: int
    amount: str
    pool_id: str


@object_list_request_wrapper(AccountHistoryResponse)
def account_history(self, stake_address: str, **kwargs):
    """
    Obtain information about the history of a specific account.

    https://docs.blockfrost.io/#tag/Cardano-Accounts/paths/~1accounts~1{stake_address}~1history/get

    :param stake_address: Bech32 stake address.
    :type stake_address: str
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
    :returns A list of AccountHistoryResponse objects.
    :rtype [AccountHistoryResponse]
    :raises ApiError: If API fails
    :raises Exception: If the API response is somehow malformed.
    """
    return requests.get(
        url=f"{self.url}/accounts/{stake_address}/history",
        params=self.query_parameters(kwargs),
        headers=self.default_headers
    )


@dataclass
class AccountDelegationResponse:
    active_epoch: int
    tx_hash: str
    amount: str
    pool_id: str


@object_list_request_wrapper(AccountDelegationResponse)
def account_delegations(self, stake_address: str, **kwargs):
    """
    Obtain information about the delegation of a specific account.

    https://docs.blockfrost.io/#tag/Cardano-Accounts/paths/~1accounts~1{stake_address}~1delegations/get

    :param stake_address: Bech32 stake address.
    :type stake_address: str
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
    :returns A list of AccountDelegationResponse objects.
    :rtype: [AccountDelegationResponse]
    :raises ApiError: If API fails
    :raises Exception: If the API response is somehow malformed.
    """
    return requests.get(
        url=f"{self.url}/accounts/{stake_address}/delegations",
        params=self.query_parameters(kwargs),
        headers=self.default_headers
    )


@dataclass
class AccountRegistrationResponse:
    tx_hash: str
    action: str


@object_list_request_wrapper(AccountRegistrationResponse)
def account_registrations(self, stake_address: str, **kwargs):
    """
    Obtain information about the registrations and deregistrations of a specific account.

    https://docs.blockfrost.io/#tag/Cardano-Accounts/paths/~1accounts~1{stake_address}~1registrations/get

    :param stake_address: Bech32 stake address.
    :type stake_address: str
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
    :returns A list of AccountRegistrationResponse objects.
    :rtype: [AccountRegistrationResponse]
    :raises ApiError: If API fails
    :raises Exception: If the API response is somehow malformed.
    """
    return requests.get(
        url=f"{self.url}/accounts/{stake_address}/registrations",
        params=self.query_parameters(kwargs),
        headers=self.default_headers
    )


@dataclass
class AccountWithdrawalResponse:
    tx_hash: str
    amount: str


@object_list_request_wrapper(AccountWithdrawalResponse)
def account_withdrawals(self, stake_address: str, **kwargs):
    """
    Obtain information about the withdrawals of a specific account.

    https://docs.blockfrost.io/#tag/Cardano-Accounts/paths/~1accounts~1{stake_address}~1withdrawals/get

    :param stake_address: Bech32 stake address.
    :type stake_address: str
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
    :returns A list of AccountWithdrawalResponse objects.
    :rtype: [AccountWithdrawalResponse]
    :raises ApiError: If API fails
    :raises Exception: If the API response is somehow malformed.
    """
    return requests.get(
        url=f"{self.url}/accounts/{stake_address}/withdrawals",
        params=self.query_parameters(kwargs),
        headers=self.default_headers
    )


@dataclass
class AccountMIRSResponse:
    tx_hash: str
    amount: str


@object_list_request_wrapper(AccountMIRSResponse)
def account_mirs(self, stake_address: str, **kwargs):
    """
    Obtain information about the MIRs of a specific account.

    https://docs.blockfrost.io/#tag/Cardano-Accounts/paths/~1accounts~1{stake_address}~1mirs/get

    :param stake_address: Bech32 stake address.
    :type stake_address: str
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
    :returns A list of AccountMIRSResponse objects.
    :rtype: [AccountMIRSResponse]
    :raises ApiError: If API fails
    :raises Exception: If the API response is somehow malformed.
    """
    return requests.get(
        url=f"{self.url}/accounts/{stake_address}/mirs",
        params=self.query_parameters(kwargs),
        headers=self.default_headers
    )


@dataclass
class AccountAddressResponse:
    address: str


@object_list_request_wrapper(AccountAddressResponse)
def account_addresses(self, stake_address: str, **kwargs):
    """
    Obtain information about the addresses of a specific account.

    https://docs.blockfrost.io/#tag/Cardano-Accounts/paths/~1accounts~1{stake_address}~1addresses/get

    :param stake_address: Bech32 stake address.
    :type stake_address: str
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
    :returns A list of AccountAddressResponse objects.
    :rtype: [AccountAddressResponse]
    :raises ApiError: If API fails
    :raises Exception: If the API response is somehow malformed.
    """
    return requests.get(
        url=f"{self.url}/accounts/{stake_address}/addresses",
        params=self.query_parameters(kwargs),
        headers=self.default_headers
    )


@dataclass
class AccountAddressesAssetResponse:
    unit: str
    quantity: str


@object_list_request_wrapper(AccountAddressesAssetResponse)
def account_addresses_assets(self, stake_address: str, **kwargs):
    """
    Obtain information about assets associated with addresses of a specific account.

    Be careful, as an account could be part of a mangled address and does not necessarily mean the addresses are owned by user as the account.

    https://docs.blockfrost.io/#tag/Cardano-Accounts/paths/~1accounts~1{stake_address}~1addresses~1assets/get

    :param stake_address: Bech32 stake address.
    :type stake_address: str
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
    :returns A list of AccountAddressesAssetResponse objects.
    :rtype: [AccountAddressesAssetResponse]
    :raises ApiError: If API fails
    :raises Exception: If the API response is somehow malformed.
    """
    return requests.get(
        url=f"{self.url}/accounts/{stake_address}/addresses/assets",
        params=self.query_parameters(kwargs),
        headers=self.default_headers
    )
