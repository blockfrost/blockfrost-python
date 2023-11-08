import os
from blockfrost import BlockFrostApi
from blockfrost.utils import convert_json_to_object


def test_mempool(requests_mock):
    api = BlockFrostApi()
    mock_data = [
        {
            "tx_hash": "6a3511c5418edb5659c925c3287bf891fb641b67cb81380de4d4b2e21bf9ca20"
        },
        {
            "tx_hash": "9006fe580833f1a49126f698a4378473c413747486c4d43f9c8e0053b434f60c"
        },
        {
            "tx_hash": "b4ccc2ef8a381f15e68c7ad654a5789f5e31fd7f6467060663e204849f9b8247"
        },
        {
            "tx_hash": "f9e07beb51a459f8dbf02d5d68793ecabda5514bcbdfe95137a3fc1826479fb7"
        },
        {
            "tx_hash": "adcb286ccb45d7c4d43827a632c32781c86122410b38d7f39b40c06ef55a792b"
        }
    ]
    requests_mock.get(f"{api.url}/mempool", json=mock_data)
    assert api.mempool() == convert_json_to_object(mock_data)


def test_integration_mempool():
    if os.getenv('BLOCKFROST_PROJECT_ID_MAINNET'):
        api = BlockFrostApi(project_id=os.getenv(
            'BLOCKFROST_PROJECT_ID_MAINNET'))
        assert api.mempool()


def test_mempool_tx(requests_mock):
    api = BlockFrostApi()
    hash = '7f9abe0b87064b6b39ec51f0f8ae976f586273c3ac123362ff550d94690d2881'
    mock_data = [
        {
            "tx": {
                "hash": "7f9abe0b87064b6b39ec51f0f8ae976f586273c3ac123362ff550d94690d2881",
                "output_amount": [
                  {
                      "unit": "lovelace",
                      "quantity": "4597809591"
                  }
                ],
                "fees": "168493",
                "deposit": "0",
                "size": 293,
                "invalid_before": None,
                "invalid_hereafter": "32304188",
                "utxo_count": 3,
                "withdrawal_count": 0,
                "mir_cert_count": 0,
                "delegation_count": 0,
                "stake_cert_count": 0,
                "pool_update_count": 0,
                "pool_retire_count": 0,
                "asset_mint_or_burn_count": 0,
                "redeemer_count": 0,
                "valid_contract": True
            },
            "inputs": [
                {
                    "address": "addr_test1qq7ee7hjrux0zhptjpvt3rfp9rw0xfgkxwpussw8am5qwx24v0taaqmfkr2w88wfaqr6e5yz8nx42hdwulu6tw25dnuqgxnk57",
                    "tx_hash": "9c5c73008491e4ce07b2c868624ae8af5ea53e5d071723f700554c576400397b",
                    "output_index": 1,
                    "collateral": False,
                    "reference": False
                }
            ],
            "outputs": [
                {
                    "address": "addr_test1qru6ah9weaq77re5jkjv65fgteppd3y7m5ezar4x7nyav5csg06mvtj45v4nhstgf92qghdz3rrf9x5f0h9ac8n48zrs7tv53q",
                    "amount": [
                        {
                            "unit": "lovelace",
                            "quantity": "50000000"
                        }
                    ],
                    "output_index": 0,
                    "data_hash": None,
                    "inline_datum": None,
                    "collateral": False,
                    "reference_script_hash": None
                },
                {
                    "address": "addr_test1qq7ee7hjrux0zhptjpvt3rfp9rw0xfgkxwpussw8am5qwx24v0taaqmfkr2w88wfaqr6e5yz8nx42hdwulu6tw25dnuqgxnk57",
                    "amount": [
                        {
                            "unit": "lovelace",
                            "quantity": "4547809591"
                        }
                    ],
                    "output_index": 1,
                    "data_hash": None,
                    "inline_datum": None,
                    "collateral": False,
                    "reference_script_hash": None
                }
            ]
        }
    ]
    requests_mock.get(f"{api.url}/mempool/{hash}", json=mock_data)
    assert api.mempool_tx(hash) == convert_json_to_object(mock_data)


# def test_integration_mempool():
#     if os.getenv('BLOCKFROST_PROJECT_ID_MAINNET'):
#         api = BlockFrostApi(project_id=os.getenv(
#             'BLOCKFROST_PROJECT_ID_MAINNET'))
#         assert api.mempool_tx()

def test_mempool_address(requests_mock):
    address = 'addr1qyptln5t5s0mastzc9rksn6wdqp9ynt67ahw0nhzukar5keu7yzv8ay6qvmlywtgvt7exaxt783dxuzv03qal7muda5sl42hg6'
    api = BlockFrostApi()
    mock_data = [
        {
            "tx_hash": "6a3511c5418edb5659c925c3287bf891fb641b67cb81380de4d4b2e21bf9ca20"
        }
    ]
    requests_mock.get(
        f"{api.url}/mempool/addresses/{address}", json=mock_data)
    assert api.mempool_address(address) == convert_json_to_object(mock_data)


# def test_integration_mempool_address():
#     if os.getenv('BLOCKFROST_PROJECT_ID_MAINNET'):
#         api = BlockFrostApi(project_id=os.getenv(
#             'BLOCKFROST_PROJECT_ID_MAINNET'))
#         assert api.mempool_address()
