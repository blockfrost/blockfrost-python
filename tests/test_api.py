from blockfrost import BlockFrostApi, ApiError


def test_root(requests_mock):
    api = BlockFrostApi()
    mock_data = {
        "url": "https://blockfrost.io/",
        "version": "0.1.0"
    }
    requests_mock.get(api.url + '/', json=mock_data)
    response = api.root()
    assert response == mock_data
