import os, json
from blockfrost import BlockFrostApi, ApiError
from blockfrost.utils import convert_json_to_object

hash = "8f55e18a94e4c0951e5b8bd8910b2cb20aa4d742b1608fda3a06793d39fb07b1"
xpub = "d507c8f866691bd96e131334c355188b1a1d0b2fa0ab11545075aab332d77d9eb19657ad13ee581b56b0f8d744d66ca356b93d42fe176b3de007d53e9c4c4e7a"
role = 0
index = 0


def test_utils_addresses_xpub(requests_mock):
    api = BlockFrostApi()
    mock_data = [
        {
            "xpub": "d507c8f866691bd96e131334c355188b1a1d0b2fa0ab11545075aab332d77d9eb19657ad13ee581b56b0f8d744d66ca356b93d42fe176b3de007d53e9c4c4e7a",
            "role": 0,
            "index": 0,
            "address": "addr1q90sqnljxky88s0jsnps48jd872p7znzwym0jpzqnax6qs5nfrlkaatu28n0qzmqh7f2cpksxhpc9jefx3wrl0a2wu8q5amen7"
        }
    ]
    requests_mock.get(f"{api.url}/utils/addresses/xpub/{xpub}/{role}/{index}", json=mock_data)
    assert api.utils_addresses_xpub(xpub, role, index) == convert_json_to_object(mock_data)


def test_integration_utils_addresses_xpub():
    if os.getenv('BLOCKFROST_PROJECT_ID_MAINNET'):
        api = BlockFrostApi(project_id=os.getenv('BLOCKFROST_PROJECT_ID_MAINNET'))
        assert api.utils_addresses_xpub(xpub, role, index)


def test_utils_transaction_evaluate(requests_mock):
    api = BlockFrostApi()
    mock_data = hash
    requests_mock.post(f"{api.url}/utils/txs/evaluate", json=mock_data)
    assert api.transaction_evaluate(file_path="./README.md") == convert_json_to_object(mock_data)
