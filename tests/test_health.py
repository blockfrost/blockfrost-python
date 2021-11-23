import os
from blockfrost import BlockFrostApi, ApiError
from blockfrost.utils import convert_json_to_object


def test_health(requests_mock):
    api = BlockFrostApi()
    mock_data = {
        "is_healthy": True
    }
    requests_mock.get(api.url + '/health', json=mock_data)
    assert api.health() == convert_json_to_object(mock_data)


def test_integration_health():
    if os.getenv('BLOCKFROST_PROJECT_ID_MAINNET'):
        api = BlockFrostApi(project_id=os.getenv('BLOCKFROST_PROJECT_ID_MAINNET'))
        assert api.health()


def test_clock(requests_mock):
    api = BlockFrostApi()
    mock_data = {
        "server_time": 1603400958947
    }
    requests_mock.get(api.url + '/health/clock', json=mock_data)
    assert api.clock() == convert_json_to_object(mock_data)


def test_integration_clock():
    if os.getenv('BLOCKFROST_PROJECT_ID_MAINNET'):
        api = BlockFrostApi(project_id=os.getenv('BLOCKFROST_PROJECT_ID_MAINNET'))
        assert api.clock()
