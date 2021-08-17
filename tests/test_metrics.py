from blockfrost import BlockFrostApi, ApiError


def test_metrics(requests_mock):
    api = BlockFrostApi()
    mock_data = [
        [
            {
                "date": 1612543884,
                "calls": 42
            },
            {
                "date": 1614523884,
                "calls": 6942
            }
        ]
    ]
    requests_mock.get(api.url + '/metrics', json=mock_data)
    mock_object = mock_data
    assert api.metrics() == mock_object


def test_metrics_endpoints(requests_mock):
    api = BlockFrostApi()
    mock_data = [
        [
            {
                "date": 1612543814,
                "calls": 182,
                "endpoint": "block"
            },
            {
                "date": 1612543814,
                "calls": 42,
                "endpoint": "epoch"
            },
            {
                "date": 1612543812,
                "calls": 775,
                "endpoint": "block"
            },
            {
                "date": 1612523884,
                "calls": 4,
                "endpoint": "epoch"
            },
            {
                "date": 1612553884,
                "calls": 89794,
                "endpoint": "block"
            }
        ]
    ]
    requests_mock.get(api.url + '/metrics/endpoints', json=mock_data)
    response = api.metrics_endpoints()
    assert response == mock_data
