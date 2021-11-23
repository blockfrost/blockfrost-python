from blockfrost import BlockFrostIPFS, ApiError
from blockfrost.utils import convert_json_to_object

IPFS_path = "QmZbHqiCxKEVX7QfijzJTkZiSi3WEVTcvANgNAWzDYgZDr"


def test_pin_object(requests_mock):
    ipfs = BlockFrostIPFS()
    mock_data = {
        "ipfs_hash": IPFS_path,
        "state": "queued"
    }
    requests_mock.post(f"{ipfs.url}/ipfs/pin/add/{IPFS_path}", json=mock_data)
    assert ipfs.pin_object(IPFS_path=IPFS_path) == convert_json_to_object(mock_data)


def test_pined_list(requests_mock):
    ipfs = BlockFrostIPFS()
    mock_data = [
        {
            "time_created": 1615551024,
            "time_pinned": 1615551024,
            "ipfs_hash": IPFS_path,
            "size": 1615551024,
            "state": "pinned"
        }
    ]
    requests_mock.get(f"{ipfs.url}/ipfs/pin/list", json=mock_data)
    assert ipfs.pined_list() == convert_json_to_object(mock_data)


def test_pined_object(requests_mock):
    ipfs = BlockFrostIPFS()
    mock_data = {
        "time_created": 1615551024,
        "time_pinned": 1615551024,
        "ipfs_hash": IPFS_path,
        "size": 1615551024,
        "state": "pinned"
    }
    requests_mock.get(f"{ipfs.url}/ipfs/pin/list/{IPFS_path}", json=mock_data)
    assert ipfs.pined_object(IPFS_path=IPFS_path) == convert_json_to_object(mock_data)


def test_pined_object_remove(requests_mock):
    ipfs = BlockFrostIPFS()
    mock_data = {
        "ipfs_hash": IPFS_path,
        "state": "unpinned"
    }
    requests_mock.post(f"{ipfs.url}/ipfs/pin/remove/{IPFS_path}", json=mock_data)
    assert ipfs.pined_object_remove(IPFS_path=IPFS_path) == convert_json_to_object(mock_data)
