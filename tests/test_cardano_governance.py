import os
from blockfrost import BlockFrostApi, ApiError
from blockfrost.utils import convert_json_to_object


tx_hash = 'example_tx_hash'
cert_index = 0
drep_id = 'example_drep_id'
key_hash = 'example_key_hash'


def test_governance_proposals(requests_mock):
    api = BlockFrostApi()
    mock_data = [
        {"id": "1", "title": "Proposal 1", "status": "active"},
        {"id": "2", "title": "Proposal 2", "status": "closed"}
    ]
    requests_mock.get(f"{api.url}/governance/proposals", json=mock_data)
    assert api.governance_proposals() == convert_json_to_object(mock_data)


def test_integration_governance_proposals():
    if os.getenv('BLOCKFROST_PROJECT_ID_MAINNET'):
        api = BlockFrostApi(project_id=os.getenv('BLOCKFROST_PROJECT_ID_MAINNET'))
        assert api.governance_proposals()


def test_governance_proposal(requests_mock):
    api = BlockFrostApi()
    mock_data = {"id": "1", "title": "Proposal 1", "status": "active"}
    requests_mock.get(f"{api.url}/governance/proposals/{tx_hash}/{cert_index}", json=mock_data)
    assert api.governance_proposal(tx_hash=tx_hash, cert_index=cert_index) == convert_json_to_object(mock_data)


def test_integration_governance_proposal():
    if os.getenv('BLOCKFROST_PROJECT_ID_MAINNET'):
        api = BlockFrostApi(project_id=os.getenv('BLOCKFROST_PROJECT_ID_MAINNET'))
        assert api.governance_proposal(tx_hash=tx_hash, cert_index=cert_index)


def test_governance_proposal_votes(requests_mock):
    api = BlockFrostApi()
    mock_data = [
        {"voter": "voter1", "vote": "yes"},
        {"voter": "voter2", "vote": "no"}
    ]
    requests_mock.get(f"{api.url}/governance/proposals/{tx_hash}/{cert_index}/votes", json=mock_data)
    assert api.governance_proposal_votes(tx_hash=tx_hash, cert_index=cert_index) == convert_json_to_object(mock_data)


def test_integration_governance_proposal_votes():
    if os.getenv('BLOCKFROST_PROJECT_ID_MAINNET'):
        api = BlockFrostApi(project_id=os.getenv('BLOCKFROST_PROJECT_ID_MAINNET'))
        assert api.governance_proposal_votes(tx_hash=tx_hash, cert_index=cert_index)


def test_governance_votes(requests_mock):
    api = BlockFrostApi()
    mock_data = [
        {"voter": "voter1", "vote": "yes"},
        {"voter": "voter2", "vote": "no"}
    ]
    requests_mock.get(f"{api.url}/governance/votes", json=mock_data)
    assert api.governance_votes() == convert_json_to_object(mock_data)


def test_integration_governance_votes():
    if os.getenv('BLOCKFROST_PROJECT_ID_MAINNET'):
        api = BlockFrostApi(project_id=os.getenv('BLOCKFROST_PROJECT_ID_MAINNET'))
        assert api.governance_votes()


def test_governance_vote(requests_mock):
    api = BlockFrostApi()
    mock_data = {"voter": "voter1", "vote": "yes"}
    requests_mock.get(f"{api.url}/governance/votes/{tx_hash}/{cert_index}", json=mock_data)
    assert api.governance_vote(tx_hash=tx_hash, cert_index=cert_index) == convert_json_to_object(mock_data)


def test_integration_governance_vote():
    if os.getenv('BLOCKFROST_PROJECT_ID_MAINNET'):
        api = BlockFrostApi(project_id=os.getenv('BLOCKFROST_PROJECT_ID_MAINNET'))
        assert api.governance_vote(tx_hash=tx_hash, cert_index=cert_index)


def test_governance_dreps(requests_mock):
    api = BlockFrostApi()
    mock_data = [
        {"id": "1", "name": "DRep 1"},
        {"id": "2", "name": "DRep 2"}
    ]
    requests_mock.get(f"{api.url}/governance/dreps", json=mock_data)
    assert api.governance_dreps() == convert_json_to_object(mock_data)


def test_integration_governance_dreps():
    if os.getenv('BLOCKFROST_PROJECT_ID_MAINNET'):
        api = BlockFrostApi(project_id=os.getenv('BLOCKFROST_PROJECT_ID_MAINNET'))
        assert api.governance_dreps()


def test_governance_drep(requests_mock):
    api = BlockFrostApi()
    mock_data = {"id": "1", "name": "DRep 1"}
    requests_mock.get(f"{api.url}/governance/dreps/{drep_id}", json=mock_data)
    assert api.governance_drep(drep_id=drep_id) == convert_json_to_object(mock_data)


def test_integration_governance_drep():
    if os.getenv('BLOCKFROST_PROJECT_ID_MAINNET'):
        api = BlockFrostApi(project_id=os.getenv('BLOCKFROST_PROJECT_ID_MAINNET'))
        assert api.governance_drep(drep_id=drep_id)


def test_governance_committee(requests_mock):
    api = BlockFrostApi()
    mock_data = [
        {"id": "1", "name": "Member 1"},
        {"id": "2", "name": "Member 2"}
    ]
    requests_mock.get(f"{api.url}/governance/committee", json=mock_data)
    assert api.governance_committee() == convert_json_to_object(mock_data)


