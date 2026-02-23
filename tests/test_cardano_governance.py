import os
from blockfrost import BlockFrostApi, ApiError
from blockfrost.utils import convert_json_to_object

drep_id = 'drep1yfaaaaa270yjt6tu5skndugekprf5ykv5jshanl0c6gqx5qpstskf'
tx_hash = '51f495aa23f4b3b3aa90afde4a0e67823bb7ac4ac65f5ffbb138373b863f2f74'
cert_index = 0
# proposal with metadata (treasury_withdrawals type)
metadata_tx_hash = '60ed6ab43c840ff888a8af30a1ed27b41e9f4a91a89822b2b63d1bfc52aeec45'


def test_governance_dreps(requests_mock):
    api = BlockFrostApi()
    mock_data = [
        {
            "drep_id": drep_id,
            "hex": "db1bc3c3f99fd22aa1e09f1c34c0ada5795c5e1f32f2652a246f73db"
        },
        {
            "drep_id": "drep1cxayn4fgy27yaucvhamsvqj3v6835mh3tjjx6t8rm65ndd3lcjm",
            "hex": "c1d932a9a0457a13bc6195f7600c919d1e3476f715c86d2c8f7a9a66"
        }
    ]
    requests_mock.get(f"{api.url}/governance/dreps", json=mock_data)
    assert api.governance_dreps() == convert_json_to_object(mock_data)


def test_integration_governance_dreps():
    if os.getenv('BLOCKFROST_PROJECT_ID_MAINNET'):
        api = BlockFrostApi(project_id=os.getenv('BLOCKFROST_PROJECT_ID_MAINNET'))
        api.governance_dreps()


def test_governance_drep(requests_mock):
    api = BlockFrostApi()
    mock_data = {
        "drep_id": drep_id,
        "hex": "db1bc3c3f99fd22aa1e09f1c34c0ada5795c5e1f32f2652a246f73db",
        "amount": "2000000",
        "active": True,
        "active_epoch": 420,
        "has_script": False,
        "retired": False,
        "expired": False,
        "last_active_epoch": 500
    }
    requests_mock.get(f"{api.url}/governance/dreps/{drep_id}", json=mock_data)
    assert api.governance_drep(drep_id=drep_id) == convert_json_to_object(mock_data)


def test_integration_governance_drep():
    if os.getenv('BLOCKFROST_PROJECT_ID_MAINNET'):
        api = BlockFrostApi(project_id=os.getenv('BLOCKFROST_PROJECT_ID_MAINNET'))
        api.governance_drep(drep_id=drep_id)


def test_governance_drep_delegators(requests_mock):
    api = BlockFrostApi()
    mock_data = [
        {
            "address": "stake1ux3g2c9dx2nhhehyrezyxpkstartcqmu9hk63qgfkccw5rqttygt7",
            "amount": "1029328"
        }
    ]
    requests_mock.get(f"{api.url}/governance/dreps/{drep_id}/delegators", json=mock_data)
    assert api.governance_drep_delegators(drep_id=drep_id) == convert_json_to_object(mock_data)


def test_integration_governance_drep_delegators():
    if os.getenv('BLOCKFROST_PROJECT_ID_MAINNET'):
        api = BlockFrostApi(project_id=os.getenv('BLOCKFROST_PROJECT_ID_MAINNET'))
        api.governance_drep_delegators(drep_id=drep_id)


def test_governance_drep_metadata(requests_mock):
    api = BlockFrostApi()
    mock_data = {
        "drep_id": drep_id,
        "hex": "db1bc3c3f99fd22aa1e09f1c34c0ada5795c5e1f32f2652a246f73db",
        "url": "https://example.com/drep-metadata.json",
        "hash": "a14a5ad4a83b1c8b04c5175f0a16b4a2d8b1e5a08c7b6d1e2f3c4d5e6f7a8b9",
        "json_metadata": None,
        "bytes": "\\xa100"
    }
    requests_mock.get(f"{api.url}/governance/dreps/{drep_id}/metadata", json=mock_data)
    assert api.governance_drep_metadata(drep_id=drep_id) == convert_json_to_object(mock_data)


