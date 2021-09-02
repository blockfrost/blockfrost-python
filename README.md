[![Python package](https://github.com/blockfrost/blockfrost-python/actions/workflows/python-package.yml/badge.svg)](https://github.com/blockfrost/blockfrost-python/actions/workflows/python-package.yml)

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
$ pip install git+https://github.com/blockfrost/blockfrost-python
```

<br/>

## Usage

Using the SDK is pretty straight-forward as you can see from the following examples.

### Cardano

```python
from blockfrost import BlockFrostApi, ApiError

api = BlockFrostApi(
    project_id='YOUR API KEY HERE'  # or export environment variable BLOCKFROST_PROJECT_ID
)
try:
    health = api.health()
    print(health.is_healthy) # True

    account_rewards = api.account_rewards(
        stake_address='stake1ux3g2c9dx2nhhehyrezyxpkstartcqmu9hk63qgfkccw5rqttygt7',
        count=20,
    )
    print(account_rewards[0].epoch) # prints 221
    print(len(account_rewards))  # prints 20

    account_rewards = api.account_rewards(
        stake_address='stake1ux3g2c9dx2nhhehyrezyxpkstartcqmu9hk63qgfkccw5rqttygt7',
        count=20,
        gather_pages=True,
    )
    print(account_rewards[0].epoch) # prints 221
    print(len(account_rewards))  # prints 57

    address = api.address(
        address='addr1qxqs59lphg8g6qndelq8xwqn60ag3aeyfcp33c2kdp46a09re5df3pzwwmyq946axfcejy5n4x0y99wqpgtp2gd0k09qsgy6pz')
    print(address.type) # prints 'shelley'
    for amount in address.amount:
        print(amount.unit) # prints 'lovelace'
    
except ApiError as e:
    print(e)
```

### IPFS

```python
from blockfrost import BlockFrostIPFS, ApiError

ipfs = BlockFrostIPFS(
    project_id='YOUR API KEY HERE'  # or export environment variable BLOCKFROST_PROJECT_ID
)
try:
    response = ipfs.add('./README.md')
    print(response)
except ApiError as e:
    print(e)
```