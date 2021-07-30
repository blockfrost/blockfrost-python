from blockfrost import BlockFrostApi
from blockfrost.api import ApiError


def test_root(requests_mock):
    api = BlockFrostApi()
    mock_data = {
        "url": "https://blockfrost.io/",
        "version": "0.1.0"
    }
    requests_mock.get(api.url + '/', json=mock_data)
    response = api.root()
    assert response == mock_data


def test_health(requests_mock):
    api = BlockFrostApi()
    mock_data = {
        "is_healthy": True
    }
    requests_mock.get(api.url + '/health', json=mock_data)
    response = api.health()
    assert response == mock_data


def test_health_clock(requests_mock):
    api = BlockFrostApi()
    mock_data = {
        "server_time": 1603400958947
    }
    requests_mock.get(api.url + '/health/clock', json=mock_data)
    response = api.clock()
    assert response == mock_data
