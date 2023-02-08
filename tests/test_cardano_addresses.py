import os

from blockfrost import BlockFrostApi, ApiError
from blockfrost.utils import convert_json_to_object

address = 'addr1qyptln5t5s0mastzc9rksn6wdqp9ynt67ahw0nhzukar5keu7yzv8ay6qvmlywtgvt7exaxt783dxuzv03qal7muda5sl42hg6'
stake_address = 'stake1ux3g2c9dx2nhhehyrezyxpkstartcqmu9hk63qgfkccw5rqttygt7'
asset = 'f4988f549728dc76b58d7677849443caf6e5385dc67e6c25f6aa901e506978656c54696c653235'


def test_address(requests_mock):
    api = BlockFrostApi()
    mock_data = {
        "address": address,
        "amount": [
            {
                "unit": "lovelace",
                "quantity": "42000000"
            },
            {
                "unit": "b0d07d45fe9514f80213f4020e5a61241458be626841cde717cb38a76e7574636f696e",
                "quantity": "12"
            }
        ],
        "stake_address": stake_address,
        "type": "shelley",
        "script": False,
    }
    requests_mock.get(f"{api.url}/addresses/{address}", json=mock_data)
    assert api.address(address=address) == convert_json_to_object(mock_data)


def test_integration_address():
    if os.getenv('BLOCKFROST_PROJECT_ID_MAINNET'):
        api = BlockFrostApi(project_id=os.getenv('BLOCKFROST_PROJECT_ID_MAINNET'))
        assert api.address(address=address)


def test_address_extended(requests_mock):
    api = BlockFrostApi()
    mock_data = {
        "address": address,
        "amount": [
            {
                "unit": "lovelace",
                "quantity": "42000000",
                "decimals": 6,
                "has_nft_onchain_metadata": None
            },
            {
                "unit": "b0d07d45fe9514f80213f4020e5a61241458be626841cde717cb38a76e7574636f696e",
                "quantity": "12",
                "decimals": None,
                "has_nft_onchain_metadata": True
            }
        ],
        "stake_address": "stake1ux3g2c9dx2nhhehyrezyxpkstartcqmu9hk63qgfkccw5rqttygt7",
        "type": "shelley",
        "script": False
    }
    requests_mock.get(f"{api.url}/addresses/{address}/extended", json=mock_data)
    assert api.address_extended(address=address) == convert_json_to_object(mock_data)


def test_integration_address_extended():
    if os.getenv('BLOCKFROST_PROJECT_ID_MAINNET'):
        api = BlockFrostApi(project_id=os.getenv('BLOCKFROST_PROJECT_ID_MAINNET'))
        assert api.address_extended(address=address)


def test_address_total(requests_mock):
    api = BlockFrostApi()
    mock_data = {
        "address": address,
        "received_sum": [
            {
                "unit": "lovelace",
                "quantity": "42000000"
            },
            {
                "unit": "b0d07d45fe9514f80213f4020e5a61241458be626841cde717cb38a76e7574636f696e",
                "quantity": "12"
            }
        ],
        "sent_sum": [
            {
                "unit": "lovelace",
                "quantity": "42000000"
            },
            {
                "unit": "b0d07d45fe9514f80213f4020e5a61241458be626841cde717cb38a76e7574636f696e",
                "quantity": "12"
            }
        ],
        "tx_count": 12
    }
    requests_mock.get(f"{api.url}/addresses/{address}/total", json=mock_data)
    assert api.address_total(address=address) == convert_json_to_object(mock_data)


def test_integration_address_total():
    if os.getenv('BLOCKFROST_PROJECT_ID_MAINNET'):
        api = BlockFrostApi(project_id=os.getenv('BLOCKFROST_PROJECT_ID_MAINNET'))
        assert api.address_total(address=address)


