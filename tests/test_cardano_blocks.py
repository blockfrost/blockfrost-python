from blockfrost import BlockFrostApi, ApiError
from blockfrost.api.cardano.blocks import \
    BlockResponse

hash = '4ea1ba291e8eef538635a53e59fddba7810d1679631cc3aed7c8e6c4091a516a'
slot_number = 412162133
epoch_number = 425


def test_block_latest(requests_mock):
    api = BlockFrostApi()
    mock_data = {
        "time": 1641338934,
        "height": 15243593,
        "hash": hash,
        "slot": slot_number,
        "epoch": epoch_number,
        "epoch_slot": 12,
        "slot_leader": "pool1pu5jlj4q9w9jlxeu370a3c9myx47md5j5m2str0naunn2qnikdy",
        "size": 3,
        "tx_count": 1,
        "output": "128314491794",
        "fees": "592661",
        "block_vrf": "vrf_vk1wf2k6lhujezqcfe00l6zetxpnmh9n6mwhpmhm0dvfh3fxgmdnrfqkms8ty",
        "previous_block": "43ebccb3ac72c7cebd0d9b755a4b08412c9f5dcb81b8a0ad1e3c197d29d47b05",
        "next_block": "8367f026cf4b03e116ff8ee5daf149b55ba5a6ec6dec04803b8dc317721d15fa",
        "confirmations": 4698
    }
    requests_mock.get(f"{api.url}/blocks/latest", json=mock_data)
    mock_object = BlockResponse(**mock_data)
    assert api.block_latest() == mock_object


def test_block_latest_transactions(requests_mock):
    api = BlockFrostApi()
    mock_data = [
        "8788591983aa73981fc92d6cddbbe643959f5a784e84b8bee0db15823f575a5b",
        "4eef6bb7755d8afbeac526b799f3e32a624691d166657e9d862aaeb66682c036",
        "52e748c4dec58b687b90b0b40d383b9fe1f24c1a833b7395cdf07dd67859f46f",
        "e8073fd5318ff43eca18a852527166aa8008bee9ee9e891f585612b7e4ba700b"
    ]
    requests_mock.get(f"{api.url}/blocks/latest/txs", json=mock_data)
    mock_object = mock_data
    assert api.block_latest_transactions() == mock_object


def test_block(requests_mock):
    api = BlockFrostApi()
    mock_data = {
        "time": 1641338934,
        "height": 15243593,
        "hash": hash,
        "slot": slot_number,
        "epoch": epoch_number,
        "epoch_slot": 12,
        "slot_leader": "pool1pu5jlj4q9w9jlxeu370a3c9myx47md5j5m2str0naunn2qnikdy",
        "size": 3,
        "tx_count": 1,
        "output": "128314491794",
        "fees": "592661",
        "block_vrf": "vrf_vk1wf2k6lhujezqcfe00l6zetxpnmh9n6mwhpmhm0dvfh3fxgmdnrfqkms8ty",
        "previous_block": "43ebccb3ac72c7cebd0d9b755a4b08412c9f5dcb81b8a0ad1e3c197d29d47b05",
        "next_block": "8367f026cf4b03e116ff8ee5daf149b55ba5a6ec6dec04803b8dc317721d15fa",
        "confirmations": 4698
    }
    requests_mock.get(f"{api.url}/blocks/{hash}", json=mock_data)
    mock_object = BlockResponse(**mock_data)
    assert api.block(hash_or_number=hash) == mock_object


def test_block_slot(requests_mock):
    api = BlockFrostApi()
    mock_data = {
        "time": 1641338934,
        "height": 15243593,
        "hash": hash,
        "slot": slot_number,
        "epoch": epoch_number,
        "epoch_slot": 12,
        "slot_leader": "pool1pu5jlj4q9w9jlxeu370a3c9myx47md5j5m2str0naunn2qnikdy",
        "size": 3,
        "tx_count": 1,
        "output": "128314491794",
        "fees": "592661",
        "block_vrf": "vrf_vk1wf2k6lhujezqcfe00l6zetxpnmh9n6mwhpmhm0dvfh3fxgmdnrfqkms8ty",
        "previous_block": "43ebccb3ac72c7cebd0d9b755a4b08412c9f5dcb81b8a0ad1e3c197d29d47b05",
        "next_block": "8367f026cf4b03e116ff8ee5daf149b55ba5a6ec6dec04803b8dc317721d15fa",
        "confirmations": 4698
    }
    requests_mock.get(f"{api.url}/blocks/slot/{slot_number}", json=mock_data)
    mock_object = BlockResponse(**mock_data)
    assert api.block_slot(slot_number=slot_number) == mock_object


