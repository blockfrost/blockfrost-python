import os
from blockfrost import BlockFrostApi, ApiError
from blockfrost.utils import convert_json_to_object

stake_address = 'stake1ux3g2c9dx2nhhehyrezyxpkstartcqmu9hk63qgfkccw5rqttygt7'


def test_accounts(requests_mock):
    api = BlockFrostApi()
    mock_data = {
        "stake_address": stake_address,
        "active": True,
        "active_epoch": 412,
        "controlled_amount": "619154618165",
        "rewards_sum": "319154618165",
        "withdrawals_sum": "12125369253",
        "reserves_sum": "319154618165",
        "treasury_sum": "12000000",
        "withdrawable_amount": "319154618165",
        "pool_id": "pool1pu5jlj4q9w9jlxeu370a3c9myx47md5j5m2str0naunn2q3lkdy"
    }
    requests_mock.get(f"{api.url}/accounts/{stake_address}", json=mock_data)
    assert api.accounts(stake_address=stake_address) == convert_json_to_object(mock_data)


def test_integration_accounts():
    if os.getenv('BLOCKFROST_PROJECT_ID_MAINNET'):
        api = BlockFrostApi(project_id=os.getenv('BLOCKFROST_PROJECT_ID_MAINNET'))
        assert api.accounts(stake_address=stake_address)


def test_account_rewards(requests_mock):
    api = BlockFrostApi()
    mock_data = [
        {
            "epoch": 215,
            "amount": "12695385",
            "pool_id": "pool1pu5jlj4q9w9jlxeu370a3c9myx47md5j5m2str0naunn2q3lkdy",
            "type": "member"
        },
        {
            "epoch": 216,
            "amount": "3586329",
            "pool_id": "pool1pu5jlj4q9w9jlxeu370a3c9myx47md5j5m2str0naunn2q3lkdy",
            "type": "member"
        },
        {
            "epoch": 217,
            "amount": "1",
            "pool_id": "pool1pu5jlj4q9w9jlxeu370a3c9myx47md5j5m2str0naunn2q3lkdy",
            "type": "member"
        },
        {
            "epoch": 217,
            "amount": "1337",
            "pool_id": "pool1cytwr0n7eas6du2h2xshl8ypa1yqr18f0erlhhjcuczysiunjcs",
            "type": "leader"
        },
        {
            "epoch": 218,
            "amount": "1395265",
            "pool_id": "pool1pu5jlj4q9w9jlxeu370a3c9myx47md5j5m2str0naunn2q3lkdy",
            "type": "member"
        },
        {
            "epoch": 218,
            "amount": "500000000",
            "pool_id": "pool1cytwr0n7eas6du2h2xshl8ypa1yqr18f0erlhhjcuczysiunjcs",
            "type": "pool_deposit_refund"
        }
    ]
    requests_mock.get(f"{api.url}/accounts/{stake_address}/rewards", json=mock_data)
    assert api.account_rewards(stake_address=stake_address) == convert_json_to_object(mock_data)


def test_integration_account_rewards():
    if os.getenv('BLOCKFROST_PROJECT_ID_MAINNET'):
        api = BlockFrostApi(project_id=os.getenv('BLOCKFROST_PROJECT_ID_MAINNET'))
        assert api.account_rewards(stake_address=stake_address)


def test_account_history(requests_mock):
    api = BlockFrostApi()
    mock_data = [
        {
            "active_epoch": 210,
            "amount": "12695385",
            "pool_id": "pool1pu5jlj4q9w9jlxeu370a3c9myx47md5j5m2str0naunn2q3lkdy"
        },
        {
            "active_epoch": 211,
            "amount": "22695385",
            "pool_id": "pool1pu5jlj4q9w9jlxeu370a3c9myx47md5j5m2str0naunn2q3lkdy"
        }
    ]
    requests_mock.get(f"{api.url}/accounts/{stake_address}/history", json=mock_data)
    assert api.account_history(stake_address=stake_address) == convert_json_to_object(mock_data)


