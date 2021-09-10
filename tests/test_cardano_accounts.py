from blockfrost import BlockFrostApi, ApiError
from blockfrost.api.cardano.accounts import \
    AccountResponse, \
    AccountRewardResponse

address = 'addr1q9ucyt3s5f4naz3n7fwpnt3a0t75kl3rxdvpe63e2gdes7dzs4s26v4800nwg8jygvrdqh6xhsphct0d4zqsnd3sagxq6kwrts'
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
    mock_object = AccountResponse(**mock_data)
    assert api.accounts(stake_address=stake_address).stake_address == mock_object.stake_address


def test_account_rewards(requests_mock):
    api = BlockFrostApi()
    mock_data = [
        {
            "epoch": 215,
            "amount": "12695385",
            "pool_id": "pool1pu5jlj4q9w9jlxeu370a3c9myx47md5j5m2str0naunn2q3lkdy"
        },
        {
            "epoch": 216,
            "amount": "3586329",
            "pool_id": "pool1pu5jlj4q9w9jlxeu370a3c9myx47md5j5m2str0naunn2q3lkdy"
        },
        {
            "epoch": 217,
            "amount": "0",
            "pool_id": "pool1pu5jlj4q9w9jlxeu370a3c9myx47md5j5m2str0naunn2q3lkdy"
        },
        {
            "epoch": 218,
            "amount": "1395265",
            "pool_id": "pool1pu5jlj4q9w9jlxeu370a3c9myx47md5j5m2str0naunn2q3lkdy"
        }
    ]
    requests_mock.get(f"{api.url}/accounts/{stake_address}/rewards", json=mock_data)
    mock_object = [AccountRewardResponse(**data) for data in mock_data]
    assert api.account_rewards(stake_address=stake_address)[0].pool_id == mock_object[0].pool_id


def test_account_history():
    assert True


def test_account_delegations():
    assert True


def test_account_registrations():
    assert True


def test_account_withdrawals():
    assert True


def test_account_mirs():
    assert True


def test_account_addresses():
    assert True


def test_account_addresses_assets():
    assert True


def test_account():
    assert True


def test_account_reward():
    assert True


def test_account_history():
    assert True


def test_account_delegation():
    assert True


def test_account_registration():
    assert True


def test_account_withdrawals():
    assert True


def test_account_mirs():
    assert True


def test_account_address():
    assert True


def test_account_addresses_asset():
    assert True
