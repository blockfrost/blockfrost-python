from blockfrost import BlockFrostApi, ApiError
from blockfrost.api.cardano.scripts import \
    ScriptsResponse, \
    ScriptResponse, \
    ScriptRedeemersResponse

script_hash = "13a3efd825703a352a8f71f4e2758d08c28c564e8dfcce9f77776ad1"


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
