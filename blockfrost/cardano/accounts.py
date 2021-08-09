from ..utils import object_request_wrapper, list_request_wrapper
import requests


@object_request_wrapper
def accounts(self, stake_address: str) -> requests.Response:
    """
    Obtain information about a specific networkStake account.

    https://docs.blockfrost.io/#tag/Cardano-Accounts/paths/~1accounts~1{stake_address}/get
    """
    return requests.get(
        url=f"{self.url}/accounts/{stake_address}",
        headers=self.authentication_header
    )


@list_request_wrapper
def account_rewards(self, stake_address: str, **kwargs) -> requests.Response:
    """
    Obtain information about the history of a specific account.

    https://docs.blockfrost.io/#tag/Cardano-Accounts/paths/~1accounts~1{stake_address}~1rewards/get
    """
    return requests.get(
        url=f"{self.url}/accounts/{stake_address}/rewards",
        params=self.query_parameters(kwargs),
        headers=self.authentication_header
    )


@list_request_wrapper
def account_history(self, stake_address: str, **kwargs) -> requests.Response:
    """
    Obtain information about the history of a specific account.

    https://docs.blockfrost.io/#tag/Cardano-Accounts/paths/~1accounts~1{stake_address}~1history/get
    """
    return requests.get(
        url=f"{self.url}/accounts/{stake_address}/history",
        params=self.query_parameters(kwargs),
        headers=self.authentication_header
    )


@list_request_wrapper
def account_delegations(self, stake_address: str, **kwargs) -> requests.Response:
    """
    Obtain information about the delegation of a specific account.

    https://docs.blockfrost.io/#tag/Cardano-Accounts/paths/~1accounts~1{stake_address}~1delegations/get
    """
    return requests.get(
        url=f"{self.url}/accounts/{stake_address}/delegations",
        params=self.query_parameters(kwargs),
        headers=self.authentication_header
    )


@list_request_wrapper
def account_registrations(self, stake_address: str, **kwargs) -> requests.Response:
    """
    Obtain information about the registrations and deregistrations of a specific account.

    https://docs.blockfrost.io/#tag/Cardano-Accounts/paths/~1accounts~1{stake_address}~1registrations/get
    """
    return requests.get(
        url=f"{self.url}/accounts/{stake_address}/registrations",
        params=self.query_parameters(kwargs),
        headers=self.authentication_header
    )


@list_request_wrapper
def account_withdrawals(self, stake_address: str, **kwargs) -> requests.Response:
    """
    Obtain information about the withdrawals of a specific account.

    https://docs.blockfrost.io/#tag/Cardano-Accounts/paths/~1accounts~1{stake_address}~1withdrawals/get
    """
    return requests.get(
        url=f"{self.url}/accounts/{stake_address}/withdrawals",
        params=self.query_parameters(kwargs),
        headers=self.authentication_header
    )


@list_request_wrapper
def account_mirs(self, stake_address: str, **kwargs) -> requests.Response:
    """
    Obtain information about the MIRs of a specific account.

    https://docs.blockfrost.io/#tag/Cardano-Accounts/paths/~1accounts~1{stake_address}~1mirs/get
    """
    return requests.get(
        url=f"{self.url}/accounts/{stake_address}/mirs",
        params=self.query_parameters(kwargs),
        headers=self.authentication_header
    )


@list_request_wrapper
def account_addresses(self, stake_address: str, **kwargs) -> requests.Response:
    """
    Obtain information about the addresses of a specific account.

    https://docs.blockfrost.io/#tag/Cardano-Accounts/paths/~1accounts~1{stake_address}~1addresses/get
    """
    return requests.get(
        url=f"{self.url}/accounts/{stake_address}/addresses",
        params=self.query_parameters(kwargs),
        headers=self.authentication_header
    )


@list_request_wrapper
def account_addresses_assets(self, stake_address: str, **kwargs) -> requests.Response:
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
