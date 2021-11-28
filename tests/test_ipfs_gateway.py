from blockfrost import BlockFrostIPFS, ApiError
from blockfrost.utils import convert_json_to_object

IPFS_path = "QmZbHqiCxKEVX7QfijzJTkZiSi3WEVTcvANgNAWzDYgZDr"


def test_gateway(requests_mock):
    ipfs = BlockFrostIPFS()
    mock_data = "data"
    requests_mock.get(f"{ipfs.url}/ipfs/gateway/{IPFS_path}", text=mock_data)
    assert ipfs.gateway(IPFS_path=IPFS_path).text == convert_json_to_object(mock_data)