def test_integration_governance_drep_metadata():
    if os.getenv('BLOCKFROST_PROJECT_ID_MAINNET'):
        api = BlockFrostApi(project_id=os.getenv('BLOCKFROST_PROJECT_ID_MAINNET'))
        api.governance_drep_metadata(drep_id=drep_id)


def test_governance_drep_updates(requests_mock):
    api = BlockFrostApi()
    mock_data = [
        {
            "tx_hash": "f5ca33220afcc0340d1fa3cba9b0e1f3c3c6e1eab57d688ed700ae56bbce9170",
            "cert_index": 0,
            "action": "registered"
        },
        {
            "tx_hash": "0e98ac6a8b1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6e7f8a9b0c1d2e3f4a5b6c7",
            "cert_index": 0,
            "action": "updated"
        }
    ]
    requests_mock.get(f"{api.url}/governance/dreps/{drep_id}/updates", json=mock_data)
    assert api.governance_drep_updates(drep_id=drep_id) == convert_json_to_object(mock_data)


def test_integration_governance_drep_updates():
    if os.getenv('BLOCKFROST_PROJECT_ID_MAINNET'):
        api = BlockFrostApi(project_id=os.getenv('BLOCKFROST_PROJECT_ID_MAINNET'))
        api.governance_drep_updates(drep_id=drep_id)


def test_governance_drep_votes(requests_mock):
    api = BlockFrostApi()
    mock_data = [
        {
            "tx_hash": "f5ca33220afcc0340d1fa3cba9b0e1f3c3c6e1eab57d688ed700ae56bbce9170",
            "cert_index": 0,
            "vote": "yes",
            "proposal_tx_hash": "b302de9b2ed2bca4d65e40cae4ae6d0b8e7c0f1a2b3c4d5e6f7a8b9c0d1e2f3a",
            "proposal_cert_index": 0
        }
    ]
    requests_mock.get(f"{api.url}/governance/dreps/{drep_id}/votes", json=mock_data)
    assert api.governance_drep_votes(drep_id=drep_id) == convert_json_to_object(mock_data)


def test_integration_governance_drep_votes():
    if os.getenv('BLOCKFROST_PROJECT_ID_MAINNET'):
        api = BlockFrostApi(project_id=os.getenv('BLOCKFROST_PROJECT_ID_MAINNET'))
        api.governance_drep_votes(drep_id=drep_id)


def test_governance_proposals(requests_mock):
    api = BlockFrostApi()
    mock_data = [
        {
            "tx_hash": tx_hash,
            "cert_index": cert_index,
            "governance_type": "treasury_withdrawals",
            "deposit": "100000000000",
            "return_address": "stake1ux3g2c9dx2nhhehyrezyxpkstartcqmu9hk63qgfkccw5rqttygt7",
            "governance_description": None,
            "ratified_epoch": None,
            "enacted_epoch": None,
            "dropped_epoch": None,
            "expired_epoch": None,
            "expiration": 550
        }
    ]
    requests_mock.get(f"{api.url}/governance/proposals", json=mock_data)
    assert api.governance_proposals() == convert_json_to_object(mock_data)


def test_integration_governance_proposals():
    if os.getenv('BLOCKFROST_PROJECT_ID_MAINNET'):
        api = BlockFrostApi(project_id=os.getenv('BLOCKFROST_PROJECT_ID_MAINNET'))
        api.governance_proposals()


def test_governance_proposal(requests_mock):
    api = BlockFrostApi()
    mock_data = {
        "tx_hash": tx_hash,
        "cert_index": cert_index,
        "governance_type": "treasury_withdrawals",
        "deposit": "100000000000",
        "return_address": "stake1ux3g2c9dx2nhhehyrezyxpkstartcqmu9hk63qgfkccw5rqttygt7",
        "governance_description": None,
        "ratified_epoch": None,
        "enacted_epoch": None,
        "dropped_epoch": None,
        "expired_epoch": None,
        "expiration": 550
    }
    requests_mock.get(f"{api.url}/governance/proposals/{tx_hash}/{cert_index}", json=mock_data)
    assert api.governance_proposal(tx_hash=tx_hash, cert_index=cert_index) == convert_json_to_object(mock_data)


