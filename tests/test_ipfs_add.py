from blockfrost import BlockFrostIPFS, ApiError
from blockfrost.utils import convert_json_to_object

file_path = "README.md"


def test_add(requests_mock):
    ipfs = BlockFrostIPFS()
    mock_data = {
        "name": file_path,
        "ipfs_hash": "QmZbHqiCxKEVX7QfijzJTkZiSi3WEVTcvANgNAWzDYgZDr",
        "size": 125297
    }
    requests_mock.post(f"{ipfs.url}/ipfs/add", json=mock_data)
    assert ipfs.add(file_path=file_path) == convert_json_to_object(mock_data)
