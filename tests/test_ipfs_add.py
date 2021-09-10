from blockfrost import BlockFrostIPFS, ApiError
from blockfrost.ipfs.add import IPFSObjectResponse

file_path = "README.md"


def test_add(requests_mock):
    ipfs = BlockFrostIPFS()
    mock_data = {
        "name": file_path,
        "ipfs_hash": "QmZbHqiCxKEVX7QfijzJTkZiSi3WEVTcvANgNAWzDYgZDr",
        "size": 125297
    }
    requests_mock.post(f"{ipfs.url}/ipfs/add", json=mock_data)
    mock_object = IPFSObjectResponse(**mock_data)
    assert ipfs.add(file_path=file_path).ipfs_hash == mock_object.ipfs_hash
