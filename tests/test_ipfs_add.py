from blockfrost import BlockFrostIPFS, ApiError
from blockfrost.utils import convert_json_to_object

file_path = "README.md"


def test_add(requests_mock, tmp_path):
    tmp_file = tmp_path / "tmp_file"
    tmp_file.touch()
    tmp_file.write_text("Test content for IPFS add")

    ipfs = BlockFrostIPFS()
    mock_data = {
        "name": tmp_file.name,
        "ipfs_hash": "QmZbHqiCxKEVX7QfijzJTkZiSi3WEVTcvANgNAWzDYgZDr",
        "size": 125297
    }
    requests_mock.post(f"{ipfs.url}/ipfs/add", json=mock_data)
    assert ipfs.add(file_path=tmp_file) == convert_json_to_object(mock_data)