def test_integration_governance_proposal():
    if os.getenv('BLOCKFROST_PROJECT_ID_MAINNET'):
        api = BlockFrostApi(project_id=os.getenv('BLOCKFROST_PROJECT_ID_MAINNET'))
        api.governance_proposal(tx_hash=tx_hash, cert_index=cert_index)


def test_governance_proposal_parameters(requests_mock):
    api = BlockFrostApi()
    mock_data = {
        "tx_hash": tx_hash,
        "cert_index": cert_index,
        "parameters": {
            "min_fee_a": 44,
            "min_fee_b": 155381,
            "key_deposit": "2000000",
            "pool_deposit": "500000000"
        }
    }
    requests_mock.get(f"{api.url}/governance/proposals/{tx_hash}/{cert_index}/parameters", json=mock_data)
    assert api.governance_proposal_parameters(tx_hash=tx_hash, cert_index=cert_index) == convert_json_to_object(mock_data)


def test_integration_governance_proposal_parameters():
    if os.getenv('BLOCKFROST_PROJECT_ID_MAINNET'):
        api = BlockFrostApi(project_id=os.getenv('BLOCKFROST_PROJECT_ID_MAINNET'))
        api.governance_proposal_parameters(tx_hash=tx_hash, cert_index=cert_index)


def test_governance_proposal_withdrawals(requests_mock):
    api = BlockFrostApi()
    mock_data = [
        {
            "stake_address": "stake1ux3g2c9dx2nhhehyrezyxpkstartcqmu9hk63qgfkccw5rqttygt7",
            "amount": "454541212442"
        }
    ]
    requests_mock.get(f"{api.url}/governance/proposals/{tx_hash}/{cert_index}/withdrawals", json=mock_data)
    assert api.governance_proposal_withdrawals(tx_hash=tx_hash, cert_index=cert_index) == convert_json_to_object(mock_data)


def test_integration_governance_proposal_withdrawals():
    if os.getenv('BLOCKFROST_PROJECT_ID_MAINNET'):
        api = BlockFrostApi(project_id=os.getenv('BLOCKFROST_PROJECT_ID_MAINNET'))
        api.governance_proposal_withdrawals(tx_hash=tx_hash, cert_index=cert_index)


def test_governance_proposal_votes(requests_mock):
    api = BlockFrostApi()
    mock_data = [
        {
            "tx_hash": "f5ca33220afcc0340d1fa3cba9b0e1f3c3c6e1eab57d688ed700ae56bbce9170",
            "cert_index": 0,
            "voter": "drep1mvdu8slennngja7w4un6knwezufra70887zuxpprd64jxfveahn",
            "voter_role": "drep",
            "vote": "yes"
        }
    ]
    requests_mock.get(f"{api.url}/governance/proposals/{tx_hash}/{cert_index}/votes", json=mock_data)
    assert api.governance_proposal_votes(tx_hash=tx_hash, cert_index=cert_index) == convert_json_to_object(mock_data)


def test_integration_governance_proposal_votes():
    if os.getenv('BLOCKFROST_PROJECT_ID_MAINNET'):
        api = BlockFrostApi(project_id=os.getenv('BLOCKFROST_PROJECT_ID_MAINNET'))
        api.governance_proposal_votes(tx_hash=tx_hash, cert_index=cert_index)


def test_governance_proposal_metadata(requests_mock):
    api = BlockFrostApi()
    mock_data = {
        "tx_hash": tx_hash,
        "cert_index": cert_index,
        "url": "https://example.com/proposal-metadata.json",
        "hash": "a14a5ad4a83b1c8b04c5175f0a16b4a2d8b1e5a08c7b6d1e2f3c4d5e6f7a8b9",
        "json_metadata": None,
        "bytes": "\\xa100"
    }
    requests_mock.get(f"{api.url}/governance/proposals/{tx_hash}/{cert_index}/metadata", json=mock_data)
    assert api.governance_proposal_metadata(tx_hash=tx_hash, cert_index=cert_index) == convert_json_to_object(mock_data)


def test_integration_governance_proposal_metadata():
    if os.getenv('BLOCKFROST_PROJECT_ID_MAINNET'):
        api = BlockFrostApi(project_id=os.getenv('BLOCKFROST_PROJECT_ID_MAINNET'))
        api.governance_proposal_metadata(tx_hash=metadata_tx_hash, cert_index=cert_index)
