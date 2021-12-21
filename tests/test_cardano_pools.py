import os
from blockfrost import BlockFrostApi, ApiError
from blockfrost.utils import convert_json_to_object

pool_id = 'pool1pu5jlj4q9w9jlxeu370a3c9myx47md5j5m2str0naunn2q3lkdy'


def test_pools(requests_mock):
    api = BlockFrostApi()
    mock_data = [
        "pool1pu5jlj4q9w9jlxeu370a3c9myx47md5j5m2str0naunn2q3lkdy",
        "pool1hn7hlwrschqykupwwrtdfkvt2u4uaxvsgxyh6z63703p2knj288",
        "pool1ztjyjfsh432eqetadf82uwuxklh28xc85zcphpwq6mmezavzad2"
    ]
    requests_mock.get(f"{api.url}/pools", json=mock_data)
    assert api.pools() == convert_json_to_object(mock_data)


def test_integration_pools():
    if os.getenv('BLOCKFROST_PROJECT_ID_MAINNET'):
        api = BlockFrostApi(project_id=os.getenv('BLOCKFROST_PROJECT_ID_MAINNET'))
        assert api.pools()


def test_pools_extended(requests_mock):
    api = BlockFrostApi()
    mock_data = [
        {
            "pool_id": "pool19u64770wqp6s95gkajc8udheske5e6ljmpq33awxk326zjaza0q",
            "active_stake": "1541200000",
            "live_stake": "1541400000"
        },
        {
            "pool_id": "pool1dvla4zq98hpvacv20snndupjrqhuc79zl6gjap565nku6et5zdx",
            "active_stake": "22200000",
            "live_stake": "48955550"
        },
        {
            "pool_id": "pool1wvccajt4eugjtf3k0ja3exjqdj7t8egsujwhcw4tzj4rzsxzw5w",
            "active_stake": "9989541215",
            "live_stake": "168445464878"
        }
    ]
    requests_mock.get(f"{api.url}/pools/extended", json=mock_data)
    assert api.pools_extended() == convert_json_to_object(mock_data)


def test_integration_pools_extended():
    if os.getenv('BLOCKFROST_PROJECT_ID_MAINNET'):
        api = BlockFrostApi(project_id=os.getenv('BLOCKFROST_PROJECT_ID_MAINNET'))
        assert api.pools_extended()


def test_pools_retired(requests_mock):
    api = BlockFrostApi()
    mock_data = [
        {
            "pool_id": "pool19u64770wqp6s95gkajc8udheske5e6ljmpq33awxk326zjaza0q",
            "epoch": 225
        },
        {
            "pool_id": "pool1dvla4zq98hpvacv20snndupjrqhuc79zl6gjap565nku6et5zdx",
            "epoch": 215
        },
        {
            "pool_id": "pool1wvccajt4eugjtf3k0ja3exjqdj7t8egsujwhcw4tzj4rzsxzw5w",
            "epoch": 231
        }
    ]
    requests_mock.get(f"{api.url}/pools/retired", json=mock_data)
    assert api.pools_retired() == convert_json_to_object(mock_data)


def test_integration_pools_retired():
    if os.getenv('BLOCKFROST_PROJECT_ID_MAINNET'):
        api = BlockFrostApi(project_id=os.getenv('BLOCKFROST_PROJECT_ID_MAINNET'))
        assert api.pools_retired()


def test_pools_retiring(requests_mock):
    api = BlockFrostApi()
    mock_data = [
        {
            "pool_id": "pool19u64770wqp6s95gkajc8udheske5e6ljmpq33awxk326zjaza0q",
            "epoch": 225
        },
        {
            "pool_id": "pool1dvla4zq98hpvacv20snndupjrqhuc79zl6gjap565nku6et5zdx",
            "epoch": 215
        },
        {
            "pool_id": "pool1wvccajt4eugjtf3k0ja3exjqdj7t8egsujwhcw4tzj4rzsxzw5w",
            "epoch": 231
        }
    ]
    requests_mock.get(f"{api.url}/pools/retiring", json=mock_data)
    assert api.pools_retiring() == convert_json_to_object(mock_data)


