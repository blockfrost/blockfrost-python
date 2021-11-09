from blockfrost import BlockFrostApi, ApiError
from blockfrost.api.cardano.transactions import \
    TransactionResponse, \
    TransactionAddressUTXOSResponse, \
    TransactionStakeResponse, \
    TransactionDelegationResponse, \
    TransactionWithdrawalResponse, \
    TransactionMIRResponse, \
    TransactionPoolUpdateResponse, \
    TransactionPoolRetiresResponse, \
    TransactionMetadataResponse, \
    TransactionMetadataCBORResponse, \
    TransactionRedeemersResponse

hash = "1e043f100dce12d107f679685acd2fc0610e10f72a92d412794c9773d11d8477"


def test_transaction(requests_mock):
    api = BlockFrostApi()
    mock_data = {
        "hash": hash,
        "block": "356b7d7dbb696ccd12775c016941057a9dc70898d87a63fc752271bb46856940",
        "block_height": 123456,
        "block_time": 1635505891,
        "slot": 42000000,
        "index": 1,
        "output_amount": [
            {
                "unit": "lovelace",
                "quantity": "42000000"
            },
            {
                "unit": "b0d07d45fe9514f80213f4020e5a61241458be626841cde717cb38a76e7574636f696e",
                "quantity": "12"
            }
        ],
        "fees": "182485",
        "deposit": "0",
        "size": 433,
        "invalid_before": None,
        "invalid_hereafter": "13885913",
        "utxo_count": 4,
        "withdrawal_count": 0,
        "mir_cert_count": 0,
        "delegation_count": 0,
        "stake_cert_count": 0,
        "pool_update_count": 0,
        "pool_retire_count": 0,
        "asset_mint_or_burn_count": 0,
        "redeemer_count": 0,
        "valid_contract": True
    }
    requests_mock.get(f"{api.url}/txs/{hash}", json=mock_data)
    mock_object = TransactionResponse(**mock_data)
    assert api.transaction(hash=hash) == mock_object


def test_transaction_utxos(requests_mock):
    api = BlockFrostApi()
    mock_data = {
        "hash": "1e043f100dce12d107f679685acd2fc0610e10f72a92d412794c9773d11d8477",
        "inputs": [
            {
                "address": "addr1q9ld26v2lv8wvrxxmvg90pn8n8n5k6tdst06q2s856rwmvnueldzuuqmnsye359fqrk8hwvenjnqultn7djtrlft7jnq7dy7wv",
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
                "tx_hash": "1a0570af966fb355a7160e4f82d5a80b8681b7955f5d44bec0dce628516157f0",
                "output_index": 0,
                "data_hash": "9e478573ab81ea7a8e31891ce0648b81229f408d596a3483e6f4f9b92d3cf710",
                "collateral": False
            }
        ],
        "outputs": [
            {
                "address": "addr1q9ld26v2lv8wvrxxmvg90pn8n8n5k6tdst06q2s856rwmvnueldzuuqmnsye359fqrk8hwvenjnqultn7djtrlft7jnq7dy7wv",
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
                "output_index": 0,
                "data_hash": "9e478573ab81ea7a8e31891ce0648b81229f408d596a3483e6f4f9b92d3cf710"
            }
        ]
    }
    requests_mock.get(f"{api.url}/txs/{hash}/utxos", json=mock_data)
    mock_object = TransactionAddressUTXOSResponse(**mock_data)
    assert api.transaction_utxos(hash=hash) == mock_object


def test_transaction_stakes(requests_mock):
    api = BlockFrostApi()
    mock_data = [
        {
            "cert_index": 0,
            "address": "stake1u9t3a0tcwune5xrnfjg4q7cpvjlgx9lcv0cuqf5mhfjwrvcwrulda",
            "registration": True
        }
    ]
    requests_mock.get(f"{api.url}/txs/{hash}/stakes", json=mock_data)
    mock_object = [TransactionStakeResponse(**data) for data in mock_data]
    assert api.transaction_stakes(hash=hash) == mock_object


def test_transaction_delegations(requests_mock):
    api = BlockFrostApi()
    mock_data = [
        {
            "index": 0,
            "cert_index": 0,
            "address": "stake1u9r76ypf5fskppa0cmttas05cgcswrttn6jrq4yd7jpdnvc7gt0yc",
            "pool_id": "pool1pu5jlj4q9w9jlxeu370a3c9myx47md5j5m2str0naunn2q3lkdy",
            "active_epoch": 210
        }
    ]
    requests_mock.get(f"{api.url}/txs/{hash}/delegations", json=mock_data)
    mock_object = [TransactionDelegationResponse(**data) for data in mock_data]
    assert api.transaction_delegations(hash=hash) == mock_object


def test_transaction_withdrawals(requests_mock):
    api = BlockFrostApi()
    mock_data = [
        {
            "address": "stake1u9r76ypf5fskppa0cmttas05cgcswrttn6jrq4yd7jpdnvc7gt0yc",
            "amount": "431833601"
        }
    ]
    requests_mock.get(f"{api.url}/txs/{hash}/withdrawals", json=mock_data)
    mock_object = [TransactionWithdrawalResponse(**data) for data in mock_data]
    assert api.transaction_withdrawals(hash=hash) == mock_object


