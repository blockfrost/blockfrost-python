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

To use this SDK, you first need login into to [blockfrost.io](https://blockfrost.io) create your project to retrieve your API key.

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
    response = api.health()
    print(response)
    
    response = api.account_rewards(
        stake_address='stake1ux3g2c9dx2nhhehyrezyxpkstartcqmu9hk63qgfkccw5rqttygt7',
        count=20,
    )
    print(len(response)) # prints 20
    
    response = api.account_rewards(
        stake_address='stake1ux3g2c9dx2nhhehyrezyxpkstartcqmu9hk63qgfkccw5rqttygt7',
        count=20,
        gather_pages=True,
    )
    print(len(response)) # prints 57
    
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