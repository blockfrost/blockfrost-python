import os, json
from blockfrost import BlockFrostApi, ApiError
from blockfrost.utils import convert_json_to_object

script_hash = "65c197d565e88a20885e535f93755682444d3c02fd44dd70883fe89e"
datum_hash = "923918e403bf43c34b4ef6b48eb2ee04babed17320d8d1b9ff9ad086e86f44ec"


def test_scripts(requests_mock):
    api = BlockFrostApi()
    mock_data = [
        {
            "script_hash": script_hash
        },
        {
            "script_hash": "e1457a0c47dfb7a2f6b8fbb059bdceab163c05d34f195b87b9f2b30e"
        },
        {
            "script_hash": "a6e63c0ff05c96943d1cc30bf53112ffff0f34b45986021ca058ec54"
        }
    ]
    requests_mock.get(f"{api.url}/scripts", json=mock_data)
    assert api.scripts() == convert_json_to_object(mock_data)


def test_integration_scripts():
    if os.getenv('BLOCKFROST_PROJECT_ID_MAINNET'):
        api = BlockFrostApi(project_id=os.getenv('BLOCKFROST_PROJECT_ID_MAINNET'))
        assert api.scripts()


def test_script(requests_mock):
    api = BlockFrostApi()
    mock_data = {
        "script_hash": "13a3efd825703a352a8f71f4e2758d08c28c564e8dfcce9f77776ad1",
        "type": "plutus",
        "serialised_size": 3119
    }
    requests_mock.get(f"{api.url}/scripts/{script_hash}", json=mock_data)
    assert api.script(script_hash=script_hash) == convert_json_to_object(mock_data)


def test_integration_script():
    if os.getenv('BLOCKFROST_PROJECT_ID_MAINNET'):
        api = BlockFrostApi(project_id=os.getenv('BLOCKFROST_PROJECT_ID_MAINNET'))
        assert api.script(script_hash=script_hash)


def test_script_json(requests_mock):
    api = BlockFrostApi()
    mock_data = {
        "json": {
            "type": "atLeast",
            "scripts": [
                {
                    "type": "sig",
                    "keyHash": "654891a4db2ea44b5263f4079a33efa0358ba90769e3d8f86a4a0f81"
                },
                {
                    "type": "sig",
                    "keyHash": "8685ad48f9bebb8fdb6447abbe140645e0bf743ff98da62e63e2147f"
                },
                {
                    "type": "sig",
                    "keyHash": "cb0f3b3f91693374ff7ce1d473cf6e721c7bab52b0737f04164e5a2d"
                }
            ],
            "required": 2
        }
    }
    requests_mock.get(f"{api.url}/scripts/{script_hash}/json", json=mock_data)
    assert api.script_json(script_hash=script_hash) == convert_json_to_object(mock_data)


def test_integration_script_json():
    if os.getenv('BLOCKFROST_PROJECT_ID_MAINNET'):
        api = BlockFrostApi(project_id=os.getenv('BLOCKFROST_PROJECT_ID_MAINNET'))
        assert api.script_json(script_hash=script_hash)


def test_script_cbor(requests_mock):
    api = BlockFrostApi()
    mock_data = {
        "cbor": "4e4d01000033222220051200120011"
    }
    requests_mock.get(f"{api.url}/scripts/{script_hash}/cbor", json=mock_data)
    assert api.script_cbor(script_hash=script_hash) == convert_json_to_object(mock_data)


def test_integration_script_cbor():
    if os.getenv('BLOCKFROST_PROJECT_ID_MAINNET'):
        api = BlockFrostApi(project_id=os.getenv('BLOCKFROST_PROJECT_ID_MAINNET'))
        assert api.script_cbor(script_hash=script_hash)


def test_script_redeemers(requests_mock):
    api = BlockFrostApi()
    mock_data = [
        {
            "tx_hash": "1a0570af966fb355a7160e4f82d5a80b8681b7955f5d44bec0dce628516157f0",
            "tx_index": 0,
            "purpose": "spend",
            "unit_mem": "1700",
            "unit_steps": "476468",
            "fee": "172033"
        }
    ]
    requests_mock.get(f"{api.url}/scripts/{script_hash}/redeemers", json=mock_data)
    assert api.script_redeemers(script_hash=script_hash) == convert_json_to_object(mock_data)


def test_integration_script_redeemers():
    if os.getenv('BLOCKFROST_PROJECT_ID_MAINNET'):
        api = BlockFrostApi(project_id=os.getenv('BLOCKFROST_PROJECT_ID_MAINNET'))
        assert api.script_redeemers(script_hash=script_hash) == []


def test_script_datum(requests_mock):
    api = BlockFrostApi()
    mock_data = {
        "json_value": {
            "int": 42
        }
    }
    requests_mock.get(f"{api.url}/scripts/datum/{datum_hash}", json=mock_data)
    assert api.script_datum(datum_hash=datum_hash) == convert_json_to_object(mock_data)


def test_integration_script_datum():
    if os.getenv('BLOCKFROST_PROJECT_ID_MAINNET'):
        api = BlockFrostApi(project_id=os.getenv('BLOCKFROST_PROJECT_ID_MAINNET'))
        assert api.script_datum(datum_hash=datum_hash)

def test_script_datum_cbor(requests_mock):
    api = BlockFrostApi()
    mock_data = {
        "cbor": "4e4d01000033222220051200120011"
    }
    requests_mock.get(f"{api.url}/scripts/datum/{datum_hash}/cbor", json=mock_data)
    assert api.script_datum_cbor(datum_hash=datum_hash) == convert_json_to_object(mock_data)


def test_integration_script_datum_cbor():
    if os.getenv('BLOCKFROST_PROJECT_ID_MAINNET'):
        api = BlockFrostApi(project_id=os.getenv('BLOCKFROST_PROJECT_ID_MAINNET'))
        assert api.script_datum_cbor(datum_hash=datum_hash)
