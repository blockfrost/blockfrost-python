import requests
from blockfrost.utils import request_wrapper, list_request_wrapper


@request_wrapper
def accounts(self, stake_address: str, **kwargs):
    """
    Obtain information about a specific networkStake account.

    https://docs.blockfrost.io/#tag/Cardano-Accounts/paths/~1accounts~1{stake_address}/get

    :param stake_address: Bech32 stake address.
    :type stake_address: str
    :param return_type: Optional. "object", "json" or "pandas". Default: "object".
    :type return_type: str
    :returns object.
    :rtype: Namespace
    :raises ApiError: If API fails
    :raises Exception: If the API response is somehow malformed.
    """
    return requests.get(
        url=f"{self.url}/accounts/{stake_address}",
        headers=self.default_headers
    )


@list_request_wrapper
def account_rewards(self, stake_address: str, **kwargs):
    """
    Obtain information about the history of a specific account.

    https://docs.blockfrost.io/#tag/Cardano-Accounts/paths/~1accounts~1{stake_address}~1rewards/get

    :param stake_address: Bech32 stake address.
    :type stake_address: str
    :param return_type: Optional. "object", "json" or "pandas". Default: "object".
    :type return_type: str
    :param gather_pages: Optional. Default: false. Will collect all pages into one return
    :type gather_pages: bool
    :param count: Optional. Default: 100. The number of results displayed on one page.
    :type count: int
    :param page: Optional. The page number for listing the results.
    :type page: int
    :param order: Optional. "asc" or "desc". Default: "asc".
    :type order: str
    :returns A list of objects.
    :rtype [Namespace]
    :raises ApiError: If API fails
    :raises Exception: If the API response is somehow malformed.
    """
    return requests.get(
        url=f"{self.url}/accounts/{stake_address}/rewards",
        params=self.query_parameters(kwargs),
        headers=self.default_headers
    )


@list_request_wrapper
def account_history(self, stake_address: str, **kwargs):
    """
    Obtain information about the history of a specific account.

    https://docs.blockfrost.io/#tag/Cardano-Accounts/paths/~1accounts~1{stake_address}~1history/get

    :param stake_address: Bech32 stake address.
    :type stake_address: str
    :param return_type: Optional. "object", "json" or "pandas". Default: "object".
    :type return_type: str
    :param gather_pages: Optional. Default: false. Will collect all pages into one return
    :type gather_pages: bool
    :param count: Optional. Default: 100. The number of results displayed on one page.
    :type count: int
    :param page: Optional. The page number for listing the results.
    :type page: int
    :param order: Optional. "asc" or "desc". Default: "asc".
    :type order: str
    :returns A list of objects.
    :rtype [Namespace]
    :raises ApiError: If API fails
    :raises Exception: If the API response is somehow malformed.
    """
    return requests.get(
        url=f"{self.url}/accounts/{stake_address}/history",
        params=self.query_parameters(kwargs),
        headers=self.default_headers
    )


@list_request_wrapper
def account_delegations(self, stake_address: str, **kwargs):
    """
    Obtain information about the delegation of a specific account.

    https://docs.blockfrost.io/#tag/Cardano-Accounts/paths/~1accounts~1{stake_address}~1delegations/get

    :param stake_address: Bech32 stake address.
    :type stake_address: str
    :param return_type: Optional. "object", "json" or "pandas". Default: "object".
    :type return_type: str
    :param gather_pages: Optional. Default: false. Will collect all pages into one return
    :type gather_pages: bool
    :param count: Optional. Default: 100. The number of results displayed on one page.
    :type count: int
    :param page: Optional. The page number for listing the results.
    :type page: int
    :param order: Optional. "asc" or "desc". Default: "asc".
    :type order: str
    :returns A list of objects.
    :rtype [Namespace]
    :raises ApiError: If API fails
    :raises Exception: If the API response is somehow malformed.
    """
    return requests.get(
        url=f"{self.url}/accounts/{stake_address}/delegations",
        params=self.query_parameters(kwargs),
        headers=self.default_headers
    )


@list_request_wrapper
def account_registrations(self, stake_address: str, **kwargs):
    """
    Obtain information about the registrations and deregistrations of a specific account.

    https://docs.blockfrost.io/#tag/Cardano-Accounts/paths/~1accounts~1{stake_address}~1registrations/get

    :param stake_address: Bech32 stake address.
    :type stake_address: str
    :param return_type: Optional. "object", "json" or "pandas". Default: "object".
    :type return_type: str
    :param gather_pages: Optional. Default: false. Will collect all pages into one return
    :type gather_pages: bool
    :param count: Optional. Default: 100. The number of results displayed on one page.
    :type count: int
    :param page: Optional. The page number for listing the results.
    :type page: int
    :param order: Optional. "asc" or "desc". Default: "asc".
    :type order: str
    :returns A list of objects.
    :rtype [Namespace]
    :raises ApiError: If API fails
    :raises Exception: If the API response is somehow malformed.
    """
    return requests.get(
        url=f"{self.url}/accounts/{stake_address}/registrations",
        params=self.query_parameters(kwargs),
        headers=self.default_headers
    )