def test_integration_pools_retiring():
    if os.getenv('BLOCKFROST_PROJECT_ID_MAINNET'):
        api = BlockFrostApi(project_id=os.getenv('BLOCKFROST_PROJECT_ID_MAINNET'))
        assert api.pools_retiring()


def test_pool(requests_mock):
    api = BlockFrostApi()
    mock_data = {
        "pool_id": pool_id,
        "hex": "0f292fcaa02b8b2f9b3c8f9fd8e0bb21abedb692a6d5058df3ef2735",
        "vrf_key": "0b5245f9934ec2151116fb8ec00f35fd00e0aa3b075c4ed12cce440f999d8233",
        "blocks_minted": 69,
        "blocks_epoch": 4,
        "live_stake": "6900000000",
        "live_size": 0.42,
        "live_saturation": 0.93,
        "live_delegators": 127,
        "active_stake": "4200000000",
        "active_size": 0.43,
        "declared_pledge": "5000000000",
        "live_pledge": "5000000001",
        "margin_cost": 0.05,
        "fixed_cost": "340000000",
        "reward_account": "stake1uxkptsa4lkr55jleztw43t37vgdn88l6ghclfwuxld2eykgpgvg3f",
        "owners": [
            "stake1u98nnlkvkk23vtvf9273uq7cph5ww6u2yq2389psuqet90sv4xv9v"
        ],
        "registration": [
            "9f83e5484f543e05b52e99988272a31da373f3aab4c064c76db96643a355d9dc",
            "7ce3b8c433bf401a190d58c8c483d8e3564dfd29ae8633c8b1b3e6c814403e95",
            "3e6e1200ce92977c3fe5996bd4d7d7e192bcb7e231bc762f9f240c76766535b9"
        ],
        "retirement": [
            "252f622976d39e646815db75a77289cf16df4ad2b287dd8e3a889ce14c13d1a8"
        ]
    }
    requests_mock.get(f"{api.url}/pools/{pool_id}", json=mock_data)
    assert api.pool(pool_id=pool_id) == convert_json_to_object(mock_data)


def test_integration_pool():
    if os.getenv('BLOCKFROST_PROJECT_ID_MAINNET'):
        api = BlockFrostApi(project_id=os.getenv('BLOCKFROST_PROJECT_ID_MAINNET'))
        assert api.pool(pool_id=pool_id)


def test_pool_history(requests_mock):
    api = BlockFrostApi()
    mock_data = [
        {
            "epoch": 233,
            "blocks": 22,
            "active_stake": "20485965693569",
            "active_size": 1.2345,
            "delegators_count": 115,
            "rewards": "206936253674159",
            "fees": "1290968354"
        }
    ]
    requests_mock.get(f"{api.url}/pools/{pool_id}/history", json=mock_data)
    assert api.pool_history(pool_id=pool_id) == convert_json_to_object(mock_data)


def test_integration_pool_history():
    if os.getenv('BLOCKFROST_PROJECT_ID_MAINNET'):
        api = BlockFrostApi(project_id=os.getenv('BLOCKFROST_PROJECT_ID_MAINNET'))
        assert api.pool_history(pool_id=pool_id)


def test_pool_metadata(requests_mock):
    api = BlockFrostApi()
    mock_data = {
        "pool_id": pool_id,
        "hex": "0f292fcaa02b8b2f9b3c8f9fd8e0bb21abedb692a6d5058df3ef2735",
        "url": "https://stakenuts.com/mainnet.json",
        "hash": "47c0c68cb57f4a5b4a87bad896fc274678e7aea98e200fa14a1cb40c0cab1d8c",
        "ticker": "NUTS",
        "name": "Stake Nuts",
        "description": "The best pool ever",
        "homepage": "https://stakentus.com/"
    }
    requests_mock.get(f"{api.url}/pools/{pool_id}/metadata", json=mock_data)
    assert api.pool_metadata(pool_id=pool_id) == convert_json_to_object(mock_data)


def test_integration_pool_metadata():
    if os.getenv('BLOCKFROST_PROJECT_ID_MAINNET'):
        api = BlockFrostApi(project_id=os.getenv('BLOCKFROST_PROJECT_ID_MAINNET'))
        assert api.pool_metadata(pool_id=pool_id)