def test_integration_account_history():
    if os.getenv('BLOCKFROST_PROJECT_ID_MAINNET'):
        api = BlockFrostApi(project_id=os.getenv('BLOCKFROST_PROJECT_ID_MAINNET'))
        assert api.account_history(stake_address=stake_address)


def test_account_delegations(requests_mock):
    api = BlockFrostApi()
    mock_data = [
        {
            "active_epoch": 210,
            "tx_hash": "2dd15e0ef6e6a17841cb9541c27724072ce4d4b79b91e58432fbaa32d9572531",
            "amount": "12695385",
            "pool_id": "pool1pu5jlj4q9w9jlxeu370a3c9myx47md5j5m2str0naunn2q3lkdy"
        },
        {
            "active_epoch": 242,
            "tx_hash": "1a0570af966fb355a7160e4f82d5a80b8681b7955f5d44bec0dde628516157f0",
            "amount": "12691385",
            "pool_id": "pool1kchver88u3kygsak8wgll7htr8uxn5v35lfrsyy842nkscrzyvj"
        }
    ]
    requests_mock.get(f"{api.url}/accounts/{stake_address}/delegations", json=mock_data)
    assert api.account_delegations(stake_address=stake_address) == convert_json_to_object(mock_data)


def test_integration_account_delegations():
    if os.getenv('BLOCKFROST_PROJECT_ID_MAINNET'):
        api = BlockFrostApi(project_id=os.getenv('BLOCKFROST_PROJECT_ID_MAINNET'))
        assert api.account_delegations(stake_address=stake_address)


def test_account_registrations(requests_mock):
    api = BlockFrostApi()
    mock_data = [
        {
            "tx_hash": "2dd15e0ef6e6a17841cb9541c27724072ce4d4b79b91e58432fbaa32d9572531",
            "action": "registered"
        },
        {
            "tx_hash": "1a0570af966fb355a7160e4f82d5a80b8681b7955f5d44bec0dde628516157f0",
            "action": "deregistered"
        }
    ]
    requests_mock.get(f"{api.url}/accounts/{stake_address}/registrations", json=mock_data)
    assert api.account_registrations(stake_address=stake_address) == convert_json_to_object(mock_data)


def test_integration_account_registrations():
    if os.getenv('BLOCKFROST_PROJECT_ID_MAINNET'):
        api = BlockFrostApi(project_id=os.getenv('BLOCKFROST_PROJECT_ID_MAINNET'))
        assert api.account_registrations(stake_address=stake_address)


def test_account_withdrawals(requests_mock):
    api = BlockFrostApi()
    mock_data = [
        {
            "tx_hash": "48a9625c841eea0dd2bb6cf551eabe6523b7290c9ce34be74eedef2dd8f7ecc5",
            "amount": "454541212442"
        },
        {
            "tx_hash": "4230b0cbccf6f449f0847d8ad1d634a7a49df60d8c142bb8cc2dbc8ca03d9e34",
            "amount": "97846969"
        }
    ]
    requests_mock.get(f"{api.url}/accounts/{stake_address}/withdrawals", json=mock_data)
    assert api.account_withdrawals(stake_address=stake_address) == convert_json_to_object(mock_data)


def test_integration_account_withdrawals():
    if os.getenv('BLOCKFROST_PROJECT_ID_MAINNET'):
        api = BlockFrostApi(project_id=os.getenv('BLOCKFROST_PROJECT_ID_MAINNET'))
        assert api.account_withdrawals(stake_address=stake_address)


def test_account_mirs(requests_mock):
    api = BlockFrostApi()
    mock_data = [
        {
            "tx_hash": "69705bba1d687a816ff5a04ec0c358a1f1ef075ab7f9c6cc2763e792581cec6d",
            "amount": "2193707473"
        },
        {
            "tx_hash": "baaa77b63d4d7d2bb3ab02c9b85978c2092c336dede7f59e31ad65452d510c13",
            "amount": "14520198574"
        }
    ]
    requests_mock.get(f"{api.url}/accounts/{stake_address}/mirs", json=mock_data)
    assert api.account_mirs(stake_address=stake_address) == convert_json_to_object(mock_data)


