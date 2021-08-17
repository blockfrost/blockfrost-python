from blockfrost import BlockFrostApi, ApiError
from blockfrost.api.health import Health, Clock


def test_health(requests_mock):
    api = BlockFrostApi()
    mock_data = {
        "is_healthy": True
    }
    requests_mock.get(api.url + '/health', json=mock_data)
    mock_object = Health(**mock_data)
    assert api.health().is_healthy == mock_object.is_healthy


def test_clock(requests_mock):
    api = BlockFrostApi()
    mock_data = {
        "server_time": 1603400958947
    }
    requests_mock.get(api.url + '/health/clock', json=mock_data)
    mock_object = Clock(**mock_data)
    assert api.clock().server_time == mock_object.server_time
