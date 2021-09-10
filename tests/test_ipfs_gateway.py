from blockfrost import BlockFrostIPFS, ApiError

IPFS_path = "QmZbHqiCxKEVX7QfijzJTkZiSi3WEVTcvANgNAWzDYgZDr"


def test_gateway(requests_mock):
    ipfs = BlockFrostIPFS()
    mock_data = "data"
    requests_mock.get(f"{ipfs.url}/ipfs/gateway/{IPFS_path}", text=mock_data)
    mock_object = mock_data
    assert ipfs.gateway(IPFS_path=IPFS_path).text == mock_object
