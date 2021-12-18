import os
from blockfrost import BlockFrostApi, ApiError
from blockfrost.utils import convert_json_to_object


def test_root(requests_mock):
    api = BlockFrostApi()
    mock_data = {
        "url": "https://blockfrost.io/",
        "version": "0.1.0"
    }
    requests_mock.get(api.url + '/', json=mock_data)
    assert api.root() == convert_json_to_object(mock_data)


def test_integration_root():
    if os.getenv('BLOCKFROST_PROJECT_ID_MAINNET'):
        api = BlockFrostApi(project_id=os.getenv('BLOCKFROST_PROJECT_ID_MAINNET'))
        assert api.root()


def test_integration_root():
    if os.getenv('BLOCKFROST_PROJECT_ID_MAINNET'):
        assert True