def test_integration_governance_committee():
    if os.getenv('BLOCKFROST_PROJECT_ID_MAINNET'):
        api = BlockFrostApi(project_id=os.getenv('BLOCKFROST_PROJECT_ID_MAINNET'))
        assert api.governance_committee()


def test_governance_committee_member(requests_mock):
    api = BlockFrostApi()
    mock_data = {"id": "1", "name": "Member 1"}
    requests_mock.get(f"{api.url}/governance/committee/{key_hash}", json=mock_data)
    assert api.governance_committee_member(key_hash=key_hash) == convert_json_to_object(mock_data)


def test_integration_governance_committee_member():
    if os.getenv('BLOCKFROST_PROJECT_ID_MAINNET'):
        api = BlockFrostApi(project_id=os.getenv('BLOCKFROST_PROJECT_ID_MAINNET'))
        assert api.governance_committee_member(key_hash=key_hash)

def test_governance_drep_votes(requests_mock):
    api = BlockFrostApi()
    mock_data = [
        {"proposal_id": "1", "vote": "yes", "timestamp": "2023-01-01T00:00:00Z"},
        {"proposal_id": "2", "vote": "no", "timestamp": "2023-01-02T00:00:00Z"}
    ]
    requests_mock.get(f"{api.url}/governance/dreps/{drep_id}/votes", json=mock_data)
    assert api.governance_drep_votes(drep_id=drep_id) == convert_json_to_object(mock_data)

def test_integration_governance_drep_votes():
    if os.getenv('BLOCKFROST_PROJECT_ID_MAINNET'):
        api = BlockFrostApi(project_id=os.getenv('BLOCKFROST_PROJECT_ID_MAINNET'))
        assert api.governance_drep_votes(drep_id=drep_id)

def test_governance_drep_delegators(requests_mock):
    api = BlockFrostApi()
    mock_data = [
        {"stake_address": "stake1u9l5q5jwgelgagzyt6nuaasefgmn8pd25c8e9qpeprq0tdcp0e3uk", "amount": "1000000"},
        {"stake_address": "stake1ux4vspfvwuus9uwyp5p3f0ky7a30jq5j80jxse0fr7pa56sgn8kha", "amount": "2000000"}
    ]
    requests_mock.get(f"{api.url}/governance/dreps/{drep_id}/delegators", json=mock_data)
    assert api.governance_drep_delegators(drep_id=drep_id) == convert_json_to_object(mock_data)

def test_integration_governance_drep_delegators():
    if os.getenv('BLOCKFROST_PROJECT_ID_MAINNET'):
        api = BlockFrostApi(project_id=os.getenv('BLOCKFROST_PROJECT_ID_MAINNET'))
        assert api.governance_drep_delegators(drep_id=drep_id)

def test_governance_drep_metadata(requests_mock):
    api = BlockFrostApi()
    mock_data = {
        "url": "https://example.com/metadata.json",
        "hash": "abcd1234567890",
        "json_metadata": {
            "name": "Example DRep",
            "description": "An example delegated representative"
        }
    }
    requests_mock.get(f"{api.url}/governance/dreps/{drep_id}/metadata", json=mock_data)
    assert api.governance_drep_metadata(drep_id=drep_id) == convert_json_to_object(mock_data)

def test_integration_governance_drep_metadata():
    if os.getenv('BLOCKFROST_PROJECT_ID_MAINNET'):
        api = BlockFrostApi(project_id=os.getenv('BLOCKFROST_PROJECT_ID_MAINNET'))
        assert api.governance_drep_metadata(drep_id=drep_id)

def test_governance_drep_updates(requests_mock):
    api = BlockFrostApi()
    mock_data = [
        {
            "tx_hash": "6804edf9712d2b619edb6ac86861fe93a730693183a262b165fcc1ba1bc99cad",
            "cert_index": 0,
            "action": "registered"
        },
        {
            "tx_hash": "9c190bc1ac88b2ab0c05a82d7de8b71b67a9316377e865748a89d4426c0d3005",
            "cert_index": 1,
            "action": "updated"
        }
    ]
    requests_mock.get(f"{api.url}/governance/dreps/{drep_id}/updates", json=mock_data)
    assert api.governance_drep_updates(drep_id=drep_id) == convert_json_to_object(mock_data)

def test_integration_governance_drep_updates():
    if os.getenv('BLOCKFROST_PROJECT_ID_MAINNET'):
        api = BlockFrostApi(project_id=os.getenv('BLOCKFROST_PROJECT_ID_MAINNET'))
        assert api.governance_drep_updates(drep_id=drep_id)

def test_governance_committee_member_votes(requests_mock):
    api = BlockFrostApi()
    mock_data = [
        {"proposal_id": "1", "vote": "yes", "timestamp": "2023-01-01T00:00:00Z"},
        {"proposal_id": "2", "vote": "abstain", "timestamp": "2023-01-02T00:00:00Z"}
    ]
    requests_mock.get(f"{api.url}/governance/committee/{key_hash}/votes", json=mock_data)
    assert api.governance_committee_member_votes(key_hash=key_hash) == convert_json_to_object(mock_data)

def test_integration_governance_committee_member_votes():
    if os.getenv('BLOCKFROST_PROJECT_ID_MAINNET'):
        api = BlockFrostApi(project_id=os.getenv('BLOCKFROST_PROJECT_ID_MAINNET'))
        assert api.governance_committee_member_votes(key_hash=key_hash)