def test_pool_relays(requests_mock):
    api = BlockFrostApi()
    mock_data = [
        {
            "ipv4": "4.4.4.4",
            "ipv6": "https://stakenuts.com/mainnet.json",
            "dns": "relay1.stakenuts.com",
            "dns_srv": "_relays._tcp.relays.stakenuts.com",
            "port": 3001
        }
    ]
    requests_mock.get(f"{api.url}/pools/{pool_id}/relays", json=mock_data)
    assert api.pool_relays(pool_id=pool_id) == convert_json_to_object(mock_data)


def test_integration_pool_relays():
    if os.getenv('BLOCKFROST_PROJECT_ID_MAINNET'):
        api = BlockFrostApi(project_id=os.getenv('BLOCKFROST_PROJECT_ID_MAINNET'))
        assert api.pool_relays(pool_id=pool_id)


def test_pool_delegators(requests_mock):
    api = BlockFrostApi()
    mock_data = [
        {
            "address": "stake1ux4vspfvwuus9uwyp5p3f0ky7a30jq5j80jxse0fr7pa56sgn8kha",
            "live_stake": "1137959159981411"
        },
        {
            "address": "stake1uylayej7esmarzd4mk4aru37zh9yz0luj3g9fsvgpfaxulq564r5u",
            "live_stake": "16958865648"
        },
        {
            "address": "stake1u8lr2pnrgf8f7vrs9lt79hc3sxm8s2w4rwvgpncks3axx6q93d4ck",
            "live_stake": "18605647"
        }
    ]
    requests_mock.get(f"{api.url}/pools/{pool_id}/delegators", json=mock_data)
    assert api.pool_delegators(pool_id=pool_id) == convert_json_to_object(mock_data)


def test_integration_pool_delegators():
    if os.getenv('BLOCKFROST_PROJECT_ID_MAINNET'):
        api = BlockFrostApi(project_id=os.getenv('BLOCKFROST_PROJECT_ID_MAINNET'))
        assert api.pool_delegators(pool_id=pool_id)


def test_pool_blocks(requests_mock):
    api = BlockFrostApi()
    mock_data = [
        "d8982ca42cfe76b747cc681d35d671050a9e41e9cfe26573eb214e94fe6ff21d",
        "026436c539e2ce84c7f77ffe669f4e4bbbb3b9c53512e5857dcba8bb0b4e9a8c",
        "bcc8487f419b8c668a18ea2120822a05df6dfe1de1f0fac3feba88cf760f303c",
        "86bf7b4a274e0f8ec9816171667c1b4a0cfc661dc21563f271acea9482b62df7"
    ]
    requests_mock.get(f"{api.url}/pools/{pool_id}/blocks", json=mock_data)
    assert api.pool_blocks(pool_id=pool_id) == convert_json_to_object(mock_data)


def test_integration_pool_blocks():
    if os.getenv('BLOCKFROST_PROJECT_ID_MAINNET'):
        api = BlockFrostApi(project_id=os.getenv('BLOCKFROST_PROJECT_ID_MAINNET'))
        assert api.pool_blocks(pool_id=pool_id)


def test_pool_updates(requests_mock):
    api = BlockFrostApi()
    mock_data = [
        {
            "tx_hash": "6804edf9712d2b619edb6ac86861fe93a730693183a262b165fcc1ba1bc99cad",
            "cert_index": 0,
            "action": "registered"
        },
        {
            "tx_hash": "9c190bc1ac88b2ab0c05a82d7de8b71b67a9316377e865748a89d4426c0d3005",
            "cert_index": 0,
            "action": "deregistered"
        },
        {
            "tx_hash": "e14a75b0eb2625de7055f1f580d70426311b78e0d36dd695a6bdc96c7b3d80e0",
            "cert_index": 1,
            "action": "registered"
        }
    ]
    requests_mock.get(f"{api.url}/pools/{pool_id}/updates", json=mock_data)
    assert api.pool_updates(pool_id=pool_id) == convert_json_to_object(mock_data)


def test_integration_pool_updates():
    if os.getenv('BLOCKFROST_PROJECT_ID_MAINNET'):
        api = BlockFrostApi(project_id=os.getenv('BLOCKFROST_PROJECT_ID_MAINNET'))
        assert api.pool_updates(pool_id=pool_id)