def test_address_utxos(requests_mock):
    api = BlockFrostApi()
    mock_data = [
        {
            "tx_hash": "39a7a284c2a0948189dc45dec670211cd4d72f7b66c5726c08d9b3df11e44d58",
            "tx_index": 1,
            "output_index": 0,
            "amount": [
                {
                    "unit": "lovelace",
                    "quantity": "42000000"
                }
            ],
            "block": "7eb8e27d18686c7db9a18f8bbcfe34e3fed6e047afaa2d969904d15e934847e6",
            "data_hash": "9e478573ab81ea7a8e31891ce0648b81229f408d596a3483e6f4f9b92d3cf710"
        },
        {
            "tx_hash": "4c4e67bafa15e742c13c592b65c8f74c769cd7d9af04c848099672d1ba391b49",
            "tx_index": 1,
            "output_index": 0,
            "amount": [
                {
                    "unit": "lovelace",
                    "quantity": "729235000"
                }
            ],
            "block": "953f1b80eb7c11a7ffcd67cbd4fde66e824a451aca5a4065725e5174b81685b7",
            "data_hash": None
        },
        {
            "tx_hash": "768c63e27a1c816a83dc7b07e78af673b2400de8849ea7e7b734ae1333d100d2",
            "tx_index": 1,
            "output_index": 1,
            "amount": [
                {
                    "unit": "lovelace",
                    "quantity": "42000000"
                },
                {
                    "unit": "b0d07d45fe9514f80213f4020e5a61241458be626841cde717cb38a76e7574636f696e",
                    "quantity": "12"
                }
            ],
            "block": "5c571f83fe6c784d3fbc223792627ccf0eea96773100f9aedecf8b1eda4544d7",
            "data_hash": None
        }
    ]
    requests_mock.get(f"{api.url}/addresses/{address}/utxos", json=mock_data)
    assert api.address_utxos(address=address) == convert_json_to_object(mock_data)


def test_integration_address_utxos():
    if os.getenv('BLOCKFROST_PROJECT_ID_MAINNET'):
        api = BlockFrostApi(project_id=os.getenv('BLOCKFROST_PROJECT_ID_MAINNET'))
        assert api.address_utxos(address=address) == []


def test_address_utxos_asset(requests_mock):
    api = BlockFrostApi()
    mock_data = [
        {
            "tx_hash": "39a7a284c2a0948189dc45dec670211cd4d72f7b66c5726c08d9b3df11e44d58",
            "output_index": 0,
            "amount": [
                {
                    "unit": "lovelace",
                    "quantity": "42000000"
                }
            ],
            "block": "7eb8e27d18686c7db9a18f8bbcfe34e3fed6e047afaa2d969904d15e934847e6",
            "data_hash": "9e478573ab81ea7a8e31891ce0648b81229f408d596a3483e6f4f9b92d3cf710"
        },
        {
            "tx_hash": "4c4e67bafa15e742c13c592b65c8f74c769cd7d9af04c848099672d1ba391b49",
            "output_index": 0,
            "amount": [
                {
                    "unit": "lovelace",
                    "quantity": "729235000"
                }
            ],
            "block": "953f1b80eb7c11a7ffcd67cbd4fde66e824a451aca5a4065725e5174b81685b7",
            "data_hash": None
        },
        {
            "tx_hash": "768c63e27a1c816a83dc7b07e78af673b2400de8849ea7e7b734ae1333d100d2",
            "output_index": 1,
            "amount": [
                {
                    "unit": "lovelace",
                    "quantity": "42000000"
                },
                {
                    "unit": "b0d07d45fe9514f80213f4020e5a61241458be626841cde717cb38a76e7574636f696e",
                    "quantity": "12"
                }
            ],
            "block": "5c571f83fe6c784d3fbc223792627ccf0eea96773100f9aedecf8b1eda4544d7",
            "data_hash": None
        }
    ]
    requests_mock.get(f"{api.url}/addresses/{address}/utxos/{asset}", json=mock_data)
    assert api.address_utxos_asset(address=address, asset=asset) == convert_json_to_object(mock_data)


def test_integration_address_utxos_asset():
    if os.getenv('BLOCKFROST_PROJECT_ID_MAINNET'):
        api = BlockFrostApi(project_id=os.getenv('BLOCKFROST_PROJECT_ID_MAINNET'))
        assert api.address_utxos_asset(address=address, asset=asset) == []


def test_address_transactions(requests_mock):
    api = BlockFrostApi()
    mock_data = [
        {
            "tx_hash": "8788591983aa73981fc92d6cddbbe643959f5a784e84b8bee0db15823f575a5b",
            "tx_index": 6,
            "block_height": 69,
            "block_time": 1635505891
        },
        {
            "tx_hash": "52e748c4dec58b687b90b0b40d383b9fe1f24c1a833b7395cdf07dd67859f46f",
            "tx_index": 9,
            "block_height": 4547,
            "block_time": 1635505987
        },
        {
            "tx_hash": "e8073fd5318ff43eca18a852527166aa8008bee9ee9e891f585612b7e4ba700b",
            "tx_index": 0,
            "block_height": 564654,
            "block_time": 1834505492
        }
    ]
    requests_mock.get(f"{api.url}/addresses/{address}/transactions", json=mock_data)
    assert api.address_transactions(address=address) == convert_json_to_object(mock_data)


def test_integration_address_transactions():
    if os.getenv('BLOCKFROST_PROJECT_ID_MAINNET'):
        api = BlockFrostApi(project_id=os.getenv('BLOCKFROST_PROJECT_ID_MAINNET'))
        assert api.address_transactions(address=address)
