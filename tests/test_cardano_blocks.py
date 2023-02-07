import os
from blockfrost import BlockFrostApi, ApiError
from blockfrost.utils import convert_json_to_object

# hash = '4ea1ba291e8eef538635a53e59fddba7810d1679631cc3aed7c8e6c4091a516a'
hash = '796b28e192f1c9040e3749feb1bd2b35ce9a262976c7db95b43a3d3c417d37d4'
slot_number = 46138897
epoch_number = 304


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
    assert api.block_latest() == convert_json_to_object(mock_data)


def test_integration_block_latest():
    if os.getenv('BLOCKFROST_PROJECT_ID_MAINNET'):
        api = BlockFrostApi(project_id=os.getenv('BLOCKFROST_PROJECT_ID_MAINNET'))
        assert api.block_latest()


def test_block_latest_transactions(requests_mock):
    api = BlockFrostApi()
    mock_data = [
        "8788591983aa73981fc92d6cddbbe643959f5a784e84b8bee0db15823f575a5b",
        "4eef6bb7755d8afbeac526b799f3e32a624691d166657e9d862aaeb66682c036",
        "52e748c4dec58b687b90b0b40d383b9fe1f24c1a833b7395cdf07dd67859f46f",
        "e8073fd5318ff43eca18a852527166aa8008bee9ee9e891f585612b7e4ba700b"
    ]
    requests_mock.get(f"{api.url}/blocks/latest/txs", json=mock_data)
    assert api.block_latest_transactions() == convert_json_to_object(mock_data)


def test_integration_block_latest_transactions():
    if os.getenv('BLOCKFROST_PROJECT_ID_MAINNET'):
        api = BlockFrostApi(project_id=os.getenv('BLOCKFROST_PROJECT_ID_MAINNET'))
        assert (api.block_latest_transactions() or
                api.block_latest_transactions() == [])


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
    assert api.block(hash_or_number=hash) == convert_json_to_object(mock_data)


def test_integration_block():
    if os.getenv('BLOCKFROST_PROJECT_ID_MAINNET'):
        api = BlockFrostApi(project_id=os.getenv('BLOCKFROST_PROJECT_ID_MAINNET'))
        assert api.block(hash_or_number=hash)


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
    assert api.block_slot(slot_number=slot_number) == convert_json_to_object(mock_data)


def test_integration_block_slot():
    if os.getenv('BLOCKFROST_PROJECT_ID_MAINNET'):
        api = BlockFrostApi(project_id=os.getenv('BLOCKFROST_PROJECT_ID_MAINNET'))
        assert api.block_slot(slot_number=slot_number)


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
    assert api.block_epoch_slot(epoch_number=epoch_number, slot_number=slot_number) == convert_json_to_object(mock_data)


def test_integration_block_epoch_slot():
    if os.getenv('BLOCKFROST_PROJECT_ID_MAINNET'):
        api = BlockFrostApi(project_id=os.getenv('BLOCKFROST_PROJECT_ID_MAINNET'))
        assert api.block_epoch_slot(epoch_number=epoch_number, slot_number=174097)


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
    assert api.blocks_next(hash_or_number=hash) == convert_json_to_object(mock_data)


def test_integration_blocks_next():
    if os.getenv('BLOCKFROST_PROJECT_ID_MAINNET'):
        api = BlockFrostApi(project_id=os.getenv('BLOCKFROST_PROJECT_ID_MAINNET'))
        assert api.blocks_next(hash_or_number=hash)


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
    assert api.blocks_previous(hash_or_number=hash) == convert_json_to_object(mock_data)


def test_integration_blocks_previous():
    if os.getenv('BLOCKFROST_PROJECT_ID_MAINNET'):
        api = BlockFrostApi(project_id=os.getenv('BLOCKFROST_PROJECT_ID_MAINNET'))
        assert api.blocks_previous(hash_or_number=hash)


def test_block_transactions(requests_mock):
    api = BlockFrostApi()
    mock_data = [
        "8788591983aa73981fc92d6cddbbe643959f5a784e84b8bee0db15823f575a5b",
        "4eef6bb7755d8afbeac526b799f3e32a624691d166657e9d862aaeb66682c036",
        "52e748c4dec58b687b90b0b40d383b9fe1f24c1a833b7395cdf07dd67859f46f",
        "e8073fd5318ff43eca18a852527166aa8008bee9ee9e891f585612b7e4ba700b"
    ]
    requests_mock.get(f"{api.url}/blocks/{hash}/txs", json=mock_data)
    assert api.block_transactions(hash_or_number=hash) == convert_json_to_object(mock_data)


def test_integration_block_transactions():
    if os.getenv('BLOCKFROST_PROJECT_ID_MAINNET'):
        api = BlockFrostApi(project_id=os.getenv('BLOCKFROST_PROJECT_ID_MAINNET'))
        assert api.block_transactions(hash_or_number=hash)


def test_blocks_blocks_addresses(requests_mock):
    api = BlockFrostApi()
    mock_data = [
        {
            "address": "addr1q9ld26v2lv8wvrxxmvg90pn8n8n5k6tdst06q2s856rwmvnueldzuuqmnsye359fqrk8hwvenjnqultn7djtrlft7jnq7dy7wv",
            "transactions": [
                {
                    "tx_hash": "1a0570af966fb355a7160e4f82d5a80b8681b7955f5d44bec0dce628516157f0"
                }
            ]
        },
        {
            "address": "addr1qxqs59lphg8g6qndelq8xwqn60ag3aeyfcp33c2kdp46a09re5df3pzwwmyq946axfcejy5n4x0y99wqpgtp2gd0k09qsgy6pz",
            "transactions": [
                {
                    "tx_hash": "1a0570af966fb355a7160e4f82d5a80b8681b7955f5d44bec0dce628516157d0"
                }
            ]
        }
    ]
    requests_mock.get(f"{api.url}/blocks/{hash}/addresses", json=mock_data)
    assert api.blocks_addresses(hash_or_number=hash) == convert_json_to_object(mock_data)


def test_integration_blocks_addresses():
    if os.getenv('BLOCKFROST_PROJECT_ID_MAINNET'):
        api = BlockFrostApi(project_id=os.getenv('BLOCKFROST_PROJECT_ID_MAINNET'))
        assert api.blocks_addresses(hash_or_number=hash)
