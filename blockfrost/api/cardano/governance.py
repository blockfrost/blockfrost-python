import requests
from blockfrost.utils import request_wrapper, list_request_wrapper


@list_request_wrapper
def governance_dreps(self, **kwargs):
    """
    Return the list of registered delegated representatives (DReps).

    https://docs.blockfrost.io/#tag/cardano--governance/GET/governance/dreps

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
        url=f"{self.url}/governance/dreps",
        params=self.query_parameters(kwargs),
        headers=self.default_headers
    )


@request_wrapper
def governance_drep(self, drep_id: str, **kwargs):
    """
    Return information about a specific delegated representative (DRep).

    https://docs.blockfrost.io/#tag/cardano--governance/GET/governance/dreps/{drep_id}

    :param drep_id: The DRep ID (Bech32 or hex encoded).
    :type drep_id: str
    :param return_type: Optional. "object", "json" or "pandas". Default: "object".
    :type return_type: str
    :returns object.
    :rtype: Namespace
    :raises ApiError: If API fails
    :raises Exception: If the API response is somehow malformed.
    """
    return requests.get(
        url=f"{self.url}/governance/dreps/{drep_id}",
        headers=self.default_headers
    )


@list_request_wrapper
def governance_drep_delegators(self, drep_id: str, **kwargs):
    """
    Return the list of delegators to a specific DRep.

    https://docs.blockfrost.io/#tag/cardano--governance/GET/governance/dreps/{drep_id}/delegators

    :param drep_id: The DRep ID (Bech32 or hex encoded).
    :type drep_id: str
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
        url=f"{self.url}/governance/dreps/{drep_id}/delegators",
        params=self.query_parameters(kwargs),
        headers=self.default_headers
    )


@request_wrapper
def governance_drep_metadata(self, drep_id: str, **kwargs):
    """
    Return the metadata of a specific DRep.

    https://docs.blockfrost.io/#tag/cardano--governance/GET/governance/dreps/{drep_id}/metadata

    :param drep_id: The DRep ID (Bech32 or hex encoded).
    :type drep_id: str
    :param return_type: Optional. "object", "json" or "pandas". Default: "object".
    :type return_type: str
    :returns object.
    :rtype: Namespace
    :raises ApiError: If API fails
    :raises Exception: If the API response is somehow malformed.
    """
    return requests.get(
        url=f"{self.url}/governance/dreps/{drep_id}/metadata",
        headers=self.default_headers
    )


@list_request_wrapper
def governance_drep_updates(self, drep_id: str, **kwargs):
    """
    Return the list of certificate updates to a specific DRep.

    https://docs.blockfrost.io/#tag/cardano--governance/GET/governance/dreps/{drep_id}/updates

    :param drep_id: The DRep ID (Bech32 or hex encoded).
    :type drep_id: str
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
        url=f"{self.url}/governance/dreps/{drep_id}/updates",
        params=self.query_parameters(kwargs),
        headers=self.default_headers
    )


@list_request_wrapper
def governance_drep_votes(self, drep_id: str, **kwargs):
    """
    Return the list of votes by a specific DRep.

    https://docs.blockfrost.io/#tag/cardano--governance/GET/governance/dreps/{drep_id}/votes

    :param drep_id: The DRep ID (Bech32 or hex encoded).
    :type drep_id: str
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
        url=f"{self.url}/governance/dreps/{drep_id}/votes",
        params=self.query_parameters(kwargs),
        headers=self.default_headers
    )


@list_request_wrapper
def governance_proposals(self, **kwargs):
    """
    Return the list of governance proposals.

    https://docs.blockfrost.io/#tag/cardano--governance/GET/governance/proposals

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
        url=f"{self.url}/governance/proposals",
        params=self.query_parameters(kwargs),
        headers=self.default_headers
    )


@request_wrapper
def governance_proposal(self, tx_hash: str, cert_index: int, **kwargs):
    """
    Return information about a specific governance proposal.

    https://docs.blockfrost.io/#tag/cardano--governance/GET/governance/proposals/{tx_hash}/{cert_index}

    :param tx_hash: The transaction hash of the proposal.
    :type tx_hash: str
    :param cert_index: The index of the certificate within the proposal transaction.
    :type cert_index: int
    :param return_type: Optional. "object", "json" or "pandas". Default: "object".
    :type return_type: str
    :returns object.
    :rtype: Namespace
    :raises ApiError: If API fails
    :raises Exception: If the API response is somehow malformed.
    """
    return requests.get(
        url=f"{self.url}/governance/proposals/{tx_hash}/{cert_index}",
        headers=self.default_headers
    )


@request_wrapper
def governance_proposal_parameters(self, tx_hash: str, cert_index: int, **kwargs):
    """
    Return the parameters of a specific governance proposal.

    https://docs.blockfrost.io/#tag/cardano--governance/GET/governance/proposals/{tx_hash}/{cert_index}/parameters

    :param tx_hash: The transaction hash of the proposal.
    :type tx_hash: str
    :param cert_index: The index of the certificate within the proposal transaction.
    :type cert_index: int
    :param return_type: Optional. "object", "json" or "pandas". Default: "object".
    :type return_type: str
    :returns object.
    :rtype: Namespace
    :raises ApiError: If API fails
    :raises Exception: If the API response is somehow malformed.
    """
    return requests.get(
        url=f"{self.url}/governance/proposals/{tx_hash}/{cert_index}/parameters",
        headers=self.default_headers
    )


@list_request_wrapper
def governance_proposal_withdrawals(self, tx_hash: str, cert_index: int, **kwargs):
    """
    Return the withdrawals of a specific governance proposal.

    https://docs.blockfrost.io/#tag/cardano--governance/GET/governance/proposals/{tx_hash}/{cert_index}/withdrawals

    :param tx_hash: The transaction hash of the proposal.
    :type tx_hash: str
    :param cert_index: The index of the certificate within the proposal transaction.
    :type cert_index: int
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
        url=f"{self.url}/governance/proposals/{tx_hash}/{cert_index}/withdrawals",
        params=self.query_parameters(kwargs),
        headers=self.default_headers
    )


@list_request_wrapper
def governance_proposal_votes(self, tx_hash: str, cert_index: int, **kwargs):
    """
    Return the votes of a specific governance proposal.

    https://docs.blockfrost.io/#tag/cardano--governance/GET/governance/proposals/{tx_hash}/{cert_index}/votes

    :param tx_hash: The transaction hash of the proposal.
    :type tx_hash: str
    :param cert_index: The index of the certificate within the proposal transaction.
    :type cert_index: int
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
        url=f"{self.url}/governance/proposals/{tx_hash}/{cert_index}/votes",
        params=self.query_parameters(kwargs),
        headers=self.default_headers
    )


@request_wrapper
def governance_proposal_metadata(self, tx_hash: str, cert_index: int, **kwargs):
    """
    Return the metadata of a specific governance proposal.

    https://docs.blockfrost.io/#tag/cardano--governance/GET/governance/proposals/{tx_hash}/{cert_index}/metadata

    :param tx_hash: The transaction hash of the proposal.
    :type tx_hash: str
    :param cert_index: The index of the certificate within the proposal transaction.
    :type cert_index: int
    :param return_type: Optional. "object", "json" or "pandas". Default: "object".
    :type return_type: str
    :returns object.
    :rtype: Namespace
    :raises ApiError: If API fails
    :raises Exception: If the API response is somehow malformed.
    """
    return requests.get(
        url=f"{self.url}/governance/proposals/{tx_hash}/{cert_index}/metadata",
        headers=self.default_headers
    )
