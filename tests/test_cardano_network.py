import os
from blockfrost import BlockFrostApi, ApiError
from blockfrost.utils import convert_json_to_object


def test_network(requests_mock):
    api = BlockFrostApi()
    mock_data = {
        "supply": {
            "max": "45000000000000000",
            "total": "32890715183299160",
            "circulating": "32412601976210393",
            "locked": "125006953355",
            "treasury": "98635632000000",
            "reserves": "46635632000000"
        },
        "stake": {
            "live": "23204950463991654",
            "active": "22210233523456321"
        }
    }
    requests_mock.get(f"{api.url}/network", json=mock_data)
    assert api.network() == convert_json_to_object(mock_data)


def test_integration_network():
    if os.getenv('BLOCKFROST_PROJECT_ID_MAINNET'):
        api = BlockFrostApi(project_id=os.getenv('BLOCKFROST_PROJECT_ID_MAINNET'))
        assert api.network()
