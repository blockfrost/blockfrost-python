[![Package Test](https://github.com/blockfrost/blockfrost-python/actions/workflows/package-test.yml/badge.svg)](https://github.com/blockfrost/blockfrost-python/actions/workflows/package-test.yml)
[![PyPI Latest Release](https://img.shields.io/pypi/v/blockfrost-python.svg)](https://pypi.org/project/blockfrost-python/)
[![Package Status](https://img.shields.io/pypi/status/blockfrost-python.svg)](https://pypi.org/project/blockfrost-python/)
[![License](https://img.shields.io/pypi/l/blockfrost-python.svg)](https://github.com/blockfrost/blockfrost-python/blob/master/LICENSE)


<img src="https://blockfrost.io/images/logo.svg" width="250" align="right" height="90">

# blockfrost-python

<br/>

<p align="center">A Python SDK for Blockfrost.io API.</p>
<p align="center">
  <a href="#getting-started">Getting started</a> •
  <a href="#installation">Installation</a> •
  <a href="#usage">Usage</a>
</p>
<br>

## Getting started

To use this SDK, you first need login into to [blockfrost.io](https://blockfrost.io) create your project to retrieve
your API key.

<img src="https://i.imgur.com/smY12ro.png">

<br/>

## Installation

```console
$ pip install blockfrost-python
```

<br/>

## Usage

Using the SDK is pretty straight-forward as you can see from the following examples.

### Cardano

```python
from blockfrost import BlockFrostApi, ApiError, ApiUrls

api = BlockFrostApi(
    project_id='YOUR API KEY HERE',  # or export environment variable BLOCKFROST_PROJECT_ID
    # optional: pass base_url or export BLOCKFROST_API_URL to use testnet, defaults to ApiUrls.mainnet.value
    base_url=ApiUrls.testnet.value,
)
try:
    health = api.health()
    print(health)   # prints object:    HealthResponse(is_healthy=True)
    health = api.health(return_type='json') # Can be useful if python wrapper is behind api version
    print(health)   # prints json:      {"is_healthy":True}
    health = api.health(return_type='pandas')
    print(health)   # prints Dataframe:         is_healthy
                    #                       0         True

    
    account_rewards = api.account_rewards(
        stake_address='stake1ux3g2c9dx2nhhehyrezyxpkstartcqmu9hk63qgfkccw5rqttygt7',
        count=20,
    )
    print(account_rewards[0].epoch)  # prints 221
    print(len(account_rewards))  # prints 20

    account_rewards = api.account_rewards(
        stake_address='stake1ux3g2c9dx2nhhehyrezyxpkstartcqmu9hk63qgfkccw5rqttygt7',
        count=20,
        gather_pages=True, # will collect all pages
    )
    print(account_rewards[0].epoch)  # prints 221
    print(len(account_rewards))  # prints 57

    address = api.address(
        address='addr1qxqs59lphg8g6qndelq8xwqn60ag3aeyfcp33c2kdp46a09re5df3pzwwmyq946axfcejy5n4x0y99wqpgtp2gd0k09qsgy6pz')
    print(address.type)  # prints 'shelley'
    for amount in address.amount:
        print(amount.unit)  # prints 'lovelace'

except ApiError as e:
    print(e)
```

### IPFS

```python
from blockfrost import BlockFrostIPFS, ApiError

ipfs = BlockFrostIPFS(
    project_id='YOUR API KEY HERE'  # or export environment variable BLOCKFROST_PROJECT_ID
)
file_hash = None
try:
    ipfs_object = ipfs.add('./README.md')
    file_hash = ipfs_object.ipfs_hash
    print(file_hash)
except ApiError as e:
    print(e)

try:
    with open('./README_downloaded.md', 'w') as file:
        file_data = ipfs.gateway(IPFS_path=file_hash).text
        file.write(file_data)
except ApiError as e:
    print(e)
```