from blockfrost import BlockFrostApi, ApiError
from blockfrost.api.cardano.network import \
    NetworkResponse


def test_network(requests_mock):
    api = BlockFrostApi()
    mock_data = {
        "supply": {
            "max": "45000000000000000",
            "total": "32890715183299160",
            "circulating": "32412601976210393",
            "locked": "125006953355"
        },
        "stake": {
            "live": "23204950463991654",
            "active": "22210233523456321"
        }
    }
    requests_mock.get(f"{api.url}/network", json=mock_data)
    mock_object = NetworkResponse(**mock_data)
    assert api.network() == mock_object
