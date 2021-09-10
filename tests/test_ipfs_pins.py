from blockfrost import BlockFrostIPFS, ApiError
from blockfrost.ipfs.pins import IPFSPinnedObjectResponse, IPFSPinnedListObjectResponse

IPFS_path = "QmZbHqiCxKEVX7QfijzJTkZiSi3WEVTcvANgNAWzDYgZDr"


def test_pin_object(requests_mock):
    ipfs = BlockFrostIPFS()
    mock_data = {
        "ipfs_hash": IPFS_path,
        "state": "queued"
    }
    requests_mock.post(f"{ipfs.url}/ipfs/pin/add/{IPFS_path}", json=mock_data)
    mock_object = IPFSPinnedObjectResponse(**mock_data)
    assert ipfs.pin_object(IPFS_path=IPFS_path).ipfs_hash == mock_object.ipfs_hash


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
    mock_object = [IPFSPinnedListObjectResponse(**data) for data in mock_data]
    assert ipfs.pined_list()[0].ipfs_hash == mock_object[0].ipfs_hash


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
    mock_object = IPFSPinnedListObjectResponse(**mock_data)
    assert ipfs.pined_object(IPFS_path=IPFS_path).ipfs_hash == mock_object.ipfs_hash


def test_pined_object_remove(requests_mock):
    ipfs = BlockFrostIPFS()
    mock_data = {
        "ipfs_hash": IPFS_path,
        "state": "unpinned"
    }
    requests_mock.post(f"{ipfs.url}/ipfs/pin/remove/{IPFS_path}", json=mock_data)
    mock_object = IPFSPinnedObjectResponse(**mock_data)
    assert ipfs.pined_object_remove(IPFS_path=IPFS_path).ipfs_hash == mock_object.ipfs_hash
