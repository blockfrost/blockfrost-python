import os
from blockfrost import BlockFrostApi, ApiError
from blockfrost.utils import convert_json_to_object

epoch = 225
pool_id = 'pool1pu5jlj4q9w9jlxeu370a3c9myx47md5j5m2str0naunn2q3lkdy'


def test_epoch_latest(requests_mock):
    api = BlockFrostApi()
    mock_data = {
        "epoch": epoch,
        "start_time": 1603403091,
        "end_time": 1603835086,
        "first_block_time": 1603403092,
        "last_block_time": 1603835084,
        "block_count": 21298,
        "tx_count": 17856,
        "output": "7849943934049314",
        "fees": "4203312194",
        "active_stake": "784953934049314"
    }
    requests_mock.get(f"{api.url}/epochs/latest", json=mock_data)
    assert api.epoch_latest() == convert_json_to_object(mock_data)


def test_integration_epoch_latest():
    if os.getenv('BLOCKFROST_PROJECT_ID_MAINNET'):
        api = BlockFrostApi(project_id=os.getenv('BLOCKFROST_PROJECT_ID_MAINNET'))
        assert api.epoch_latest()


def test_epoch_latest_parameters(requests_mock):
    api = BlockFrostApi()
    mock_data = {
        "epoch": epoch,
        "min_fee_a": 44,
        "min_fee_b": 155381,
        "max_block_size": 65536,
        "max_tx_size": 16384,
        "max_block_header_size": 1100,
        "key_deposit": "2000000",
        "pool_deposit": "500000000",
        "e_max": 18,
        "n_opt": 150,
        "a0": 0.3,
        "rho": 0.003,
        "tau": 0.2,
        "decentralisation_param": 0.5,
        "extra_entropy": None,
        "protocol_major_ver": 2,
        "protocol_minor_ver": 0,
        "min_utxo": "1000000",
        "min_pool_cost": "340000000",
        "nonce": "1a3be38bcbb7911969283716ad7aa550250226b76a61fc51cc9a9a35d9276d81",
        "price_mem": 0.0577,
        "price_step": 0.0000721,
        "max_tx_ex_mem": "10000000",
        "max_tx_ex_steps": "10000000000",
        "max_block_ex_mem": "50000000",
        "max_block_ex_steps": "40000000000",
        "max_val_size": "5000",
        "collateral_percent": 150,
        "max_collateral_inputs": 3,
        "coins_per_utxo_word": "34482"
    }
    requests_mock.get(f"{api.url}/epochs/latest/parameters", json=mock_data)
    assert api.epoch_latest_parameters() == convert_json_to_object(mock_data)


def test_integration_epoch_latest_parameters():
    if os.getenv('BLOCKFROST_PROJECT_ID_MAINNET'):
        api = BlockFrostApi(project_id=os.getenv('BLOCKFROST_PROJECT_ID_MAINNET'))
        assert api.epoch_latest_parameters()


def test_epoch(requests_mock):
    api = BlockFrostApi()
    mock_data = {
        "epoch": epoch,
        "start_time": 1603403091,
        "end_time": 1603835086,
        "first_block_time": 1603403092,
        "last_block_time": 1603835084,
        "block_count": 21298,
        "tx_count": 17856,
        "output": "7849943934049314",
        "fees": "4203312194",
        "active_stake": "784953934049314"
    }
    requests_mock.get(f"{api.url}/epochs/{epoch}", json=mock_data)
    assert api.epoch(number=epoch) == convert_json_to_object(mock_data)


def test_integration_epoch():
    if os.getenv('BLOCKFROST_PROJECT_ID_MAINNET'):
        api = BlockFrostApi(project_id=os.getenv('BLOCKFROST_PROJECT_ID_MAINNET'))
        assert api.epoch(number=epoch)


def test_epochs_next(requests_mock):
    api = BlockFrostApi()
    mock_data = [
        {
            "epoch": 225,
            "start_time": 1603403091,
            "end_time": 1603835086,
            "first_block_time": 1603403092,
            "last_block_time": 1603835084,
            "block_count": 21298,
            "tx_count": 17856,
            "output": "7849943934049314",
            "fees": "4203312194",
            "active_stake": "784953934049314"
        }
    ]
    requests_mock.get(f"{api.url}/epochs/{epoch}/next", json=mock_data)
    assert api.epochs_next(number=epoch) == convert_json_to_object(mock_data)


def test_integration_epochs_next():
    if os.getenv('BLOCKFROST_PROJECT_ID_MAINNET'):
        api = BlockFrostApi(project_id=os.getenv('BLOCKFROST_PROJECT_ID_MAINNET'))
        assert api.epochs_next(number=epoch)


def test_epochs_previous(requests_mock):
    api = BlockFrostApi()
    mock_data = [
        {
            "epoch": 225,
            "start_time": 1603403091,
            "end_time": 1603835086,
            "first_block_time": 1603403092,
            "last_block_time": 1603835084,
            "block_count": 21298,
            "tx_count": 17856,
            "output": "7849943934049314",
            "fees": "4203312194",
            "active_stake": "784953934049314"
        }
    ]
    requests_mock.get(f"{api.url}/epochs/{epoch}/previous", json=mock_data)
    assert api.epochs_previous(number=epoch) == convert_json_to_object(mock_data)


def test_integration_epochs_previous():
    if os.getenv('BLOCKFROST_PROJECT_ID_MAINNET'):
        api = BlockFrostApi(project_id=os.getenv('BLOCKFROST_PROJECT_ID_MAINNET'))
        assert api.epochs_previous(number=epoch)