def test_block_epoch_slot(requests_mock):
    api = BlockFrostApi()
    mock_data = {
        "time": 1641338934,
        "height": 15243593,
        "hash": hash,
        "slot": slot_number,
        "epoch": epoch_number,
        "epoch_slot": 12,
        "slot_leader": "pool1pu5jlj4q9w9jlxeu370a3c9myx47md5j5m2str0naunn2qnikdy",
        "size": 3,
        "tx_count": 1,
        "output": "128314491794",
        "fees": "592661",
        "block_vrf": "vrf_vk1wf2k6lhujezqcfe00l6zetxpnmh9n6mwhpmhm0dvfh3fxgmdnrfqkms8ty",
        "previous_block": "43ebccb3ac72c7cebd0d9b755a4b08412c9f5dcb81b8a0ad1e3c197d29d47b05",
        "next_block": "8367f026cf4b03e116ff8ee5daf149b55ba5a6ec6dec04803b8dc317721d15fa",
        "confirmations": 4698
    }
    requests_mock.get(f"{api.url}/blocks/epoch/{epoch_number}/slot/{slot_number}", json=mock_data)
    mock_object = BlockResponse(**mock_data)
    assert api.block_epoch_slot(epoch_number=epoch_number, slot_number=slot_number) == mock_object


def test_blocks_next(requests_mock):
    api = BlockFrostApi()
    mock_data = [
        {
            "time": 1641338934,
            "height": 15243593,
            "hash": hash,
            "slot": slot_number,
            "epoch": epoch_number,
            "epoch_slot": 12,
            "slot_leader": "pool1pu5jlj4q9w9jlxeu370a3c9myx47md5j5m2str0naunn2qnikdy",
            "size": 3,
            "tx_count": 1,
            "output": "128314491794",
            "fees": "592661",
            "block_vrf": "vrf_vk1wf2k6lhujezqcfe00l6zetxpnmh9n6mwhpmhm0dvfh3fxgmdnrfqkms8ty",
            "previous_block": "43ebccb3ac72c7cebd0d9b755a4b08412c9f5dcb81b8a0ad1e3c197d29d47b05",
            "next_block": "8367f026cf4b03e116ff8ee5daf149b55ba5a6ec6dec04803b8dc317721d15fa",
            "confirmations": 4698
        }
    ]
    requests_mock.get(f"{api.url}/blocks/{hash}/next", json=mock_data)
    mock_object = [BlockResponse(**data) for data in mock_data]
    assert api.blocks_next(hash_or_number=hash) == mock_object


def test_blocks_previous(requests_mock):
    api = BlockFrostApi()
    mock_data = [
        {
            "time": 1641338934,
            "height": 15243593,
            "hash": hash,
            "slot": slot_number,
            "epoch": epoch_number,
            "epoch_slot": 12,
            "slot_leader": "pool1pu5jlj4q9w9jlxeu370a3c9myx47md5j5m2str0naunn2qnikdy",
            "size": 3,
            "tx_count": 1,
            "output": "128314491794",
            "fees": "592661",
            "block_vrf": "vrf_vk1wf2k6lhujezqcfe00l6zetxpnmh9n6mwhpmhm0dvfh3fxgmdnrfqkms8ty",
            "previous_block": "43ebccb3ac72c7cebd0d9b755a4b08412c9f5dcb81b8a0ad1e3c197d29d47b05",
            "next_block": "8367f026cf4b03e116ff8ee5daf149b55ba5a6ec6dec04803b8dc317721d15fa",
            "confirmations": 4698
        }
    ]
    requests_mock.get(f"{api.url}/blocks/{hash}/previous", json=mock_data)
    mock_object = [BlockResponse(**data) for data in mock_data]
    assert api.blocks_previous(hash_or_number=hash) == mock_object


def test_block_transactions(requests_mock):
    api = BlockFrostApi()
    mock_data = [
        "8788591983aa73981fc92d6cddbbe643959f5a784e84b8bee0db15823f575a5b",
        "4eef6bb7755d8afbeac526b799f3e32a624691d166657e9d862aaeb66682c036",
        "52e748c4dec58b687b90b0b40d383b9fe1f24c1a833b7395cdf07dd67859f46f",
        "e8073fd5318ff43eca18a852527166aa8008bee9ee9e891f585612b7e4ba700b"
    ]
    requests_mock.get(f"{api.url}/blocks/{hash}/txs", json=mock_data)
    mock_object = mock_data
    assert api.block_transactions(hash_or_number=hash) == mock_object
