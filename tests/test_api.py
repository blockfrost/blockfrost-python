from blockfrost import BlockFrostApi, ApiError
from blockfrost.api import RootResponse


def test_root(requests_mock):
    api = BlockFrostApi()
    mock_data = {
        "url": "https://blockfrost.io/",
        "version": "0.1.0"
    }
    requests_mock.get(api.url + '/', json=mock_data)
    mock_object = RootResponse(**mock_data)
    assert api.root().url == mock_object.url