def test_epoch_stakes(requests_mock):
    api = BlockFrostApi()
    mock_data = [
        {
            "stake_address": "stake1u9l5q5jwgelgagzyt6nuaasefgmn8pd25c8e9qpeprq0tdcp0e3uk",
            "pool_id": pool_id,
            "amount": "4440295078"
        }
    ]
    requests_mock.get(f"{api.url}/epochs/{epoch}/stakes", json=mock_data)
    assert api.epoch_stakes(number=epoch) == convert_json_to_object(mock_data)


def test_integration_epoch_stakes():
    if os.getenv('BLOCKFROST_PROJECT_ID_MAINNET'):
        api = BlockFrostApi(project_id=os.getenv('BLOCKFROST_PROJECT_ID_MAINNET'))
        assert api.epoch_stakes(number=epoch)


def test_epoch_pool_stakes(requests_mock):
    api = BlockFrostApi()
    mock_data = [
        {
            "stake_address": "stake1u9l5q5jwgelgagzyt6nuaasefgmn8pd25c8e9qpeprq0tdcp0e3uk",
            "amount": "4440295078"
        }
    ]
    requests_mock.get(f"{api.url}/epochs/{epoch}/stakes/{pool_id}", json=mock_data)
    assert api.epoch_pool_stakes(number=epoch, pool_id=pool_id) == convert_json_to_object(mock_data)


def test_integration_epoch_pool_stakes():
    if os.getenv('BLOCKFROST_PROJECT_ID_MAINNET'):
        api = BlockFrostApi(project_id=os.getenv('BLOCKFROST_PROJECT_ID_MAINNET'))
        assert api.epoch_pool_stakes(number=epoch, pool_id=pool_id)


def test_epoch_blocks(requests_mock):
    api = BlockFrostApi()
    mock_data = [
        "d0fa315687e99ccdc96b14cc2ea74a767405d64427b648c470731a9b69e4606e",
        "38bc6efb92a830a0ed22a64f979d120d26483fd3c811f6622a8c62175f530878",
        "f3258fcd8b975c061b4fcdcfcbb438807134d6961ec278c200151274893b6b7d"
    ]
    requests_mock.get(f"{api.url}/epochs/{epoch}/blocks", json=mock_data)
    assert api.epoch_blocks(number=epoch) == convert_json_to_object(mock_data)


def test_integration_epoch_blocks():
    if os.getenv('BLOCKFROST_PROJECT_ID_MAINNET'):
        api = BlockFrostApi(project_id=os.getenv('BLOCKFROST_PROJECT_ID_MAINNET'))
        assert api.epoch_blocks(number=epoch)


def test_epoch_pool_blocks(requests_mock):
    api = BlockFrostApi()
    mock_data = [
        "d0fa315687e99ccdc96b14cc2ea74a767405d64427b648c470731a9b69e4606e",
        "38bc6efb92a830a0ed22a64f979d120d26483fd3c811f6622a8c62175f530878",
        "f3258fcd8b975c061b4fcdcfcbb438807134d6961ec278c200151274893b6b7d"
    ]
    requests_mock.get(f"{api.url}/epochs/{epoch}/blocks/{pool_id}", json=mock_data)
    assert api.epoch_pool_blocks(number=epoch, pool_id=pool_id) == convert_json_to_object(mock_data)


def test_integration_epoch_pool_blocks():
    if os.getenv('BLOCKFROST_PROJECT_ID_MAINNET'):
        api = BlockFrostApi(project_id=os.getenv('BLOCKFROST_PROJECT_ID_MAINNET'))
        assert api.epoch_pool_blocks(number=epoch, pool_id=pool_id)


def test_epoch_latest_parameters(requests_mock):
    api = BlockFrostApi()
    mock_data = {
        "epoch": epoch,
        "min_fee_a": 44,
        "min_fee_b": 155381,
        "max_block_size": 65536,
        "max_tx_size": 16384,
        "max_block_header_size": 1100,
        "key_deposit": "2000000",
        "pool_deposit": "500000000",
        "e_max": 18,
        "n_opt": 150,
        "a0": 0.3,
        "rho": 0.003,
        "tau": 0.2,
        "decentralisation_param": 0.5,
        "extra_entropy": None,
        "protocol_major_ver": 2,
        "protocol_minor_ver": 0,
        "min_utxo": "1000000",
        "min_pool_cost": "340000000",
        "nonce": "1a3be38bcbb7911969283716ad7aa550250226b76a61fc51cc9a9a35d9276d81",
        "price_mem": 0.001,
        "price_step": 0.01,
        "max_tx_ex_mem": "11000000000",
        "max_tx_ex_steps": "11000000000",
        "max_block_ex_mem": "110000000000",
        "max_block_ex_steps": "110000000000",
        "max_val_size": "5000",
        "collateral_percent": 1.5,
        "max_collateral_inputs": 6,
        "coins_per_utxo_word": "34482"
    }
    requests_mock.get(f"{api.url}/epochs/{epoch}/parameters", json=mock_data)
    assert api.epoch_protocol_parameters(number=epoch) == convert_json_to_object(mock_data)


def test_integration_epoch_latest_parameters():
    if os.getenv('BLOCKFROST_PROJECT_ID_MAINNET'):
        api = BlockFrostApi(project_id=os.getenv('BLOCKFROST_PROJECT_ID_MAINNET'))
        assert api.epoch_protocol_parameters(number=epoch)
