import requests
from blockfrost.utils import request_wrapper, list_request_wrapper


@list_request_wrapper
def governance_proposals(self, **kwargs):
    """
    List of governance proposals.

    https://docs.blockfrost.io/#tag/Cardano-Governance/paths/~1governance~1proposals/get

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
    Specific governance proposal.

    https://docs.blockfrost.io/#tag/Cardano-Governance/paths/~1governance~1proposals~1{tx_hash}~1{cert_index}/get

    :param tx_hash: Hash of the transaction containing the proposal.
    :type tx_hash: str
    :param cert_index: Certificate index within the transaction.
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


@list_request_wrapper
def governance_proposal_votes(self, tx_hash: str, cert_index: int, **kwargs):
    """
    Votes for a specific governance proposal.

    https://docs.blockfrost.io/#tag/Cardano-Governance/paths/~1governance~1proposals~1{tx_hash}~1{cert_index}~1votes/get

    :param tx_hash: Hash of the transaction containing the proposal.
    :type tx_hash: str
    :param cert_index: Certificate index within the transaction.
    :type cert_index: int
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
def governance_proposal_parameters(self, tx_hash: str, cert_index: int, **kwargs):
    """
    Parameters of a specific governance proposal.

    https://docs.blockfrost.io/#tag/Cardano-Governance/paths/~1governance~1proposals~1{tx_hash}~1{cert_index}~1parameters/get

    :param tx_hash: Hash of the transaction containing the proposal.
    :type tx_hash: str
    :param cert_index: Certificate index within the transaction.
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
    Withdrawals of a specific governance proposal.

    https://docs.blockfrost.io/#tag/Cardano-Governance/paths/~1governance~1proposals~1{tx_hash}~1{cert_index}~1withdrawals/get

    :param tx_hash: Hash of the transaction containing the proposal.
    :type tx_hash: str
    :param cert_index: Certificate index within the transaction.
    :type cert_index: int
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


@request_wrapper
def governance_proposal_metadata(self, tx_hash: str, cert_index: int, **kwargs):
    """
    Metadata of a specific governance proposal.

    https://docs.blockfrost.io/#tag/Cardano-Governance/paths/~1governance~1proposals~1{tx_hash}~1{cert_index}~1metadata/get

    :param tx_hash: Hash of the transaction containing the proposal.
    :type tx_hash: str
    :param cert_index: Certificate index within the transaction.
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


@list_request_wrapper
def governance_votes(self, **kwargs):
    """
    List of governance votes.

    https://docs.blockfrost.io/#tag/Cardano-Governance/paths/~1governance~1votes/get

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
        url=f"{self.url}/governance/votes",
        params=self.query_parameters(kwargs),
        headers=self.default_headers
    )


@request_wrapper
def governance_vote(self, tx_hash: str, cert_index: int, **kwargs):
    """
    Specific governance vote.

    https://docs.blockfrost.io/#tag/Cardano-Governance/paths/~1governance~1votes~1{tx_hash}~1{cert_index}/get

    :param tx_hash: Hash of the transaction containing the vote.
    :type tx_hash: str
    :param cert_index: Certificate index within the transaction.
    :type cert_index: int
    :param return_type: Optional. "object", "json" or "pandas". Default: "object".
    :type return_type: str
    :returns object.
    :rtype: Namespace
    :raises ApiError: If API fails
    :raises Exception: If the API response is somehow malformed.
    """
    return requests.get(
        url=f"{self.url}/governance/votes/{tx_hash}/{cert_index}",
        headers=self.default_headers
    )


@request_wrapper
def governance_drep(self, drep_id: str, **kwargs):
    """
    Specific delegated representative (DRep).

    https://docs.blockfrost.io/#tag/Cardano-Governance/paths/~1governance~1dreps~1{drep_id}/get

    :param drep_id: Bech32 or hexadecimal DRep ID.
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
def governance_dreps(self, **kwargs):
    """
    List of delegated representatives (DReps).

    https://docs.blockfrost.io/#tag/Cardano-Governance/paths/~1governance~1dreps/get

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


@list_request_wrapper
def governance_drep_votes(self, drep_id: str, **kwargs):
    """
    Votes cast by a specific delegated representative (DRep).

    https://docs.blockfrost.io/#tag/Cardano-Governance/paths/~1governance~1dreps~1{drep_id}~1votes/get

    :param drep_id: Bech32 or hexadecimal DRep ID.
    :type drep_id: str
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
def governance_drep_delegators(self, drep_id: str, **kwargs):
    """
    Delegators of a specific delegated representative (DRep).

    https://docs.blockfrost.io/#tag/Cardano-Governance/paths/~1governance~1dreps~1{drep_id}~1delegators/get

    :param drep_id: Bech32 or hexadecimal DRep ID.
    :type drep_id: str
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
    Metadata of a specific delegated representative (DRep).

    https://docs.blockfrost.io/#tag/Cardano-Governance/paths/~1governance~1dreps~1{drep_id}~1metadata/get

    :param drep_id: Bech32 or hexadecimal DRep ID.
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
    Updates for a specific delegated representative (DRep).

    https://docs.blockfrost.io/#tag/Cardano-Governance/paths/~1governance~1dreps~1{drep_id}~1updates/get

    :param drep_id: Bech32 or hexadecimal DRep ID.
    :type drep_id: str
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
def governance_committee(self, **kwargs):
    """
    Current governance committee.

    https://docs.blockfrost.io/#tag/Cardano-Governance/paths/~1governance~1committee/get

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
        url=f"{self.url}/governance/committee",
        params=self.query_parameters(kwargs),
        headers=self.default_headers
    )


@request_wrapper
def governance_committee_member(self, key_hash: str, **kwargs):
    """
    Specific governance committee member.

    https://docs.blockfrost.io/#tag/Cardano-Governance/paths/~1governance~1committee~1{key_hash}/get

    :param key_hash: Hash of the committee member's cold key.
    :type key_hash: str
    :param return_type: Optional. "object", "json" or "pandas". Default: "object".
    :type return_type: str
    :returns object.
    :rtype: Namespace
    :raises ApiError: If API fails
    :raises Exception: If the API response is somehow malformed.
    """
    return requests.get(
        url=f"{self.url}/governance/committee/{key_hash}",
        headers=self.default_headers
    )


@list_request_wrapper
def governance_committee_member_votes(self, key_hash: str, **kwargs):
    """
    Votes cast by a specific governance committee member.

    https://docs.blockfrost.io/#tag/Cardano-Governance/paths/~1governance~1committee~1{key_hash}~1votes/get

    :param key_hash: Hash of the committee member's cold key.
    :type key_hash: str
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
        url=f"{self.url}/governance/committee/{key_hash}/votes",
        params=self.query_parameters(kwargs),
        headers=self.default_headers
    )
