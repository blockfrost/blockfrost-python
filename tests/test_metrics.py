from blockfrost import BlockFrostApi, ApiError
from blockfrost.utils import convert_json_to_object


def test_metrics(requests_mock):
    api = BlockFrostApi()
    mock_data = [
        {
            "time": 1612543884,
            "calls": 42
        },
        {
            "time": 1614523884,
            "calls": 6942
        }
    ]

    requests_mock.get(api.url + '/metrics', json=mock_data)
    assert api.metrics() == convert_json_to_object(mock_data)


def test_metrics_endpoints(requests_mock):
    api = BlockFrostApi()
    mock_data = [
        {
            "time": 1612543814,
            "calls": 182,
            "endpoint": "block"
        },
        {
            "time": 1612543814,
            "calls": 42,
            "endpoint": "epoch"
        },
    ]

    requests_mock.get(api.url + '/metrics/endpoints', json=mock_data)
    assert api.metrics_endpoints() == convert_json_to_object(mock_data)
