import pandas as pd
from pandas._testing import assert_frame_equal
from blockfrost import BlockFrostApi, ApiError
from blockfrost.utils import convert_json_to_object

api = BlockFrostApi()

mock_data = {
    "is_healthy": True
}


def test_default_mapper(requests_mock):
    requests_mock.get(api.url + '/health', json=mock_data)
    assert api.health() == convert_json_to_object(mock_data)


def test_object_mapper(requests_mock):
    requests_mock.get(api.url + '/health', json=mock_data)
    assert api.health(return_type="object") == convert_json_to_object(mock_data)


def test_json_mapper(requests_mock):
    requests_mock.get(api.url + '/health', json=mock_data)
    assert api.health(return_type="json") == mock_data


def test_pandas_mapper(requests_mock):
    requests_mock.get(api.url + '/health', json=mock_data)
    mock_pandas = pd.json_normalize(mock_data)
    assert_frame_equal(api.health(return_type="pandas"), mock_pandas)
