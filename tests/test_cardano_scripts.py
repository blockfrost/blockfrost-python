from blockfrost import BlockFrostApi, ApiError
from blockfrost.api.cardano.scripts import \
    ScriptsResponse, \
    ScriptResponse, \
    ScriptJsonResponse, \
    ScriptCBORResponse, \
    ScriptRedeemersResponse, \
    ScriptDatumResponse

script_hash = "13a3efd825703a352a8f71f4e2758d08c28c564e8dfcce9f77776ad1"
datum_hash = "db583ad85881a96c73fbb26ab9e24d1120bb38f45385664bb9c797a2ea8d9a2d"


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
    mock_object = [ScriptsResponse(**data) for data in mock_data]
    assert api.scripts() == mock_object


def test_script(requests_mock):
    api = BlockFrostApi()
    mock_data = {
        "script_hash": "13a3efd825703a352a8f71f4e2758d08c28c564e8dfcce9f77776ad1",
        "type": "plutus",
        "serialised_size": 3119
    }
    requests_mock.get(f"{api.url}/scripts/{script_hash}", json=mock_data)
    mock_object = ScriptResponse(**mock_data)
    assert api.script(script_hash=script_hash) == mock_object


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
    mock_object = ScriptJsonResponse(**mock_data)
    assert api.script_json(script_hash=script_hash) == mock_object


def test_script_cbor(requests_mock):
    api = BlockFrostApi()
    mock_data = {
        "cbor": "4e4d01000033222220051200120011"
    }
    requests_mock.get(f"{api.url}/scripts/{script_hash}/cbor", json=mock_data)
    mock_object = ScriptCBORResponse(**mock_data)
    assert api.script_cbor(script_hash=script_hash) == mock_object


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
    mock_object = [ScriptRedeemersResponse(**data) for data in mock_data]
    assert api.script_redeemers(script_hash=script_hash) == mock_object


def test_script_redeemers(requests_mock):
    api = BlockFrostApi()
    mock_data = {
        "json_value": {
            "int": 42
        }
    }
    requests_mock.get(f"{api.url}/scripts/datum/{datum_hash}", json=mock_data)
    mock_object = ScriptDatumResponse(**mock_data)
    assert api.script_datum(datum_hash=datum_hash) == mock_object