def test_transaction_mirs(requests_mock):
    api = BlockFrostApi()
    mock_data = [
        {
            "pot": "reserve",
            "cert_index": 0,
            "address": "stake1u9r76ypf5fskppa0cmttas05cgcswrttn6jrq4yd7jpdnvc7gt0yc",
            "amount": "431833601"
        }
    ]
    requests_mock.get(f"{api.url}/txs/{hash}/mirs", json=mock_data)
    mock_object = [TransactionMIRResponse(**data) for data in mock_data]
    assert api.transaction_mirs(hash=hash) == mock_object


def test_transaction_pool_updates(requests_mock):
    api = BlockFrostApi()
    mock_data = [
        {
            "cert_index": 0,
            "pool_id": "pool1pu5jlj4q9w9jlxeu370a3c9myx47md5j5m2str0naunn2q3lkdy",
            "vrf_key": "0b5245f9934ec2151116fb8ec00f35fd00e0aa3b075c4ed12cce440f999d8233",
            "pledge": "5000000000",
            "margin_cost": 0.05,
            "fixed_cost": "340000000",
            "reward_account": "stake1uxkptsa4lkr55jleztw43t37vgdn88l6ghclfwuxld2eykgpgvg3f",
            "owners": [
                "stake1u98nnlkvkk23vtvf9273uq7cph5ww6u2yq2389psuqet90sv4xv9v"
            ],
            "metadata": {
                "url": "https://stakenuts.com/mainnet.json",
                "hash": "47c0c68cb57f4a5b4a87bad896fc274678e7aea98e200fa14a1cb40c0cab1d8c",
                "ticker": "NUTS",
                "name": "Stake Nuts",
                "description": "The best pool ever",
                "homepage": "https://stakentus.com/"
            },
            "relays": [
                {
                    "ipv4": "4.4.4.4",
                    "ipv6": "https://stakenuts.com/mainnet.json",
                    "dns": "relay1.stakenuts.com",
                    "dns_srv": "_relays._tcp.relays.stakenuts.com",
                    "port": 3001
                }
            ],
            "active_epoch": 210
        }
    ]
    requests_mock.get(f"{api.url}/txs/{hash}/pool_updates", json=mock_data)
    mock_object = [TransactionPoolUpdateResponse(**data) for data in mock_data]
    assert api.transaction_pool_updates(hash=hash) == mock_object


def test_transaction_pool_retires(requests_mock):
    api = BlockFrostApi()
    mock_data = [
        {
            "cert_index": 0,
            "pool_id": "pool1pu5jlj4q9w9jlxeu370a3c9myx47md5j5m2str0naunn2q3lkdy",
            "retiring_epoch": 216
        }
    ]
    requests_mock.get(f"{api.url}/txs/{hash}/pool_retires", json=mock_data)
    mock_object = [TransactionPoolRetiresResponse(**data) for data in mock_data]
    assert api.transaction_pool_retires(hash=hash) == mock_object


def test_transaction_metadata(requests_mock):
    api = BlockFrostApi()
    mock_data = [
        {
            "label": "1967",
            "json_metadata": {
                "metadata": "https://nut.link/metadata.json",
                "hash": "6bf124f217d0e5a0a8adb1dbd8540e1334280d49ab861127868339f43b3948af"
            }
        },
        {
            "label": "1968",
            "json_metadata": {
                "ADAUSD": [
                    {
                        "value": "0.10409800535729975",
                        "source": "ergoOracles"
                    }
                ]
            }
        }
    ]
    requests_mock.get(f"{api.url}/txs/{hash}/metadata", json=mock_data)
    mock_object = [TransactionMetadataResponse(**data) for data in mock_data]
    assert api.transaction_metadata(hash=hash) == mock_object


def test_transaction_metadata_cbor(requests_mock):
    api = BlockFrostApi()
    mock_data = [
        {
            "label": "1968",
            "cbor_metadata": "\\xa100a16b436f6d62696e6174696f6e8601010101010c",
            "metadata": "a100a16b436f6d62696e6174696f6e8601010101010c"
        }
    ]
    requests_mock.get(f"{api.url}/txs/{hash}/metadata/cbor", json=mock_data)
    mock_object = [TransactionMetadataCBORResponse(**data) for data in mock_data]
    assert api.transaction_metadata_cbor(hash=hash) == mock_object


def test_transaction_redeemers(requests_mock):
    api = BlockFrostApi()
    mock_data = [
        {
            "tx_index": 0,
            "purpose": "spend",
            "script_hash": "ec26b89af41bef0f7585353831cb5da42b5b37185e0c8a526143b824",
            "datum_hash": "923918e403bf43c34b4ef6b48eb2ee04babed17320d8d1b9ff9ad086e86f44ec",
            "unit_mem": "1700",
            "unit_steps": "476468",
            "fee": "172033"
        }
    ]
    requests_mock.get(f"{api.url}/txs/{hash}/redeemers", json=mock_data)
    mock_object = [TransactionRedeemersResponse(**data) for data in mock_data]
    assert api.transaction_redeemers(hash=hash) == mock_object


def test_transaction_submit(requests_mock):
    api = BlockFrostApi()
    mock_data = hash
    requests_mock.post(f"{api.url}/tx/submit", json=mock_data)
    mock_object = mock_data
    assert api.transaction_submit(file_path="./README.md") == mock_object