def test_integration_account_mirs():
    if os.getenv('BLOCKFROST_PROJECT_ID_MAINNET'):
        api = BlockFrostApi(project_id=os.getenv('BLOCKFROST_PROJECT_ID_MAINNET'))
        assert api.account_mirs(stake_address=stake_address)


def test_account_addresses(requests_mock):
    api = BlockFrostApi()
    mock_data = [
        {
            "address": "addr1qx2kd28nq8ac5prwg32hhvudlwggpgfp8utlyqxu6wqgz62f79qsdmm5dsknt9ecr5w468r9ey0fxwkdrwh08ly3tu9sy0f4qd"
        },
        {
            "address": "addr1qys3czp8s9thc6u2fqed9yq3h24nyw28uk0m6mkgn9dkckjf79qsdmm5dsknt9ecr5w468r9ey0fxwkdrwh08ly3tu9suth4w4"
        },
        {
            "address": "addr1q8j55h253zcvl326sk5qdt2n8z7eghzspe0ekxgncr796s2f79qsdmm5dsknt9ecr5w468r9ey0fxwkdrwh08ly3tu9sjmd35m"
        },
        {
            "address": "addr1q8f7gxrprank3drhx8k5grlux7ene0nlwun8y9thu8mc3yjf79qsdmm5dsknt9ecr5w468r9ey0fxwkdrwh08ly3tu9sls6vnt"
        }
    ]
    requests_mock.get(f"{api.url}/accounts/{stake_address}/addresses", json=mock_data)
    assert api.account_addresses(stake_address=stake_address) == convert_json_to_object(mock_data)


def test_integration_account_addresses():
    if os.getenv('BLOCKFROST_PROJECT_ID_MAINNET'):
        api = BlockFrostApi(project_id=os.getenv('BLOCKFROST_PROJECT_ID_MAINNET'))
        assert api.account_addresses(stake_address=stake_address)


def test_account_addresses_assets(requests_mock):
    api = BlockFrostApi()
    mock_data = [
        {
            "unit": "d5e6bf0500378d4f0da4e8dde6becec7621cd8cbf5cbb9b87013d4cc537061636542756433343132",
            "quantity": "1"
        },
        {
            "unit": "b0d07d45fe9514f80213f4020e5a61241458be626841cde717cb38a76e7574636f696e",
            "quantity": "125"
        }
    ]
    requests_mock.get(f"{api.url}/accounts/{stake_address}/addresses/assets", json=mock_data)
    assert api.account_addresses_assets(stake_address=stake_address) == convert_json_to_object(mock_data)


def test_integration_account_addresses_assets():
    if os.getenv('BLOCKFROST_PROJECT_ID_MAINNET'):
        api = BlockFrostApi(project_id=os.getenv('BLOCKFROST_PROJECT_ID_MAINNET'))
        assert api.account_addresses_assets(stake_address=stake_address) == []


def test_account_addresses_total(requests_mock):
    api = BlockFrostApi()
    mock_data = {
        "stake_address": "stake1u9l5q5jwgelgagzyt6nuaasefgmn8pd25c8e9qpeprq0tdcp0e3uk",
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
    requests_mock.get(f"{api.url}/accounts/{stake_address}/addresses/total", json=mock_data)
    assert api.account_addresses_total(stake_address=stake_address) == convert_json_to_object(mock_data)


def test_integration_account_addresses_total():
    if os.getenv('BLOCKFROST_PROJECT_ID_MAINNET'):
        api = BlockFrostApi(project_id=os.getenv('BLOCKFROST_PROJECT_ID_MAINNET'))
        assert api.account_addresses_total(stake_address=stake_address)