@list_request_wrapper
def account_withdrawals(self, stake_address: str, **kwargs):
    """
    Obtain information about the withdrawals of a specific account.

    https://docs.blockfrost.io/#tag/Cardano-Accounts/paths/~1accounts~1{stake_address}~1withdrawals/get

    :param stake_address: Bech32 stake address.
    :type stake_address: str
    :param return_type: Optional. "object", "json" or "pandas". Default: "object".
    :type return_type: str
    :param gather_pages: Optional. Default: false. Will collect all pages into one return
    :type gather_pages: bool
    :param count: Optional. Default: 100. The number of results displayed on one page.
    :type count: int
    :param page: Optional. The page number for listing the results.
    :type page: int
    :param order: Optional. "asc" or "desc". Default: "asc".
    :type order: str
    :returns A list of objects.
    :rtype [Namespace]
    :raises ApiError: If API fails
    :raises Exception: If the API response is somehow malformed.
    """
    return requests.get(
        url=f"{self.url}/accounts/{stake_address}/withdrawals",
        params=self.query_parameters(kwargs),
        headers=self.default_headers
    )


@list_request_wrapper
def account_mirs(self, stake_address: str, **kwargs):
    """
    Obtain information about the MIRs of a specific account.

    https://docs.blockfrost.io/#tag/Cardano-Accounts/paths/~1accounts~1{stake_address}~1mirs/get

    :param stake_address: Bech32 stake address.
    :type stake_address: str
    :param return_type: Optional. "object", "json" or "pandas". Default: "object".
    :type return_type: str
    :param gather_pages: Optional. Default: false. Will collect all pages into one return
    :type gather_pages: bool
    :param count: Optional. Default: 100. The number of results displayed on one page.
    :type count: int
    :param page: Optional. The page number for listing the results.
    :type page: int
    :param order: Optional. "asc" or "desc". Default: "asc".
    :type order: str
    :returns A list of objects.
    :rtype [Namespace]
    :raises ApiError: If API fails
    :raises Exception: If the API response is somehow malformed.
    """
    return requests.get(
        url=f"{self.url}/accounts/{stake_address}/mirs",
        params=self.query_parameters(kwargs),
        headers=self.default_headers
    )


@list_request_wrapper
def account_addresses(self, stake_address: str, **kwargs):
    """
    Obtain information about the addresses of a specific account.

    https://docs.blockfrost.io/#tag/Cardano-Accounts/paths/~1accounts~1{stake_address}~1addresses/get

    :param stake_address: Bech32 stake address.
    :type stake_address: str
    :param return_type: Optional. "object", "json" or "pandas". Default: "object".
    :type return_type: str
    :param gather_pages: Optional. Default: false. Will collect all pages into one return
    :type gather_pages: bool
    :param count: Optional. Default: 100. The number of results displayed on one page.
    :type count: int
    :param page: Optional. The page number for listing the results.
    :type page: int
    :param order: Optional. "asc" or "desc". Default: "asc".
    :type order: str
    :returns A list of objects.
    :rtype [Namespace]
    :raises ApiError: If API fails
    :raises Exception: If the API response is somehow malformed.
    """
    return requests.get(
        url=f"{self.url}/accounts/{stake_address}/addresses",
        params=self.query_parameters(kwargs),
        headers=self.default_headers
    )


@list_request_wrapper
def account_addresses_assets(self, stake_address: str, **kwargs):
    """
    Obtain information about assets associated with addresses of a specific account.

    Be careful, as an account could be part of a mangled address and does not necessarily mean the addresses are owned by user as the account.

    https://docs.blockfrost.io/#tag/Cardano-Accounts/paths/~1accounts~1{stake_address}~1addresses~1assets/get

    :param stake_address: Bech32 stake address.
    :type stake_address: str
    :param return_type: Optional. "object", "json" or "pandas". Default: "object".
    :type return_type: str
    :param gather_pages: Optional. Default: false. Will collect all pages into one return
    :type gather_pages: bool
    :param count: Optional. Default: 100. The number of results displayed on one page.
    :type count: int
    :param page: Optional. The page number for listing the results.
    :type page: int
    :param order: Optional. "asc" or "desc". Default: "asc".
    :type order: str
    :returns A list of objects.
    :rtype [Namespace]
    :raises ApiError: If API fails
    :raises Exception: If the API response is somehow malformed.
    """
    return requests.get(
        url=f"{self.url}/accounts/{stake_address}/addresses/assets",
        params=self.query_parameters(kwargs),
        headers=self.default_headers
    )


@request_wrapper
def account_addresses_total(self, stake_address: str, **kwargs):
    """
    Obtain summed details about all addresses associated with a given account.

    Be careful, as an account could be part of a mangled address and does not necessarily mean the addresses are owned by user as the account.

    https://docs.blockfrost.io/#tag/Cardano-Addresses/paths/~1accounts~1{stake_address}~1addresses~1total/get

    :param stake_address: Bech32 address.
    :type stake_address: str
    :param return_type: Optional. "object", "json" or "pandas". Default: "object".
    :type return_type: str
    :returns object.
    :rtype: Namespace
    :raises ApiError: If API fails
    :raises Exception: If the API response is somehow malformed.
    """
    return requests.get(
        url=f"{self.url}/accounts/{stake_address}/addresses/total",
        headers=self.default_headers
    )
