[![Package Test](https://img.shields.io/github/actions/workflow/status/blockfrost/blockfrost-python/package-test.yml?logo=GitHub&label=package%20test)](https://github.com/blockfrost/blockfrost-python/actions/workflows/package-test.yml)
[![PyPI Latest Release](https://img.shields.io/pypi/v/blockfrost-python.svg?logo=pypi&label=pypi%20latest)](https://pypi.org/project/blockfrost-python/)
[![PyPI - Downloads](https://img.shields.io/pypi/dm/blockfrost-python?logo=pypi&label=pypi%20downloads)](https://pypistats.org/packages/blockfrost-python)
[![Package Status](https://img.shields.io/pypi/status/blockfrost-python.svg)](https://pypi.org/project/blockfrost-python/)
[![License](https://img.shields.io/pypi/l/blockfrost-python.svg)](https://github.com/blockfrost/blockfrost-python/blob/master/LICENSE)
[![Made by Five Binaries](https://img.shields.io/badge/made%20by-Five%20Binaries-darkviolet.svg)](https://fivebinaries.com/)
[![Maintained by Mathias Frohlich](https://img.shields.io/badge/maintained%20by-Mathias%20Frohlich-blue.svg)](https://github.com/mathiasfrohlich)

<img src="https://blockfrost.io/images/logo.svg" width="250" align="right" height="90">

# blockfrost-python

<br/>

<p align="center">A Python SDK for Blockfrost.io API</p>
<p align="center">
  <a href="#getting-started">Getting started</a> •
  <a href="#installation">Installation</a> •
  <a href="#usage">Usage</a>
</p>
<br>

## Getting started

To use this SDK, you first need login into [blockfrost.io](https://blockfrost.io) and create your project to retrieve
your API key.

<img src="https://i.imgur.com/smY12ro.png">

<br/>

## Installation

[![PyPI Latest Release](https://img.shields.io/pypi/v/blockfrost-python.svg)](https://pypi.org/project/blockfrost-python/)

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

### Verifying Secure Webhook signature

Webhooks enable Blockfrost to push real-time notifications to your application. In order to prevent malicious actor from pretending to be Blockfrost every webhook request is signed. The signature is included in a request's `Blockfrost-Signature` header. This allows you to verify that the events were sent by Blockfrost, not by a third party.
To learn more about Secure Webhooks, see [Secure Webhooks Docs](https://blockfrost.dev/docs/start-building/webhooks/).

You can verify the signature using `verifyWebhookSignature` function.

Example:

```python
# Example of Python Flask app with /webhook endpoint
# for processing events sent by Blockfrost Secure Webhooks
from flask import Flask, request, json
from blockfrost import verify_webhook_signature, SignatureVerificationError

SECRET_AUTH_TOKEN = "SECRET-WEBHOOK-AUTH-TOKEN"

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    if request.method == 'POST':
        # Validate webhook signature
        request_bytes = request.get_data()
        try:
            verify_webhook_signature(
                request_bytes, request.headers['Blockfrost-Signature'], SECRET_AUTH_TOKEN)
        except SignatureVerificationError as e:
            # for easier debugging you can access passed header and request_body values (e.header, e.request_body)
            print('Webhook signature is invalid.', e)
            return 'Invalid signature', 403

        # Get the payload as JSON
        event = request.json

        print('Received request id {}, webhook_id: {}'.format(
            event['id'], event['webhook_id']))

        if event['type'] == "block":
            # process Block event
            print('Received block hash {}'.format(event['payload']['hash']))
        elif event['type'] == "...":
            # truncated
        else:
            # Unexpected event type
            print('Unexpected event type {}'.format(event['type']))

        return 'Webhook received', 200
    else:
        return 'POST Method not supported', 405



if __name__ == "__main__":
    app.run(host='0.0.0.0', port=6666)
```

## Development

Install dependencies

```
pip install -r requirements.txt
pip install -r rest-requirements.txt
```

Install package

```
 pip install .
```

Run integration and unit tests:

```
pytest
```

_For integration tests you need to set env variable `BLOCKFROST_PROJECT_ID_MAINNET`_

### Release workflow

To release the package create a new release via GitHub releases.
This action triggers the automated release workflow that packages and uploads the distribution to PyPI.
